#!/usr/bin/env python3
"""Keep every cs.SE paper and semantically filter cs.AI for SemOpt-related work."""

import argparse
import json
import os
import time
from pathlib import Path

import requests

SYSTEM_PROMPT = """你是 LLM Agent 与自动代码优化方向的论文筛选专家。用户研究基于 LLM 的自动代码优化 agent（SemOpt 系列），同时希望跟踪可迁移到 agent 研究的一般方法进展。

判断 cs.AI 论文是否值得每日推送。满足以下任一条件即可保留：
1. LLM/coding agent 自动进行程序性能优化、编译器优化、代码效率提升，或研究自动代码优化 benchmark 与可靠 speedup 验证；
2. coding agent、software engineering agent、代码生成/修复/测试/审查 agent，尤其包含检索、规划、工具反馈、验证或长程执行；
3. 通用 LLM agent 的新方法：规划、记忆、反思、自我改进、工具使用、harness/workflow、轨迹/经验复用、多 agent 协作、长程任务、agent 评测、可靠性与安全控制；
4. 虽然应用领域不是软件工程，但提出了可迁移到 SemOpt 或 coding agent 的通用 agent 架构、训练/推理机制、benchmark 或实证结论。

应排除：纯模型训练/压缩/量化或普通推理增强而没有 agent；与程序无关的数学优化；仅把现成 agent 用于医疗、教育、金融、农业等垂直任务且没有通用方法贡献；仅因摘要出现 agent/optimization 字样但主题无关的论文。

筛选目标是宽松但有信息价值，不要求与自动代码优化强相关。边界论文若对 agent 设计有潜在启发，应保留。score 表示对用户研究的价值：0.9-1.0 直接相关，0.7-0.89 明显可迁移，0.5-0.69 一般 agent 方法但值得跟踪。relevant=true 通常要求 score>=0.5。只输出有效 JSON，不要 Markdown。格式：
{"decisions":[{"id":"arxiv id","relevant":true,"score":0.0,"reason_zh":"一句具体理由"}]}
必须对输入中的每个 id 恰好输出一次。"""


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--batch-size", type=int, default=20)
    return parser.parse_args()


def call_filter(batch, model, base_url, api_key):
    papers = [
        {
            "id": item["id"],
            "title": item.get("title", ""),
            "abstract": item.get("summary", "")[:2400],
            "categories": item.get("categories", []),
        }
        for item in batch
    ]
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps({"papers": papers}, ensure_ascii=False)},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
    }
    last_error = None
    for attempt in range(3):
        try:
            response = requests.post(
                base_url.rstrip("/") + "/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json=payload,
                timeout=180,
            )
            response.raise_for_status()
            body = response.json()
            parsed = json.loads(body["choices"][0]["message"]["content"])
            decisions = parsed["decisions"]
            expected = {paper["id"] for paper in papers}
            returned = [decision["id"] for decision in decisions]
            if set(returned) != expected or len(returned) != len(expected):
                raise ValueError(f"Filter returned mismatched ids: expected={expected}, returned={returned}")
            return decisions, body.get("usage", {})
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"cs.AI relevance filter failed after 3 attempts: {last_error}")


def main():
    args = parse_args()
    model = os.environ["MODEL_NAME"]
    base_url = os.environ["OPENAI_BASE_URL"]
    api_key = os.environ["OPENAI_API_KEY"]
    data_path = Path(args.data)
    raw_items = [json.loads(line) for line in data_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    items = []
    seen_ids = set()
    for item in raw_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            items.append(item)

    se_items = []
    ai_candidates = []
    for item in items:
        categories = set(item.get("categories", []))
        if "cs.SE" in categories:
            item["selection"] = {
                "policy": "cs.SE_all",
                "score": 1.0,
                "reason_zh": "cs.SE 论文按全量策略收录。",
            }
            se_items.append(item)
        elif "cs.AI" in categories:
            ai_candidates.append(item)

    usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    decisions_by_id = {}
    for start in range(0, len(ai_candidates), args.batch_size):
        decisions, batch_usage = call_filter(
            ai_candidates[start:start + args.batch_size], model, base_url, api_key
        )
        decisions_by_id.update({decision["id"]: decision for decision in decisions})
        for key in usage:
            usage[key] += int(batch_usage.get(key, 0) or 0)

    kept_ai = []
    for item in ai_candidates:
        decision = decisions_by_id[item["id"]]
        if bool(decision.get("relevant")):
            item["selection"] = {
                "policy": "cs.AI_semopt_relevance",
                "score": float(decision.get("score", 0)),
                "reason_zh": str(decision.get("reason_zh", "与自动代码优化研究相关。")),
            }
            kept_ai.append(item)

    kept_ids = {item["id"] for item in se_items + kept_ai}
    kept = [item for item in items if item["id"] in kept_ids]
    data_path.write_text(
        "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in kept),
        encoding="utf-8",
    )

    report = {
        "model": model,
        "policy": "keep_all_cs.SE_and_semantically_filter_cs.AI_for_SemOpt",
        "input_records": len(raw_items),
        "input_total": len(items),
        "cs.SE_kept": len(se_items),
        "cs.AI_candidates": len(ai_candidates),
        "cs.AI_kept": len(kept_ai),
        "output_total": len(kept),
        "filter_usage": usage,
        "cs.AI_decisions": [decisions_by_id[item["id"]] for item in ai_candidates],
    }
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("input_total", "cs.SE_kept", "cs.AI_candidates", "cs.AI_kept", "output_total", "filter_usage")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
