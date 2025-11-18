---
description: Interactive skill creation workflow using skill-crafter meta-agent
argument-hint: <skill-description>
---

Use the **skill-crafter agent** and **skill-crafter skill** to create a new Claude Code skill.

## Task

Create a new skill for: $ARGUMENTS

## Interactive Design Process

The skill-crafter will guide you through an interactive conversation to design and generate a complete skill. You'll be asked about:

### 1. Purpose & Use Case
- What task or domain should this skill help with?
- When should Claude automatically use this skill?
- Can you give 2-3 example scenarios?

### 2. Scope & Complexity
- Simple (just instructions), Medium (+ references), or Complex (+ scripts)?
- What level of detail needed (basic, detailed, comprehensive)?
- Does this work alone or combine with other skills?

### 3. Tools & Dependencies
- What tools does this skill need (Read, Grep, Glob, Bash, Edit, Write)?
- Any external dependencies (packages, system tools)?
- Need templates, examples, or reference files?

### 4. Integration
- Which agents might use this skill?
- Does it relate to existing skills?
- Any specific terminology or glossary needed?

## What You'll Get

The skill-crafter will generate:

1. **Complete SKILL.md file** with:
   - Proper YAML frontmatter (name, description with 10-15 trigger keywords, version)
   - Purpose statement
   - When to Use scenarios
   - Prerequisites
   - 3-6 phase workflow with Goals + Actions + Quality Checks
   - Output format template
   - Concrete examples
   - Integration notes
   - Quick reference

2. **Supporting files** (if needed):
   - Reference files (detailed frameworks, specifications)
   - Example files (comprehensive examples)
   - Template files (boilerplate structures)
   - Script files (automation utilities)

3. **Validation report** confirming:
   - YAML frontmatter well-formed
   - Description has proper trigger keywords
   - Workflow structure follows best practices
   - Progressive disclosure implemented
   - Quality standards met

4. **Integration recommendations**:
   - Which agents should use this skill
   - How it works with other skills
   - Where to add it in `.claude/agents/*.md` files

5. **Testing plan**:
   - Test scenarios to validate the skill
   - How to verify it triggers correctly
   - How to check output quality

## Output Location

New skill will be created at:
```
.claude/skills/[skill-name]/
├── SKILL.md (required)
├── examples.md (optional)
├── references/ (optional)
├── scripts/ (optional)
└── templates/ (optional)
```

## Next Steps After Creation

1. **Review** the generated SKILL.md
2. **Test** with the provided test scenarios
3. **Refine** if needed (adjust description, add examples, enhance workflow)
4. **Integrate** by adding to relevant agents' `skills:` frontmatter
5. **Document** by updating `.claude/skills/README.md`
6. **Commit** to version control: `git add .claude/skills/[skill-name] && git commit -m "feat: Add [skill-name] skill"`

The skill will be immediately available for use once created!

## Quality Standards

All generated skills will:
- Follow progressive disclosure (metadata → core → references)
- Include 10-15 trigger keywords for auto-invocation
- Have 3-6 phase structured workflow
- Include quality checks for each phase
- Provide concrete examples
- Integrate smoothly with existing framework
