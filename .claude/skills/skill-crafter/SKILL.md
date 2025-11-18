---
name: skill-crafter
description: Design and generate new skills with templates and validation patterns. Triggers - create skill, new skill, design skill, generate skill, skill template.
version: 1.0.0
allowed-tools: Read, Write
---

# Skill: Skill Crafter (Meta-Skill)

## Purpose

This meta-skill provides systematic patterns for creating new Claude Code Skills. It guides the design process through conversation, generates complete SKILL.md files with proper structure, and ensures new skills follow best practices and integrate seamlessly with the MyClaude framework.

## When to Use

Use this skill when:
- Creating a new skill from scratch
- Packaging domain expertise into a reusable skill
- Extending framework capabilities
- Formalizing ad-hoc patterns into skills
- Helping users design custom skills

**Trigger scenarios**: "create a skill for API testing", "I need a skill for data validation", "help me design a skill", "generate skill template"

## Prerequisites

- Understanding of what the skill should accomplish
- Knowledge of the domain/task the skill addresses
- Familiarity with Claude Code Skills format
- Access to write files in `.claude/skills/`

## Skill Creation Process

### Phase 1: Discovery Interview

**Goal**: Understand what skill the user wants to create

**Interview Template**:

```markdown
I'll help you create a new skill! Let me ask some questions to design it properly:

## 1. Purpose & Use Case
- **What task or domain should this skill help with?**
  [Wait for answer]

- **When should Claude automatically use this skill?**
  [Wait for answer]

- **Can you give me 2-3 example scenarios where this skill would be useful?**
  [Wait for answer]

## 2. Scope & Complexity
- **Is this a simple prompt-based skill or does it need scripts/templates?**
  Options:
  a) Simple: Just instructions and patterns (most common)
  b) Medium: Instructions + reference files
  c) Complex: Instructions + scripts + templates

- **What level of detail do you need?**
  Options:
  a) Basic: Core workflow (~300 lines)
  b) Detailed: Comprehensive patterns (~500 lines)
  c) Reference-heavy: Core + extensive references (~500 + 2000 lines)

- **Does this work alone or combine with other skills?**
  [Wait for answer]

## 3. Tools & Dependencies
- **What tools does this skill need?**
  Common: Read, Grep, Glob, Bash, Edit, Write
  [Wait for answer]

- **Any external dependencies?**
  (Python packages, npm modules, system tools)
  [Wait for answer]

- **Does it need templates, examples, or reference files?**
  [Wait for answer]

## 4. Integration
- **Which agents might use this skill?**
  [Wait for answer]

- **Does it relate to existing skills?**
  (Works well with X, extends Y, alternative to Z)
  [Wait for answer]

- **Any specific terminology or glossary needed?**
  [Wait for answer]
```

**Output from Discovery**: Clear understanding of skill requirements captured in structured notes.

### Phase 2: Skill Design

**Goal**: Design the skill structure and content

**Actions**:

1. **Propose Skill Name**
   - Lowercase with hyphens
   - Gerund form when possible: "processing-data", "validating-api"
   - Clear and specific: avoid "helper", "utils", "misc"
   - Length: 2-4 words ideal

   Examples:
   - ✅ "api-testing", "code-refactoring", "data-validation"
   - ❌ "test-helper", "stuff", "utils"

2. **Craft Description** (Critical for auto-invocation)
   - Answer: "What does it do?" and "When to use it?"
   - Include trigger keywords (10-15 keywords)
   - Max 1024 characters
   - Natural language, not keyword stuffing

   Template:
   ```
   [Capability description] including [key features]. Use for [scenarios] or when [conditions]. Trigger keywords - [10-15 relevant keywords].
   ```

   Example:
   ```yaml
   description: API testing and validation patterns including request/response validation, authentication testing, and error handling. Use for testing REST/GraphQL APIs, validating endpoints, or ensuring API compliance. Trigger keywords - API, testing, endpoint, validation, request, response, REST, GraphQL, HTTP, status code, authentication.
   ```

3. **Determine Structure**

   **Level 1 - Metadata** (YAML frontmatter, always loaded):
   ```yaml
   ---
   name: skill-name
   description: [Comprehensive description with triggers]
   version: 1.0.0
   dependencies: package>=version (if needed)
   allowed-tools: Tool1, Tool2 (if restrictions needed)
   ---
   ```

   **Level 2 - Core Instructions** (SKILL.md body, ~300-500 lines):
   - Purpose
   - When to Use
   - Prerequisites
   - Core Process (3-6 phases)
   - Output Format
   - Examples
   - Integration notes
   - Quick reference

   **Level 3 - References** (Optional, ~2000+ lines):
   - frameworks.md: Detailed frameworks
   - examples.md: Comprehensive examples
   - templates/: Template files
   - scripts/: Automation scripts

4. **Design Workflow Pattern**

   Standard workflow structure (3-6 phases):

   ```markdown
   ### Phase 1: [Name]
   **Goal**: [What this phase accomplishes]

   **Actions**:
   1. [Specific action 1]
   2. [Specific action 2]
   3. [Specific action 3]

   **Quality Check**:
   - [ ] [Validation 1]
   - [ ] [Validation 2]
   - [ ] [Validation 3]

   **Example Output**:
   ```[format]
   [Example]
   ```
   ```

   Common phase patterns:
   - Discovery/Understanding → Analysis → Execution → Validation
   - Planning → Implementation → Testing → Delivery
   - Clarification → Decomposition → Investigation → Synthesis

**Output from Design**: Complete skill specification ready for generation.

### Phase 3: Generation

**Goal**: Generate all skill files

**Actions**:

1. **Create Directory Structure**:
   ```bash
   mkdir -p .claude/skills/[skill-name]/{scripts,templates,references}
   ```

2. **Generate SKILL.md** (Use template from templates/skill-template.md):

   ```markdown
   ---
   name: skill-name
   description: [Generated description with triggers]
   version: 1.0.0
   dependencies: [If needed]
   allowed-tools: [If restrictions]
   ---

   # Skill: [Human-Friendly Name]

   ## Purpose
   [What this skill accomplishes in 2-3 sentences]

   ## When to Use
   [Bulleted list of scenarios]
   - [Scenario 1]
   - [Scenario 2]
   - [Scenario 3]

   **Trigger scenarios**: [Quote trigger phrases]

   ## Prerequisites
   - [Prerequisite 1]
   - [Prerequisite 2]

   ## Core [Domain] Process

   [Generate 3-6 phases following the pattern]

   ## Output Format Template
   [Structure of expected output]

   ## [Domain-Specific] Patterns
   [Key patterns and techniques]

   ## Common Pitfalls
   [What to avoid]

   ## Integration with Agents
   [Which agents use this, works well with which other skills]

   ## Quick Reference
   [One-line summaries of key points]
   ```

3. **Generate Supporting Files** (if needed):

   **references/[topic].md**:
   - Detailed specifications
   - Comprehensive frameworks
   - Advanced techniques

   **examples.md**:
   - Complete worked examples
   - Before/after comparisons
   - Real-world scenarios

   **templates/[template-name]**:
   - Template files
   - Boilerplate structures
   - Configuration examples

   **scripts/[script-name].py**:
   - Automation scripts
   - Validation tools
   - Helper utilities

**Output from Generation**: Complete, ready-to-use skill files.

### Phase 4: Validation

**Goal**: Ensure skill follows best practices

**Validation Checklist**:

#### YAML Frontmatter
- [ ] `name` is lowercase with hyphens
- [ ] `name` uses gerund form (if applicable)
- [ ] `name` is specific and clear (not generic)
- [ ] `description` answers "what" and "when"
- [ ] `description` includes 10-15 trigger keywords
- [ ] `description` is under 1024 characters
- [ ] `version` follows semver (1.0.0)
- [ ] `dependencies` specified (if needed)
- [ ] `allowed-tools` specified (if restrictions)

#### SKILL.md Body
- [ ] Clear "Purpose" statement (2-3 sentences)
- [ ] Specific "When to Use" scenarios (3-5 bullets)
- [ ] "Trigger scenarios" with example phrases
- [ ] Prerequisites listed
- [ ] Core process with 3-6 phases
- [ ] Each phase has Goal + Actions + Quality Check
- [ ] Output format template provided
- [ ] At least one concrete example
- [ ] Integration notes (agents, skills)
- [ ] Quick reference section
- [ ] Under 500 lines (or justify if longer)

#### Progressive Disclosure
- [ ] Core instructions in SKILL.md (Level 2)
- [ ] Detailed references separate (Level 3)
- [ ] References one level deep (no nested refs)
- [ ] Reference files have clear purpose
- [ ] Total Level 2 content < 500 lines

#### Quality
- [ ] Clear, actionable instructions
- [ ] Consistent terminology throughout
- [ ] Proper markdown formatting
- [ ] No broken references
- [ ] Examples are concrete and helpful
- [ ] Quality checks are specific
- [ ] Output template is clear

#### Integration
- [ ] Lists which agents use it
- [ ] Lists related skills
- [ ] Explains how skills work together
- [ ] No conflicts with existing skills

**Validation Process**:
1. Read generated SKILL.md
2. Check against validation checklist
3. Test that description triggers correctly
4. Verify examples make sense
5. Check file references are valid

**Output from Validation**: Validated, production-ready skill.

### Phase 5: Documentation & Integration

**Goal**: Document and integrate the new skill

**Actions**:

1. **Update `.claude/skills/README.md`**:
   ```markdown
   ### [Category]

   - **[skill-name](skill-name/)** - [Brief one-line description]
   ```

2. **Suggest Agent Integration**:
   ```markdown
   Consider adding this skill to:
   - **[agent-name]**: Add `skill-name` to `skills:` frontmatter
   - **[agent-name]**: Would enhance [capability]
   ```

3. **Create Usage Example**:
   ```markdown
   ## Using the [Skill Name] Skill

   **Scenario**: [Example scenario]

   **Task**: "[Example task that triggers skill]"

   **Expected Behavior**:
   1. Skill auto-loads based on description keywords
   2. Claude follows [skill-name] workflow
   3. Output matches [skill-name] format
   4. Quality checks applied

   **Verification**:
   - [ ] Skill invoked automatically
   - [ ] Workflow followed correctly
   - [ ] Output format matched
   ```

4. **Document in Project README** (if significant):
   Add to main skills list with category and description.

**Output from Documentation**: Fully integrated and documented skill.

### Phase 6: Testing Guidance

**Goal**: Help user test the new skill

**Testing Template**:

```markdown
## Testing: [Skill Name]

### Test 1: Skill Loads
- [ ] Start new Claude conversation
- [ ] Skill metadata appears in available skills (check context)
- [ ] No YAML errors

### Test 2: Skill Triggers
**Test Case 1**:
- Give Claude: "[Task that should trigger skill]"
- Expected: Skill invokes automatically
- Verify: Claude mentions using [skill-name] skill

**Test Case 2**:
- Give Claude: "[Another trigger phrase]"
- Expected: Skill invokes automatically
- Verify: Workflow phases are followed

### Test 3: Output Quality
- [ ] Output follows skill's format template
- [ ] Quality checks are applied
- [ ] Examples match skill documentation

### Test 4: Progressive Disclosure
- [ ] Metadata loads at startup (low tokens)
- [ ] SKILL.md body loads when triggered
- [ ] Reference files load only on explicit need

### Test 5: Agent Integration
- [ ] [Agent-name] uses skill correctly
- [ ] Skill enhances agent's capabilities
- [ ] No conflicts with other skills

## Test Scenarios

1. **[Scenario 1 Name]**
   - Task: "[Specific task]"
   - Expected: [Expected behavior]
   - Verify: [What to check]

2. **[Scenario 2 Name]**
   - Task: "[Specific task]"
   - Expected: [Expected behavior]
   - Verify: [What to check]

3. **[Scenario 3 Name]**
   - Task: "[Specific task]"
   - Expected: [Expected behavior]
   - Verify: [What to check]
```

**Output from Testing**: Testing plan and validation criteria.

## Quality Standards

### Every Generated Skill Should:

1. **Be Discoverable**
   - Clear, specific name
   - Description with 10-15 trigger keywords
   - Obvious when to use

2. **Be Self-Contained**
   - Complete instructions in skill
   - All dependencies documented
   - No external knowledge required (except domain basics)

3. **Follow Progressive Disclosure**
   - Metadata compact (< 100 tokens)
   - Core instructions reasonable (300-500 lines)
   - References separate and optional

4. **Be Actionable**
   - Step-by-step workflow
   - Quality checks included
   - Clear output format
   - Concrete examples

5. **Be Maintainable**
   - Versioned (semver)
   - Well-documented
   - Consistent structure
   - Easy to update

## Skill Templates

### Template for Simple Skill (Prompt-based)

Location: `templates/simple-skill-template.md`

Use when:
- Just instructions and patterns
- No scripts or external dependencies
- Straightforward workflow

### Template for Complex Skill (Script-based)

Location: `templates/complex-skill-template.md`

Use when:
- Needs automation scripts
- Has external dependencies
- Complex validation or processing

### Template for Reference-Heavy Skill

Location: `templates/reference-heavy-template.md`

Use when:
- Large amount of reference material
- Multiple frameworks or patterns
- Comprehensive documentation needs

## Output Template

When delivering a new skill to user:

```markdown
# New Skill Created: [skill-name]

## Skill Overview

**Name**: `[skill-name]`
**Description**: [One-line summary]
**Version**: 1.0.0
**Category**: [category]
**Complexity**: [Simple/Medium/Complex]

## Files Created

✅ `.claude/skills/[skill-name]/SKILL.md` - Core instructions ([X] lines)
✅ `.claude/skills/[skill-name]/examples.md` - Usage examples (if created)
✅ `.claude/skills/[skill-name]/references/[topic].md` - References (if created)
✅ `.claude/skills/[skill-name]/scripts/[script].py` - Scripts (if created)
✅ `.claude/skills/[skill-name]/templates/` - Templates (if created)

## Progressive Disclosure Structure

**Level 1 (Metadata)**: ~[X] tokens - Always loaded
**Level 2 (Core)**: ~[Y] tokens - Loaded when triggered
**Level 3 (References)**: ~[Z] tokens - Loaded on demand

**Total context usage at startup**: ~[X] tokens (minimal impact)

## How to Use

This skill will automatically activate when:
- [Trigger phrase 1]
- [Trigger phrase 2]
- [Trigger phrase 3]

Or invoke explicitly: "Use the [skill-name] skill to [task]"

## Integration Recommendations

**Add to agents**:
- **[agent-name]**: Add `[skill-name]` to `skills:` frontmatter in `.claude/agents/[agent-name].md`
  ```yaml
  skills: existing-skill, [skill-name]
  ```

**Works well with**:
- **[skill-name]**: For [use case]
- **[skill-name]**: When [scenario]

## Testing Plan

[Include testing template with specific test cases]

## Next Steps

1. **Test the skill**: Try the test scenarios above
2. **Review output**: Read `.claude/skills/[skill-name]/SKILL.md`
3. **Refine if needed**:
   - Adjust description if not triggering
   - Add more examples if unclear
   - Enhance workflow if missing steps
4. **Integrate**: Add to relevant agents
5. **Document**: Update `.claude/skills/README.md`
6. **Commit**: `git add .claude/skills/[skill-name] && git commit -m "feat: Add [skill-name] skill"`

## Files Ready to Save

[Display complete SKILL.md content for review]

---

**Skill creation complete!** 🎉

The skill is ready to use immediately. Test it with the scenarios above and refine as needed.
```

## Common Skill Patterns

### Analysis-Type Skills
- Systematic decomposition
- Multi-dimensional evaluation
- Evidence gathering
- Structured recommendations

### Validation-Type Skills
- Checklist-driven
- Pass/fail criteria
- Evidence-based verification
- Gap identification

### Transformation-Type Skills
- Input → Process → Output
- Quality validation
- Format preservation
- Examples and templates

### Meta-Type Skills
- Interactive design
- Template-based generation
- Validation and testing
- Integration guidance

## Integration with Agents

This skill is used by:
- **skill-crafter agent**: Primary user
- Any user wanting to create skills

Works well with:
- **agent-crafter**: For creating agents that use new skills
- **analysis**: For analyzing what skills are needed

## Quick Reference

**Process**: Interview → Design → Generate → Validate → Document → Test

**Key outputs**: SKILL.md (always), references/ (optional), scripts/ (optional), templates/ (optional)

**Critical elements**: Clear description with triggers, 3-6 phase workflow, quality checks, examples, integration notes

**Progressive disclosure**: Metadata (50 tokens) → Core (300-500 lines) → References (2000+ lines)

**Validation**: 20+ point checklist ensuring quality and integration

For skill templates and generation helpers, see:
- **[templates/](templates/)** - Skill generation templates
- **[scripts/generate_skill.py](scripts/generate_skill.py)** - Skill generation script (future)
