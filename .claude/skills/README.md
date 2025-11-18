# MyClaude Skills

This directory contains Agent Skills that extend Claude's capabilities through **progressive disclosure**. Skills auto-load based on context and provide domain expertise without overwhelming the initial context window.

## Progressive Disclosure Pattern

Skills use a 3-level loading strategy:

**Level 1 - Metadata** (~50 tokens, always loaded):
- name, description, version
- Triggers automatic skill discovery

**Level 2 - Instructions** (~500 tokens, loaded when triggered):
- SKILL.md body with core workflow
- Key patterns and processes

**Level 3 - References** (~2000+ tokens, loaded on demand):
- Detailed frameworks (reference.md)
- Comprehensive examples (examples.md)
- Templates and scripts

## Available Skills

### Core Business Skills

- **[analysis/](analysis/)** - Systematic analysis patterns for complex problems
- **[doc-compliance/](doc-compliance/)** - Documentation verification with checklists
- **[translation/](translation/)** - Translation patterns with glossaries and tone control
- **[proofreading/](proofreading/)** - Editing patterns and style enforcement

### Quality & Validation Skills

- **[implementation-guardrails/](implementation-guardrails/)** - Pre-implementation 5-check validation system

### Meta Skills

- **[skill-crafter/](skill-crafter/)** - Meta-skill for creating new skills interactively

## Skill Anatomy

Each skill is a directory with:

```
skill-name/
├── SKILL.md           # Required: Core instructions with YAML frontmatter
├── reference.md       # Optional: Detailed specifications
├── examples.md        # Optional: Comprehensive examples
├── scripts/           # Optional: Helper scripts
├── templates/         # Optional: Template files
└── assets/            # Optional: Binary resources
```

### SKILL.md Format

```yaml
---
name: skill-name                           # Required: lowercase-with-hyphens
description: What it does and when to use  # Required: with trigger keywords
version: 1.0.0                             # Optional: Semantic versioning
dependencies: python>=3.8, requests>=2.28  # Optional: External dependencies
allowed-tools: Bash, Read, Write           # Optional: Tool restrictions
---

# Skill: [Name]

## Purpose
Brief description

## When to Use
- Scenario 1
- Scenario 2

## Process
Step-by-step workflow

## Output Format
Expected deliverable structure

## Examples
Concrete demonstrations

## Integration
Works well with [other skills/agents]
```

## How Skills Work

1. **Startup**: Claude loads metadata (name + description) for all skills
2. **Task Received**: Claude matches task to relevant skills based on description keywords
3. **Skill Activated**: SKILL.md body loads into context
4. **On-Demand**: Reference files load only when explicitly needed

## Using Skills

### Automatic (Recommended)

Claude automatically invokes skills when relevant:

```
User: "Analyze the authentication system architecture"
→ Claude automatically loads 'analysis' skill
→ Applies systematic analysis patterns
→ Produces structured analysis
```

### Explicit

You can explicitly request a skill:

```
Use the analysis skill to evaluate these options
Use doc-compliance to verify against requirements
Use implementation-guardrails before proceeding
```

## Creating New Skills

### Method 1: Use Skill Crafter (Recommended)

```bash
/skill-crafter "Create skill for [your use case]"
```

The skill-crafter will interview you and generate a complete skill.

### Method 2: Manual Creation

1. Create directory: `.claude/skills/your-skill/`
2. Create `SKILL.md` with YAML frontmatter
3. Write clear description with trigger keywords
4. Structure with clear workflow phases
5. Add examples and references as needed
6. Test with relevant tasks

## Skill Best Practices

### Writing Effective Descriptions

✅ **Good**:
```yaml
description: Extract and validate data from CSV and JSON files. Use for data import, validation, or transformation tasks. Trigger keywords - CSV, JSON, parse, validate data, import data.
```

❌ **Bad**:
```yaml
description: Helps with data stuff
```

**Include**:
- What the skill does (capabilities)
- When to use it (scenarios)
- Trigger keywords for automatic invocation

### Keeping Skills Focused

✅ **Good**: One skill per clear capability
- `api-testing` - API testing specifically
- `data-validation` - Data validation specifically

❌ **Bad**: Kitchen-sink skills
- `helpers` - Too vague
- `utils` - What utilities?

### Progressive Disclosure

✅ **Good**: Lean SKILL.md, detailed references separate
```
SKILL.md (400 lines) → core patterns
reference.md (1000 lines) → detailed specs
examples.md (500 lines) → comprehensive examples
```

❌ **Bad**: Everything in SKILL.md
```
SKILL.md (2000 lines) → everything
```

### Integration

Skills should:
- Work with multiple agents
- Reference related skills
- Provide reusable patterns
- Not duplicate existing skills

## Skill Categories

### Development
- code-analysis, test-generation, refactoring, debugging

### Analysis
- data-analysis, security-audit, performance-analysis, architecture-review

### Content
- translation, proofreading, summarization, writing-assistance

### Business
- project-planning, risk-assessment, decision-analysis, requirements-gathering

### Quality
- implementation-guardrails, quality-assurance, compliance-checking

### Meta
- skill-crafter, workflow-generator

## Troubleshooting

**Skill Not Triggering?**
- Check description includes relevant trigger keywords
- Try explicit invocation: "Use the X skill"
- Verify YAML frontmatter is valid

**Skill Loading Slow?**
- Check SKILL.md body size (keep under 500 lines)
- Move detailed content to reference.md
- Ensure references are one level deep

**Skill Conflicts?**
- Check for overlapping descriptions
- Make trigger keywords more specific
- Use allowed-tools to restrict scope

## Contributing Skills

When creating skills for the framework:

1. Use skill-crafter for consistency
2. Test with multiple scenarios
3. Document clearly with examples
4. Update this README.md
5. Commit to version control
6. Share with team

## Examples

See individual skill directories for complete examples:

- [analysis/SKILL.md](analysis/SKILL.md) - Systematic analysis patterns
- [doc-compliance/SKILL.md](doc-compliance/SKILL.md) - Verification checklists
- [implementation-guardrails/SKILL.md](implementation-guardrails/SKILL.md) - Quality gates

---

For more information:
- [User Guide: Skills](../../docs/user-guide/skills.md)
- [Developer Guide: Creating Skills](../../docs/developer-guide/creating-skills.md)
- [Official Docs](https://code.claude.com/docs/en/skills)
