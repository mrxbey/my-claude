# Developer Guide: Extending the Framework

## Overview

This guide covers advanced customization and extension of the MyClaude framework, including permissions, hooks, environment configuration, and integration with external tools.

## Architecture Overview

```
MyClaude Framework Architecture

┌─────────────────────────────────────────────────────────────┐
│                        User Layer                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Commands │  │  Agents  │  │  Skills  │  │ Workflows│   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
└───────┼─────────────┼─────────────┼─────────────┼──────────┘
        │             │             │             │
┌───────┼─────────────┼─────────────┼─────────────┼──────────┐
│       │      Framework Core Layer │             │           │
│  ┌────▼────────────────────────────▼─────────────▼──────┐  │
│  │         Claude Code Runtime Environment             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │  │
│  │  │Progressive│  │Permission│  │  Hooks   │          │  │
│  │  │Disclosure│  │  System  │  │  System  │          │  │
│  │  └──────────┘  └──────────┘  └──────────┘          │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
        │             │             │
┌───────▼─────────────▼─────────────▼──────────────────────┐
│                    Tool Layer                             │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐        │
│  │  Read  │  │  Grep  │  │  Edit  │  │  Bash  │  ...   │
│  └────────┘  └────────┘  └────────┘  └────────┘        │
└────────────────────────────────────────────────────────────┘
```

## Permission System

### Overview

Permissions control what operations Claude can perform in your codebase.

**Permission levels**:
- **allow**: Auto-approved, executes immediately
- **ask**: Requires user approval before execution
- **deny**: Blocked, will not execute

### Configuration Location

`.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Read(.claude/**)", "Read(docs/**)"],
    "ask": ["Write(.claude/**)", "Bash(git commit*)"],
    "deny": ["Read(**/.env*)", "Bash(rm -rf*)"]
  }
}
```

### Pattern Syntax

**File patterns**:
```json
"Read(.claude/**)"        // Any file in .claude/ recursively
"Read(*.md)"              // Any .md file in root
"Write(src/**/*.js)"      // Any .js file in src/ recursively
"Read(config.json)"       // Specific file
```

**Bash patterns**:
```json
"Bash(git status)"        // Exact command
"Bash(git *)"             // Any git command
"Bash(npm *)"             // Any npm command
"Bash(rm *)"              // Any rm command (dangerous!)
```

**Glob patterns**:
```json
"Glob(**/*.test.js)"      // Test files
"Glob(src/**)"            // All files in src/
```

### Default Permissions

Recommended starting point:

```json
{
  "permissions": {
    "allow": [
      // Read framework files
      "Read(.claude/**)",
      "Read(docs/**)",
      "Read(examples/**)",
      "Read(scripts/**)",
      "Read(*.md)",

      // Safe git operations
      "Bash(git status)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(git show*)",

      // Safe inspection
      "Bash(ls *)",
      "Bash(cat *.md)",
      "Bash(head *)",
      "Bash(tail *)",

      // Search operations
      "Grep(**)",
      "Glob(**)"
    ],

    "ask": [
      // Writing to framework files
      "Write(.claude/**)",
      "Write(docs/**)",
      "Edit(.claude/**)",
      "Edit(docs/**)",

      // Git modifications
      "Bash(git add*)",
      "Bash(git commit*)",
      "Bash(git push*)",

      // Package management
      "Bash(npm install*)",
      "Bash(pip install*)",

      // Writing code
      "Write(src/**)",
      "Edit(src/**)"
    ],

    "deny": [
      // Secrets and sensitive files
      "Read(**/.env*)",
      "Read(**/secrets/**)",
      "Read(**/*.key)",
      "Read(**/*credentials*)",

      // Dangerous operations
      "Bash(rm -rf*)",
      "Bash(sudo *)",
      "Bash(chmod *)",

      // Network operations
      "WebFetch(*)"
    ]
  }
}
```

### Permission Strategies

#### Strategy 1: Strict (Production)

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(git status)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Grep(**)",
      "Glob(**)"
    ],
    "ask": [
      "Write(**)",
      "Edit(**)",
      "Bash(*)"
    ],
    "deny": [
      "Read(**/.env*)",
      "Read(**/secrets/**)",
      "Bash(rm *)",
      "Bash(sudo *)",
      "WebFetch(*)"
    ]
  }
}
```

**Use when**: Production environment, critical codebase, untrusted agents

---

#### Strategy 2: Balanced (Development)

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(git *)",
      "Bash(npm *)",
      "Bash(ls *)",
      "Grep(**)",
      "Glob(**)"
    ],
    "ask": [
      "Write(src/**)",
      "Edit(src/**)",
      "Bash(rm *)"
    ],
    "deny": [
      "Read(**/.env*)",
      "Bash(sudo *)",
      "WebFetch(*)"
    ]
  }
}
```

**Use when**: Active development, trusted agents, need flexibility

---

#### Strategy 3: Permissive (Exploration)

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Write(**)",
      "Edit(**)",
      "Bash(*)",
      "Grep(**)",
      "Glob(**)"
    ],
    "ask": [],
    "deny": [
      "Read(**/.env*)",
      "Bash(rm -rf /)"
    ]
  }
}
```

**Use when**: Learning, experimentation, personal projects

**⚠️ Warning**: Only use in safe environments

---

### Per-Agent Permissions

Set different permissions for specific agents via `permissionMode`:

```yaml
---
name: read-only-agent
permissionMode: default
tools: Read, Grep, Glob
---
```

Options:
- `default`: Use global permissions
- `acceptEdits`: Auto-approve edits (for editing agents)
- `plan`: Present plan before executing (for high-risk agents)

---

## Hook System

### Overview

Hooks execute custom logic at specific points in the workflow:

- **PreToolUse**: Before tool executes
- **PostToolUse**: After tool completes
- **OnError**: When tool fails

### Hook Configuration

`.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write(.claude/**)",
      "hooks": [{
        "command": "python scripts/validate_before_write.py $FILE_PATH",
        "mode": "blocking"
      }]
    }],

    "PostToolUse": [{
      "matcher": "Write(**/*.md)",
      "hooks": [{
        "command": "prettier --write $FILE_PATH",
        "mode": "async"
      }]
    }]
  }
}
```

### Hook Variables

Available in hook commands:

- `$FILE_PATH`: File being operated on
- `$TOOL_NAME`: Tool name (Read, Write, Edit, etc.)
- `$ARGUMENTS`: Tool arguments (JSON)

### Hook Modes

**`blocking`** (synchronous):
```json
{
  "command": "python validate.py $FILE_PATH",
  "mode": "blocking"
}
```

- Waits for hook to complete
- Exit code 0 → continue
- Exit code 2 → block operation, show error
- Exit code other → error, show to Claude

**`async`** (asynchronous):
```json
{
  "command": "prettier --write $FILE_PATH",
  "mode": "async"
}
```

- Runs in background
- Doesn't block operation
- Use for formatting, notifications

### Common Hook Patterns

#### Pattern 1: Validation Hook

Validate before writing framework files:

```json
{
  "PreToolUse": [{
    "matcher": "Write(.claude/**/*.md)",
    "hooks": [{
      "command": "python scripts/validate_framework.py --file $FILE_PATH",
      "mode": "blocking"
    }]
  }]
}
```

Script (`scripts/validate_framework.py`):
```python
#!/usr/bin/env python3
import sys
import yaml

def validate_file(path):
    if not path.endswith('.md'):
        return 0

    with open(path, 'r') as f:
        content = f.read()

    # Check for YAML frontmatter
    if not content.startswith('---'):
        print(f"❌ Error: No YAML frontmatter in {path}")
        return 2  # Block operation

    # Validate YAML
    try:
        yaml_content = content.split('---')[1]
        yaml.safe_load(yaml_content)
    except Exception as e:
        print(f"❌ Error: Invalid YAML in {path}: {e}")
        return 2  # Block operation

    print(f"✅ Validation passed: {path}")
    return 0

if __name__ == "__main__":
    sys.exit(validate_file(sys.argv[1]))
```

---

#### Pattern 2: Formatting Hook

Auto-format after writing:

```json
{
  "PostToolUse": [{
    "matcher": "Write(**/*.md)",
    "hooks": [{
      "command": "prettier --write $FILE_PATH",
      "mode": "async"
    }]
  }, {
    "matcher": "Write(**/*.js)",
    "hooks": [{
      "command": "eslint --fix $FILE_PATH",
      "mode": "async"
    }]
  }]
}
```

---

#### Pattern 3: Audit Trail Hook

Log all operations:

```json
{
  "PostToolUse": [{
    "matcher": "Write(**)",
    "hooks": [{
      "command": "echo \"$(date) - Wrote: $FILE_PATH\" >> .claude/logs/audit.log",
      "mode": "async"
    }]
  }, {
    "matcher": "Bash(*)",
    "hooks": [{
      "command": "echo \"$(date) - Bash: $ARGUMENTS\" >> .claude/logs/audit.log",
      "mode": "async"
    }]
  }]
}
```

---

#### Pattern 4: Quality Gate Hook

Run quality checks before critical operations:

```json
{
  "PreToolUse": [{
    "matcher": "Bash(git push*)",
    "hooks": [{
      "command": "npm test",
      "mode": "blocking"
    }, {
      "command": "npm run lint",
      "mode": "blocking"
    }, {
      "command": "python scripts/health_check.py",
      "mode": "blocking"
    }]
  }]
}
```

---

#### Pattern 5: Notification Hook

Notify on significant events:

```json
{
  "PostToolUse": [{
    "matcher": "Bash(git push*)",
    "hooks": [{
      "command": "notify-send 'MyClaude' 'Code pushed to repository'",
      "mode": "async"
    }]
  }]
}
```

---

## Environment Configuration

### Configuration Layers

MyClaude supports multi-layer configuration:

```
Priority (highest to lowest):
1. Environment variables
2. .claude/settings.local.json (gitignored)
3. .claude/settings.json (version controlled)
```

### Base Configuration

`.claude/settings.json` (committed to git):

```json
{
  "permissions": {
    "allow": ["Read(**)", "Bash(git *)"],
    "ask": ["Write(**)", "Edit(**)"],
    "deny": ["Read(**/.env*)"]
  },

  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(**/*.md)",
      "hooks": [{
        "command": "prettier --write $FILE_PATH",
        "mode": "async"
      }]
    }]
  },

  "env": {
    "FRAMEWORK_MODE": "development",
    "LOG_LEVEL": "info"
  }
}
```

### Local Overrides

`.claude/settings.local.json` (gitignored, personal):

```json
{
  "permissions": {
    "allow": ["Write(experiments/**)"]
  },

  "env": {
    "FRAMEWORK_MODE": "experimental",
    "LOG_LEVEL": "debug"
  }
}
```

Settings merge:
- Permissions: Additive (local adds to base)
- Hooks: Additive (local adds to base)
- Env: Override (local overrides base)

### Environment Variables

Override via shell environment:

```bash
export FRAMEWORK_MODE=production
export LOG_LEVEL=warn

claude
```

Highest priority - overrides both settings files.

### Use Cases

**Use Case 1**: Shared team config + personal customization

```
# Committed
.claude/settings.json:
  - Team permissions
  - Team hooks
  - Default environment

# Local (not committed)
.claude/settings.local.json:
  - Personal experiment permissions
  - Personal hooks
  - Local overrides
```

**Use Case 2**: Environment-specific configuration

```bash
# Development
export FRAMEWORK_MODE=development
export ENABLE_DEBUG_HOOKS=true

# Production
export FRAMEWORK_MODE=production
export ENABLE_DEBUG_HOOKS=false
```

---

## Progressive Disclosure Optimization

### Token Budget Strategy

**Metadata** (Level 1): ~50 tokens/component
```yaml
name: component-name
description: Brief description with keywords
version: 1.0.0
```

**Core** (Level 2): ~500 tokens/component
```markdown
## Purpose
## When to Use
## Workflow (concise)
## Quick Reference
```

**References** (Level 3): ~2000+ tokens
```markdown
# Detailed frameworks
# Extensive examples
# Comprehensive specs
```

### Target Budget

- **Startup**: <500 tokens (all metadata)
- **Single agent active**: ~1500 tokens (metadata + 1 agent + 1-2 skills)
- **Complex workflow**: ~5000 tokens (metadata + multiple agents/skills + some references)
- **Deep expertise**: ~10000 tokens (full context with references)

### Measuring Context Usage

Create `scripts/measure_context.py`:

```python
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
        for agent_file in agents_dir.glob("*.md"):
            l1 = measure_component(agent_file, 1)
            l2 = measure_component(agent_file, 2)
            total_l1 += l1
            total_l2 += l2
            print(f"  {agent_file.stem:20} L1:{l1:4.0f}t  L2:{l2:4.0f}t")

        print(f"\n  Total agents:        L1:{total_l1:4.0f}t  L2:{total_l2:4.0f}t")

    # Measure skills
    print("\n🎯 Skills")
    skills_dir = root / "skills"
    total_l1 = 0
    total_l2 = 0
    total_l3 = 0

    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists():
                    l1 = measure_component(skill_file, 1)
                    l2 = measure_component(skill_file, 2)
                    l3 = measure_component(skill_file, 3)
                    total_l1 += l1
                    total_l2 += l2
                    total_l3 += l3
                    print(f"  {skill_dir.name:20} L1:{l1:4.0f}t  L2:{l2:4.0f}t  L3:{l3:4.0f}t")

        print(f"\n  Total skills:        L1:{total_l1:4.0f}t  L2:{total_l2:4.0f}t  L3:{total_l3:4.0f}t")

    print("\n" + "="*60)
    print(f"\nFramework Startup:   ~{total_l1:.0f} tokens (all metadata)")
    print(f"Typical Active Use:  ~{total_l1 + 1000:.0f} tokens (metadata + 1 agent + 2 skills)")
    print(f"Maximum Context:     ~{total_l3:.0f} tokens (everything loaded)")

    print("\n✅ Target: <500 tokens at startup")
    if total_l1 < 500:
        print(f"   PASS: {total_l1:.0f} tokens")
    else:
        print(f"   FAIL: {total_l1:.0f} tokens (reduce metadata)")

if __name__ == "__main__":
    main()
```

Run:
```bash
python scripts/measure_context.py
```

---

## External Tool Integration

### Integration Patterns

#### Pattern 1: Database Migrations

Create agent for database migrations:

`.claude/agents/database-migration-agent.md`:

```yaml
---
name: database-migration-agent
description: Database migration specialist for schema changes, data transformations, rollback planning
tools: Read, Grep, Glob, Edit, Write, Bash
model: sonnet
---
```

Hook for automatic migration validation:

```json
{
  "PreToolUse": [{
    "matcher": "Write(**/migrations/**)",
    "hooks": [{
      "command": "python scripts/validate_migration.py $FILE_PATH",
      "mode": "blocking"
    }]
  }]
}
```

---

#### Pattern 2: API Testing

Create skill for API testing:

`.claude/skills/api-testing/SKILL.md`:

Integration hook:

```json
{
  "PostToolUse": [{
    "matcher": "Write(src/api/**)",
    "hooks": [{
      "command": "npm run test:api",
      "mode": "blocking"
    }]
  }]
}
```

---

#### Pattern 3: Deployment Automation

Create command for deployment:

`.claude/commands/deploy.md`:

```markdown
---
description: Deploy application to specified environment
argument-hint: <environment>
---

## Task

Deploy to: $ARGUMENTS

## Pre-Deployment Validation

!python scripts/health_check.py
!npm test
!npm run lint

## Deployment

!npm run build
!npm run deploy:$ARGUMENTS

## Post-Deployment

!curl https://$ARGUMENTS.example.com/health
```

---

#### Pattern 4: CI/CD Integration

Use commands in GitHub Actions:

```yaml
# .github/workflows/claude-review.yml
name: Claude Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Claude
        run: |
          pip install claude-code

      - name: Run Code Review
        run: |
          claude /workflows/code-review ${{ github.event.pull_request.head.ref }}

      - name: Check Quality Gates
        run: |
          python scripts/health_check.py
```

---

## Custom Validation Scripts

### Validation Script Template

```python
#!/usr/bin/env python3
"""
Custom Validation Script Template

Usage:
  python validate.py <file-path>

Exit codes:
  0 - Validation passed
  1 - Validation failed (warning)
  2 - Validation failed (block operation)
"""

import sys
from pathlib import Path

def validate(file_path):
    """
    Validate file according to your criteria.

    Returns:
      0: Pass
      1: Warning (show but continue)
      2: Block (prevent operation)
    """

    path = Path(file_path)

    # Example validation: Check file size
    if path.stat().st_size > 1_000_000:  # 1MB
        print(f"⚠️  Warning: File is very large ({path.stat().st_size} bytes)")
        return 1

    # Example validation: Check content
    with open(path, 'r') as f:
        content = f.read()

    if 'TODO' in content:
        print(f"❌ Error: File contains TODO markers")
        return 2

    print(f"✅ Validation passed: {path}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate.py <file-path>")
        sys.exit(1)

    sys.exit(validate(sys.argv[1]))
```

---

## Security Best Practices

### Principle of Least Privilege

Start restrictive, expand as needed:

```json
{
  "permissions": {
    "allow": [
      "Read(**)"  // Start with read-only
    ],
    "ask": [
      "Write(**)",
      "Bash(*)"
    ],
    "deny": [
      "Read(**/.env*)",
      "Read(**/secrets/**)"
    ]
  }
}
```

### Secret Protection

**Never allow**:
```json
{
  "deny": [
    "Read(**/.env*)",
    "Read(**/*.key)",
    "Read(**/secrets/**)",
    "Read(**/*credentials*)",
    "Read(**/*password*)",
    "Read(**/id_rsa*)"
  ]
}
```

**Gitignore**:
```
.env*
secrets/
*.key
*credentials*
.claude/settings.local.json
```

### Dangerous Operation Protection

**Block destructive commands**:
```json
{
  "deny": [
    "Bash(rm -rf*)",
    "Bash(sudo *)",
    "Bash(chmod 777*)",
    "Bash(dd *)",
    "Bash(mkfs*)",
    "Bash(shutdown*)",
    "Bash(reboot*)"
  ]
}
```

### Audit Trail

Log all operations:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(**)",
      "hooks": [{
        "command": "echo \"$(date '+%Y-%m-%d %H:%M:%S') - $TOOL_NAME - $FILE_PATH\" >> .claude/logs/audit.log",
        "mode": "async"
      }]
    }, {
      "matcher": "Bash(*)",
      "hooks": [{
        "command": "echo \"$(date '+%Y-%m-%d %H:%M:%S') - Bash - $ARGUMENTS\" >> .claude/logs/audit.log",
        "mode": "async"
      }]
    }]
  }
}
```

Review audit log:
```bash
tail -f .claude/logs/audit.log
```

---

## Performance Optimization

### Reduce Hook Overhead

**❌ Slow**: Run expensive validation on every file write
```json
{
  "PostToolUse": [{
    "matcher": "Write(**)",
    "hooks": [{
      "command": "expensive-validation $FILE_PATH",
      "mode": "blocking"
    }]
  }]
}
```

**✅ Fast**: Only validate critical files
```json
{
  "PostToolUse": [{
    "matcher": "Write(.claude/**)",  // Only framework files
    "hooks": [{
      "command": "quick-validation $FILE_PATH",
      "mode": "blocking"
    }]
  }]
}
```

### Async Non-Critical Hooks

**Use async for**:
- Formatting
- Notifications
- Logging
- Non-critical validation

```json
{
  "PostToolUse": [{
    "matcher": "Write(**/*.md)",
    "hooks": [{
      "command": "prettier --write $FILE_PATH",
      "mode": "async"  // Don't wait for completion
    }]
  }]
}
```

### Cache Validation Results

```python
import hashlib
import json
from pathlib import Path

CACHE_FILE = ".claude/cache/validation.json"

def get_file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def validate_with_cache(path):
    cache = {}
    if Path(CACHE_FILE).exists():
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)

    file_hash = get_file_hash(path)

    if cache.get(path) == file_hash:
        print(f"✅ Cached validation: {path}")
        return 0

    # Run actual validation
    result = expensive_validation(path)

    if result == 0:
        cache[path] = file_hash
        Path(CACHE_FILE).parent.mkdir(exist_ok=True)
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f)

    return result
```

---

## Troubleshooting

### Permission Denied

**Problem**: Operation blocked unexpectedly

**Solutions**:
- Check `.claude/settings.json` permissions
- Check `deny` list for pattern match
- Try explicit `allow` pattern
- Check local overrides in `settings.local.json`

### Hook Not Running

**Problem**: Hook doesn't execute

**Solutions**:
- Verify matcher pattern matches operation
- Check hook command is executable
- Test hook command manually
- Check hook script permissions (`chmod +x`)
- Review stderr for hook errors

### Hook Blocking Operations

**Problem**: Hook prevents operation incorrectly

**Solutions**:
- Check exit codes (0=pass, 2=block)
- Run hook manually to debug
- Add debug output to hook script
- Change to async if non-critical
- Remove hook temporarily to bypass

### Context Overflow

**Problem**: Too much context loaded

**Solutions**:
- Run `scripts/measure_context.py`
- Move content to Level 3 (references)
- Reduce metadata size (<50 tokens)
- Reduce core size (<500 tokens)
- Split large skills into multiple smaller skills

---

## Best Practices Summary

### Do

✅ **Start restrictive** with permissions, expand as needed
✅ **Use hooks** for validation, formatting, auditing
✅ **Layer configuration** (base → local → env)
✅ **Measure context usage** regularly
✅ **Version control** base configuration
✅ **Document custom extensions** for team
✅ **Test hooks** thoroughly before deploying
✅ **Use async hooks** for non-critical operations

### Don't

❌ **Don't allow** secret file access
❌ **Don't skip** validation for critical operations
❌ **Don't commit** `settings.local.json`
❌ **Don't use blocking hooks** for slow operations
❌ **Don't hardcode** paths in hooks (use variables)
❌ **Don't ignore** exit codes from validation scripts

---

## Next Steps

1. **Configure permissions** for your environment
2. **Set up hooks** for validation and formatting
3. **Create validation scripts** for your specific needs
4. **Measure context usage** and optimize if needed
5. **Document extensions** for your team
6. **Integrate with CI/CD** for automation

---

## Related Documentation

- [User Guide: Overview](../user-guide/README.md)
- [Developer Guide: Creating Agents](creating-agents.md)
- [Developer Guide: Creating Skills](creating-skills.md)
- [Developer Guide: Creating Commands](creating-commands.md)
- [Reference: Configuration Reference](../reference/configuration-reference.md)
