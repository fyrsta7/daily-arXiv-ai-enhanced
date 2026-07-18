#!/usr/bin/env python3
"""Fetch cs.SE/cs.AI arXiv submissions for one historical UTC date."""

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path

import arxiv


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--categories",
        default=os.environ.get("CATEGORIES", "cs.SE, cs.AI"),
    )
    return parser.parse_args()


def main():
    args = parse_args()
    target = date.fromisoformat(args.date)
    categories = [
        category.strip()
        for category in args.categories.split(",")
        if category.strip()
    ]
    if not categories:
        raise ValueError("At least one arXiv category is required")

    category_query = " OR ".join(f"cat:{category}" for category in categories)
    day = target.strftime("%Y%m%d")
    query = (
        f"({category_query}) AND "
        f"submittedDate:[{day}000000 TO {day}235959]"
    )
    search = arxiv.Search(
        query=query,
        max_results=2000,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending,
    )
    client = arxiv.Client(
        page_size=100,
        delay_seconds=3.0,
        num_retries=3,
    )

    items = []
    seen_ids = set()
    for paper in client.results(search):
        arxiv_id = re.sub(r"v\d+$", "", paper.get_short_id())
        if arxiv_id in seen_ids:
            continue
        seen_ids.add(arxiv_id)
        items.append(
            {
                "id": arxiv_id,
                "pdf": paper.pdf_url or f"https://arxiv.org/pdf/{arxiv_id}",
                "abs": paper.entry_id or f"https://arxiv.org/abs/{arxiv_id}",
                "authors": [author.name for author in paper.authors],
                "title": paper.title,
                "categories": list(paper.categories),
                "comment": paper.comment,
                "summary": paper.summary,
            }
        )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(
            json.dumps(item, ensure_ascii=False) + "\n"
            for item in items
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "date": args.date,
                "categories": categories,
                "count": len(items),
                "query": query,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
