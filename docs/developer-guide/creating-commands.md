# Developer Guide: Creating Commands

## Overview

This guide covers how to create custom slash commands for the MyClaude framework. Commands are user-invoked workflows that provide explicit control over complex, multi-phase processes.

## When to Create a Command

Create a new command when:

✅ **Repeatable workflow**: Task you run frequently with consistent structure
✅ **Multi-agent orchestration**: Coordinating several agents in sequence
✅ **Explicit invocation**: User should trigger this, not automatic
✅ **Team standardization**: Ensuring consistent execution across team

❌ Don't create a command when:

- Task should auto-trigger → Use agent or skill instead
- Single-step task → Just use regular Claude
- Never reused → Not worth creating command
- Too project-specific → Use project instructions

## Command Types

### Simple Command

Invokes single agent with specific instructions:

```markdown
---
description: Brief description
argument-hint: <what-arguments>
---

Use the **agent-name** to accomplish [task].

[Instructions for the agent...]
```

**Example**: `/analyze <topic>` - Invokes analyze-agent

---

### Workflow Command

Multi-phase process coordinating multiple agents:

```markdown
---
description: Multi-step workflow description
argument-hint: <what-arguments>
---

## Phase 1: [Name] (agent-1)
[Instructions...]

## Phase 2: [Name] (agent-2)
[Instructions...]

## Phase 3: [Name] (agent-1)
[Instructions...]
```

**Example**: `/workflows/code-review` - 6-phase review process

---

### Orchestration Command

Parallel or conditional agent coordination:

```markdown
---
description: Complex orchestration
argument-hint: <what-arguments>
---

## Parallel Phase: Analysis

Run in parallel:
- agent-1: [task]
- agent-2: [task]
- agent-3: [task]

## Sequential Phase: Synthesis

Combine results from parallel phase...
```

**Example**: Multi-aspect analysis with parallel execution

## Creation Process

### Step 1: Design Command

Answer these questions:

1. **What does this command do?**
   - Clear, specific purpose
   - Single responsibility

2. **Who is this for?**
   - Developers, content creators, managers?
   - Technical level required?

3. **When would someone use this?**
   - Specific scenarios
   - Frequency of use

4. **What are the inputs?**
   - Required arguments
   - Optional arguments
   - File references needed?

5. **What is the output?**
   - Structured report
   - Modified files
   - Action checklist

6. **What agents/skills needed?**
   - Which agents to use
   - In what sequence
   - Which skills to leverage

### Step 2: Create Command File

```bash
# For simple command
touch .claude/commands/my-command.md

# For workflow command
mkdir -p .claude/commands/workflows
touch .claude/commands/workflows/my-workflow.md

# For category organization
mkdir -p .claude/commands/category-name
touch .claude/commands/category-name/my-command.md
```

### Step 3: Write Command

Use template based on command type (see templates below)

### Step 4: Test Command

```
/my-command test arguments
```

Verify:
- Command triggers correctly
- Arguments expand properly
- Agents execute as expected
- Output matches template

### Step 5: Document Command

Add to `.claude/commands/README.md`:

```markdown
#### /my-command

**Description**: What this command does

**Usage**: `/my-command <argument-hint>`

**What it does**: Detailed explanation

**Output**: What you get

**Example**:
```
/my-command example input
```
```

## Simple Command Template

```markdown
---
description: Clear, concise description of what this command does (one sentence)
argument-hint: <descriptive-placeholder-for-arguments>
---

Use the **[agent-name]** and **[skill-name]** to accomplish [specific goal].

## Task

[Action verb]: $ARGUMENTS

## Instructions

[Specific step-by-step instructions for the agent to follow]

### Context

[Provide any necessary context or constraints]

### Requirements

[List specific requirements or criteria for success]

### Output Format

[Define the expected output structure]

## Quality Standards

[Define what constitutes good output]
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
```

### Example: Simple Analysis Command

```markdown
---
description: Deep analysis of code, architecture, or business problem
argument-hint: <what-to-analyze>
---

Use the **analyze-agent** and **analysis skill** to perform deep, systematic analysis.

## Task

Analyze: $ARGUMENTS

## Instructions

Follow the 6-phase analysis workflow:

1. **Clarify**: Restate the problem, identify sub-questions
2. **Decompose**: Break into dimensions, note constraints
3. **Investigate**: Explore codebase, gather evidence
4. **Options**: Generate 2-4 realistic alternatives
5. **Synthesize**: Evaluate trade-offs, make recommendation
6. **Present**: Structured report with action checklist

### Context

- Focus on architectural and strategic aspects
- Consider both short-term and long-term implications
- Identify risks and mitigation strategies

### Requirements

- All claims must have evidence (file:line references)
- Present 2-4 realistic options
- Clear recommendation with rationale
- Actionable next steps

### Output Format

Use the analysis skill's standard output template:
- Context & Goal
- Key Findings (with evidence)
- Options Analysis (comparison table)
- Recommendation (with rationale)
- Action Checklist

## Quality Standards

- **Evidence-based**: Every finding has specific reference
- **Actionable**: Recommendations are concrete and achievable
- **Balanced**: Shows both pros and cons
- **Clear**: Jargon-free, well-structured
```

## Workflow Command Template

```markdown
---
description: Multi-phase workflow description
argument-hint: <what-arguments>
---

[Brief introduction to workflow and its purpose]

## Task

[Task description]: $ARGUMENTS

## Multi-Phase Workflow

This workflow [describes overall approach and benefits].

### Phase 1: [Name] ([agent-name])

**Use [agent-name]** to [phase goal]:

**Actions**:
1. [Specific action]
2. [Specific action]
3. [Specific action]

**Deliverable**: [What this phase produces]

**Quality Gate**: [Validation question]
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**If gate fails**: [Remediation steps]

### Phase 2: [Name] ([agent-name])

[Same pattern...]

[3-9 phases total]

## Output Format

At the end of this workflow, provide:

### [Report Title]

**[Section 1]**: [Description]

**[Section 2]**: [Description]

**[Section 3]**: [Description]

## Quality Standards

This workflow ensures:
- [Standard 1]
- [Standard 2]
- [Standard 3]
```

### Example: Feature Development Workflow

```markdown
---
description: Feature development workflow from analysis through implementation
argument-hint: <feature-description>
---

Complete feature development workflow using multiple agents and quality gates.

## Task

Develop feature: $ARGUMENTS

## Multi-Phase Workflow

This workflow guides feature development from conception through completion with built-in quality gates.

### Phase 1: Requirements Analysis (analyze-agent)

**Use analyze-agent** to understand requirements:

**Actions**:
1. Clarify requirements - restate in your own words
2. Identify user stories and acceptance criteria
3. List functional and non-functional requirements
4. Define success metrics
5. Analyze context - how does this fit into existing system?
6. Identify constraints (technical, timeline, resources, compliance)

**Deliverable**: Requirements analysis document with clear acceptance criteria

**Quality Gate 1**: Do we understand the requirement fully?
- [ ] Requirements clear and unambiguous
- [ ] Acceptance criteria defined
- [ ] Constraints identified
- [ ] Scope bounded

**If gate fails**: Clarify with stakeholders, document assumptions

### Phase 2: Pre-Implementation Validation (implementation-guardrails)

**Use implementation-guardrails skill** for 5-check validation:

**Actions**:
1. Duplicate Check (0.0-1.0): Does functionality already exist?
2. Architecture Fit (0.0-1.0): Does approach align with architecture?
3. Documentation Compliance (0.0-1.0): Consulted relevant docs?
4. Existing Solutions (0.0-1.0): Can we use existing libraries?
5. Problem Understanding (0.0-1.0): Solving root cause?

Calculate confidence: (D1 + D2 + D3 + D4 + D5) / 5

**Deliverable**: Confidence score and validation report

**Quality Gate 2**: Should we proceed with this approach?
- [ ] Confidence score ≥ 0.7 (preferably ≥ 0.9)
- [ ] No major architectural concerns
- [ ] No better existing solutions ignored
- [ ] Root cause understood

**If confidence < 0.7**: STOP and re-analyze. Use analyze-agent + doc-compliance to address gaps.

### Phase 3: Design (analyze-agent)

[Continue with remaining phases...]

## Output Format

At the end of this workflow, provide:

### Feature Completion Report

**Feature**: [Name]
**Status**: ✅ Complete / ⚠️ Complete with notes / ❌ Blocked

**Quality Gates Summary**:
- [List all gates with pass/fail status]

**Deliverables**:
- [ ] Working implementation
- [ ] Tests
- [ ] Documentation
- [ ] Pull Request

**Key Metrics**:
- Confidence Score: [score]
- Code Coverage: [percentage]
- [Other metrics]

## Quality Standards

This workflow ensures:
- Quality-first: Multiple validation gates prevent issues
- Evidence-based: Decisions backed by analysis
- Well-documented: Documentation planned and executed
- Well-tested: Comprehensive test coverage
- Production-ready: All gates passed before deployment
```

## Advanced Features

### Arguments

**`$ARGUMENTS`** - All arguments as single string:

```markdown
Analyze: $ARGUMENTS
```

Usage: `/analyze caching strategy`
Expands to: `Analyze: caching strategy`

---

**Positional arguments** - Individual arguments:

```markdown
Translate from $1 to $2: $3
```

Usage: `/translate English Spanish "Hello world"`
Expands to: `Translate from English to Spanish: Hello world`

---

### File References

Include file contents with `@` prefix:

```markdown
---
description: Documentation verification
argument-hint: @<doc-file> against implementation
---

Verify documentation accuracy.

## Documentation

The following documentation will be checked:

@$1

## Implementation

Check the implementation in the codebase matches the documentation above.
```

Usage: `/check-docs @docs/api-spec.md`

Claude reads `docs/api-spec.md` and includes content in context.

---

### Bash Execution

Run bash commands first with `!` prefix:

```markdown
---
description: Analyze recent code changes
argument-hint: <last-N-commits>
---

!git log --oneline -$1
!git diff HEAD~$1..HEAD

Based on the git history and diff above, analyze:

1. What changed and why
2. Potential impacts
3. Testing recommendations
4. Documentation updates needed
```

Usage: `/analyze-changes 5`

Runs git commands first, then Claude analyzes the output.

---

### Conditional Logic

```markdown
## Task

Review: $ARGUMENTS

## Process

First, determine the type of review needed:

**If this is a security review** (keywords: security, auth, permissions, encryption):
  1. Use **docs-agent** to check security policy compliance
  2. Use **analyze-agent** to identify security vulnerabilities
  3. Run security-specific checklist

**If this is a performance review** (keywords: performance, speed, optimization):
  1. Use **analyze-agent** to identify bottlenecks
  2. Check algorithmic complexity
  3. Run performance benchmarks

**Otherwise** (general code review):
  1. Run `/workflows/code-review` workflow
```

---

### Parallel Execution

```markdown
## Phase 1: Parallel Analysis

Run the following analyses in parallel:

### 1A: Security Analysis (docs-agent)
Use **docs-agent** to verify security policy compliance.

### 1B: Performance Analysis (analyze-agent)
Use **analyze-agent** to identify performance bottlenecks.

### 1C: Code Quality (analyze-agent)
Use **analyze-agent** to evaluate code quality metrics.

## Phase 2: Synthesis

Combine insights from all three parallel analyses:
[Instructions for synthesis...]
```

---

### Nested Commands

Call other commands from within a command:

```markdown
## Phase 5: Code Review

Run the comprehensive code review workflow:

```
/workflows/code-review $ARGUMENTS
```

Incorporate the code review findings into the overall feature assessment.
```

---

## Organization Strategies

### Flat Organization

```
.claude/commands/
├── analyze.md
├── check-docs.md
├── translate.md
├── proofread.md
├── skill-crafter.md
└── agent-crafter.md
```

**Use when**:
- Small number of commands (< 10)
- All commands are top-level functionality

**Invoke**:
```
/analyze <topic>
/check-docs <target>
```

---

### Category Organization

```
.claude/commands/
├── analyze.md
├── check-docs.md
├── workflows/
│   ├── code-review.md
│   └── feature-development.md
└── admin/
    ├── backup.md
    └── deploy.md
```

**Use when**:
- Medium number of commands (10-30)
- Natural categories exist
- Want to group related commands

**Invoke**:
```
/analyze <topic>
/workflows/code-review <path>
/admin/backup <target>
```

---

### Hierarchical Organization

```
.claude/commands/
├── development/
│   ├── analyze.md
│   ├── code-review.md
│   └── refactor.md
├── content/
│   ├── translate.md
│   ├── proofread.md
│   └── summarize.md
└── operations/
    ├── deploy.md
    ├── rollback.md
    └── monitor.md
```

**Use when**:
- Large number of commands (> 30)
- Complex project with many domains
- Want clear separation of concerns

**Invoke**:
```
/development/analyze <topic>
/content/translate <language>
/operations/deploy <environment>
```

---

## Best Practices

### Command Naming

**✅ Good names**:
- `/analyze` - Clear action verb
- `/code-review` - Hyphenated compound
- `/workflows/feature-development` - Descriptive, categorized

**❌ Poor names**:
- `/do-stuff` - Too vague
- `/cr` - Unclear abbreviation
- `/theCommandThatDoesCodeReview` - camelCase (use hyphens)

---

### Description Writing

**✅ Good description**:
```yaml
description: Comprehensive code review workflow orchestrating multiple agents for security, quality, and best practices analysis
```

Clear, specific, mentions key benefits.

**❌ Poor description**:
```yaml
description: Reviews code
```

Too vague, no details.

---

### Argument Hints

**✅ Good hints**:
```yaml
argument-hint: <path-to-review>
argument-hint: <source-language> to <target-language>
argument-hint: <feature-description>
```

Specific, shows expected format.

**❌ Poor hints**:
```yaml
argument-hint: <args>
argument-hint: <input>
```

Too generic.

---

### Output Format Definition

**✅ Good output definition**:
```markdown
## Output Format

Provide a complete code review report including:

### Executive Summary
- Overall assessment (Approve/Changes/Reject)
- Code quality rating (1-10)
- Critical issues count

### Detailed Findings
[Structured sections...]

### Prioritized Issues
| Priority | Issue | File:Line | Recommendation |

### Action Items
- [ ] Specific actionable steps
```

**❌ Poor output definition**:
```markdown
## Output

Give me the results.
```

---

### Quality Standards

**✅ Good standards**:
```markdown
## Quality Standards

All outputs must:
- Include specific file:line references
- Prioritize issues (Critical/High/Medium/Low)
- Provide actionable recommendations
- Use consistent formatting
```

**❌ Poor standards**:
```markdown
## Quality

Make it good.
```

---

## Testing Commands

### Manual Testing

1. **Test basic invocation**:
   ```
   /my-command test input
   ```

2. **Test with arguments**:
   ```
   /my-command arg1 arg2 arg3
   ```

3. **Test with file references**:
   ```
   /my-command @path/to/file
   ```

4. **Test edge cases**:
   ```
   /my-command
   /my-command ""
   /my-command very long argument string with many words
   ```

### Validation Checklist

- [ ] **Command file exists** in `.claude/commands/`
- [ ] **YAML frontmatter** is valid
- [ ] **Description** is clear and concise
- [ ] **Argument hint** shows expected format
- [ ] **$ARGUMENTS** expands correctly (if used)
- [ ] **Agent references** use `**agent-name**` format
- [ ] **Skill references** use `**skill-name**` format
- [ ] **Output format** is defined
- [ ] **Quality standards** are explicit
- [ ] **File references** work (if used)
- [ ] **Bash commands** execute (if used)
- [ ] **Documented** in README.md

---

## Integration

### Add to README

Update `.claude/commands/README.md`:

```markdown
### My Category

#### /my-command

**Description**: What this command does

**Usage**: `/my-command <argument-hint>`

**What it does**: Detailed explanation of the workflow

**Output**: What you get at the end

**Example**:
```
/my-command example input
→ Expected behavior and output
```
```

---

### Team Documentation

Create team guide for command usage:

```markdown
# Team Commands Guide

## Daily Development Commands

### Code Analysis
```
/analyze <topic>
```
Use for architectural decisions, trade-off analysis, strategic planning.

### Code Review
```
/workflows/code-review <path>
```
Run before merging. Checks security, quality, tests, best practices.

### Feature Development
```
/workflows/feature-development <description>
```
Use for new features. Includes requirements, validation, design, implementation, testing.

## Content Commands

[Continue with all team commands...]
```

---

## Advanced Topics

### Command Hooks

Trigger commands via hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(src/**/*.js)",
      "hooks": [{
        "command": "claude /analyze-impact $FILE_PATH"
      }]
    }]
  }
}
```

Automatically runs `/analyze-impact` after writing JavaScript files.

---

### CI/CD Integration

Use commands in automated pipelines:

```yaml
# .github/workflows/review.yml
name: Automated Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run Code Review
        run: |
          claude /workflows/code-review src/ > review-report.md

      - name: Check for Critical Issues
        run: |
          if grep -q "🔴 Critical" review-report.md; then
            echo "Critical issues found"
            exit 1
          fi

      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('review-report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

---

### Command Chaining

Chain commands in bash:

```bash
# Sequential execution
claude /analyze architecture > analysis.md && \
claude /check-docs @analysis.md against implementation > compliance.md && \
claude /proofread @compliance.md > final-report.md

# Parallel execution
claude /workflows/code-review src/auth & \
claude /workflows/code-review src/api & \
claude /workflows/code-review src/database & \
wait

echo "All reviews complete"
```

---

## Common Patterns

### Analysis Pattern

```markdown
Use **analyze-agent** and **analysis skill** to:
1. Clarify the question
2. Decompose into dimensions
3. Explore options (2-4 alternatives)
4. Synthesize findings
5. Present recommendation with action checklist
```

---

### Verification Pattern

```markdown
Use **docs-agent** and **doc-compliance skill** to:
1. Identify relevant documentation
2. Extract requirements
3. Build compliance table (✅/⚠️/❌)
4. Generate gap analysis
5. Provide remediation roadmap
```

---

### Multi-Agent Orchestration Pattern

```markdown
## Phase 1: Analysis (analyze-agent)
[Analysis instructions]

## Phase 2: Verification (docs-agent)
[Verification instructions]

## Phase 3: Synthesis
Combine insights from both agents and produce unified report.
```

---

### Quality Gate Pattern

```markdown
### Phase [N]: [Name]

**Deliverable**: [What this produces]

**Quality Gate**: [Validation question]
- [ ] Criterion 1
- [ ] Criterion 2

**If gate fails**: [Remediation steps]
```

---

## Troubleshooting

### Command Not Found

**Problem**: Claude says "Command not found"

**Solutions**:
- Check file is in `.claude/commands/` (or subdirectory)
- Verify filename matches command (without `.md`)
- Check YAML frontmatter is valid
- Restart Claude Code to reload commands

---

### Arguments Not Expanding

**Problem**: `$ARGUMENTS` shows literally instead of expanding

**Solutions**:
- Use `$ARGUMENTS` (case-sensitive, all caps)
- Check you're providing arguments: `/command arg1 arg2`
- Try positional: `$1`, `$2`, `$3`
- Verify no typos in variable name

---

### File Reference Not Working

**Problem**: `@file` not loading content

**Solutions**:
- Use `@path/to/file` syntax (relative to project root)
- Verify file exists: `ls path/to/file`
- Check file is readable (permissions)
- Try absolute path if relative doesn't work

---

### Command Too Slow

**Problem**: Command takes too long to complete

**Solutions**:
- Reduce scope of analysis/review
- Break into smaller commands
- Use specific agents instead of full workflows
- Check for hanging bash commands (`!`)
- Run phases in parallel where possible

---

### Inconsistent Output

**Problem**: Command produces different output each time

**Solutions**:
- Strengthen output template in command
- Add specific quality standards
- Include example output
- Make workflow steps more prescriptive
- Add validation steps

---

## Example Commands

### Example 1: Simple Command

`.claude/commands/summarize.md`:

```markdown
---
description: Summarize code, documentation, or complex topics
argument-hint: <what-to-summarize>
---

Use the **analyze-agent** to create a concise summary.

## Task

Summarize: $ARGUMENTS

## Instructions

Create a clear, concise summary that:

1. **Identifies** the main purpose or function
2. **Highlights** key components or concepts
3. **Explains** how it works at a high level
4. **Notes** important details or gotchas
5. **Lists** dependencies or requirements

## Output Format

```markdown
# Summary: [Topic]

## Purpose
[1-2 sentences]

## Key Components
- [Component 1]: [Brief description]
- [Component 2]: [Brief description]

## How It Works
[2-3 sentence explanation]

## Important Notes
- [Note 1]
- [Note 2]

## Dependencies
- [Dependency 1]
```

## Quality Standards

- **Concise**: Summary should be 1/10th the length of original
- **Clear**: Jargon-free language
- **Complete**: Covers all essential aspects
```

Usage: `/summarize authentication system`

---

### Example 2: Workflow Command

See `.claude/commands/workflows/code-review.md` for complete production example.

---

## Next Steps

1. **Identify need**: What repetitive task could benefit from a command?
2. **Design command**: Use templates and patterns from this guide
3. **Create and test**: Build command, test thoroughly
4. **Document**: Add to README, create team guide
5. **Iterate**: Refine based on usage and feedback

---

## Related Documentation

- [User Guide: Commands](../user-guide/commands.md)
- [Developer Guide: Creating Agents](creating-agents.md)
- [Developer Guide: Creating Workflows](creating-workflows.md)
- [Reference: Command Specifications](../reference/commands-reference.md)
