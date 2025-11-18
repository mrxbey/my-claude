#!/usr/bin/env python3
"""Measure context usage of framework components"""

import os
from pathlib import Path
import re


def estimate_tokens(text):
    """Rough token estimate: 1 token ≈ 4 characters"""
    return len(text) / 4


def measure_component(path, level):
    """Measure tokens for a component at given level"""

    with open(path, 'r') as f:
        content = f.read()

    if level == 1:  # Metadata only
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if yaml_match:
            return estimate_tokens(yaml_match.group(1))
        return 0

    elif level == 2:  # Metadata + core
        # Everything in main file
        return estimate_tokens(content)

    else:  # Full context
        # Main file + references
        tokens = estimate_tokens(content)

        # Add reference files
        component_dir = path.parent
        refs_dir = component_dir / "references"

        if refs_dir.exists():
            for ref_file in refs_dir.glob("*.md"):
                with open(ref_file, 'r') as f:
                    tokens += estimate_tokens(f.read())

        return tokens


def main():
    root = Path(".claude")

    print("Context Usage Analysis\n")
    print("="*60)

    # Measure agents
    print("\n📍 Agents")
    agents_dir = root / "agents"
    total_l1 = 0
    total_l2 = 0

    if agents_dir.exists():
        # Exclude README.md files
        agent_files = [f for f in agents_dir.glob("*.md") if f.name != "README.md"]

        for agent_file in agent_files:
            l1 = measure_component(agent_file, 1)
            l2 = measure_component(agent_file, 2)
            total_l1 += l1
            total_l2 += l2
            print(f"  {agent_file.stem:20} L1:{l1:4.0f}t  L2:{l2:4.0f}t")

        print(f"\n  Total agents:        L1:{total_l1:4.0f}t  L2:{total_l2:4.0f}t")

    # Measure skills
    print("\n🎯 Skills")
    skills_dir = root / "skills"
    total_l1_skills = 0
    total_l2_skills = 0
    total_l3 = 0

    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    l1 = measure_component(skill_file, 1)
                    l2 = measure_component(skill_file, 2)
                    l3 = measure_component(skill_file, 3)
                    total_l1_skills += l1
                    total_l2_skills += l2
                    total_l3 += l3
                    print(f"  {skill_dir.name:20} L1:{l1:4.0f}t  L2:{l2:4.0f}t  L3:{l3:4.0f}t")

        print(f"\n  Total skills:        L1:{total_l1_skills:4.0f}t  L2:{total_l2_skills:4.0f}t  L3:{total_l3:4.0f}t")

    # Overall totals
    total_startup = total_l1 + total_l1_skills

    print("\n" + "="*60)
    print(f"\nFramework Startup:   ~{total_startup:.0f} tokens (all metadata)")
    print(f"Typical Active Use:  ~{total_startup + 1000:.0f} tokens (metadata + 1 agent + 2 skills)")
    print(f"Maximum Context:     ~{total_l3:.0f} tokens (everything loaded)")

    print("\n✅ Target: <500 tokens at startup")
    if total_startup < 500:
        print(f"   PASS: {total_startup:.0f} tokens")
    else:
        print(f"   FAIL: {total_startup:.0f} tokens (reduce metadata)")


if __name__ == "__main__":
    main()
