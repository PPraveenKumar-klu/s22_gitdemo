# Git Basics

This guide covers the fundamental Git commands you need to know.

## Setting Up Git

Before you start using Git, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Basic Workflow

### 1. Initialize or Clone
```bash
# Create a new repository
git init

# Or clone an existing one
git clone https://github.com/username/repository.git
```

### 2. Make Changes
Edit your files using your favorite editor.

### 3. Stage Changes
```bash
# Stage specific files
git add filename.py

# Stage all changes
git add .
```

### 4. Commit Changes
```bash
git commit -m "Descriptive commit message"
```

### 5. Push to Remote
```bash
git push origin main
```

## Checking Status

```bash
# View current status
git status

# View commit history
git log

# View changes
git diff
```

## Common Commands Reference

| Command | Description |
|---------|-------------|
| `git status` | Show the working tree status |
| `git add <file>` | Add file to staging area |
| `git commit -m "message"` | Commit staged changes |
| `git push` | Upload local changes to remote |
| `git pull` | Download and merge remote changes |
| `git log` | Show commit history |
| `git diff` | Show changes between commits |

## Best Practices

1. **Commit Often**: Make small, logical commits
2. **Write Clear Messages**: Describe what and why, not how
3. **Pull Before Push**: Always sync before pushing
4. **Use Branches**: Keep main branch stable
5. **Review Before Commit**: Check what you're committing

## Next Steps

- Learn about [branching and merging](branching-guide.md)
- Explore [collaboration workflows](collaboration.md)
- Practice [conflict resolution](conflict-resolution.md)
