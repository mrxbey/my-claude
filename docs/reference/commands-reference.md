# Commands API Reference

Quick reference for all MyClaude slash commands. See [Commands User Guide](../user-guide/commands.md) for detailed documentation.

## Command List

| Command | Purpose | Arguments |
|---------|---------|-----------|
| /analyze | Deep analysis workflow | `<what-to-analyze>` |
| /check-docs | Documentation verification | `<what-to-verify>` |
| /translate | Translation workflow | `<source> to <target>` |
| /proofread | Professional editing | `<content-to-edit>` |
| /skill-crafter | Create new skill interactively | `<skill-description>` |
| /agent-crafter | Create new agent interactively | `<agent-description>` |
| /workflows/code-review | Comprehensive code review | `<path-to-review>` |
| /workflows/feature-development | Feature development workflow | `<feature-description>` |

## Quick Reference

### /analyze

**Usage**: `/analyze <topic>`

**What it does**: 6-phase systematic analysis using analyze-agent

**Output**: Analysis report with options table, recommendation, action checklist

**Example**:
```
/analyze the caching strategy
/analyze database schema design
```

---

### /check-docs

**Usage**: `/check-docs <target>`

**What it does**: Verify documentation accuracy and compliance

**Output**: Compliance table with ✅/⚠️/❌ status, gap analysis, remediation roadmap

**Example**:
```
/check-docs @docs/api-spec.md against implementation
/check-docs compliance with security policy
```

---

### /translate

**Usage**: `/translate <source-language> to <target-language>`

**What it does**: High-quality translation with glossary management

**Output**: Translation, glossary, decision notes, quality metrics

**Example**:
```
/translate English to Spanish
/translate this documentation to French, formal tone
```

---

### /proofread

**Usage**: `/proofread <content>`

**What it does**: Professional editing for grammar, clarity, style, consistency

**Output**: Edited content, change summary, major improvements

**Example**:
```
/proofread this blog post
/proofread README.md for clarity
```

---

### /skill-crafter

**Usage**: `/skill-crafter <skill-description>`

**What it does**: Interactive skill creation with templates and validation

**Output**: Complete skill in `.claude/skills/[name]/SKILL.md`

**Example**:
```
/skill-crafter Create a skill for API testing
/skill-crafter Design a skill for data validation
```

---

### /agent-crafter

**Usage**: `/agent-crafter <agent-description>`

**What it does**: Interactive agent creation with identity design

**Output**: Complete agent in `.claude/agents/[name].md`

**Example**:
```
/agent-crafter Create an agent for security audits
/agent-crafter Design an agent for database migrations
```

---

### /workflows/code-review

**Usage**: `/workflows/code-review <path>`

**What it does**: 6-phase comprehensive code review

**Phases**:
1. Initial Analysis (analyze-agent)
2. Documentation Verification (docs-agent)
3. Quality Analysis
4. Test Coverage Analysis
5. Best Practices Check
6. Synthesis & Recommendations

**Output**: Complete review report with prioritized issues, recommendations, improvement roadmap

**Example**:
```
/workflows/code-review src/auth/
/workflows/code-review .
```

---

### /workflows/feature-development

**Usage**: `/workflows/feature-development <feature>`

**What it does**: 9-phase feature development with quality gates

**Phases**:
1. Requirements Analysis (analyze-agent)
2. Pre-Implementation Validation (implementation-guardrails)
3. Design (analyze-agent)
4. Documentation Planning (docs-agent)
5. Implementation
6. Code Review
7. Documentation
8. Integration Testing
9. Final Review & Deployment Prep

**Output**: Feature completion report with quality gates summary, deliverables, key metrics

**Example**:
```
/workflows/feature-development user authentication system
/workflows/feature-development real-time notifications
```

## Command Features

### Arguments

**$ARGUMENTS**: All arguments as single string
```markdown
Task: $ARGUMENTS
```

**Positional**: Individual arguments
```markdown
Translate from $1 to $2
```

### File References

Include file contents with `@`:
```
/check-docs @docs/spec.md
```

### Bash Execution

Run bash commands with `!`:
```markdown
!git log --oneline -10
Based on git history above...
```

## YAML Frontmatter Schema

```yaml
---
description: What this command does (required)
argument-hint: <expected-arguments> (optional)
---
```

## Related Documentation

- [Commands User Guide](../user-guide/commands.md) - Comprehensive guide
- [Creating Commands](../developer-guide/creating-commands.md) - Development guide
