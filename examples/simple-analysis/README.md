# Example: Simple Analysis Workflow

## Scenario

You're evaluating caching strategies for a web application and need to make an architectural decision. This example demonstrates using the analyze-agent and analysis skill.

## Files in This Example

- `current-implementation.md` - Current caching approach
- `requirements.md` - Requirements for new caching system
- `analysis-output.md` - Example output from analysis workflow

## How to Run

### Method 1: Using /analyze Command

```bash
cd my-claude

# Run analysis command
claude
> /analyze the caching strategy options in examples/simple-analysis/
```

### Method 2: Natural Language Request

```bash
claude
> Analyze the caching strategies described in examples/simple-analysis/
> and recommend the best approach for our requirements
```

The analyze-agent will automatically trigger based on the keyword "analyze".

## What Happens

1. **Agent Triggers**: analyze-agent loads automatically (keyword: "analyze")

2. **Skill Loads**: analysis skill provides:
   - 6-step analysis workflow
   - 10 analysis frameworks (SWOT, Cost-Benefit, Decision Matrix, etc.)

3. **Workflow Execution**:
   - **Phase 1: Clarify** - Restates the caching decision
   - **Phase 2: Decompose** - Breaks into dimensions (performance, complexity, cost, scalability)
   - **Phase 3: Investigate** - Reads current implementation and requirements
   - **Phase 4: Options** - Generates 3-4 caching alternatives
   - **Phase 5: Synthesize** - Compares options using Decision Matrix
   - **Phase 6: Present** - Structured report with recommendation

4. **Output**: Comprehensive analysis report (see `analysis-output.md`)

## Key Features Demonstrated

### ✅ Automatic Agent Delegation

No need to explicitly invoke the agent - Claude recognizes "analyze" keyword and delegates to analyze-agent.

### ✅ Skill Integration

analyze-agent automatically loads the analysis skill, gaining access to all 10 analysis frameworks.

### ✅ Systematic Workflow

The 6-phase workflow ensures thorough, structured analysis with quality checkpoints.

### ✅ Evidence-Based Output

All findings include specific references to source files and line numbers.

### ✅ Actionable Recommendations

Output includes clear recommendation with rationale and action checklist.

## Expected Output Structure

```markdown
# Analysis: Caching Strategy Selection

## Context & Goal
[Problem restatement]

## Key Findings
- Current approach: File-based caching (current-implementation.md:15)
- Performance requirement: <100ms response time (requirements.md:8)
- [More findings...]

## Options Analysis

| Option | Performance | Complexity | Cost | Scalability | Total Score |
|--------|------------|------------|------|-------------|-------------|
| Redis  | 5/5        | 3/5        | 3/5  | 5/5         | 16/20       |
| Memcached | 5/5     | 4/5        | 4/5  | 4/5         | 17/20       |
| In-Memory | 4/5      | 5/5        | 5/5  | 2/5         | 16/20       |

## Recommendation

**Use Memcached** for the following reasons:
- [Rationale 1]
- [Rationale 2]

## Action Checklist
- [ ] Set up Memcached cluster
- [ ] Implement caching layer
- [ ] Run performance tests
- [ ] Monitor cache hit rates
```

## Learning Points

1. **Trigger Keywords**: Words like "analyze", "evaluate", "compare" trigger analyze-agent

2. **Skill Auto-Loading**: Skills load automatically when agents reference them in frontmatter

3. **Progressive Disclosure**:
   - Level 1: Metadata loaded at startup (<50 tokens)
   - Level 2: Core workflow loaded when triggered (~500 tokens)
   - Level 3: Detailed frameworks loaded on demand (~2000 tokens)

4. **Quality Gates**: Each phase has validation checkpoints to ensure quality

5. **Structured Output**: Consistent format makes analysis results actionable

## Try It Yourself

1. **Modify requirements.md** - Change requirements and see how analysis adapts

2. **Add a new option** - Describe another caching solution in a file and ask for analysis

3. **Use specific framework** - Request "Use SWOT analysis" to get SWOT-specific output

4. **Change focus** - Ask to analyze different aspects (cost, security, maintenance)

## Related Examples

- [Document Review](../document-review/) - Using docs-agent for compliance checking
- [Translation Workflow](../translation-workflow/) - Using translate-agent
- [Custom Agent](../custom-agent/) - Creating your own agents

## Next Steps

- Try `/workflows/code-review` on actual code
- Use `/check-docs` to verify documentation accuracy
- Create custom analysis command for your specific needs
