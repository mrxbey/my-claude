# User Guide: Skills

## Overview

Skills are reusable domain expertise that agents automatically load when relevant. Unlike agents (independent workers) and commands (user-invoked workflows), skills are **context-sensitive capabilities** that enhance agents with specialized knowledge and patterns.

Skills are ideal for:
- **Reusable patterns**: Frameworks and methodologies used across tasks
- **Domain expertise**: Specialized knowledge in specific areas
- **Progressive disclosure**: Efficient context loading (metadata → core → references)
- **Auto-triggering**: Load automatically based on keywords in conversation

## How Skills Work

### Automatic Loading

Skills load automatically when their trigger keywords match the conversation:

```
You: "I need to analyze our caching strategy using SWOT analysis"

Keywords detected: "analyze", "SWOT analysis"
→ Loads `analysis` skill
→ Provides SWOT framework and 9 other analysis methods
→ Claude uses appropriate framework for task
```

### Progressive Disclosure (3 Levels)

Skills use a 3-level loading strategy for context efficiency:

**Level 1: Metadata** (~50 tokens, always loaded)
```yaml
---
name: analysis
description: Systematic analysis patterns including SWOT, cost-benefit,
  decision matrices. Use for complex decisions, evaluations, comparisons.
  Trigger keywords - analyze, analysis, evaluate, assessment, SWOT, cost-benefit.
version: 1.0.0
---
```

**Level 2: Core Instructions** (~500 tokens, loaded when skill used)
```markdown
# Analysis Skill

## When to Use
[Scenarios and use cases]

## Workflow
[3-6 phase structured process]

## Quick Reference
[Essential patterns]
```

**Level 3: References** (~2000+ tokens, loaded on explicit need)
```markdown
# frameworks.md
## SWOT Analysis Framework
[Detailed methodology with examples]

## Cost-Benefit Analysis Framework
[Detailed methodology with examples]

[8 more frameworks...]
```

This approach keeps initial context under 500 tokens while providing deep expertise when needed.

### Skill Lifecycle

```
1. Metadata Loading (Always)
   └─ Name + description + trigger keywords loaded at startup

2. Trigger Detection
   └─ Keywords in conversation match skill description

3. Core Loading
   └─ SKILL.md body loads into agent context

4. Reference Loading (On Demand)
   └─ Detailed frameworks load when explicitly needed

5. Usage
   └─ Agent applies skill patterns to task
```

---

## Available Skills

### Core Business Skills

#### analysis

**Expertise**: Systematic analysis patterns for complex problems and decisions

**When it loads**:
- Keywords: analyze, analysis, evaluate, assessment, compare, investigate, examine, study, review, decision, strategic, options, breakdown

**What it provides**:
- **6-step analysis workflow**: Clarify → Decompose → Explore → Evaluate → Synthesize → Present
- **10 analysis frameworks**: SWOT, Cost-Benefit, Risk Matrix, Decision Matrix, Force Field, Eisenhower Matrix, Pareto Analysis, 5 Whys, Comparative Analysis, Gap Analysis
- **Structured output templates**: Standardized analysis reports

**Level 2 content** (SKILL.md):
```markdown
## Workflow

### Phase 1: Clarify
**Goal**: Understand exactly what needs analysis
**Actions**: Restate problem, list sub-questions
**Quality Check**: Is the problem clear and bounded?

### Phase 2: Decompose
**Goal**: Break into analyzable dimensions
**Actions**: Identify factors, constraints, assumptions
**Quality Check**: Are dimensions comprehensive?

[4 more phases...]
```

**Level 3 content** (frameworks.md):
```markdown
## SWOT Analysis

**Purpose**: Evaluate internal strengths/weaknesses and external
opportunities/threats

**When to use**: Strategic planning, competitive analysis, project evaluation

**Template**:
| Strengths | Weaknesses |
|-----------|------------|
| ...       | ...        |

| Opportunities | Threats |
|---------------|---------|
| ...           | ...     |

**Process**:
1. Brainstorm each quadrant
2. Prioritize items by impact
3. Develop strategies:
   - SO: Use strengths to capture opportunities
   - ST: Use strengths to mitigate threats
   - WO: Address weaknesses to capture opportunities
   - WT: Minimize weaknesses and avoid threats

[9 more frameworks with full detail...]
```

**Best for**: Architecture decisions, strategic planning, complex evaluations, trade-off analysis

---

#### doc-compliance

**Expertise**: Documentation verification patterns and compliance checking

**When it loads**:
- Keywords: documentation, docs, verify, compliance, policy, specification, requirements, validate, check against, standards, regulations, accuracy, coverage

**What it provides**:
- **5-step verification workflow**: Discovery → Requirements → Verification → Gap Analysis → Reporting
- **Requirements extraction patterns**: How to identify testable requirements
- **Compliance table templates**: Structured verification tracking
- **Gap analysis methodology**: Identifying and prioritizing documentation gaps

**Level 2 content** (SKILL.md):
```markdown
## Workflow

### Phase 1: Discovery
**Goal**: Find all relevant documentation
**Actions**:
- Search project docs/
- Identify external policies
- Find inline comments
**Quality Check**: Complete documentation inventory?

### Phase 2: Requirements Extraction
**Goal**: Build testable requirements list
**Actions**:
- Extract requirement statements
- Assign requirement IDs
- Categorize by type (functional, security, performance)
**Quality Check**: All requirements have IDs and categories?

### Phase 3: Verification
**Goal**: Check implementation against requirements
**Actions**:
- For each requirement, find implementation evidence
- Mark status: ✅ Met, ⚠️ Partial, ❌ Not met
- Record file:line references
**Quality Check**: Every requirement verified?

[2 more phases...]
```

**Compliance Table Template**:
```markdown
| ID | Requirement | Status | Evidence | Priority | Gap |
|----|-------------|--------|----------|----------|-----|
| SEC-001 | Passwords hashed | ✅ | src/auth.js:12 | Critical | - |
| SEC-002 | Rate limiting | ⚠️ | Partial impl | High | Missing: API endpoints |
| API-001 | All endpoints documented | ❌ | - | Medium | 5 undocumented endpoints |
```

**Best for**: Documentation audits, policy compliance, requirements validation, API specification verification

---

#### translation

**Expertise**: Translation and localization patterns with cultural adaptation

**When it loads**:
- Keywords: translate, translation, localize, localization, language, multilingual, convert, adapt, French, Spanish, German, Japanese, Chinese, cultural, tone, formality

**What it provides**:
- **6-step translation workflow**: Context → Glossary → Translate → Cultural → Variants → Document
- **Glossary management**: Consistent terminology tracking
- **Cultural adaptation patterns**: Language-family specific guidance (Romance, Germanic, Asian, RTL)
- **Tone control**: Formality and register management
- **Quality validation**: Completeness and consistency checks

**Level 2 content** (SKILL.md):
```markdown
## Workflow

### Phase 1: Understand Context
**Goal**: Clear translation requirements
**Actions**:
- Identify target language
- Determine audience (technical, general, marketing)
- Establish formality level (formal, neutral, casual)
- Note style guidelines
**Quality Check**: Translation parameters clear?

### Phase 2: Build/Update Glossary
**Goal**: Consistent terminology
**Actions**:
- Extract key terms from source
- Check existing project glossary
- Define translations for new terms
- Document choices
**Quality Check**: All domain terms in glossary?

### Phase 3: Translate
**Goal**: Accurate, natural translation
**Actions**:
- Preserve meaning first
- Adapt tone appropriately
- Maintain terminology from glossary
- Keep formatting consistent
**Quality Check**: Meaning preserved? Natural flow?

[3 more phases...]
```

**Cultural Adaptation Patterns**:
```markdown
## Romance Languages (Spanish, French, Italian)
- Longer text (~15-25% expansion)
- More formal structures available
- Gender agreement required
- Address forms important (tú/usted, tu/vous)

## Germanic Languages (German, Dutch)
- Compound words common
- Capitalization rules differ
- Formal/informal distinction (du/Sie)
- Text expansion (~15-20%)

## Asian Languages (Chinese, Japanese, Korean)
- Significant text compression (~30-50%)
- Honorific systems complex
- Vertical text consideration
- Context-dependent translation

[More patterns...]
```

**Best for**: Documentation localization, content adaptation, multi-language support, international marketing

---

#### proofreading

**Expertise**: Professional editing patterns with comprehensive checklists

**When it loads**:
- Keywords: proofread, edit, editing, grammar, clarity, style, polish, improve writing, fix errors, consistency, tone, writing quality, review text

**What it provides**:
- **5-category editing checklist**: Grammar, Clarity, Structure, Tone, Consistency
- **Change tracking templates**: Before/after documentation
- **Style enforcement patterns**: Consistency across documents
- **Improvement highlighting**: Focus on major changes

**Level 2 content** (SKILL.md):
```markdown
## 5-Category Editing Checklist

### Category 1: Grammar & Punctuation
- [ ] Spelling errors
- [ ] Punctuation (commas, periods, semicolons)
- [ ] Subject-verb agreement
- [ ] Pronoun reference clarity
- [ ] Apostrophe usage (possessives, contractions)
- [ ] Run-on sentences and fragments

### Category 2: Clarity & Conciseness
- [ ] Unclear or ambiguous phrasing
- [ ] Overly complex sentences (split if >25 words)
- [ ] Passive voice (prefer active)
- [ ] Redundant phrases ("past history", "advance planning")
- [ ] Jargon (simplify or explain)
- [ ] Wordy constructions

### Category 3: Structure & Flow
- [ ] Logical paragraph organization
- [ ] Clear headings hierarchy (H1 → H2 → H3)
- [ ] Smooth transitions between sections
- [ ] Consistent formatting (bullets, numbers, code blocks)
- [ ] Appropriate paragraph length (3-5 sentences)

### Category 4: Tone & Style
- [ ] Appropriate tone for audience (formal, neutral, casual)
- [ ] Consistent voice throughout
- [ ] Active vs. passive voice consistency
- [ ] Personal pronouns appropriate (you, we, I)
- [ ] Contractions appropriate to formality

### Category 5: Terminology & Consistency
- [ ] Consistent terminology usage
- [ ] Consistent capitalization (especially product names)
- [ ] Consistent formatting (dates, numbers, lists)
- [ ] Hyphenation consistency (e-mail vs email)
- [ ] Abbreviation consistency (first use spelled out)
```

**Change Summary Template**:
```markdown
## Change Summary

**Grammar & Punctuation** (12 changes):
- Fixed 5 comma splices
- Corrected 3 subject-verb agreements
- Fixed 4 spelling errors: "occured" → "occurred"

**Clarity** (8 improvements):
- Simplified 5 complex sentences (avg 32 words → 18 words)
- Removed 3 passive voice constructions
- Eliminated redundant phrase: "completely eliminate" → "eliminate"

**Structure** (3 changes):
- Added missing H2 heading for "Configuration" section
- Reorganized introduction: moved background to separate section
- Improved transitions between sections 2 and 3

**Tone** (2 adjustments):
- Shifted formal → conversational (per request)
- Changed "shall" → "should" (5 instances)

**Terminology** (4 fixes):
- Standardized "e-mail" → "email" throughout
- Consistent capitalization: "API" (not "api" or "Api")
```

**Best for**: Content polishing, consistency enforcement, quality improvement, documentation editing

---

### Quality & Validation Skills

#### implementation-guardrails

**Expertise**: Pre-implementation quality gates with 5-dimensional confidence checking

**When it loads**:
- Keywords: before implementing, validate approach, quality gate, confidence check, check duplicate, verify architecture, existing solutions, problem understanding

**What it provides**:
- **5-check validation system**: Prevents building wrong things
- **Confidence scoring**: Quantitative validation (0.0-1.0 per dimension)
- **Decision thresholds**: ≥0.9 Proceed, 0.7-0.89 Clarify, <0.7 Stop
- **Automated validation**: Python script for CI/CD integration

**The 5 Checks**:

```markdown
## 1. Duplicate Check (0.0-1.0)

**Question**: Does this functionality already exist?

**Scoring**:
- 1.0: Thoroughly searched, confirmed unique
- 0.7: Searched likely places, appears unique
- 0.5: Limited search, unsure
- 0.0: Haven't searched or duplicates found

**Actions**:
- Grep codebase for similar functionality
- Check existing modules and libraries
- Search documentation
- Ask team members (if applicable)

## 2. Architecture Fit (0.0-1.0)

**Question**: Does this approach align with architecture?

**Scoring**:
- 1.0: Follows established patterns exactly
- 0.7: Mostly aligns, minor deviations justified
- 0.5: Significant architectural questions remain
- 0.0: Violates architecture or unknown fit

**Actions**:
- Review architecture docs
- Check how similar features are built
- Verify layer boundaries respected
- Confirm dependency direction correct

## 3. Documentation Compliance (0.0-1.0)

**Question**: Have we consulted relevant docs and policies?

**Scoring**:
- 1.0: All docs reviewed, constraints understood
- 0.7: Key docs reviewed, minor gaps acceptable
- 0.5: Some docs reviewed, significant gaps
- 0.0: Haven't consulted documentation

**Actions**:
- Read project docs and ADRs
- Review relevant policies (security, performance)
- Check for breaking changes
- Understand constraints

## 4. Existing Solutions (0.0-1.0)

**Question**: Can we use existing libraries/tools?

**Scoring**:
- 1.0: Evaluated alternatives, justified custom approach
- 0.7: Checked common solutions, custom needed
- 0.5: Limited research on alternatives
- 0.0: Haven't looked for existing solutions

**Actions**:
- Search npm/pip/etc for relevant packages
- Review internal libraries and tools
- Check framework built-ins
- Document why not reusing (if custom)

## 5. Problem Understanding (0.0-1.0)

**Question**: Are we solving root cause or symptom?

**Scoring**:
- 1.0: Root cause clearly identified
- 0.7: Understand problem, minor uncertainty
- 0.5: Treating symptoms, root cause unclear
- 0.0: Don't understand underlying problem

**Actions**:
- Ask "5 Whys" to find root cause
- Understand user/system need
- Verify this solves actual problem
- Confirm simplest solution
```

**Confidence Calculation**:
```
Overall Confidence = (D1 + D2 + D3 + D4 + D5) / 5

Decision Rules:
- ≥ 0.9: ✅ PROCEED - High confidence, go ahead
- 0.7-0.89: ⚠️ CLARIFY - Gaps exist, address them first
- < 0.7: ❌ STOP - Too many unknowns, re-analyze
```

**Usage Pattern**:
```markdown
Before implementing [feature]:

**Duplicate Check**: 0.9
- Searched src/ and lib/ - no duplicates found
- Checked similar features - different use case

**Architecture Fit**: 0.8
- Follows MVC pattern like other features
- Reuses existing auth middleware
- Minor question: Which layer for validation? (resolved)

**Documentation Compliance**: 1.0
- Reviewed architecture docs
- Checked security policy - all compliant
- No breaking changes

**Existing Solutions**: 0.9
- Evaluated 3 npm packages: too heavy or missing features
- Using framework built-in validation: ✓
- Custom logic justified: unique business rules

**Problem Understanding**: 1.0
- Root cause: Users can't track progress
- This solves actual need
- Simplest solution that works

**Overall Confidence**: 0.92 ✅ PROCEED
```

**Automated Script** (`scripts/confidence_check.py`):
```bash
# Interactive mode
python scripts/confidence_check.py

# Quick mode (for CI/CD)
python scripts/confidence_check.py --quick --threshold 0.7

# Returns exit codes:
# 0: Confidence ≥ threshold
# 1: Confidence < threshold (block operation)
```

**Best for**: Pre-implementation validation, preventing wasted work, quality assurance, risk reduction

---

### Meta-Skills

#### skill-crafter

**Expertise**: Meta-skill for creating new skills through guided conversation

**When it loads**:
- Keywords: create skill, new skill, skill for, design skill, generate skill, build skill, extend framework, add capability
- Explicit command: `/skill-crafter`

**What it provides**:
- **6-phase design process**: Interview → Design → Generate → Validate → Integrate → Test
- **Skill templates**: Boilerplate for simple/medium/complex skills
- **Validation patterns**: 20+ checklist for quality
- **Integration guidance**: Which agents should use the skill

**Design Questions**:
```markdown
## Phase 1: Interview

1. **Purpose & Use Case**:
   - What task or domain should this skill help with?
   - When should Claude automatically use this skill?
   - Can you give 2-3 example scenarios?

2. **Scope & Complexity**:
   - Simple (just instructions)?
   - Medium (+ reference materials)?
   - Complex (+ scripts/templates)?

3. **Tools & Dependencies**:
   - What tools needed? (Read, Grep, Bash, etc.)
   - Any external dependencies?
   - Need templates or examples?

4. **Integration**:
   - Which agents might use this?
   - Relate to existing skills?
   - Any terminology or glossary?

## Phase 2: Design

[Proposes structure based on answers]

## Phase 3: Generate

[Creates complete SKILL.md with proper frontmatter]

## Phase 4: Validate

[Runs 20+ validation checks]

## Phase 5: Integrate

[Recommends which agents to add this to]

## Phase 6: Test

[Provides test scenarios]
```

**Output Structure**:
```
.claude/skills/[skill-name]/
├── SKILL.md (required)
├── examples.md (optional)
├── references/ (optional)
│   └── detailed-framework.md
├── scripts/ (optional)
│   └── automation.py
└── templates/ (optional)
    └── template.md
```

**Best for**: Extending framework capabilities, adding domain expertise, packaging reusable patterns

---

## Using Skills Effectively

### Triggering Skills

Skills load based on trigger keywords:

**✅ Explicit triggering**:
```
"Use SWOT analysis to evaluate our caching strategy"
→ Loads `analysis` skill
→ Uses SWOT framework specifically
```

**✅ Implicit triggering**:
```
"I need to verify our API documentation matches the implementation"
→ Loads `doc-compliance` skill (keywords: "verify", "documentation", "matches")
→ Uses compliance verification workflow
```

**✅ Combined triggering**:
```
"Analyze the authentication system for compliance with our security policy"
→ Loads `analysis` skill (keyword: "analyze")
→ Loads `doc-compliance` skill (keywords: "compliance", "policy")
→ Uses both together
```

### Progressive Disclosure in Action

```
# Initial state (metadata only)
Context usage: ~500 tokens (all skills metadata loaded)

User: "Analyze the caching strategy"

# Level 2 loads
→ `analysis` skill core workflow loads (~500 tokens)
→ Total context: ~1000 tokens

User: "Use SWOT analysis specifically"

# Level 3 loads
→ `analysis/frameworks.md` loads (~2000 tokens)
→ SWOT framework details available
→ Total context: ~3000 tokens
```

This allows unlimited skills while keeping startup context minimal.

### Combining Multiple Skills

Agents can use multiple skills together:

```
analyze-agent using:
- `analysis` skill: SWOT, decision matrices
- `implementation-guardrails` skill: Pre-implementation validation

Result: Analysis that includes quality gate checking
```

---

## Skill Anatomy

### Skill File Structure

```markdown
---
name: skill-name
description: What this skill does, when to use it. Trigger keywords - keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8, keyword9, keyword10.
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
project: false
---

# [Skill Name] Skill

## Purpose

[Clear statement of what this skill provides]

## When to Use

Use this skill when:
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

## Prerequisites

- [Requirement 1]
- [Requirement 2]

## Workflow

### Phase 1: [Name]
**Goal**: [What this achieves]
**Actions**:
- [Step 1]
- [Step 2]
**Quality Check**:
- [ ] [Validation]

[Phases 2-6...]

## Output Format

[Template for structured output]

## Quick Reference

[Essential patterns, checklists, templates]

## Integration

- **Used by agents**: [agent-1], [agent-2]
- **Combines with skills**: [skill-1], [skill-2]
- **Related tools**: [tool-1], [tool-2]

## Examples

### Example 1: [Scenario]
[Detailed walkthrough]

### Example 2: [Scenario]
[Detailed walkthrough]
```

### YAML Frontmatter

**Required fields**:
- `name`: Skill identifier (e.g., `analysis`)
- `description`: What it does + 10-15 trigger keywords
- `version`: Semantic versioning (e.g., `1.0.0`)

**Optional fields**:
- `allowed-tools`: Tools this skill needs
- `project`: `true` if project-specific, `false` if managed

### Trigger Keywords Strategy

**✅ Good description** (will trigger correctly):
```yaml
description: Systematic analysis patterns including SWOT, cost-benefit, risk matrices, decision matrices. Use for complex decisions, strategic evaluation, multi-factor comparison, options analysis, trade-off analysis. Trigger keywords - analyze, analysis, evaluate, assessment, compare, investigate, examine, study, review, decision, strategic, options, SWOT, cost-benefit, breakdown.
```

**❌ Poor description** (won't trigger):
```yaml
description: Helps with analysis
```

Include keywords for:
- **Primary actions**: analyze, evaluate, translate, proofread, verify
- **Related verbs**: investigate, examine, review, edit, check, validate
- **Domain terms**: SWOT, compliance, localization, grammar
- **Use cases**: decision-making, quality-checking, cultural-adaptation
- **Frameworks**: risk-matrix, cost-benefit, gap-analysis

---

## Skill Patterns

### Simple Skills (Instructions Only)

**Structure**:
```
.claude/skills/skill-name/
└── SKILL.md
```

**Use for**:
- Straightforward workflows
- Checklists and templates
- Basic patterns

**Example**: Simple validation skill with checklist

---

### Medium Skills (Instructions + References)

**Structure**:
```
.claude/skills/skill-name/
├── SKILL.md
└── references/
    └── detailed-framework.md
```

**Use for**:
- Complex frameworks
- Detailed methodologies
- Multiple approaches

**Example**: `analysis` skill with 10 frameworks in reference file

---

### Complex Skills (Instructions + References + Scripts + Templates)

**Structure**:
```
.claude/skills/skill-name/
├── SKILL.md
├── references/
│   └── specifications.md
├── scripts/
│   └── validation.py
└── templates/
    └── report-template.md
```

**Use for**:
- Automated workflows
- Validation with scripts
- Standardized outputs

**Example**: `implementation-guardrails` with validation script

---

## Best Practices

### When to Create New Skills

**✅ Create new skill when**:
- Reusable pattern used across projects
- Domain expertise to package
- Multiple agents will benefit
- Progressive disclosure valuable (large reference material)

**❌ Don't create skill when**:
- One-off task or project-specific
- Already covered by existing skill
- Too simple (just use instructions in agent)
- Won't be reused

### Designing Skill Workflow

**✅ Good workflow**:
- 3-6 clear phases
- Each phase has: Goal + Actions + Quality Check
- Progressive (builds on previous phases)
- Output template defined

**❌ Poor workflow**:
- Single "do everything" phase
- No validation checkpoints
- Unclear success criteria

### Progressive Disclosure Design

**Level 1 (Metadata)**: Essential info only
```yaml
name: analysis
description: [50-100 chars with keywords]
version: 1.0.0
```

**Level 2 (Core)**: Workflow and quick reference (~500 tokens)
```markdown
## Workflow
[3-6 phases with goals, actions, checks]

## Quick Reference
[Most common patterns]
```

**Level 3 (References)**: Deep detail (~2000+ tokens)
```markdown
# Detailed Frameworks
[10 comprehensive methodologies with examples]
```

---

## Advanced Usage

### Skill + Agent Integration

Add skills to agents via YAML frontmatter:

```yaml
---
name: analyze-agent
skills: analysis, implementation-guardrails
---
```

Agent automatically loads both skills when invoked.

### Skill Versioning

Use semantic versioning:

```yaml
version: 1.0.0  # Major.Minor.Patch
```

- **Major**: Breaking changes to workflow or output
- **Minor**: New features, new frameworks added
- **Patch**: Bug fixes, clarifications

### Skill Dependencies

Skills can reference each other:

```markdown
## Integration

**Combines well with**:
- `analysis` skill: For decision-making before validation
- `doc-compliance` skill: For checking architecture documentation

**Typical usage**:
1. Use `analysis` to evaluate options
2. Use `implementation-guardrails` before building
3. Use `doc-compliance` to verify against specs
```

---

## Creating Custom Skills

See [Developer Guide: Creating Skills](../developer-guide/creating-skills.md) for detailed instructions.

**Quick steps**:

1. **Use `/skill-crafter`** (recommended):
   ```
   /skill-crafter Create a skill for API testing
   ```

2. **Or create manually**:
   ```bash
   mkdir -p .claude/skills/my-skill
   touch .claude/skills/my-skill/SKILL.md
   ```

3. **Follow 3-level pattern**:
   - Level 1: YAML frontmatter with keywords
   - Level 2: Core workflow in SKILL.md
   - Level 3: References in separate files

4. **Test**:
   ```
   "Use my-skill to [task description]"
   ```

5. **Iterate**:
   - Adjust keywords if not triggering
   - Refine workflow based on usage
   - Add reference materials as needed

---

## Skill Categories

### Analysis Skills
- `analysis` - Systematic analysis frameworks

### Verification Skills
- `doc-compliance` - Documentation verification
- `implementation-guardrails` - Pre-implementation validation

### Content Skills
- `translation` - Translation and localization
- `proofreading` - Professional editing

### Meta-Skills
- `skill-crafter` - Create new skills

---

## Troubleshooting

### Skill Not Loading

**Problem**: Skill doesn't seem to be available

**Solutions**:
- Check YAML frontmatter is valid
- Verify file named exactly `SKILL.md`
- Use trigger keywords in your request
- Check skill directory structure correct
- Restart Claude Code to reload metadata

### Wrong Skill Loading

**Problem**: Different skill loads than expected

**Solutions**:
- Be more specific with keywords
- Check trigger keywords in skill descriptions
- Explicitly name the skill: "Use [skill-name] skill"
- Verify no keyword conflicts with other skills

### Skill Missing Capabilities

**Problem**: Skill doesn't have expected feature

**Solutions**:
- Check SKILL.md content for available workflows
- Look in references/ for detailed frameworks
- Verify you're using latest version
- Consider creating new skill if capability missing

### Skill Consumes Too Much Context

**Problem**: Skill causes context overflow

**Solutions**:
- Move detailed content to references/
- Use progressive disclosure properly
- Check Level 2 (core) is < 500 tokens
- Keep Level 1 (metadata) minimal

---

## Next Steps

1. **Try existing skills**: Use different skills in your requests
2. **Study skill files**: Read `.claude/skills/*/SKILL.md` to understand patterns
3. **Create custom skill**: Use `/skill-crafter` for your domain
4. **Integrate with agents**: Add skills to existing agents

## Related Documentation

- [Agents User Guide](agents.md) - Agents that use skills
- [Commands User Guide](commands.md) - Commands that orchestrate skills
- [Workflows Guide](workflows.md) - Multi-skill workflows
- [Developer Guide: Creating Skills](../developer-guide/creating-skills.md)
