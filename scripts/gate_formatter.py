#!/usr/bin/env python3
"""
Aleatoric Uncertainty Resolver - Gate Formatter & Validator

Validates that decision options conform to strict brevity guardrails:
- 2 to 4 principal branches.
- Maximum 2 to 3 sentences per branch.
- Optional micro-snippets strictly <= 3 lines.
- Outputs standardized Markdown decision gate and matrix.
"""

import argparse
import json
import re
import sys
from typing import Any, Dict, List, Optional


def count_sentences(text: str) -> int:
    """Approximate sentence count in a text block."""
    cleaned = text.strip()
    if not cleaned:
        return 0
    sentences = [s for s in re.split(r"[.!?]+(?:\s+|$)", cleaned) if s.strip()]
    return len(sentences)


def validate_option(opt: Dict[str, Any], index: int) -> List[str]:
    errors = []
    label = opt.get("label", f"Option {chr(65 + index)}")
    philosophy = opt.get("philosophy", "")
    deliverable = opt.get("deliverable", "")
    pro = opt.get("pro", "")
    con = opt.get("con", "")
    snippet = opt.get("snippet", "")

    if not philosophy:
        errors.append(f"[{label}]: Missing 'philosophy' description.")
    else:
        s_count = count_sentences(philosophy)
        if s_count > 3:
            errors.append(f"[{label}]: Philosophy exceeds 3 sentences ({s_count} detected).")

    if not deliverable:
        errors.append(f"[{label}]: Missing 'deliverable' shape definition.")

    if not pro or not con:
        errors.append(f"[{label}]: Missing 'pro' or 'con' trade-off points.")

    if snippet:
        lines = [line for line in snippet.strip().split("\n") if line.strip()]
        if len(lines) > 3:
            errors.append(f"[{label}]: Micro-snippet exceeds 3 lines ({len(lines)} lines detected).")

    return errors


def format_gate(data: Dict[str, Any]) -> str:
    input_analysis = data.get("input_analysis", "High semantic entropy identified in user request.")
    options = data.get("options", [])

    if len(options) < 2 or len(options) > 4:
        raise ValueError(f"Options must be between 2 and 4. Found: {len(options)}")

    all_errors = []
    for idx, opt in enumerate(options):
        errs = validate_option(opt, idx)
        all_errors.extend(errs)

    if all_errors:
        raise ValueError("Validation errors:\n" + "\n".join(f"- {e}" for e in all_errors))

    out = []
    out.append("### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected\n")
    out.append(f"**Input Analysis**: {input_analysis}\n")
    out.append("---\n")

    for idx, opt in enumerate(options):
        key = f"[Option {chr(65 + idx)}]"
        title = opt.get("title", f"Path {chr(65 + idx)}")
        lang = opt.get("snippet_lang", "python")
        out.append(f"#### {key}: {title}")
        out.append(f"- **Philosophy**: {opt['philosophy'].strip()}")
        out.append(f"- **Deliverable**: {opt['deliverable'].strip()}")
        out.append(f"- **Trade-off**: **Pro**: {opt['pro'].strip()} | **Con**: {opt['con'].strip()}")
        if opt.get("snippet"):
            out.append(f"```{lang}\n{opt['snippet'].strip()}\n```")
        out.append("")

    out.append("---")
    out.append("")
    out.append("### Decision Matrix")
    out.append("")
    out.append("| Option | Approach | Deliverable Shape | Key Advantage |")
    out.append("| :--- | :--- | :--- | :--- |")
    for idx, opt in enumerate(options):
        key = f"**[Option {chr(65 + idx)}]**"
        title = opt.get("title", f"Path {chr(65 + idx)}")
        shape = opt.get("shape_summary", opt.get("deliverable", ""))
        pro = opt.get("pro", "")
        out.append(f"| {key} | {title} | {shape} | {pro} |")

    out.append("")
    prompt = data.get(
        "prompt",
        f"Which option best aligns with your goals? (Reply with `Option A`, `Option B`"
        + (f", `Option C`" if len(options) >= 3 else "")
        + (f", `Option D`" if len(options) >= 4 else "")
        + ", or specify custom constraints to begin).",
    )
    out.append(f"**Next Step**: {prompt}")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(
        description="Format and validate Aleatoric Uncertainty Decision Gates."
    )
    parser.add_argument(
        "--file", "-f", type=str, help="Path to JSON file containing gate options data."
    )
    parser.add_argument(
        "--demo", action="store_true", help="Print a pre-configured demo decision gate."
    )

    args = parser.parse_args()

    if args.demo:
        demo_data = {
            "input_analysis": "The request asks to 'build a metrics collection pipeline' which has multiple diverging architectures depending on ingestion rate and persistence model.",
            "options": [
                {
                    "title": "In-Memory Ring Buffer with Push Gateway",
                    "philosophy": "Collect low-overhead metrics locally in an ephemeral ring buffer. Flush periodically to Prometheus push gateway.",
                    "deliverable": "Single-file Python module with zero external database dependencies.",
                    "shape_summary": "Python module (zero-dependency)",
                    "pro": "Ultra-fast execution with zero infrastructure footprint",
                    "con": "Metrics lost if process crashes before flush",
                    "snippet": "buffer = RingBuffer(capacity=10_000)\nbuffer.record('latency_ms', 12.4)",
                },
                {
                    "title": "Time-Series Database Service Adapter",
                    "philosophy": "Direct asynchronous batched writes to an external TSDB (e.g., InfluxDB or TimescaleDB). Prioritize durability and analytical querying.",
                    "deliverable": "Async client wrapper with batching worker and Docker Compose service.",
                    "shape_summary": "Client SDK + Docker Compose",
                    "pro": "Full persistence and rich time-series query syntax",
                    "con": "Requires active database service running",
                    "snippet": "await tsdb_client.write_batch(points=metric_batch)",
                },
            ],
        }
        print(format_gate(demo_data))
        return

    if not args.file:
        parser.print_help()
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        output = format_gate(data)
        print(output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
