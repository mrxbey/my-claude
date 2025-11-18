#!/usr/bin/env python3
"""
MyClaude Framework Health Check

Runs comprehensive health diagnostics on the framework, including:
- Structural validation
- Component loading tests
- Integration tests
- Performance checks
- Security validation

Usage:
    python scripts/health_check.py [--detailed] [--json]

Options:
    --detailed   Show detailed diagnostic output
    --json       Output results in JSON format
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime

# Import validation from validate_framework
try:
    from validate_framework import FrameworkValidator, ValidationResult
except ImportError:
    # If running from different directory
    sys.path.insert(0, str(Path(__file__).parent))
    from validate_framework import FrameworkValidator, ValidationResult


@dataclass
class HealthCheck:
    """Single health check result"""
    name: str
    category: str
    status: str  # pass, warn, fail, skip
    message: str
    duration_ms: float = 0.0
    details: Dict[str, Any] = field(default_factory=dict)

    def __str__(self):
        icon = {
            "pass": "✅",
            "warn": "⚠️",
            "fail": "❌",
            "skip": "⏭️"
        }[self.status]
        duration = f" ({self.duration_ms:.0f}ms)" if self.duration_ms > 0 else ""
        return f"{icon} {self.name}: {self.message}{duration}"


@dataclass
class HealthReport:
    """Complete health check report"""
    timestamp: str
    framework_version: str
    overall_status: str  # healthy, degraded, critical
    checks: List[HealthCheck] = field(default_factory=list)
    summary: Dict[str, int] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON output"""
        return {
            "timestamp": self.timestamp,
            "framework_version": self.framework_version,
            "overall_status": self.overall_status,
            "checks": [asdict(check) for check in self.checks],
            "summary": self.summary,
            "recommendations": self.recommendations
        }


class FrameworkHealthChecker:
    """Comprehensive health checker for MyClaude framework"""

    def __init__(self, root_dir: Path, detailed: bool = False):
        self.root_dir = root_dir
        self.detailed = detailed
        self.report = HealthReport(
            timestamp=datetime.now().isoformat(),
            framework_version=self._detect_version(),
            overall_status="unknown"
        )

    def _detect_version(self) -> str:
        """Detect framework version"""
        # Try to read from PROJECT_STATUS.md or similar
        status_file = self.root_dir / "PROJECT_STATUS.md"
        if status_file.exists():
            with open(status_file, 'r') as f:
                content = f.read()
                # Look for version pattern
                import re
                match = re.search(r'Version:\s*(\d+\.\d+\.\d+)', content)
                if match:
                    return match.group(1)
        return "unknown"

    def run_all_checks(self) -> HealthReport:
        """Run all health checks"""
        print("🏥 MyClaude Framework Health Check\n")

        # Category 1: Structural Validation
        self._check_structure()

        # Category 2: Component Loading
        self._check_components()

        # Category 3: Configuration
        self._check_configuration()

        # Category 4: Integration
        self._check_integration()

        # Category 5: Performance
        self._check_performance()

        # Category 6: Security
        self._check_security()

        # Generate summary and recommendations
        self._generate_summary()

        return self.report

    def _add_check(self, name: str, category: str, status: str,
                   message: str, duration_ms: float = 0.0,
                   details: Optional[Dict] = None):
        """Add a health check result"""
        check = HealthCheck(
            name=name,
            category=category,
            status=status,
            message=message,
            duration_ms=duration_ms,
            details=details or {}
        )
        self.report.checks.append(check)

        if self.detailed or status in ["warn", "fail"]:
            print(f"  {check}")

    def _check_structure(self):
        """Structural validation checks"""
        print("📁 Checking structure...")

        start = time.time()

        # Run framework validator
        validator = FrameworkValidator(
            root_dir=self.root_dir,
            verbose=False,
            fix_issues=False
        )

        # Run validation
        validation_passed = validator.validate_all()

        duration = (time.time() - start) * 1000

        # Count errors and warnings
        errors = [r for r in validator.results if not r.passed and r.severity == "error"]
        warnings = [r for r in validator.results if not r.passed and r.severity == "warning"]

        if validation_passed and not warnings:
            self._add_check(
                "Structural Validation",
                "structure",
                "pass",
                "All structural checks passed",
                duration,
                {"errors": 0, "warnings": 0}
            )
        elif validation_passed:
            self._add_check(
                "Structural Validation",
                "structure",
                "warn",
                f"{len(warnings)} warnings found",
                duration,
                {"errors": 0, "warnings": len(warnings)}
            )
        else:
            self._add_check(
                "Structural Validation",
                "structure",
                "fail",
                f"{len(errors)} errors, {len(warnings)} warnings",
                duration,
                {"errors": len(errors), "warnings": len(warnings)}
            )

    def _check_components(self):
        """Component loading checks"""
        print("\n🔧 Checking components...")

        # Check agents
        self._check_agents_loadable()

        # Check skills
        self._check_skills_loadable()

        # Check commands
        self._check_commands_loadable()

    def _check_agents_loadable(self):
        """Check if all agents can be loaded"""
        start = time.time()

        agents_dir = self.root_dir / ".claude" / "agents"
        if not agents_dir.exists():
            self._add_check(
                "Agents Loading",
                "components",
                "fail",
                "Agents directory not found"
            )
            return

        agent_files = list(agents_dir.glob("*.md"))
        loadable = 0
        errors = []

        for agent_file in agent_files:
            try:
                with open(agent_file, 'r') as f:
                    content = f.read()

                # Check for YAML frontmatter
                if content.startswith("---"):
                    loadable += 1
                else:
                    errors.append(f"{agent_file.name}: No YAML frontmatter")

            except Exception as e:
                errors.append(f"{agent_file.name}: {str(e)}")

        duration = (time.time() - start) * 1000

        if loadable == len(agent_files):
            self._add_check(
                "Agents Loading",
                "components",
                "pass",
                f"All {loadable} agents loadable",
                duration,
                {"total": len(agent_files), "loadable": loadable}
            )
        else:
            self._add_check(
                "Agents Loading",
                "components",
                "fail",
                f"{loadable}/{len(agent_files)} agents loadable",
                duration,
                {"total": len(agent_files), "loadable": loadable, "errors": errors}
            )

    def _check_skills_loadable(self):
        """Check if all skills can be loaded"""
        start = time.time()

        skills_dir = self.root_dir / ".claude" / "skills"
        if not skills_dir.exists():
            self._add_check(
                "Skills Loading",
                "components",
                "fail",
                "Skills directory not found"
            )
            return

        skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
        loadable = 0
        errors = []

        for skill_dir in skill_dirs:
            skill_file = skill_dir / "SKILL.md"

            if not skill_file.exists():
                errors.append(f"{skill_dir.name}: No SKILL.md")
                continue

            try:
                with open(skill_file, 'r') as f:
                    content = f.read()

                if content.startswith("---"):
                    loadable += 1
                else:
                    errors.append(f"{skill_dir.name}: No YAML frontmatter")

            except Exception as e:
                errors.append(f"{skill_dir.name}: {str(e)}")

        duration = (time.time() - start) * 1000

        if loadable == len(skill_dirs):
            self._add_check(
                "Skills Loading",
                "components",
                "pass",
                f"All {loadable} skills loadable",
                duration,
                {"total": len(skill_dirs), "loadable": loadable}
            )
        else:
            self._add_check(
                "Skills Loading",
                "components",
                "fail",
                f"{loadable}/{len(skill_dirs)} skills loadable",
                duration,
                {"total": len(skill_dirs), "loadable": loadable, "errors": errors}
            )

    def _check_commands_loadable(self):
        """Check if all commands can be loaded"""
        start = time.time()

        commands_dir = self.root_dir / ".claude" / "commands"
        if not commands_dir.exists():
            self._add_check(
                "Commands Loading",
                "components",
                "fail",
                "Commands directory not found"
            )
            return

        command_files = list(commands_dir.rglob("*.md"))
        command_files = [f for f in command_files if f.name != "README.md"]

        loadable = 0
        errors = []

        for cmd_file in command_files:
            try:
                with open(cmd_file, 'r') as f:
                    content = f.read()

                if content.startswith("---"):
                    loadable += 1
                else:
                    errors.append(f"{cmd_file.name}: No YAML frontmatter")

            except Exception as e:
                errors.append(f"{cmd_file.name}: {str(e)}")

        duration = (time.time() - start) * 1000

        if loadable == len(command_files):
            self._add_check(
                "Commands Loading",
                "components",
                "pass",
                f"All {loadable} commands loadable",
                duration,
                {"total": len(command_files), "loadable": loadable}
            )
        else:
            self._add_check(
                "Commands Loading",
                "components",
                "fail",
                f"{loadable}/{len(command_files)} commands loadable",
                duration,
                {"total": len(command_files), "loadable": loadable, "errors": errors}
            )

    def _check_configuration(self):
        """Configuration validation checks"""
        print("\n⚙️  Checking configuration...")

        self._check_settings_valid()
        self._check_permissions_secure()

    def _check_settings_valid(self):
        """Check settings.json is valid"""
        start = time.time()

        settings_file = self.root_dir / ".claude" / "settings.json"

        if not settings_file.exists():
            self._add_check(
                "Settings File",
                "configuration",
                "fail",
                "settings.json not found"
            )
            return

        try:
            with open(settings_file, 'r') as f:
                settings = json.load(f)

            duration = (time.time() - start) * 1000

            # Check for required sections
            required_sections = ["permissions", "hooks", "env"]
            missing = [s for s in required_sections if s not in settings]

            if not missing:
                self._add_check(
                    "Settings File",
                    "configuration",
                    "pass",
                    "Valid JSON with all sections",
                    duration
                )
            else:
                self._add_check(
                    "Settings File",
                    "configuration",
                    "warn",
                    f"Missing sections: {', '.join(missing)}",
                    duration
                )

        except json.JSONDecodeError as e:
            duration = (time.time() - start) * 1000
            self._add_check(
                "Settings File",
                "configuration",
                "fail",
                f"Invalid JSON: {str(e)}",
                duration
            )
        except Exception as e:
            duration = (time.time() - start) * 1000
            self._add_check(
                "Settings File",
                "configuration",
                "fail",
                f"Error: {str(e)}",
                duration
            )

    def _check_permissions_secure(self):
        """Check permissions are secure"""
        start = time.time()

        settings_file = self.root_dir / ".claude" / "settings.json"

        try:
            with open(settings_file, 'r') as f:
                settings = json.load(f)

            if "permissions" not in settings:
                self._add_check(
                    "Permission Security",
                    "configuration",
                    "warn",
                    "No permissions configured"
                )
                return

            perms = settings["permissions"]

            # Check for dangerous patterns in allow list
            dangerous = []

            if "allow" in perms:
                for pattern in perms["allow"]:
                    if "**/.env" in pattern or "**/secrets" in pattern:
                        dangerous.append(pattern)
                    if "Bash(rm" in pattern or "Bash(curl" in pattern:
                        dangerous.append(pattern)

            duration = (time.time() - start) * 1000

            if dangerous:
                self._add_check(
                    "Permission Security",
                    "configuration",
                    "warn",
                    f"Potentially dangerous permissions: {', '.join(dangerous)}",
                    duration
                )
            else:
                self._add_check(
                    "Permission Security",
                    "configuration",
                    "pass",
                    "No dangerous permissions in allow list",
                    duration
                )

        except Exception as e:
            duration = (time.time() - start) * 1000
            self._add_check(
                "Permission Security",
                "configuration",
                "skip",
                f"Could not check: {str(e)}",
                duration
            )

    def _check_integration(self):
        """Integration checks"""
        print("\n🔗 Checking integration...")

        self._check_skill_agent_references()
        self._check_documentation_complete()

    def _check_skill_agent_references(self):
        """Check that agents reference existing skills"""
        start = time.time()

        # Get all skill names
        skills_dir = self.root_dir / ".claude" / "skills"
        if not skills_dir.exists():
            self._add_check(
                "Skill References",
                "integration",
                "skip",
                "Skills directory not found"
            )
            return

        available_skills = {d.name for d in skills_dir.iterdir() if d.is_dir()}

        # Check agent skill references
        agents_dir = self.root_dir / ".claude" / "agents"
        if not agents_dir.exists():
            self._add_check(
                "Skill References",
                "integration",
                "skip",
                "Agents directory not found"
            )
            return

        broken_refs = []

        for agent_file in agents_dir.glob("*.md"):
            try:
                import re
                import yaml

                with open(agent_file, 'r') as f:
                    content = f.read()

                yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                if yaml_match:
                    frontmatter = yaml.safe_load(yaml_match.group(1))

                    if "skills" in frontmatter:
                        skills = frontmatter["skills"]
                        if isinstance(skills, str):
                            skills = [s.strip() for s in skills.split(",")]

                        for skill in skills:
                            if skill not in available_skills:
                                broken_refs.append(f"{agent_file.name} → {skill}")

            except Exception:
                pass

        duration = (time.time() - start) * 1000

        if not broken_refs:
            self._add_check(
                "Skill References",
                "integration",
                "pass",
                "All agent skill references valid",
                duration
            )
        else:
            self._add_check(
                "Skill References",
                "integration",
                "fail",
                f"{len(broken_refs)} broken references",
                duration,
                {"broken": broken_refs}
            )

    def _check_documentation_complete(self):
        """Check documentation completeness"""
        start = time.time()

        required_docs = [
            "README.md",
            "CLAUDE.md",
            ".claude/agents/README.md",
            ".claude/skills/README.md",
            ".claude/commands/README.md",
        ]

        missing = []
        for doc in required_docs:
            if not (self.root_dir / doc).exists():
                missing.append(doc)

        duration = (time.time() - start) * 1000

        if not missing:
            self._add_check(
                "Documentation",
                "integration",
                "pass",
                "All required docs present",
                duration
            )
        else:
            self._add_check(
                "Documentation",
                "integration",
                "warn",
                f"{len(missing)} docs missing",
                duration,
                {"missing": missing}
            )

    def _check_performance(self):
        """Performance checks"""
        print("\n⚡ Checking performance...")

        self._check_context_size()

    def _check_context_size(self):
        """Estimate context usage"""
        start = time.time()

        # Estimate tokens for all agents and skills metadata
        total_chars = 0

        # Agents
        agents_dir = self.root_dir / ".claude" / "agents"
        if agents_dir.exists():
            for agent_file in agents_dir.glob("*.md"):
                try:
                    with open(agent_file, 'r') as f:
                        # Just read YAML frontmatter
                        import re
                        content = f.read()
                        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                        if yaml_match:
                            total_chars += len(yaml_match.group(1))
                except Exception:
                    pass

        # Skills
        skills_dir = self.root_dir / ".claude" / "skills"
        if skills_dir.exists():
            for skill_dir in skills_dir.iterdir():
                if skill_dir.is_dir():
                    skill_file = skill_dir / "SKILL.md"
                    if skill_file.exists():
                        try:
                            with open(skill_file, 'r') as f:
                                import re
                                content = f.read()
                                yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                                if yaml_match:
                                    total_chars += len(yaml_match.group(1))
                        except Exception:
                            pass

        # Rough estimate: 1 token ≈ 4 characters
        estimated_tokens = total_chars / 4

        duration = (time.time() - start) * 1000

        # Target: <500 tokens for metadata
        if estimated_tokens < 500:
            self._add_check(
                "Context Size",
                "performance",
                "pass",
                f"~{estimated_tokens:.0f} tokens (excellent)",
                duration,
                {"estimated_tokens": int(estimated_tokens)}
            )
        elif estimated_tokens < 1000:
            self._add_check(
                "Context Size",
                "performance",
                "warn",
                f"~{estimated_tokens:.0f} tokens (acceptable)",
                duration,
                {"estimated_tokens": int(estimated_tokens)}
            )
        else:
            self._add_check(
                "Context Size",
                "performance",
                "fail",
                f"~{estimated_tokens:.0f} tokens (too high)",
                duration,
                {"estimated_tokens": int(estimated_tokens)}
            )

    def _check_security(self):
        """Security checks"""
        print("\n🔒 Checking security...")

        self._check_no_secrets()
        self._check_gitignore()

    def _check_no_secrets(self):
        """Check for accidental secrets in version control"""
        start = time.time()

        suspicious_files = [
            ".env",
            ".env.local",
            "secrets.json",
            "credentials.json",
            ".claude/settings.local.json"
        ]

        found = []
        for pattern in suspicious_files:
            matches = list(self.root_dir.rglob(pattern))
            # Check if in git
            for match in matches:
                # Simple check - look for it in filesystem
                # (Full check would use `git ls-files`)
                if match.exists():
                    found.append(str(match.relative_to(self.root_dir)))

        duration = (time.time() - start) * 1000

        if not found:
            self._add_check(
                "No Secrets in Repo",
                "security",
                "pass",
                "No suspicious files found",
                duration
            )
        else:
            self._add_check(
                "No Secrets in Repo",
                "security",
                "warn",
                f"Found {len(found)} suspicious files",
                duration,
                {"files": found}
            )

    def _check_gitignore(self):
        """Check .gitignore is configured"""
        start = time.time()

        gitignore = self.root_dir / ".gitignore"

        if not gitignore.exists():
            self._add_check(
                "Git Ignore",
                "security",
                "warn",
                ".gitignore not found",
                (time.time() - start) * 1000
            )
            return

        with open(gitignore, 'r') as f:
            content = f.read()

        required_patterns = [
            ".env",
            "settings.local.json"
        ]

        missing = [p for p in required_patterns if p not in content]

        duration = (time.time() - start) * 1000

        if not missing:
            self._add_check(
                "Git Ignore",
                "security",
                "pass",
                "All sensitive patterns ignored",
                duration
            )
        else:
            self._add_check(
                "Git Ignore",
                "security",
                "warn",
                f"Missing patterns: {', '.join(missing)}",
                duration,
                {"missing": missing}
            )

    def _generate_summary(self):
        """Generate summary and recommendations"""
        # Count by status
        summary = {
            "pass": sum(1 for c in self.report.checks if c.status == "pass"),
            "warn": sum(1 for c in self.report.checks if c.status == "warn"),
            "fail": sum(1 for c in self.report.checks if c.status == "fail"),
            "skip": sum(1 for c in self.report.checks if c.status == "skip"),
        }

        self.report.summary = summary

        # Determine overall status
        if summary["fail"] > 0:
            self.report.overall_status = "critical"
        elif summary["warn"] > 3:
            self.report.overall_status = "degraded"
        else:
            self.report.overall_status = "healthy"

        # Generate recommendations
        failed_checks = [c for c in self.report.checks if c.status == "fail"]
        warned_checks = [c for c in self.report.checks if c.status == "warn"]

        for check in failed_checks:
            self.report.recommendations.append(
                f"[CRITICAL] Fix: {check.name} - {check.message}"
            )

        for check in warned_checks[:3]:  # Top 3 warnings
            self.report.recommendations.append(
                f"[IMPROVE] Address: {check.name} - {check.message}"
            )


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run health check on MyClaude framework"
    )
    parser.add_argument(
        "--detailed", "-d",
        action="store_true",
        help="Show detailed diagnostic output"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
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

    checker = FrameworkHealthChecker(
        root_dir=root_path,
        detailed=args.detailed
    )

    report = checker.run_all_checks()

    if args.json:
        print("\n" + json.dumps(report.to_dict(), indent=2))
    else:
        # Print summary
        print("\n" + "="*60)
        print("📊 HEALTH SUMMARY")
        print("="*60)
        print(f"\nOverall Status: ", end="")

        if report.overall_status == "healthy":
            print("✅ HEALTHY")
        elif report.overall_status == "degraded":
            print("⚠️  DEGRADED")
        else:
            print("❌ CRITICAL")

        print(f"\nChecks:")
        print(f"  ✅ Passed:  {report.summary['pass']}")
        print(f"  ⚠️  Warnings: {report.summary['warn']}")
        print(f"  ❌ Failed:  {report.summary['fail']}")
        print(f"  ⏭️  Skipped: {report.summary['skip']}")

        if report.recommendations:
            print(f"\n💡 Recommendations:")
            for rec in report.recommendations:
                print(f"  • {rec}")

        print("\n" + "="*60)

    # Exit code based on status
    exit_codes = {
        "healthy": 0,
        "degraded": 1,
        "critical": 2
    }

    sys.exit(exit_codes[report.overall_status])


if __name__ == "__main__":
    main()
