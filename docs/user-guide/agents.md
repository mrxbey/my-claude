# User Guide: Agents

## Overview

Agents are specialized subagents that Claude automatically delegates to when tasks match their expertise. Unlike slash commands (user-invoked), agents are **model-invoked** - Claude decides when to use them based on their descriptions and trigger keywords.

Agents are ideal for:
- **Complex tasks**: Multi-phase work requiring independent context
- **Specialized expertise**: Domain-specific knowledge and workflows
- **Autonomous execution**: Self-contained tasks that run independently
- **Parallel work**: Multiple agents can work on different aspects simultaneously

## How Agents Work

### Automatic Delegation

When you make a request, Claude analyzes your intent and automatically delegates to the appropriate agent:

```
You: "Analyze our authentication system architecture"

Claude thinks: "This matches analyze-agent's expertise"
→ Automatically delegates to analyze-agent
→ analyze-agent performs 6-phase systematic analysis
→ Returns comprehensive report to Claude
→ Claude presents results to you
```

### Independent Context

Each agent runs with its own context window:
- **Fresh start**: No pollution from previous tasks
- **Focused expertise**: Only loads relevant skills and knowledge
- **Parallel execution**: Multiple agents can run simultaneously
- **Clean reports**: Returns structured output to main Claude

### Agent Lifecycle

```
1. Trigger Detection
   └─ Claude matches your request to agent description

2. Agent Launch
   └─ Loads agent prompt, skills, permissions

3. Autonomous Execution
   └─ Agent follows its workflow independently

4. Report Back
   └─ Returns structured output to Claude

5. Integration
   └─ Claude incorporates results into response
```

---

## Available Agents

### Core Business Agents

#### analyze-agent

**Expertise**: Deep analysis of code, data, business situations, and complex problems

**When Claude uses it**:
- "Analyze the caching strategy"
- "Evaluate these deployment options"
- "Compare database architectures"
- "Review the authentication flow"

**Workflow** (6 phases):
1. **Clarify**: Restate problem, identify sub-questions
2. **Decompose**: Break into dimensions, note constraints
3. **Investigate**: Explore codebase, gather evidence
4. **Options**: Generate 2-4 realistic alternatives
5. **Synthesize**: Evaluate trade-offs, make recommendation
6. **Present**: Structured report with action checklist

**Skills used**:
- `analysis` - Systematic analysis patterns and frameworks
- `implementation-guardrails` - Quality gate validation

**Tools**: Read, Grep, Glob, Edit, Write, Bash

**Output format**:
```markdown
# [Analysis Topic]

## Context
Brief problem statement

## Key Findings
- Finding 1 with evidence (file:line)
- Finding 2 with evidence

## Options Analysis
| Option | Pros | Cons | Complexity |
|--------|------|------|------------|
| A      | ... | ...  | Low        |

## Recommendation
[Clear recommendation with rationale]

## Action Checklist
- [ ] Specific step 1
- [ ] Specific step 2
```

**Best for**: Architecture decisions, strategic planning, complex evaluations

---

#### docs-agent

**Expertise**: Documentation verification, policy compliance, requirements validation

**When Claude uses it**:
- "Check if the API docs match the implementation"
- "Verify compliance with our security policy"
- "Validate requirements coverage"
- "Review documentation accuracy"

**Workflow** (5 steps):
1. **Discovery**: Identify relevant documentation and policies
2. **Requirements**: Extract testable requirements with IDs
3. **Verification**: Check implementation against requirements
4. **Gap Analysis**: Identify missing/incorrect documentation
5. **Reporting**: Compliance table with remediation roadmap

**Skills used**:
- `doc-compliance` - Documentation verification patterns
- `analysis` - Investigation and synthesis

**Tools**: Read, Grep, Glob, Edit, Write, Bash

**Output format**:
```markdown
# Documentation Compliance Report

## Requirements Table
| ID | Requirement | Status | Evidence | Priority |
|----|-------------|--------|----------|----------|
| SEC-001 | Authentication | ✅ | src/auth.js:12 | Critical |
| SEC-002 | Rate limiting | ⚠️ | Partial | High |
| API-001 | Endpoint docs | ❌ | Missing | Medium |

## Gap Analysis
**Critical Gaps** (3):
- [Gap with specific fix]

**High Priority** (5):
- [Gap with specific fix]

## Remediation Roadmap
Week 1: Fix critical gaps → [expected outcome]
Week 2-3: Address high priority → [expected outcome]
```

**Best for**: Documentation audits, compliance checking, policy verification

---

#### translate-agent

**Expertise**: High-quality translation and localization with cultural adaptation

**When Claude uses it**:
- "Translate this to Spanish"
- "Localize documentation for French users"
- "Adapt marketing copy for Japanese audience"
- "Convert this to formal German"

**Workflow** (6 steps):
1. **Context**: Understand target language, audience, formality
2. **Glossary**: Build/update project terminology
3. **Translate**: Preserve meaning, adapt tone
4. **Cultural**: Handle cultural references appropriately
5. **Variants**: Provide alternatives for ambiguous sections
6. **Document**: Note translation decisions

**Skills used**:
- `translation` - Translation patterns, glossaries, cultural adaptation

**Tools**: Read, Grep, Glob, Edit, Write

**Output format**:
```markdown
# Translation: [Source] → [Target]

## Translated Content
[Full translation]

## Project Glossary
| Source Term | Translation | Notes |
|-------------|-------------|-------|
| Authentication | Autenticación | Standard term |
| Dashboard | Panel de control | Preferred over "Tablero" |

## Translation Decisions
**Line 15**: "Get started" → "Comenzar"
- Alternative: "Empezar" (more casual)
- Rationale: Matches formal tone of audience

## Quality Metrics
- Word count: 1,234 → 1,189 (96%)
- Formality: Formal (as requested)
- Cultural adaptations: 3
```

**Best for**: Documentation localization, content adaptation, multi-language support

---

#### proofread-agent

**Expertise**: Professional editing, grammar, clarity, style consistency

**When Claude uses it**:
- "Proofread this blog post"
- "Edit the user documentation for clarity"
- "Fix grammar and improve tone"
- "Polish this README"

**Workflow** (5 categories):
1. **Grammar**: Punctuation, spelling, syntax
2. **Clarity**: Simplify complex sentences, remove ambiguity
3. **Structure**: Headings, flow, organization
4. **Tone**: Consistency, audience appropriateness
5. **Terminology**: Consistent usage across document

**Skills used**:
- `proofreading` - Editing patterns, checklists, style enforcement

**Tools**: Read, Grep, Glob, Edit, Write

**Output format**:
```markdown
# Proofread: [Document Name]

## Edited Content
[Full edited version]

## Change Summary

**Grammar & Punctuation** (12 changes):
- Fixed 5 comma splices
- Corrected 3 subject-verb agreements
- Fixed 4 spelling errors

**Clarity** (8 improvements):
- Simplified 5 complex sentences
- Removed 3 instances of passive voice

**Structure** (3 changes):
- Added missing H2 heading
- Reorganized introduction for better flow

**Tone** (2 adjustments):
- Changed formal → conversational (as requested)

## Major Improvements
### Before:
"The utilization of the aforementioned methodology..."

### After:
"Using this approach..."
```

**Best for**: Content polishing, consistency enforcement, quality improvement

---

### Meta-Agents

#### skill-crafter

**Expertise**: Creating new Claude Code skills through interactive design

**When Claude uses it**:
- "Create a skill for API testing"
- "I need a skill for data validation"
- "Design a skill for performance optimization"
- Explicitly: `/skill-crafter <description>`

**Workflow** (6 phases):
1. **Interview**: Purpose, use cases, scope, complexity
2. **Design**: Structure, workflow phases, tools needed
3. **Generate**: Complete SKILL.md with YAML frontmatter
4. **Validate**: Check structure, trigger keywords, quality
5. **Integrate**: Recommendations for which agents should use it
6. **Test**: Provide test scenarios to verify it works

**Skills used**:
- `skill-crafter` - Meta-skill for skill generation
- `analysis` - Design evaluation

**Tools**: Read, Grep, Glob, Write

**Output**: Complete skill in `.claude/skills/[skill-name]/SKILL.md`

**Best for**: Extending framework capabilities, adding domain expertise

---

#### agent-crafter

**Expertise**: Creating new Claude Code agents through interactive design

**When Claude uses it**:
- "Create an agent for security audits"
- "I need an agent for database migrations"
- "Design an agent for customer support"
- Explicitly: `/agent-crafter <description>`

**Workflow** (6 phases):
1. **Interview**: Role, typical tasks, complexity level
2. **Design**: Identity, workflow pattern, decision-making
3. **Tools**: Permissions (read-only, standard, execution)
4. **Skills**: Which existing skills to integrate
5. **Generate**: Complete agent.md with YAML + prompt
6. **Validate**: Test invocation, integration

**Skills used**:
- `analysis` - Design evaluation

**Tools**: Read, Grep, Glob, Write

**Output**: Complete agent in `.claude/agents/[agent-name].md`

**Best for**: Adding specialized agents, building new expertise areas

---

## Using Agents Effectively

### Triggering Agents

Agents trigger based on natural language requests that match their descriptions:

**✅ Good trigger phrases**:
```
"Analyze the authentication system architecture"
→ analyze-agent

"Check if our docs match the implementation"
→ docs-agent

"Translate this to Spanish"
→ translate-agent

"Proofread the README for clarity"
→ proofread-agent
```

**❌ Vague requests** (may not trigger):
```
"Look at this code"
→ Too vague, no clear agent match

"Help me with something"
→ No expertise indicated
```

### Providing Context

Give agents sufficient context to work with:

**✅ Good context**:
```
Analyze our authentication system in src/auth/.
Focus on security and scalability.
Compare our approach to industry best practices.
```

**✅ With files**:
```
Check documentation compliance:
@docs/api-spec.md - Our API specification
@src/api/ - Implementation

Verify all endpoints documented correctly.
```

**❌ Insufficient context**:
```
"Analyze this"
→ Analyze what? Where? What aspects?
```

### Combining Multiple Agents

Claude can coordinate multiple agents for complex tasks:

```
You: "Review the authentication system - check the code quality,
     verify the documentation, and ensure our implementation
     follows security best practices"

Claude coordinates:
1. analyze-agent → Code architecture and security analysis
2. docs-agent → Documentation compliance verification
3. Both reports combined into unified review
```

---

## Agent Anatomy

### Agent File Structure

Agents are Markdown files in `.claude/agents/` with YAML frontmatter:

```markdown
---
name: analyze-agent
description: Deep analysis specialist for code, data, business situations, and complex problems. Use for systematic evaluation, strategic thinking, multi-factor comparison. Trigger keywords - analyze, analysis, evaluate, assessment, compare, investigate, examine, study, review.
tools: Read, Grep, Glob, Edit, Write, Bash
model: sonnet
permissionMode: default
skills: analysis, implementation-guardrails
---

# You are the Analysis Agent

**Role**: Systematic analysis specialist

**Primary Question**: "What are we analyzing and what decision needs to be made?"

## When to Use

You are automatically invoked when...

## Workflow

### Phase 1: Clarification
**Goal**: [What this phase achieves]
**Actions**:
- [Step 1]
- [Step 2]
**Quality Check**:
- [ ] Criteria 1

[Additional phases...]

## Output Template

[Structured output format]
```

### YAML Frontmatter Fields

**Required**:
- `name`: Agent identifier (e.g., `analyze-agent`)
- `description`: What agent does + trigger keywords (100-200 chars)
- `tools`: List of allowed tools (Read, Grep, Glob, Edit, Write, Bash, Task, WebFetch)
- `model`: Model to use (sonnet, opus, haiku, inherit)

**Optional**:
- `skills`: Comma-separated list of skills to auto-load
- `permissionMode`: Permission handling (default, acceptEdits, plan)

### Agent Identity

Each agent has a clear professional identity:

```markdown
# You are the [Name] Agent

**Role**: [Specific expertise area]

**Primary Question**: "[Core question you ask for every task]"

**Decision Pattern**: [How you think about problems]

**Approach**: [Your methodology in 2-3 sentences]
```

### Workflow Structure

Agents follow structured workflows with phases:

```markdown
### Phase 1: [Name]

**Goal**: [Clear objective]

**Actions**:
1. [Specific action]
2. [Specific action]

**Quality Check**:
- [ ] [Validation criterion]
- [ ] [Validation criterion]
```

---

## Agent Patterns

### Read-Only Agents

**Purpose**: Analysis, review, verification (no modifications)

**Tools**: Read, Grep, Glob

**Use for**:
- Code analysis
- Documentation review
- Compliance checking
- Security audits

**Example**: docs-agent (verification only)

---

### Standard Agents

**Purpose**: Analysis + content creation/editing

**Tools**: Read, Grep, Glob, Edit, Write

**Use for**:
- Documentation updates
- Content creation
- Refactoring
- Translation

**Example**: translate-agent, proofread-agent

---

### Execution Agents

**Purpose**: Full capabilities including command execution

**Tools**: Read, Grep, Glob, Edit, Write, Bash

**Use for**:
- Testing
- Automation
- Complex workflows
- System operations

**Example**: analyze-agent (runs tests, checks git history)

**⚠️ Caution**: Requires careful permission configuration

---

### Meta-Agents

**Purpose**: Framework extension and self-improvement

**Tools**: Read, Grep, Glob, Write

**Use for**:
- Creating new agents
- Creating new skills
- Framework evolution

**Example**: skill-crafter, agent-crafter

---

## Best Practices

### When to Create New Agents

**✅ Create new agent when**:
- Distinct area of expertise not covered
- Complex multi-phase workflow needed
- Independent context important (memory isolation)
- Will be reused across multiple projects

**❌ Don't create agent when**:
- Simple one-off task
- Can be handled by existing agent + skill
- Just need a slash command workflow
- Too specialized (will rarely be used)

### Designing Agent Identity

**Strong identity example**:
```markdown
**Role**: Documentation Verification Specialist

**Primary Question**: "What documentation exists and does it accurately
reflect the implementation?"

**Decision Pattern**: Evidence-first - I never assume documentation is
correct, I verify every claim against source code.

**Approach**: Systematic verification using compliance tables, gap
analysis, and specific file:line references.
```

**Weak identity** (too vague):
```markdown
**Role**: Helper

**Approach**: I help with things
```

### Workflow Design

**✅ Good workflow**:
- 3-6 clear phases
- Each phase has Goal + Actions + Quality Check
- Progressive (each phase builds on previous)
- Validation loops (check quality before proceeding)
- Clear output template

**❌ Poor workflow**:
- Single "do everything" step
- No validation checkpoints
- Unclear success criteria
- No structured output

### Trigger Keyword Strategy

**✅ Good description** (will trigger correctly):
```
Deep analysis specialist for code, data, business situations, and
complex problems. Use for systematic evaluation, strategic thinking,
multi-factor comparison, decision-making. Trigger keywords - analyze,
analysis, evaluate, assessment, compare, investigate, examine, study,
review, breakdown.
```

**❌ Poor description** (won't trigger):
```
Helps with analysis
```

Include 10-15 trigger keywords covering:
- Primary actions (analyze, evaluate, translate, proofread)
- Related verbs (investigate, examine, review, edit)
- Domain terms (compliance, verification, localization)
- Use cases (decision-making, quality-checking)

---

## Advanced Usage

### Agent + Skill Combinations

Agents are more powerful when they use skills:

```yaml
---
name: analyze-agent
skills: analysis, implementation-guardrails
---
```

This agent automatically loads:
- `analysis` skill: Provides 10 analysis frameworks (SWOT, Cost-Benefit, etc.)
- `implementation-guardrails`: Provides 5-check quality gates

### Permission Modes

**`permissionMode: default`**
- Uses global permissions from settings.json
- Standard for most agents

**`permissionMode: acceptEdits`**
- Can make edits without asking each time
- Use for editing/refactoring agents

**`permissionMode: plan`**
- Plan mode: presents changes before executing
- Use for high-risk operations

### Model Selection

**`model: sonnet`** (default)
- Best balance of capability and speed
- Use for most agents

**`model: opus`**
- Maximum reasoning capability
- Use for very complex analysis
- Higher cost and latency

**`model: haiku`**
- Fastest and cheapest
- Use for simple, routine tasks
- Lower reasoning capability

**`model: inherit`**
- Uses same model as parent
- Use when context sharing important

---

## Troubleshooting

### Agent Not Triggering

**Problem**: Your request doesn't invoke the expected agent

**Solutions**:
- Use more specific trigger keywords from description
- Be explicit: "Use analyze-agent to examine..."
- Check agent description has sufficient keywords
- Try slash command instead: `/analyze`

### Agent Produces Unexpected Output

**Problem**: Agent doesn't follow expected workflow

**Solutions**:
- Check agent's workflow in `.claude/agents/[agent].md`
- Verify skills are loading correctly
- Provide clearer context in your request
- Check for permission restrictions

### Agent Can't Access Files

**Problem**: Agent reports "permission denied"

**Solutions**:
- Check `.claude/settings.json` permissions
- Verify agent has required tools (Read, Glob, etc.)
- Check file paths are correct
- Verify files exist and are readable

### Agent Loads Wrong Skills

**Problem**: Agent doesn't have expected capabilities

**Solutions**:
- Check agent's `skills:` in YAML frontmatter
- Verify skills exist in `.claude/skills/`
- Check skill YAML is valid
- Try specifying skill explicitly in request

---

## Creating Custom Agents

See [Developer Guide: Creating Agents](../developer-guide/creating-agents.md) for detailed instructions.

**Quick steps**:

1. **Use `/agent-crafter`** (recommended):
   ```
   /agent-crafter Create an agent for database migrations
   ```

2. **Or create manually**:
   ```bash
   touch .claude/agents/my-agent.md
   ```

3. **Follow pattern**:
   - YAML frontmatter with required fields
   - Clear agent identity
   - Structured workflow (3-6 phases)
   - Output template
   - Quality standards

4. **Test**:
   ```
   "Use my-agent to [task description]"
   ```

5. **Iterate**:
   - Adjust description if not triggering
   - Refine workflow based on results
   - Add skills as needed

---

## Agent Categories

### Analysis Agents
- `analyze-agent` - Deep systematic analysis

### Verification Agents
- `docs-agent` - Documentation compliance

### Content Agents
- `translate-agent` - Translation and localization
- `proofread-agent` - Professional editing

### Meta-Agents
- `skill-crafter` - Create new skills
- `agent-crafter` - Create new agents

---

## Next Steps

1. **Try existing agents**: Make requests that trigger different agents
2. **Study agent files**: Read `.claude/agents/*.md` to understand patterns
3. **Create custom agent**: Use `/agent-crafter` for your domain
4. **Combine with skills**: Enhance agents with relevant skills

## Related Documentation

- [Skills User Guide](skills.md) - Understanding skills that agents use
- [Commands User Guide](commands.md) - User-invoked workflows
- [Workflows Guide](workflows.md) - Multi-agent orchestration
- [Developer Guide: Creating Agents](../developer-guide/creating-agents.md)
