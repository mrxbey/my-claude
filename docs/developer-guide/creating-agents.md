# Developer Guide: Creating Agents

## Overview

This guide covers how to create custom agents for the MyClaude framework. Agents are specialized subagents that Claude automatically delegates to when tasks match their expertise.

## When to Create an Agent

Create a new agent when:

✅ **Distinct expertise area**: The agent fills a gap in existing agent coverage
✅ **Complex workflows**: Requires multi-phase autonomous execution
✅ **Independent context**: Benefits from isolated context window
✅ **Reusable across projects**: Will be used beyond single project

❌ Don't create an agent when:

- Simple one-off task → Use regular Claude
- Just need user-invoked workflow → Use slash command instead
- Can be handled by existing agent + skill → Extend existing agent
- Too specialized for single project → Use project-specific instructions

## Creation Methods

### Method 1: Using `/agent-crafter` (Recommended)

The fastest way to create an agent is using the meta-agent:

```
/agent-crafter Create an agent for database migrations
```

The agent-crafter will:
1. Interview you about requirements
2. Design agent identity and workflow
3. Generate complete agent file
4. Validate structure
5. Provide integration recommendations
6. Give you test scenarios

**Advantages**:
- Interactive design process
- Validates structure automatically
- Follows best practices
- Generates complete file
- Provides testing guidance

### Method 2: Manual Creation

For full control or learning purposes, create manually:

```bash
# Create agent file
touch .claude/agents/my-agent.md

# Edit with your preferred editor
code .claude/agents/my-agent.md
```

**Advantages**:
- Full control over structure
- Learn agent anatomy deeply
- Customize without constraints

## Agent File Structure

### Template

```markdown
---
name: agent-name
description: What this agent does, its expertise area. Use for [use cases]. Trigger keywords - keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8, keyword9, keyword10.
tools: Read, Grep, Glob, Edit, Write, Bash
model: sonnet
permissionMode: default
skills: skill1, skill2
---

# You are the [Name] Agent

**Role**: [Specific expertise area]

**Primary Question**: "[Core question you ask for every task]"

**Decision Pattern**: [How you think about problems]

**Approach**: [Your methodology in 2-3 sentences]

## When to Use

You are automatically invoked when:
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

Do not use when:
- [Anti-pattern 1]
- [Anti-pattern 2]

## Workflow

### Phase 1: [Name]

**Goal**: [Clear objective for this phase]

**Actions**:
1. [Specific action step]
2. [Specific action step]
3. [Specific action step]

**Quality Check**:
- [ ] [Validation criterion]
- [ ] [Validation criterion]
- [ ] [Validation criterion]

**If quality check fails**: [Remediation steps]

### Phase 2: [Name]

[Same pattern...]

[3-6 phases total]

## Skills I Use

**[skill-name]**:
- What: [What this skill provides]
- When: [When I use it]
- How: [How I use it in my workflow]

[List all skills from frontmatter]

## Tools & Techniques

### [Tool/Technique Name]

**Purpose**: [What this is for]

**Usage**:
```
[Example command or pattern]
```

**In my workflow**: [How this fits into phases]

[3-5 tools/techniques]

## Output Template

[Structured format for agent's output]

```markdown
# [Standard Output Format]

## [Section 1]
[Expected content]

## [Section 2]
[Expected content]

## [Section 3 - Always Present]
- [ ] [Action item template]
```

## Quality Standards

All outputs from this agent must:
- [ ] [Quality criterion 1]
- [ ] [Quality criterion 2]
- [ ] [Quality criterion 3]
- [ ] [Quality criterion 4]

## Integration

**Invoked by**: Main Claude when [trigger pattern]

**Coordinates with**:
- `[other-agent]`: [How they work together]
- `[another-agent]`: [How they work together]

**Used in workflows**:
- `/workflows/[workflow-name]`: [Role in workflow]

## Examples

### Example 1: [Typical Scenario]

**Input**: [What the user asks]

**My Process**:
1. [Phase 1 actions for this case]
2. [Phase 2 actions for this case]
3. [Phase 3 actions for this case]

**Output**: [What I produce]

### Example 2: [Edge Case]

[Same pattern...]

[2-3 examples total]
```

## YAML Frontmatter Reference

### Required Fields

**`name`**: Agent identifier (lowercase, hyphenated)
```yaml
name: database-migration-agent
```

**`description`**: What agent does + trigger keywords (100-200 chars)
```yaml
description: Database migration specialist for schema changes, data transformations, rollback plans. Use for migrations, schema updates, data integrity. Trigger keywords - migrate, migration, database, schema, transform, rollback, integrity, version, upgrade.
```

**`tools`**: Comma-separated list of allowed tools
```yaml
tools: Read, Grep, Glob, Edit, Write, Bash
```

Options: `Read`, `Grep`, `Glob`, `Edit`, `Write`, `Bash`, `Task`, `WebFetch`

**`model`**: Which model to use
```yaml
model: sonnet
```

Options:
- `sonnet`: Default, best balance (recommended)
- `opus`: Maximum reasoning for very complex tasks
- `haiku`: Fastest for simple tasks
- `inherit`: Use same as parent (context sharing)

### Optional Fields

**`permissionMode`**: How to handle permissions
```yaml
permissionMode: default
```

Options:
- `default`: Use global permissions from settings.json
- `acceptEdits`: Can make edits without asking each time
- `plan`: Present changes before executing (plan mode)

**`skills`**: Comma-separated list of skills to auto-load
```yaml
skills: analysis, implementation-guardrails, doc-compliance
```

## Agent Identity Design

### Strong Identity Example

```markdown
# You are the Documentation Verification Agent

**Role**: Documentation accuracy and compliance specialist

**Primary Question**: "What documentation exists and does it accurately reflect the implementation?"

**Decision Pattern**: Evidence-first - I never assume documentation is correct. I verify every claim against source code with specific file:line references.

**Approach**: Systematic verification using compliance tables. I extract requirements from docs, check each against implementation, mark with ✅/⚠️/❌, and provide gap analysis with specific remediation steps.
```

**Why this works**:
- Clear role definition
- Explicit primary question
- Documented decision pattern
- Concrete approach

### Weak Identity Example

```markdown
# You are the Helper Agent

**Role**: Helps with things

**Approach**: I help when needed
```

**Why this fails**:
- Too vague
- No clear expertise
- No decision pattern
- Won't trigger correctly

## Workflow Design

### Phase Structure

Each phase should have:

```markdown
### Phase [N]: [Clear Phase Name]

**Goal**: [Single clear objective]

**Actions**:
1. [Concrete actionable step]
2. [Concrete actionable step]
3. [Concrete actionable step]

**Quality Check**:
- [ ] [Testable validation criterion]
- [ ] [Testable validation criterion]

**If quality check fails**: [Specific remediation]
```

### Good Workflow Example (6 phases)

```markdown
### Phase 1: Understand Migration Need

**Goal**: Clear understanding of schema changes required

**Actions**:
1. Read current schema from database/migrations
2. Understand desired state from requirements
3. Identify all tables, columns, constraints affected
4. Note data that must be preserved

**Quality Check**:
- [ ] Current schema documented
- [ ] Target schema documented
- [ ] All affected entities identified
- [ ] Data preservation plan exists

**If quality check fails**: Return to requirements, clarify gaps

### Phase 2: Design Migration

[Similar structure...]

### Phase 3: Write Migration Code

[Similar structure...]

### Phase 4: Plan Rollback

[Similar structure...]

### Phase 5: Test Migration

[Similar structure...]

### Phase 6: Document Migration

[Similar structure...]
```

**Why this works**:
- 6 distinct phases
- Each has clear goal
- Concrete actions
- Testable quality checks
- Remediation paths

### Poor Workflow Example

```markdown
### Phase 1: Do the migration

**Goal**: Make it work

**Actions**:
- Figure it out
- Do the stuff
- Check if okay
```

**Why this fails**:
- Too vague
- No concrete actions
- No quality criteria
- No structure

## Trigger Keyword Strategy

### Keywords Formula

Include 10-15 keywords covering:

1. **Primary actions** (2-3): Main verbs for what agent does
   - Example: "migrate", "transform", "rollback"

2. **Domain terms** (3-4): Technical terminology
   - Example: "database", "schema", "SQL", "integrity"

3. **Related actions** (2-3): Similar or related verbs
   - Example: "upgrade", "version", "change"

4. **Use cases** (2-3): When to use this agent
   - Example: "production-migration", "data-preservation"

5. **Outcomes** (1-2): What agent produces
   - Example: "rollback-plan", "migration-script"

### Good Description Example

```yaml
description: Database migration specialist for schema changes, data transformations, and rollback planning. Use for production migrations, schema versioning, data integrity preservation. Trigger keywords - migrate, migration, database, schema, transform, rollback, integrity, version, upgrade, SQL, data-preservation, production-migration.
```

**Coverage**:
- ✅ Clear expertise: "Database migration specialist"
- ✅ Use cases: "schema changes, data transformations, rollback planning"
- ✅ When to use: "production migrations, schema versioning"
- ✅ 12 trigger keywords covering all bases

### Poor Description Example

```yaml
description: Helps with databases
```

**Problems**:
- ❌ Too vague
- ❌ No trigger keywords
- ❌ Unclear when to use

## Tool Selection

### Read-Only Agents

**Tools**: `Read, Grep, Glob`

**Use for**:
- Analysis and review
- Verification and auditing
- Documentation checking
- Security assessment (read-only)

**Example**: Agent that reviews code but never modifies

```yaml
tools: Read, Grep, Glob
```

### Standard Agents

**Tools**: `Read, Grep, Glob, Edit, Write`

**Use for**:
- Documentation updates
- Content creation
- Code refactoring
- Translation

**Example**: Agent that creates/edits documentation

```yaml
tools: Read, Grep, Glob, Edit, Write
```

### Execution Agents

**Tools**: `Read, Grep, Glob, Edit, Write, Bash`

**Use for**:
- Testing
- Automation
- Migrations
- Complex workflows with system commands

**Example**: Agent that runs tests and checks git history

```yaml
tools: Read, Grep, Glob, Edit, Write, Bash
```

**⚠️ Security Consideration**: Full access requires careful permission configuration

### Advanced Agents

**Tools**: `Read, Grep, Glob, Edit, Write, Bash, Task, WebFetch`

**Use for**:
- Complex orchestration (Task for sub-agents)
- Research requiring web access (WebFetch)
- Multi-layer workflows

**Example**: Agent that delegates to other agents and fetches external docs

```yaml
tools: Read, Grep, Glob, Edit, Write, Bash, Task, WebFetch
```

## Skill Integration

### Selecting Skills

Choose skills that complement your agent's workflow:

```yaml
skills: analysis, implementation-guardrails
```

**Analysis skill**: Provides systematic analysis frameworks
**Implementation-guardrails**: Provides pre-implementation validation

### Using Skills in Workflow

Reference skills explicitly in your phases:

```markdown
### Phase 2: Pre-Implementation Validation

**Goal**: Ensure we're building the right thing

**Actions**:
1. Use **implementation-guardrails skill** to run 5-check validation:
   - Duplicate Check (0.0-1.0)
   - Architecture Fit (0.0-1.0)
   - Documentation Compliance (0.0-1.0)
   - Existing Solutions (0.0-1.0)
   - Problem Understanding (0.0-1.0)

2. Calculate overall confidence score
3. If score < 0.7, stop and re-analyze

**Quality Check**:
- [ ] All 5 dimensions scored
- [ ] Confidence ≥ 0.7 (preferably ≥ 0.9)
```

### Skills Section

Document how you use each skill:

```markdown
## Skills I Use

**analysis**:
- What: Provides 10 analysis frameworks (SWOT, Cost-Benefit, etc.)
- When: During Phases 1 and 2 for evaluation
- How: Use SWOT for pros/cons, Decision Matrix for options comparison

**implementation-guardrails**:
- What: 5-check pre-implementation validation
- When: Before starting implementation (Phase 3)
- How: Score each dimension, ensure confidence ≥ 0.7
```

## Output Template Design

### Structured Output

Define consistent output format:

```markdown
## Output Template

```markdown
# [Agent Name]: [Task Description]

## Executive Summary
- **Status**: [Status indicator]
- **Key Finding**: [Most important finding]
- **Recommendation**: [Primary recommendation]

## Detailed Analysis

### [Section 1]
[Structured content]

### [Section 2]
[Structured content]

## Action Items
- [ ] [Prioritized action 1]
- [ ] [Prioritized action 2]
- [ ] [Prioritized action 3]

## Appendix
[Supporting data, references]
```
```

### Quality Standards

Define what constitutes good output:

```markdown
## Quality Standards

All outputs from this agent must:
- [ ] Include specific file:line references for all findings
- [ ] Prioritize issues (Critical, High, Medium, Low)
- [ ] Provide actionable recommendations (not just identify problems)
- [ ] Include evidence for all claims
- [ ] Use consistent formatting (markdown, tables)
- [ ] End with clear next steps
```

## Testing Your Agent

### Test Invocation

1. **Create test request**:
   ```
   [Create a request that should trigger your agent based on keywords]
   ```

2. **Verify agent loads**:
   - Check Claude delegates to your agent
   - Verify agent identity appears
   - Confirm skills load

3. **Check workflow execution**:
   - Phases execute in order
   - Quality checks happen
   - Output matches template

### Test Scenarios

Create 3-5 test scenarios:

```markdown
## Test Scenarios

### Test 1: Basic Use Case
**Input**: "Migrate user table to add email verification field"
**Expected**:
- Agent triggers on "migrate" keyword
- Loads database-migration-agent
- Executes 6-phase workflow
- Produces migration SQL + rollback plan

### Test 2: Edge Case
**Input**: "Migrate production database with 10M users"
**Expected**:
- Identifies this as high-risk production migration
- Extra validation in Phase 2
- More thorough testing in Phase 5
- Includes downtime plan

### Test 3: Wrong Use Case
**Input**: "Just read the database schema"
**Expected**:
- Agent should NOT trigger (no migration needed)
- Regular Claude handles simple read
```

## Validation

### Use Framework Validator

Run validation script:

```bash
python scripts/validate_framework.py --verbose
```

This checks:
- YAML frontmatter well-formed
- Required fields present
- Tools are valid
- Model is valid
- Skills exist
- Description has trigger keywords

### Manual Validation Checklist

- [ ] **YAML frontmatter**:
  - [ ] All required fields present
  - [ ] Tools list valid
  - [ ] Model valid (sonnet/opus/haiku/inherit)
  - [ ] Skills exist

- [ ] **Agent identity**:
  - [ ] Clear role definition
  - [ ] Primary question defined
  - [ ] Decision pattern documented
  - [ ] Approach concrete

- [ ] **Workflow**:
  - [ ] 3-6 phases
  - [ ] Each phase has Goal + Actions + Quality Check
  - [ ] Quality checks are testable
  - [ ] Remediation paths clear

- [ ] **Output template**:
  - [ ] Structured format defined
  - [ ] Consistent across uses
  - [ ] Quality standards explicit

- [ ] **Description**:
  - [ ] 10-15 trigger keywords
  - [ ] Clear expertise area
  - [ ] Use cases documented

- [ ] **Integration**:
  - [ ] Skills documented
  - [ ] Examples provided
  - [ ] Coordination with other agents noted

## Integration

### Add to README

Update `.claude/agents/README.md`:

```markdown
#### my-agent

**Expertise**: [What this agent does]

**When used**:
- [Trigger scenario 1]
- [Trigger scenario 2]

**Output**: [What it produces]

**Skills**: [List of skills]
```

### Coordinate with Other Agents

Document how your agent works with others:

```markdown
## Integration

**Coordinates with**:
- `analyze-agent`: I use analyze-agent for evaluation phase
- `docs-agent`: I delegate to docs-agent for compliance checking

**Used in workflows**:
- `/workflows/database-changes`: Phase 3 uses my migration capabilities
```

### Update Workflows

If agent should be used in workflows, update workflow commands:

```markdown
### Phase 3: Database Migration (database-migration-agent)

**Use database-migration-agent** to create migration:
[Instructions for using your agent in this phase]
```

## Advanced Topics

### Multi-Agent Coordination

Use `Task` tool to delegate to other agents:

```markdown
### Phase 2: Analysis

**Actions**:
1. Use Task tool to invoke **analyze-agent** for evaluation:
   ```
   Analyze the database schema and identify optimization opportunities
   ```

2. Wait for analyze-agent report

3. Incorporate findings into migration plan
```

### Permission Modes

**Plan Mode** for high-risk operations:

```yaml
permissionMode: plan
```

Agent presents plan before executing:
```markdown
### Phase 4: Execute Migration

**Plan presentation**:
1. Show migration SQL
2. Show rollback SQL
3. Show expected impact
4. Request approval

**After approval**:
[Execute migration]
```

### Model Selection Strategy

**Use sonnet** (default):
- Most agents
- Good balance of capability/speed

**Use opus**:
- Very complex reasoning required
- Critical decisions
- Complex analysis

**Use haiku**:
- Simple, routine tasks
- Speed is priority
- Lower cost acceptable

**Use inherit**:
- Need to share context with parent
- Prefer continuous conversation

## Common Patterns

### Analysis Agent Pattern

```yaml
tools: Read, Grep, Glob, Bash
skills: analysis, implementation-guardrails
model: sonnet
```

Workflow: Clarify → Decompose → Investigate → Options → Synthesize → Present

### Verification Agent Pattern

```yaml
tools: Read, Grep, Glob
skills: doc-compliance
model: sonnet
```

Workflow: Discovery → Requirements → Verification → Gap Analysis → Report

### Content Agent Pattern

```yaml
tools: Read, Grep, Glob, Edit, Write
skills: [content-specific-skill]
model: sonnet
```

Workflow: Understand → Draft → Refine → Validate → Deliver

### Execution Agent Pattern

```yaml
tools: Read, Grep, Glob, Edit, Write, Bash
skills: [domain-skills]
model: sonnet
permissionMode: plan
```

Workflow: Plan → Validate → Execute → Verify → Report

## Troubleshooting

### Agent Not Triggering

**Problem**: Claude doesn't delegate to your agent

**Solutions**:
- Add more trigger keywords to description
- Make description more specific about use cases
- Test with explicit trigger words
- Check for conflicts with other agent descriptions

### Agent Produces Inconsistent Output

**Problem**: Output format varies

**Solutions**:
- Strengthen output template section
- Add more specific quality standards
- Include example outputs
- Make workflow steps more prescriptive

### Agent Workflow Too Complex

**Problem**: Agent gets confused in workflow

**Solutions**:
- Reduce number of phases (3-6 is optimal)
- Make each phase more focused
- Simplify quality checks
- Add more explicit remediation paths

### Agent Lacks Expertise

**Problem**: Agent doesn't have needed capabilities

**Solutions**:
- Add relevant skills to frontmatter
- Document skills usage in workflow
- Add tools if needed (Edit, Write, Bash)
- Consider using Task tool to delegate

## Example: Complete Agent

See `.claude/agents/analyze-agent.md` for a complete production example.

## Next Steps

1. **Use `/agent-crafter`** to create your first custom agent
2. **Test thoroughly** with various scenarios
3. **Iterate** based on results
4. **Document** in README and integrate with workflows
5. **Share** with team via version control

## Related Documentation

- [User Guide: Agents](../user-guide/agents.md)
- [Developer Guide: Creating Skills](creating-skills.md)
- [Developer Guide: Creating Workflows](creating-workflows.md)
- [Reference: Agent Specifications](../reference/agents-reference.md)
