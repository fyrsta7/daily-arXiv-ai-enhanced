#!/usr/bin/env python3
"""Send the complete daily arXiv digest through SMTP."""

import argparse
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--raw-jsonl", required=True)
    parser.add_argument("--enhanced-jsonl", required=True)
    return parser.parse_args()


def required_env(name):
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Required environment variable {name} is not set")
    return value


def main():
    args = parse_args()
    sender = required_env("EMAIL_FROM")
    recipient = required_env("EMAIL_TO")
    password = required_env("SMTP_PASSWORD")
    categories = os.environ.get("CATEGORIES", "cs.SE")

    paths = [Path(args.markdown), Path(args.raw_jsonl), Path(args.enhanced_jsonl)]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing email attachments: {', '.join(missing)}")

    markdown = paths[0].read_text(encoding="utf-8")
    paper_count = sum(1 for line in paths[2].read_text(encoding="utf-8").splitlines() if line.strip())

    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = f"[Daily arXiv] {args.date} {categories} 新论文（{paper_count}篇）"
    message.set_content(
        f"今日共收录 {paper_count} 篇 {categories} 论文。\n"
        f"在线阅读：https://fyrsta7.github.io/daily-arXiv-ai-enhanced/\n\n"
        f"{markdown}"
    )

    attachment_types = {
        ".md": ("text", "markdown"),
        ".jsonl": ("application", "json"),
    }
    for path in paths:
        maintype, subtype = attachment_types[path.suffix]
        message.add_attachment(
            path.read_bytes(), maintype=maintype, subtype=subtype, filename=path.name
        )

    with smtplib.SMTP_SSL("smtp.163.com", 465, timeout=60) as smtp:
        smtp.login(sender, password)
        refused = smtp.send_message(message)
        if refused:
            raise RuntimeError(f"SMTP refused recipients: {', '.join(refused)}")

    print(f"Email accepted by smtp.163.com for {recipient}; papers={paper_count}")


if __name__ == "__main__":
    main()
