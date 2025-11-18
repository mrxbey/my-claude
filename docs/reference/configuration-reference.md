# Configuration Reference

Complete reference for MyClaude framework configuration in `.claude/settings.json`.

## File Location

```
.claude/settings.json       # Version-controlled team config
.claude/settings.local.json # Gitignored personal overrides (optional)
```

## Complete Schema

```json
{
  "permissions": {
    "allow": ["Pattern1", "Pattern2"],
    "ask": ["Pattern3"],
    "deny": ["Pattern4"]
  },
  "hooks": {
    "PreToolUse": [/* hook configs */],
    "PostToolUse": [/* hook configs */],
    "OnError": [/* hook configs */]
  },
  "env": {
    "VAR_NAME": "value"
  }
}
```

## Permissions

### Pattern Syntax

**File Operations**:
```json
"Read(.claude/**)"         // Any file in .claude/ recursively
"Write(src/**/*.js)"       // JavaScript files in src/
"Edit(docs/*.md)"          // Markdown files in docs/
"Read(config.json)"        // Specific file
```

**Bash Commands**:
```json
"Bash(git status)"         // Exact command
"Bash(git *)"              // Any git command
"Bash(npm install*)"       // npm install with any args
```

**Other Tools**:
```json
"Grep(**)"                 // Any grep operation
"Glob(src/**)"             // Glob in src/
"WebFetch(*)"              // Any web fetch
```

### Permission Levels

**`allow`**: Auto-approved, executes immediately
```json
"allow": [
  "Read(**)",
  "Bash(git status)",
  "Bash(git diff*)",
  "Grep(**)",
  "Glob(**)"
]
```

**`ask`**: Requires user approval
```json
"ask": [
  "Write(**)",
  "Edit(**)",
  "Bash(git commit*)",
  "Bash(npm install*)"
]
```

**`deny`**: Blocked, will not execute
```json
"deny": [
  "Read(**/.env*)",
  "Read(**/secrets/**)",
  "Bash(rm -rf*)",
  "Bash(sudo *)",
  "WebFetch(*)"
]
```

## Hooks

### Hook Types

**PreToolUse**: Execute before tool runs
```json
{
  "PreToolUse": [{
    "matcher": "Write(.claude/**)",
    "hooks": [{
      "command": "python scripts/validate.py $FILE_PATH",
      "mode": "blocking"
    }]
  }]
}
```

**PostToolUse**: Execute after tool completes
```json
{
  "PostToolUse": [{
    "matcher": "Write(**/*.md)",
    "hooks": [{
      "command": "prettier --write $FILE_PATH",
      "mode": "async"
    }]
  }]
}
```

**OnError**: Execute when tool fails
```json
{
  "OnError": [{
    "matcher": "Bash(*)",
    "hooks": [{
      "command": "echo \"Error: $ERROR_MESSAGE\" >> error.log",
      "mode": "async"
    }]
  }]
}
```

### Hook Configuration

```json
{
  "matcher": "Pattern",    // What operations to hook
  "hooks": [{
    "command": "script.sh $VAR",  // Command to run
    "mode": "blocking"            // blocking or async
  }]
}
```

### Hook Variables

Available in hook commands:

- `$FILE_PATH` - File being operated on
- `$TOOL_NAME` - Tool name (Read, Write, Edit, Bash, etc.)
- `$ARGUMENTS` - Tool arguments (JSON)
- `$ERROR_MESSAGE` - Error message (OnError only)

### Hook Modes

**`blocking`**: Wait for completion, check exit code
- Exit 0: Continue
- Exit 2: Block operation, show error to Claude
- Exit other: Error, show to Claude

**`async`**: Run in background, don't wait

## Environment Variables

```json
{
  "env": {
    "FRAMEWORK_MODE": "development",
    "LOG_LEVEL": "info",
    "CUSTOM_VAR": "value"
  }
}
```

Can be overridden by shell environment variables.

## Configuration Layers

Loaded in order (later overrides earlier):

1. `.claude/settings.json` (base, version-controlled)
2. `.claude/settings.local.json` (personal, gitignored)
3. Shell environment variables (highest priority)

## Examples

### Strict Security

```json
{
  "permissions": {
    "allow": ["Read(**)", "Bash(git status)"],
    "ask": ["Write(**)", "Bash(*)"],
    "deny": ["Read(**/.env*)", "Bash(rm*)", "WebFetch(*)"]
  }
}
```

### Auto-Formatting

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write(**/*.md)",
      "hooks": [{
        "command": "prettier --write $FILE_PATH",
        "mode": "async"
      }]
    }]
  }
}
```

### Validation Before Write

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write(.claude/**)",
      "hooks": [{
        "command": "python scripts/validate_framework.py --file $FILE_PATH",
        "mode": "blocking"
      }]
    }]
  }
}
```

## Related Documentation

- [Developer Guide: Extending Framework](../developer-guide/extending-framework.md)
