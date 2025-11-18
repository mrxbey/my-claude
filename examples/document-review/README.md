# Example: Document Review (Coming Soon)

## Status: Under Development

This example is currently being developed and will demonstrate:

- Using docs-agent for documentation verification
- Compliance checking against requirements
- Gap analysis and remediation planning
- Using the doc-compliance skill

## What This Example Will Include

- Sample documentation files to verify
- Requirements and policy documents
- Example compliance tables with ✅/⚠️/❌ status
- Complete verification workflow output

## In the Meantime

You can explore the document verification workflow by:

1. **Using the /check-docs command:**
   ```
   /check-docs @docs/api-spec.md against implementation
   ```

2. **Natural language request:**
   ```
   Verify that the authentication implementation matches the security policy
   ```

3. **Exploring the docs-agent:**
   - Located in `.claude/agents/docs-agent.md`
   - Uses the `doc-compliance` skill
   - 5-step verification workflow

## Related Examples

- [Simple Analysis](../simple-analysis/) - Analysis workflow (complete)

## Contributing

Interested in helping develop this example? Check the main project README for contribution guidelines.
