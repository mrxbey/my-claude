# User Guide: Slash Commands

## Overview

Slash commands are user-invoked workflows that provide explicit control over complex tasks. Unlike agents (model-invoked) and skills (auto-triggered), commands must be explicitly called by typing `/command-name` in Claude Code.

Commands are ideal for:
- **Repeatable workflows**: Tasks you run frequently with consistent structure
- **Multi-agent orchestration**: Coordinating several agents in sequence
- **Complex processes**: Multi-phase workflows with quality gates
- **Team standardization**: Ensuring consistent execution across team members

## Quick Start

### Basic Usage

```bash
# Start Claude Code
claude

# Run a command
/analyze the authentication system

# Run with file reference
/check-docs @docs/api-spec.md against implementation

# Run workflow
/workflows/code-review src/
```

### Available Commands

#### Core Analysis Commands

**`/analyze <what-to-analyze>`**

Deep, systematic analysis using the analyze-agent and analysis skill.

```
/analyze the caching strategy
/analyze database schema design
/analyze deployment options for production
```

**Output**: Comprehensive analysis report with:
- Problem decomposition
- Options evaluation (2-4 alternatives)
- Trade-off analysis
- Clear recommendation with rationale
- Action checklist

**When to use**: Complex decisions, architecture evaluation, strategic planning

---

**`/check-docs <what-to-verify>`**

Documentation verification and compliance checking using docs-agent.

```
/check-docs API documentation against implementation
/check-docs compliance with security policy
/check-docs requirements coverage
```

**Output**: Compliance report with:
- Requirements extraction table
- ✅/⚠️/❌ status for each requirement
- Gap analysis
- Remediation roadmap

**When to use**: Documentation accuracy, policy compliance, audit preparation

---

#### Content Workflow Commands

**`/translate <source-language> to <target-language>`**

High-quality translation with cultural adaptation using translate-agent.

```
/translate English to Spanish
/translate this documentation to French, formal tone
/translate marketing copy to Japanese
```

**Output**: Translation deliverables:
- Translated content
- Project glossary with consistent terminology
- Decision notes (where choices were made)
- Alternative phrasings for ambiguous sections

**When to use**: Documentation localization, content adaptation, multi-language support

---

**`/proofread <content-to-edit>`**

Professional editing and proofreading using proofread-agent.

```
/proofread this blog post
/proofread the user documentation
/proofread README.md for clarity
```

**Output**: Editing deliverables:
- Edited content with corrections
- Change summary by category (Grammar, Clarity, Structure, Tone, Consistency)
- Major improvements highlighted
- Before/after comparison for significant changes

**When to use**: Content polishing, consistency enforcement, quality improvement

---

#### Meta-Programming Commands

**`/skill-crafter <skill-description>`**

Interactive skill creation workflow. Guides you through designing a new skill.

```
/skill-crafter Create a skill for API testing
/skill-crafter I need a skill for data validation
/skill-crafter Design a skill for performance optimization
```

**Process**:
1. Interview: Purpose, use cases, scope
2. Design: Structure, workflow phases, tools needed
3. Generate: Complete SKILL.md with frontmatter
4. Validate: YAML structure, trigger keywords
5. Integrate: Recommendations for which agents should use it
6. Test: Scenarios to verify it works

**Output**: Complete skill in `.claude/skills/[skill-name]/`

**When to use**: Extending framework capabilities, adding domain expertise, creating reusable patterns

---

**`/agent-crafter <agent-description>`**

Interactive agent creation workflow. Guides you through designing a new agent.

```
/agent-crafter Create an agent for security audits
/agent-crafter I need an agent for database migrations
/agent-crafter Design an agent for customer support
```

**Process**:
1. Interview: Role, typical tasks, complexity
2. Design: Identity, workflow pattern, decision-making
3. Tools: Read-only vs. standard vs. execution permissions
4. Skills: Which existing skills to integrate
5. Generate: Complete agent.md with YAML + prompt
6. Test: Validation and integration testing

**Output**: Complete agent in `.claude/agents/[agent-name].md`

**When to use**: Adding specialized agents, building expertise areas, team capability expansion

---

#### Workflow Orchestration Commands

**`/workflows/code-review <path-to-review>`**

Comprehensive multi-agent code review workflow.

```
/workflows/code-review src/auth/
/workflows/code-review src/api/users.js
/workflows/code-review .
```

**6-Phase Process**:
1. **Initial Analysis** (analyze-agent): Understand structure, purpose, architecture
2. **Documentation Verification** (docs-agent): Check docs match code
3. **Quality Analysis**: Complexity, security, performance, architecture fit
4. **Test Coverage**: Evaluate testing completeness
5. **Best Practices**: Language-specific and general practices
6. **Synthesis**: Prioritized issues, recommendations, roadmap

**Output**: Complete code review report with:
- Executive summary (overall assessment, quality rating)
- Detailed findings by category
- Prioritized issues table (🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low)
- Security findings
- Performance concerns
- Test coverage analysis
- Actionable recommendations with file:line references

**When to use**: Pre-merge review, code audit, quality assessment, knowledge transfer

---

**`/workflows/feature-development <feature-description>`**

End-to-end feature development with quality gates.

```
/workflows/feature-development user authentication system
/workflows/feature-development real-time notifications
/workflows/feature-development export to PDF functionality
```

**9-Phase Process with Quality Gates**:

1. **Requirements Analysis** (analyze-agent)
   - Clarify requirements, acceptance criteria
   - **Quality Gate**: Requirements clear and unambiguous?

2. **Pre-Implementation Validation** (implementation-guardrails)
   - 5-check confidence scoring
   - **Quality Gate**: Confidence ≥ 0.7? (prefer ≥ 0.9)

3. **Design** (analyze-agent)
   - High-level and detailed design
   - Evaluate alternatives
   - **Quality Gate**: Design sound and well-documented?

4. **Documentation Planning** (docs-agent)
   - Identify docs to update
   - Draft API contracts
   - **Quality Gate**: Documentation plan complete?

5. **Implementation**
   - Core logic + tests
   - **Quality Gate**: All acceptance criteria met?

6. **Code Review** (runs `/code-review`)
   - **Quality Gate**: No critical issues?

7. **Documentation**
   - Write and proofread docs
   - **Quality Gate**: Complete and accurate?

8. **Integration Testing**
   - Integration, performance, UAT
   - **Quality Gate**: All tests passing?

9. **Final Review & Deployment Prep**
   - Deployment plan, rollback plan
   - **Quality Gate**: Ready for production?

**Output**: Feature completion report with:
- Quality gates summary (all checkpoints)
- Deliverables checklist
- Key metrics (confidence score, code coverage, review issues)
- Lessons learned

**When to use**: New feature development, complex changes, production-critical work

---

## Command Anatomy

### Command File Structure

Commands are Markdown files in `.claude/commands/` with YAML frontmatter:

```markdown
---
description: Brief description of what this command does
argument-hint: <expected-arguments>
---

Command prompt goes here. Use **bold** for agents/skills.

## Task

The specific task: $ARGUMENTS

## Process

Step-by-step instructions for Claude...
```

### Key Elements

**YAML Frontmatter**:
- `description`: Shown in command listings (required)
- `argument-hint`: Shows expected input format (optional)

**Command Body**:
- Can reference agents with `**agent-name**`
- Can reference skills with `**skill-name**`
- Use `$ARGUMENTS` to include user input
- Supports phases, workflows, quality gates
- Can include bash commands with `!command`
- Can include file references with `@file-path`

### Argument Variables

**`$ARGUMENTS`** - All arguments as single string:
```markdown
Analyze: $ARGUMENTS
```

**Positional arguments** - Individual arguments:
```markdown
Translate from $1 to $2
```

### File References

Include file contents with `@` prefix:

```
/check-docs @docs/api-spec.md against implementation
```

Claude will read `docs/api-spec.md` and include its contents in the context.

### Bash Execution

Run bash commands first with `!` prefix:

```markdown
!git log --oneline -10
!git diff HEAD~5..HEAD

Based on the git history above, analyze recent changes...
```

---

## Creating Custom Commands

### Method 1: Manual Creation

1. **Create command file**:
   ```bash
   touch .claude/commands/my-command.md
   ```

2. **Add frontmatter**:
   ```yaml
   ---
   description: What this command does
   argument-hint: <expected-arguments>
   ---
   ```

3. **Write command prompt**:
   ```markdown
   Use the **analyze-agent** to examine: $ARGUMENTS

   Provide detailed analysis with recommendations.
   ```

4. **Test**:
   ```
   /my-command test input
   ```

### Method 2: Use `/skill-crafter` or `/agent-crafter`

For complex workflows, use meta-programming commands to design your command interactively.

### Subdirectories for Organization

Organize commands in subdirectories:

```
.claude/commands/
├── analyze.md
├── workflows/
│   ├── code-review.md
│   └── feature-development.md
└── admin/
    ├── backup.md
    └── deploy.md
```

Commands work the same:
```
/workflows/code-review src/
/admin/backup production
```

---

## Best Practices

### Writing Effective Commands

**1. Clear, Specific Description**

✅ **Good**: "Comprehensive code review workflow orchestrating multiple agents"

❌ **Bad**: "Review code"

**2. Helpful Argument Hints**

✅ **Good**: `argument-hint: <path-to-review>`

❌ **Bad**: No hint provided

**3. Structured Output Definition**

Define what the command produces:

```markdown
## Output Format

Provide a complete code review report including:
- Executive summary
- Detailed findings
- Prioritized issues table
- Recommendations
```

**4. Quality Standards**

Set expectations:

```markdown
## Quality Standards

This workflow ensures:
- Evidence-based (all findings have file:line)
- Prioritized (Critical/High/Medium/Low)
- Actionable (specific fixes, not vague suggestions)
```

### Command vs. Skill vs. Agent

**Use Command when**:
- User explicitly triggers workflow
- Multi-step process needs orchestration
- Specific sequence of agents required
- Repeatable, standardized procedure

**Use Skill when**:
- Want automatic invocation based on context
- Providing reusable patterns/frameworks
- Extending agent capabilities
- Context-sensitive help

**Use Agent when**:
- Complex task needs independent context
- Specialized expertise required
- Multiple phases of autonomous work
- Model should decide when to delegate

### Examples of Good Commands

**✅ Specific and actionable**:
```
/check-docs API documentation against implementation
→ Produces compliance report with specific gaps
```

**✅ Orchestrates multiple agents**:
```
/workflows/code-review src/
→ Uses analyze-agent, docs-agent, runs quality checks
```

**✅ Clear argument structure**:
```
/translate English to Spanish
→ Knows source and target languages
```

**✅ Well-defined phases**:
```
/workflows/feature-development user authentication
→ 9 phases with quality gates at each step
```

---

## Troubleshooting

### Command not found

**Problem**: Claude says "Command not found"

**Solutions**:
- Check file is in `.claude/commands/` or subdirectory
- Verify filename matches command (no `.md` in command name)
- Restart Claude Code if you just added the command
- Check YAML frontmatter is valid

### Arguments not working

**Problem**: `$ARGUMENTS` not expanding

**Solutions**:
- Use `$ARGUMENTS` in command file (case-sensitive)
- Check you're providing arguments: `/command arg1 arg2`
- Try positional: `$1`, `$2`, `$3`
- Check spacing and quoting

### File reference not working

**Problem**: `@file` not loading content

**Solutions**:
- Use `@path/to/file` syntax
- Verify file path is correct (relative to project root)
- Check file is readable (permissions)
- Ensure file exists: `ls path/to/file`

### Command too slow

**Problem**: Command takes too long

**Solutions**:
- Break into smaller commands
- Use specific agents instead of full workflows
- Check if bash commands (`!`) are hanging
- Reduce scope of analysis/review

### Command produces wrong output

**Problem**: Command doesn't do what you expect

**Solutions**:
- Read command file to understand what it does
- Check agent descriptions to see what they're designed for
- Modify command file to adjust instructions
- Test with smaller scope first

---

## Advanced Usage

### Chaining Commands

Run multiple commands in sequence:

```bash
# In your terminal or script
claude /analyze authentication-system > analysis.md
claude /check-docs @analysis.md against implementation > compliance.md
claude /proofread @compliance.md > final-report.md
```

### Conditional Logic in Commands

Use bash execution for conditional workflows:

```markdown
!test -f .env && echo "Environment configured" || echo "No .env found"

If environment is configured, proceed with deployment...
```

### Integration with CI/CD

Use commands in automation:

```yaml
# .github/workflows/review.yml
- name: Code Review
  run: |
    claude /workflows/code-review src/ > review-report.md
    # Parse review-report.md and fail if critical issues found
```

### Custom Hooks Integration

Trigger commands via hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(src/**/*.js)",
      "hooks": [{
        "command": "claude /analyze $FILE_PATH"
      }]
    }]
  }
}
```

---

## Command Library Patterns

### Analysis Pattern

```markdown
Use the **analyze-agent** and **analysis skill** to:
1. Clarify the question
2. Decompose into sub-questions
3. Explore options (2-4 alternatives)
4. Synthesize findings
5. Present clear recommendation
```

### Verification Pattern

```markdown
Use the **docs-agent** and **doc-compliance skill** to:
1. Identify relevant documentation
2. Extract requirements
3. Build compliance table
4. Mark status (✅/⚠️/❌)
5. Generate gap analysis and remediation plan
```

### Multi-Agent Orchestration Pattern

```markdown
## Phase 1: Analysis (analyze-agent)
[Instructions for analysis phase]

## Phase 2: Verification (docs-agent)
[Instructions for verification phase]

## Phase 3: Synthesis
Combine insights from both agents and produce unified report
```

### Quality Gate Pattern

```markdown
### Phase X: [Name]

**Goal**: [What this phase achieves]

**Actions**:
- [Step 1]
- [Step 2]

**Quality Gate**: [Checkpoint question]
- [ ] Criteria 1
- [ ] Criteria 2

**If gate fails**: [Remediation steps]
```

---

## Command Categories

### Analysis Commands
- `/analyze` - Deep systematic analysis

### Verification Commands
- `/check-docs` - Documentation compliance

### Content Commands
- `/translate` - Translation and localization
- `/proofread` - Professional editing

### Meta-Programming Commands
- `/skill-crafter` - Create new skills
- `/agent-crafter` - Create new agents

### Workflow Commands
- `/workflows/code-review` - Comprehensive code review
- `/workflows/feature-development` - End-to-end feature workflow

---

## Next Steps

1. **Try core commands**: Start with `/analyze` and `/check-docs`
2. **Explore workflows**: Use `/workflows/code-review` on a codebase
3. **Create custom command**: Build a simple command for your workflow
4. **Use meta-programming**: Try `/skill-crafter` to extend the framework

## Related Documentation

- [Agents User Guide](agents.md) - Understanding model-invoked agents
- [Skills User Guide](skills.md) - Understanding auto-triggered skills
- [Workflows Guide](workflows.md) - Complex multi-phase workflows
- [Developer Guide: Creating Commands](../developer-guide/creating-commands.md)
