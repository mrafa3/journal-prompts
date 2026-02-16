#!/usr/bin/env python3
"""Validate journaling-prompts.json structure and content."""

import json
import sys
from collections import Counter
from pathlib import Path


def validate_prompts(filepath: str) -> bool:
    """Validate the prompts JSON file."""
    path = Path(filepath)

    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return False

    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        return False

    if "prompts" not in data:
        print("Error: Missing 'prompts' key")
        return False

    prompts = data["prompts"]

    if not isinstance(prompts, list):
        print("Error: 'prompts' must be an array")
        return False

    # Validate each prompt
    errors = []
    seen_prompts = set()
    categories = Counter()

    for i, prompt in enumerate(prompts):
        if not isinstance(prompt, dict):
            errors.append(f"Prompt {i}: Not an object")
            continue

        if "prompt" not in prompt:
            errors.append(f"Prompt {i}: Missing 'prompt' field")
        elif not isinstance(prompt["prompt"], str) or not prompt["prompt"].strip():
            errors.append(f"Prompt {i}: 'prompt' must be a non-empty string")
        else:
            text = prompt["prompt"].strip()
            if text in seen_prompts:
                errors.append(f"Prompt {i}: Duplicate prompt: '{text[:50]}...'")
            seen_prompts.add(text)

        if "category" not in prompt:
            errors.append(f"Prompt {i}: Missing 'category' field")
        elif not isinstance(prompt["category"], str) or not prompt["category"].strip():
            errors.append(f"Prompt {i}: 'category' must be a non-empty string")
        else:
            categories[prompt["category"]] += 1

    # Report results
    print(f"Total prompts: {len(prompts)}")
    print(f"Unique prompts: {len(seen_prompts)}")
    print()
    print("Category distribution:")
    for category, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {category}: {count}")
    print()

    if errors:
        print(f"Found {len(errors)} error(s):")
        for error in errors[:10]:  # Show first 10
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
        return False

    if len(prompts) < 365:
        print(f"Warning: Only {len(prompts)} prompts (target: 365)")
    else:
        print("All validations passed!")

    return True


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "journaling-prompts.json"
    success = validate_prompts(filepath)
    sys.exit(0 if success else 1)
