#!/usr/bin/env python3
"""Redact common student identifiers from a text planning artifact."""

from __future__ import annotations

import argparse
import pathlib
import re


PATTERNS = [
    (re.compile(r"\b\d{8}\b"), "[REDACTED_UMID]"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@umich\.edu\b", re.I), "[REDACTED_EMAIL]"),
    (re.compile(r"\b(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b"), "[REDACTED_PHONE]"),
    (re.compile(r"(?i)\b(?:uniqname|umid|student id)\s*[:=]\s*\S+"), "[REDACTED_IDENTIFIER]"),
    (re.compile(r"(?i)\b(?:password|passcode|otp|duo code|session token)\s*[:=]\s*\S+"), "[REDACTED_SECRET]"),
]


def redact(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=pathlib.Path)
    parser.add_argument("-o", "--output", type=pathlib.Path)
    args = parser.parse_args()
    result = redact(args.input.read_text(encoding="utf-8"))
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
