#!/usr/bin/env python3
"""
Implementation Guardrails Confidence Check Script

This script provides automated confidence scoring for the 5-check validation system.
Can be used standalone or via pre-commit hooks.

Usage:
    python confidence_check.py [options]

Options:
    --interactive: Interactive mode with prompts
    --threshold: Confidence threshold (default: 0.7)
    --file: File path being validated (for hooks)
    --task: Description of task being validated
    --quiet: Minimal output

Exit codes:
    0: Confidence ≥ threshold (proceed)
    1: Confidence < threshold (block)
    2: Error or invalid input
"""

import sys
import os
import argparse
from typing import Dict, Tuple


def get_threshold() -> float:
    """Get confidence threshold from environment or default"""
    return float(os.getenv('MYCLAUDE_QUALITY_GATE_THRESHOLD', '0.7'))


def validate_score(score: float) -> bool:
    """Validate score is between 0.0 and 1.0"""
    return 0.0 <= score <= 1.0


def get_dimension_score(dimension: str, description: str) -> float:
    """
    Get score for a dimension interactively

    Args:
        dimension: Name of dimension
        description: Description of what to check

    Returns:
        Score between 0.0 and 1.0
    """
    print(f"\n{'='*60}")
    print(f"Dimension: {dimension}")
    print(f"{'='*60}")
    print(f"{description}\n")

    while True:
        try:
            score_input = input(f"Score for {dimension} (0.0-1.0): ").strip()
            score = float(score_input)
            if validate_score(score):
                return score
            else:
                print("❌ Score must be between 0.0 and 1.0")
        except ValueError:
            print("❌ Please enter a valid number between 0.0 and 1.0")
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  Validation cancelled by user")
            sys.exit(2)


def get_rationale(dimension: str) -> str:
    """Get brief rationale for the score"""
    print(f"\nBrief rationale for {dimension} score:")
    try:
        rationale = input("> ").strip()
        return rationale if rationale else "(No rationale provided)"
    except (KeyboardInterrupt, EOFError):
        return "(Cancelled)"


def calculate_confidence(scores: Dict[str, float]) -> float:
    """Calculate overall confidence as average of dimension scores"""
    return sum(scores.values()) / len(scores)


def get_decision(confidence: float, threshold: float) -> Tuple[str, str, int]:
    """
    Get decision based on confidence score

    Returns:
        (decision_label, decision_action, exit_code)
    """
    if confidence >= 0.9:
        return ("✅ PROCEED", "Confidence high - proceed with implementation", 0)
    elif confidence >= threshold:
        if threshold == 0.7:
            return ("⚠️  CLARIFY", "Confidence acceptable but gaps exist - clarify first", 1)
        else:
            return ("✅ PROCEED", "Confidence above threshold - proceed", 0)
    else:
        return ("❌ STOP", "Confidence too low - stop and re-analyze", 1)


def print_report(scores: Dict[str, float], rationales: Dict[str, str],
                 confidence: float, threshold: float, task: str = None):
    """Print validation report"""
    decision_label, decision_action, _ = get_decision(confidence, threshold)

    print("\n" + "="*70)
    print("IMPLEMENTATION GUARDRAILS VALIDATION REPORT")
    print("="*70)

    if task:
        print(f"\nTask: {task}")

    print(f"\nThreshold: {threshold}")
    print(f"\n{'Dimension':<30} {'Score':<10} Rationale")
    print("-"*70)

    for dim, score in scores.items():
        status = "✅" if score >= 0.7 else "⚠️ " if score >= 0.5 else "❌"
        rationale = rationales.get(dim, "")
        print(f"{status} {dim:<27} {score:.2f}       {rationale[:40]}")

    print("-"*70)
    print(f"{'OVERALL CONFIDENCE':<30} {confidence:.2f}")
    print("-"*70)
    print(f"\n{decision_label}")
    print(f"{decision_action}")
    print("="*70 + "\n")


def interactive_mode(threshold: float, task: str = None):
    """Run interactive validation"""
    print("\n" + "="*70)
    print("IMPLEMENTATION GUARDRAILS - INTERACTIVE VALIDATION")
    print("="*70)

    if task:
        print(f"\nTask: {task}")
    else:
        print("\nWhat are you about to implement?")
        try:
            task = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nValidation cancelled")
            sys.exit(2)

    print(f"\nConfidence threshold: {threshold}")
    print("\nYou will score 5 dimensions from 0.0 (poor) to 1.0 (excellent)")
    print("Press Ctrl+C at any time to cancel")

    # Define dimensions
    dimensions = {
        "Duplicate Check": "Have you searched for existing similar functionality?",
        "Architecture Fit": "Does this approach align with existing architecture and patterns?",
        "Documentation Compliance": "Have you reviewed relevant docs, specs, and policies?",
        "Existing Solutions": "Have you evaluated existing libraries and tools?",
        "Problem Understanding": "Do you understand the ROOT CAUSE, not just symptoms?"
    }

    scores = {}
    rationales = {}

    # Get scores for each dimension
    for dimension, description in dimensions.items():
        scores[dimension] = get_dimension_score(dimension, description)
        rationales[dimension] = get_rationale(dimension)

    # Calculate confidence
    confidence = calculate_confidence(scores)

    # Print report
    print_report(scores, rationales, confidence, threshold, task)

    # Get decision
    _, _, exit_code = get_decision(confidence, threshold)

    return exit_code


def quick_mode(threshold: float, scores_input: list = None) -> int:
    """
    Quick validation with provided scores

    Args:
        threshold: Confidence threshold
        scores_input: List of 5 scores (if None, uses default passing scores)

    Returns:
        Exit code
    """
    if scores_input is None:
        # Default to all 0.8 (above threshold but not perfect)
        scores_input = [0.8, 0.8, 0.8, 0.8, 0.8]

    if len(scores_input) != 5:
        print("❌ Error: Exactly 5 scores required (one per dimension)")
        return 2

    dimensions = [
        "Duplicate Check",
        "Architecture Fit",
        "Documentation Compliance",
        "Existing Solutions",
        "Problem Understanding"
    ]

    scores = dict(zip(dimensions, scores_input))
    confidence = calculate_confidence(scores)

    decision_label, decision_action, exit_code = get_decision(confidence, threshold)

    print(f"\nConfidence: {confidence:.2f} (threshold: {threshold})")
    print(f"{decision_label}: {decision_action}\n")

    return exit_code


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Implementation Guardrails Confidence Check'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Interactive mode with prompts for each dimension'
    )
    parser.add_argument(
        '--threshold', '-t',
        type=float,
        default=None,
        help='Confidence threshold (default: 0.7 or MYCLAUDE_QUALITY_GATE_THRESHOLD env var)'
    )
    parser.add_argument(
        '--file', '-f',
        type=str,
        help='File path being validated (for hook integration)'
    )
    parser.add_argument(
        '--task',
        type=str,
        help='Description of task being validated'
    )
    parser.add_argument(
        '--scores',
        type=str,
        help='Comma-separated scores for quick mode (e.g., "0.9,0.8,0.7,1.0,0.9")'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Minimal output (just exit code)'
    )

    args = parser.parse_args()

    # Get threshold
    threshold = args.threshold if args.threshold is not None else get_threshold()

    if not 0.0 <= threshold <= 1.0:
        print(f"❌ Error: Threshold must be between 0.0 and 1.0 (got {threshold})")
        return 2

    # Build task description
    task = args.task
    if args.file and not task:
        task = f"Modifying {args.file}"

    # Run validation
    if args.interactive:
        exit_code = interactive_mode(threshold, task)
    elif args.scores:
        try:
            scores_list = [float(s.strip()) for s in args.scores.split(',')]
            exit_code = quick_mode(threshold, scores_list)
        except ValueError:
            print("❌ Error: Invalid scores format. Use comma-separated numbers (e.g., '0.9,0.8,0.7,1.0,0.9')")
            return 2
    else:
        # Default: quick mode with passing scores (for testing)
        if not args.quiet:
            print("ℹ️  Running in quick mode with default scores")
            print("   Use --interactive for full validation")
            print("   Use --scores for custom scores\n")
        exit_code = quick_mode(threshold)

    return exit_code


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Validation cancelled by user")
        sys.exit(2)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(2)
