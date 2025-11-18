# Skills API Reference

Quick reference for all MyClaude skills. See [Skills User Guide](../user-guide/skills.md) for detailed documentation.

## Skill List

| Skill | Purpose | Version | Tools |
|-------|---------|---------|-------|
| analysis | Analysis frameworks (SWOT, cost-benefit, decision matrices) | 1.0.0 | Read, Grep, Glob, Bash |
| doc-compliance | Documentation verification with compliance tables | 1.0.0 | Read, Grep, Glob |
| translation | Translation with glossary and cultural adaptation | 1.0.0 | - |
| proofreading | Professional editing with comprehensive checklists | 1.0.0 | - |
| implementation-guardrails | 5-check pre-implementation validation | 1.0.0 | Read, Grep, Glob, Bash |
| skill-crafter | Meta-skill for creating new skills | 1.0.0 | Read, Write |

## Quick Reference

### analysis

**Triggers**: analyze, evaluate, compare, SWOT, strategic, decision, options

**Provides**: 10 analysis frameworks
- SWOT Analysis
- Cost-Benefit Analysis
- Risk Matrix
- Decision Matrix
- Force Field Analysis
- Eisenhower Matrix
- Pareto Analysis
- 5 Whys
- Comparative Analysis
- Gap Analysis

**Used by**: analyze-agent, docs-agent

---

### doc-compliance

**Triggers**: documentation, docs, verify, compliance, policy, specification, validate, standards

**Provides**:
- 5-step verification workflow
- Requirements extraction patterns
- Compliance table templates (✅/⚠️/❌)
- Gap analysis methodology

**Used by**: docs-agent

---

### translation

**Triggers**: translate, localize, language, multilingual, French, Spanish, German, Japanese, cultural

**Provides**:
- 6-step translation workflow
- Glossary management
- Cultural adaptation patterns (Romance, Germanic, Asian, RTL languages)
- Tone and formality control

**Used by**: translate-agent

---

### proofreading

**Triggers**: proofread, edit, grammar, clarity, style, polish, consistency, tone

**Provides**:
- 5-category editing checklist
- Change tracking templates
- Style enforcement patterns
- Before/after comparison format

**Used by**: proofread-agent

---

### implementation-guardrails

**Triggers**: before implementing, validate approach, confidence check, quality gate, verify architecture

**Provides**:
- 5-dimensional validation system:
  1. Duplicate Check (0.0-1.0)
  2. Architecture Fit (0.0-1.0)
  3. Documentation Compliance (0.0-1.0)
  4. Existing Solutions (0.0-1.0)
  5. Problem Understanding (0.0-1.0)
- Confidence scoring formula
- Decision thresholds (≥0.9 proceed, 0.7-0.89 clarify, <0.7 stop)
- Automated validation script

**Used by**: analyze-agent

---

### skill-crafter

**Triggers**: create skill, new skill, design skill, generate skill, skill template

**Provides**:
- Interactive design process (6 phases)
- Skill templates (simple, medium, complex)
- Validation checklist (20+ items)
- Integration recommendations

**Used by**: skill-crafter agent

## YAML Frontmatter Schema

### Required Fields

```yaml
name: skill-name              # Lowercase, hyphenated
description: Short description. Triggers - keyword1, keyword2, keyword3.
version: 1.0.0                # Semantic versioning
```

### Optional Fields

```yaml
allowed-tools: Read, Write    # Tools this skill needs
project: false                # true if project-specific
```

## Progressive Disclosure

### Level 1: Metadata (~50 tokens)
```yaml
---
name: skill-name
description: Brief with triggers
version: 1.0.0
---
```

### Level 2: Core (~500 tokens)
```markdown
## Purpose
## When to Use
## Workflow (3-6 phases)
## Quick Reference
```

### Level 3: References (~2000+ tokens)
```
references/
  framework1.md
  framework2.md
```

## Related Documentation

- [Skills User Guide](../user-guide/skills.md) - Comprehensive guide
- [Creating Skills](../developer-guide/creating-skills.md) - Development guide
