# MyClaude Slash Commands

This directory contains user-invoked slash commands that orchestrate workflows. Commands package frequently-used prompts and multi-agent workflows that you explicitly control.

## Available Commands

### Core Workflow Commands

#### /analyze
**Description**: Deep analysis workflow using analyze-agent
**Usage**: `/analyze <what-to-analyze>`
**What it does**: Performs systematic 6-step analysis (Clarify → Decompose → Investigate → Options → Synthesize → Present)
**Output**: Comprehensive analysis report with evidence, options comparison, and recommendations

**Example**:
```
/analyze the authentication system architecture
/analyze these three deployment options
/analyze the performance bottleneck in the API
```

#### /check-docs
**Description**: Documentation verification and compliance checking
**Usage**: `/check-docs <what-to-verify>`
**What it does**: Verifies documentation accuracy, checks compliance with specs and policies
**Output**: Compliance report with ✅⚠️❌ status, gap analysis, remediation roadmap

**Example**:
```
/check-docs API documentation against implementation
/check-docs compliance with security policy
/check-docs requirements coverage
```

#### /translate
**Description**: Translation and localization workflow
**Usage**: `/translate <source-language> to <target-language>`
**What it does**: High-quality translation with glossary management and cultural adaptation
**Output**: Translated content with glossary, decision notes, and quality metrics

**Example**:
```
/translate English to Spanish
/translate this documentation to French, formal tone
/translate marketing copy to Japanese
```

#### /proofread
**Description**: Professional editing and proofreading
**Usage**: `/proofread <content-to-edit>`
**What it does**: Comprehensive 5-category editing (Grammar, Clarity, Structure, Tone, Consistency)
**Output**: Edited content with change summary and major changes highlighted

**Example**:
```
/proofread this blog post
/proofread the user documentation
/proofread README.md for clarity
```

### Meta-Programming Commands

#### /skill-crafter
**Description**: Interactive skill creation workflow
**Usage**: `/skill-crafter <skill-description>`
**What it does**: Guides you through creating a new skill with templates and validation
**Output**: Complete SKILL.md file with proper structure, testing plan, integration guidance

**Example**:
```
/skill-crafter Create a skill for API testing
/skill-crafter I need a skill for data validation
/skill-crafter Design a skill for performance optimization
```

#### /agent-crafter
**Description**: Interactive agent creation workflow
**Usage**: `/agent-crafter <agent-description>`
**What it does**: Guides you through creating a new agent with identity design and workflow
**Output**: Complete agent.md file with YAML frontmatter, workflow, testing plan

**Example**:
```
/agent-crafter Create an agent for security audits
/agent-crafter I need an agent for database migrations
/agent-crafter Design an agent for customer support
```

### Workflow Orchestration Commands

#### /workflows/code-review
**Description**: Comprehensive code review workflow
**Usage**: `/workflows/code-review <path-to-review>`
**What it does**: Multi-phase code review (Analysis → Docs → Quality → Tests → Best Practices → Synthesis)
**Output**: Complete code review report with prioritized issues and improvement roadmap

**Example**:
```
/workflows/code-review src/auth/
/workflows/code-review src/api/users.js
/workflows/code-review .
```

#### /workflows/feature-development
**Description**: Complete feature development workflow
**Usage**: `/workflows/feature-development <feature-description>`
**What it does**: Guides feature from requirements through deployment with quality gates
**Output**: Feature completion report with all deliverables and metrics

**Example**:
```
/workflows/feature-development user authentication system
/workflows/feature-development real-time notifications
/workflows/feature-development export to PDF functionality
```

## Command Structure

### Basic Commands (Simple Workflows)

Simple commands directly invoke agents with clear instructions:

```markdown
---
description: Brief description
argument-hint: <what-arguments>
---

Use the **[agent-name]** and **[skill-name]** to accomplish [task].

Instructions for the workflow...
```

### Workflow Commands (Multi-Agent Orchestration)

Complex workflows orchestrate multiple agents in sequence or parallel:

```markdown
---
description: Multi-step workflow description
argument-hint: <what-arguments>
---

## Phase 1: [Name] (agent-1)
Instructions for agent-1...

## Phase 2: [Name] (agent-2)
Instructions for agent-2...

## Phase 3: [Name] (agent-1 + skill-1)
Instructions combining agent and skill...
```

## Using Commands

### In CLI

```bash
# Start Claude Code
claude

# Run a command
/analyze the database schema

# Run with file reference
/check-docs @docs/api-spec.md against implementation

# Run workflow
/workflows/code-review src/
```

### In Interactive Mode

```
> /analyze
What would you like to analyze?

> the caching strategy
[Analysis proceeds...]
```

### With Arguments

Commands support `$ARGUMENTS` variable:

```markdown
Analyze: $ARGUMENTS
```

When you run `/analyze caching strategy`, it expands to:
```
Analyze: caching strategy
```

### With File References

Use `@` prefix to include file contents:

```
/check-docs @docs/spec.md
```

Claude will read the file and include its contents in the command context.

### With Bash Execution

Use `!` prefix to run bash commands first:

```markdown
!git log --oneline -10
!git diff HEAD~5..HEAD

Based on the git history above, analyze recent changes...
```

## Creating Custom Commands

### Method 1: Manual Creation

1. Create `.claude/commands/your-command.md`
2. Add frontmatter:
   ```yaml
   ---
   description: What this command does
   argument-hint: <expected-arguments>
   ---
   ```
3. Write the command prompt with `$ARGUMENTS` where needed
4. Test: `/your-command test input`

### Method 2: Use Subdirectories for Organization

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

Commands in subdirectories work the same:
```
/code-review src/           # From workflows/code-review.md
/backup production          # From admin/backup.md
```

## Command Best Practices

### Writing Effective Commands

1. **Clear Description**: Help users discover your command
2. **Argument Hints**: Show expected input format
3. **Structured Output**: Define what the command produces
4. **Quality Standards**: Set expectations for thoroughness

### Command vs. Skill vs. Agent

**Use Command when**:
- User explicitly triggers workflow
- Multi-step process needs orchestration
- Specific sequence of agents required

**Use Skill when**:
- Want automatic invocation based on context
- Providing reusable patterns
- Extending agent capabilities

**Use Agent when**:
- Complex task needs independent context
- Specialized expertise required
- Multiple phases of work

### Examples of Good Commands

✅ **Good**: Specific, actionable, clear output
```markdown
/check-docs API documentation against implementation
→ Produces compliance report with specific gaps
```

✅ **Good**: Orchestrates multiple agents
```markdown
/workflows/code-review src/
→ Uses analyze-agent, docs-agent, runs quality checks
```

✅ **Good**: Clear argument structure
```markdown
/translate English to Spanish
→ Knows source and target languages
```

## Command Categories

### Analysis Commands
- `/analyze` - Deep analysis
- `/workflows/code-review` - Code review

### Verification Commands
- `/check-docs` - Documentation compliance

### Content Commands
- `/translate` - Translation
- `/proofread` - Editing

### Meta Commands
- `/skill-crafter` - Create skills
- `/agent-crafter` - Create agents

### Workflow Commands
- `/workflows/feature-development` - Feature workflow
- `/workflows/code-review` - Review workflow

## Troubleshooting

**Command not found?**
- Check file is in `.claude/commands/` or subdirectory
- Verify filename matches command (no .md in command)
- Restart Claude Code if just added

**Arguments not working?**
- Use `$ARGUMENTS` in command file
- Or use `$1`, `$2` for positional arguments
- Check spacing and quoting

**File reference not working?**
- Use `@path/to/file` syntax
- Verify file path is correct
- Check file is readable

**Command too slow?**
- Break into smaller commands
- Use specific agents instead of workflows
- Check if bash commands (`!`) are hanging

## Contributing Commands

When creating commands for the framework:

1. Follow naming conventions (lowercase, hyphenated)
2. Include clear description and argument hints
3. Document expected output format
4. Test with various inputs
5. Add to this README
6. Commit to version control

## Version-Controlled Commands

Commands in `.claude/commands/` should be committed to git for team sharing:

```bash
git add .claude/commands/
git commit -m "feat: Add code-review workflow command"
```

Personal commands go in `~/.claude/commands/` (not version controlled).

---

For more information:
- [User Guide: Commands](../../docs/user-guide/commands.md)
- [Developer Guide: Creating Commands](../../docs/developer-guide/creating-commands.md)
- [Official Docs](https://code.claude.com/docs/en/slash-commands)
