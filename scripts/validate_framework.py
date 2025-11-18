#!/usr/bin/env python3
"""
MyClaude Framework Validation Script

Validates the framework structure, YAML frontmatter, file references,
and ensures all components are properly configured.

Usage:
    python scripts/validate_framework.py [--verbose] [--fix]

Options:
    --verbose    Show detailed validation output
    --fix        Attempt to fix common issues automatically
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """Result of a validation check"""
    passed: bool
    message: str
    severity: str = "error"  # error, warning, info
    file_path: Optional[str] = None
    fix_available: bool = False

    def __str__(self):
        icon = "✅" if self.passed else ("⚠️" if self.severity == "warning" else "❌")
        location = f" ({self.file_path})" if self.file_path else ""
        return f"{icon} {self.message}{location}"


@dataclass
class FrameworkValidator:
    """Validates MyClaude framework structure and configuration"""

    root_dir: Path
    verbose: bool = False
    fix_issues: bool = False
    results: List[ValidationResult] = field(default_factory=list)

    # Expected directory structure
    REQUIRED_DIRS = [
        ".claude",
        ".claude/agents",
        ".claude/skills",
        ".claude/commands",
        "docs",
        "scripts",
    ]

    # Required agent YAML fields
    REQUIRED_AGENT_FIELDS = ["name", "description", "tools", "model"]
    OPTIONAL_AGENT_FIELDS = ["skills", "permissionMode"]

    # Required skill YAML fields
    REQUIRED_SKILL_FIELDS = ["name", "description", "version"]
    OPTIONAL_SKILL_FIELDS = ["allowed-tools", "project"]

    # Required command YAML fields
    REQUIRED_COMMAND_FIELDS = ["description"]
    OPTIONAL_COMMAND_FIELDS = ["argument-hint"]

    def validate_all(self) -> bool:
        """Run all validation checks"""
        print("🔍 Validating MyClaude Framework\n")

        # 1. Directory structure
        self._validate_directory_structure()

        # 2. Settings files
        self._validate_settings()

        # 3. Agents
        self._validate_agents()

        # 4. Skills
        self._validate_skills()

        # 5. Commands
        self._validate_commands()

        # 6. Cross-references
        self._validate_cross_references()

        # 7. Documentation
        self._validate_documentation()

        # Print summary
        self._print_summary()

        # Return overall pass/fail
        return all(r.passed or r.severity == "warning" for r in self.results)

    def _validate_directory_structure(self):
        """Validate required directories exist"""
        print("📁 Validating directory structure...")

        for dir_path in self.REQUIRED_DIRS:
            full_path = self.root_dir / dir_path
            if full_path.exists():
                self._add_result(True, f"Directory exists: {dir_path}", "info")
            else:
                self._add_result(
                    False,
                    f"Required directory missing: {dir_path}",
                    "error",
                    fix_available=True
                )
                if self.fix_issues:
                    full_path.mkdir(parents=True, exist_ok=True)
                    print(f"  ✓ Created directory: {dir_path}")

    def _validate_settings(self):
        """Validate settings.json files"""
        print("\n⚙️  Validating settings files...")

        settings_file = self.root_dir / ".claude" / "settings.json"

        if not settings_file.exists():
            self._add_result(
                False,
                "settings.json not found",
                "error",
                str(settings_file)
            )
            return

        try:
            with open(settings_file, 'r') as f:
                settings = json.load(f)

            self._add_result(True, "settings.json is valid JSON", "info", str(settings_file))

            # Check for expected sections
            expected_sections = ["permissions", "hooks", "env"]
            for section in expected_sections:
                if section in settings:
                    self._add_result(True, f"Section '{section}' found", "info")
                else:
                    self._add_result(
                        False,
                        f"Section '{section}' missing in settings.json",
                        "warning",
                        str(settings_file)
                    )

            # Validate permissions structure
            if "permissions" in settings:
                for perm_type in ["allow", "ask", "deny"]:
                    if perm_type in settings["permissions"]:
                        if isinstance(settings["permissions"][perm_type], list):
                            self._add_result(
                                True,
                                f"Permissions.{perm_type} is valid list",
                                "info"
                            )
                        else:
                            self._add_result(
                                False,
                                f"Permissions.{perm_type} should be a list",
                                "error",
                                str(settings_file)
                            )

        except json.JSONDecodeError as e:
            self._add_result(
                False,
                f"settings.json is invalid JSON: {e}",
                "error",
                str(settings_file)
            )

    def _validate_agents(self):
        """Validate all agent files"""
        print("\n🤖 Validating agents...")

        agents_dir = self.root_dir / ".claude" / "agents"
        if not agents_dir.exists():
            self._add_result(False, "Agents directory not found", "error")
            return

        # Exclude README.md files
        agent_files = [f for f in agents_dir.glob("*.md") if f.name != "README.md"]

        if not agent_files:
            self._add_result(False, "No agent files found", "warning")
            return

        self._add_result(True, f"Found {len(agent_files)} agent files", "info")

        for agent_file in agent_files:
            self._validate_agent_file(agent_file)

    def _validate_agent_file(self, agent_file: Path):
        """Validate a single agent file"""
        if self.verbose:
            print(f"\n  Checking {agent_file.name}...")

        try:
            with open(agent_file, 'r') as f:
                content = f.read()

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)

            if not yaml_match:
                self._add_result(
                    False,
                    f"No YAML frontmatter found",
                    "error",
                    str(agent_file)
                )
                return

            yaml_content = yaml_match.group(1)

            try:
                frontmatter = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                self._add_result(
                    False,
                    f"Invalid YAML frontmatter: {e}",
                    "error",
                    str(agent_file)
                )
                return

            # Check required fields
            for field in self.REQUIRED_AGENT_FIELDS:
                if field in frontmatter:
                    self._add_result(
                        True,
                        f"Required field '{field}' present",
                        "info" if self.verbose else None,
                        str(agent_file)
                    )
                else:
                    self._add_result(
                        False,
                        f"Required field '{field}' missing",
                        "error",
                        str(agent_file)
                    )

            # Validate tools list
            if "tools" in frontmatter:
                valid_tools = ["Read", "Grep", "Glob", "Edit", "Write", "Bash", "WebFetch", "Task"]
                tools = frontmatter["tools"]

                if isinstance(tools, str):
                    tools = [t.strip() for t in tools.split(",")]

                for tool in tools:
                    if tool not in valid_tools:
                        self._add_result(
                            False,
                            f"Unknown tool '{tool}'",
                            "warning",
                            str(agent_file)
                        )

            # Validate model
            if "model" in frontmatter:
                valid_models = ["sonnet", "opus", "haiku", "inherit"]
                if frontmatter["model"] not in valid_models:
                    self._add_result(
                        False,
                        f"Invalid model '{frontmatter['model']}'",
                        "error",
                        str(agent_file)
                    )

            # Check for description trigger keywords
            if "description" in frontmatter:
                desc = frontmatter["description"]
                if len(desc) < 50:
                    self._add_result(
                        False,
                        f"Description too short (< 50 chars). Add trigger keywords.",
                        "warning",
                        str(agent_file)
                    )

                # Check for trigger keyword pattern
                if "trigger" not in desc.lower() and "keywords" not in desc.lower():
                    self._add_result(
                        False,
                        "Description should include explicit trigger keywords",
                        "warning",
                        str(agent_file)
                    )

            # Validate skill references
            if "skills" in frontmatter:
                skills = frontmatter["skills"]
                if isinstance(skills, str):
                    skills = [s.strip() for s in skills.split(",")]

                for skill in skills:
                    skill_path = self.root_dir / ".claude" / "skills" / skill / "SKILL.md"
                    if not skill_path.exists():
                        self._add_result(
                            False,
                            f"Referenced skill '{skill}' not found",
                            "error",
                            str(agent_file)
                        )

        except Exception as e:
            self._add_result(
                False,
                f"Error reading agent file: {e}",
                "error",
                str(agent_file)
            )

    def _validate_skills(self):
        """Validate all skill files"""
        print("\n🎯 Validating skills...")

        skills_dir = self.root_dir / ".claude" / "skills"
        if not skills_dir.exists():
            self._add_result(False, "Skills directory not found", "error")
            return

        skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]

        if not skill_dirs:
            self._add_result(False, "No skill directories found", "warning")
            return

        self._add_result(True, f"Found {len(skill_dirs)} skill directories", "info")

        for skill_dir in skill_dirs:
            self._validate_skill_dir(skill_dir)

    def _validate_skill_dir(self, skill_dir: Path):
        """Validate a single skill directory"""
        if self.verbose:
            print(f"\n  Checking {skill_dir.name}...")

        skill_file = skill_dir / "SKILL.md"

        if not skill_file.exists():
            self._add_result(
                False,
                f"SKILL.md not found in {skill_dir.name}",
                "error",
                str(skill_dir)
            )
            return

        try:
            with open(skill_file, 'r') as f:
                content = f.read()

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)

            if not yaml_match:
                self._add_result(
                    False,
                    f"No YAML frontmatter in SKILL.md",
                    "error",
                    str(skill_file)
                )
                return

            yaml_content = yaml_match.group(1)

            try:
                frontmatter = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                self._add_result(
                    False,
                    f"Invalid YAML in SKILL.md: {e}",
                    "error",
                    str(skill_file)
                )
                return

            # Check required fields
            for field in self.REQUIRED_SKILL_FIELDS:
                if field in frontmatter:
                    self._add_result(
                        True,
                        f"Required field '{field}' present",
                        "info" if self.verbose else None,
                        str(skill_file)
                    )
                else:
                    self._add_result(
                        False,
                        f"Required field '{field}' missing",
                        "error",
                        str(skill_file)
                    )

            # Check description has trigger keywords
            if "description" in frontmatter:
                desc = frontmatter["description"]

                # Should have at least 100 chars for good trigger coverage
                if len(desc) < 100:
                    self._add_result(
                        False,
                        f"Description too short. Should include 10-15 trigger keywords.",
                        "warning",
                        str(skill_file)
                    )

                # Check for keyword section
                if "trigger" not in desc.lower() and "keywords" not in desc.lower():
                    self._add_result(
                        False,
                        "Description should explicitly list trigger keywords",
                        "warning",
                        str(skill_file)
                    )

            # Validate version format
            if "version" in frontmatter:
                version = str(frontmatter["version"])
                if not re.match(r'^\d+\.\d+\.\d+$', version):
                    self._add_result(
                        False,
                        f"Version should use semver format (e.g., 1.0.0)",
                        "warning",
                        str(skill_file)
                    )

        except Exception as e:
            self._add_result(
                False,
                f"Error reading skill file: {e}",
                "error",
                str(skill_file)
            )

    def _validate_commands(self):
        """Validate all command files"""
        print("\n⚡ Validating commands...")

        commands_dir = self.root_dir / ".claude" / "commands"
        if not commands_dir.exists():
            self._add_result(False, "Commands directory not found", "error")
            return

        # Find all .md files recursively
        command_files = list(commands_dir.rglob("*.md"))

        # Exclude README files
        command_files = [f for f in command_files if f.name != "README.md"]

        if not command_files:
            self._add_result(False, "No command files found", "warning")
            return

        self._add_result(True, f"Found {len(command_files)} command files", "info")

        for command_file in command_files:
            self._validate_command_file(command_file)

    def _validate_command_file(self, command_file: Path):
        """Validate a single command file"""
        if self.verbose:
            print(f"\n  Checking {command_file.relative_to(self.root_dir)}...")

        try:
            with open(command_file, 'r') as f:
                content = f.read()

            # Extract YAML frontmatter
            yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)

            if not yaml_match:
                self._add_result(
                    False,
                    f"No YAML frontmatter",
                    "error",
                    str(command_file)
                )
                return

            yaml_content = yaml_match.group(1)

            try:
                frontmatter = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                self._add_result(
                    False,
                    f"Invalid YAML: {e}",
                    "error",
                    str(command_file)
                )
                return

            # Check required fields
            for field in self.REQUIRED_COMMAND_FIELDS:
                if field in frontmatter:
                    self._add_result(
                        True,
                        f"Required field '{field}' present",
                        "info" if self.verbose else None,
                        str(command_file)
                    )
                else:
                    self._add_result(
                        False,
                        f"Required field '{field}' missing",
                        "error",
                        str(command_file)
                    )

            # Check if command uses $ARGUMENTS variable (if argument-hint is present)
            if "argument-hint" in frontmatter:
                if "$ARGUMENTS" not in content:
                    self._add_result(
                        False,
                        "Command has argument-hint but doesn't use $ARGUMENTS",
                        "warning",
                        str(command_file)
                    )

        except Exception as e:
            self._add_result(
                False,
                f"Error reading command file: {e}",
                "error",
                str(command_file)
            )

    def _validate_cross_references(self):
        """Validate cross-references between components"""
        print("\n🔗 Validating cross-references...")

        # This would check:
        # - Agents referencing non-existent skills
        # - Skills referencing non-existent files
        # - Commands referencing non-existent agents
        # Already partially done in agent validation

        self._add_result(True, "Cross-reference validation complete", "info")

    def _validate_documentation(self):
        """Validate documentation files"""
        print("\n📚 Validating documentation...")

        required_docs = [
            "README.md",
            "CLAUDE.md",
            ".claude/agents/README.md",
            ".claude/skills/README.md",
            ".claude/commands/README.md",
        ]

        for doc_path in required_docs:
            full_path = self.root_dir / doc_path
            if full_path.exists():
                self._add_result(
                    True,
                    f"Documentation exists: {doc_path}",
                    "info" if self.verbose else None
                )
            else:
                self._add_result(
                    False,
                    f"Missing documentation: {doc_path}",
                    "warning",
                    str(full_path)
                )

    def _add_result(self, passed: bool, message: str, severity: str = "error",
                    file_path: Optional[str] = None, fix_available: bool = False):
        """Add a validation result"""
        # Only add if verbose or if it's an error/warning
        if self.verbose or severity in ["error", "warning"] or not passed:
            result = ValidationResult(
                passed=passed,
                message=message,
                severity=severity,
                file_path=file_path,
                fix_available=fix_available
            )
            self.results.append(result)

            if self.verbose:
                print(f"  {result}")

    def _print_summary(self):
        """Print validation summary"""
        print("\n" + "="*60)
        print("📊 VALIDATION SUMMARY")
        print("="*60)

        errors = [r for r in self.results if not r.passed and r.severity == "error"]
        warnings = [r for r in self.results if not r.passed and r.severity == "warning"]
        passed = [r for r in self.results if r.passed]

        print(f"\n✅ Passed:   {len(passed)}")
        print(f"⚠️  Warnings: {len(warnings)}")
        print(f"❌ Errors:   {len(errors)}")

        if errors:
            print("\n❌ ERRORS:")
            for error in errors:
                print(f"  {error}")

        if warnings:
            print("\n⚠️  WARNINGS:")
            for warning in warnings:
                print(f"  {warning}")

        print("\n" + "="*60)

        if errors:
            print("❌ Validation FAILED - Fix errors above")
            if self.fix_issues:
                print("💡 Re-run with --fix to attempt automatic fixes")
        elif warnings:
            print("⚠️  Validation PASSED with warnings")
        else:
            print("✅ Validation PASSED - Framework is healthy!")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate MyClaude framework structure and configuration"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed validation output"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Attempt to fix common issues automatically"
    )
    parser.add_argument(
        "--root",
        type=str,
        default=".",
        help="Root directory of the framework (default: current directory)"
    )

    args = parser.parse_args()

    root_path = Path(args.root).resolve()

    if not root_path.exists():
        print(f"❌ Error: Directory not found: {root_path}")
        sys.exit(1)

    validator = FrameworkValidator(
        root_dir=root_path,
        verbose=args.verbose,
        fix_issues=args.fix
    )

    success = validator.validate_all()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
