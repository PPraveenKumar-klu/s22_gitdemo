# Branching and Merging Guide

Branches allow you to develop features, fix bugs, or experiment with new ideas in isolation from the main codebase.

## Why Use Branches?

- **Isolation**: Work on features without affecting the main code
- **Collaboration**: Multiple people can work simultaneously
- **Organization**: Keep different types of work separate
- **Safety**: Main branch remains stable

## Creating and Switching Branches

### Create a New Branch
```bash
# Create a new branch
git branch feature-name

# Create and switch to new branch
git checkout -b feature-name
```

### Switch Between Branches
```bash
# Switch to existing branch
git checkout branch-name

# Modern alternative
git switch branch-name
```

### List Branches
```bash
# List local branches
git branch

# List all branches (including remote)
git branch -a
```

## Merging Branches

### Fast-Forward Merge
When there are no new commits on the target branch:
```bash
git checkout main
git merge feature-branch
```

### Three-Way Merge
When both branches have new commits:
```bash
git checkout main
git merge feature-branch
```

## Branch Management

### Delete a Branch
```bash
# Delete local branch (after merging)
git branch -d branch-name

# Force delete (even if not merged)
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

### Rename a Branch
```bash
# Rename current branch
git branch -m new-name

# Rename a specific branch
git branch -m old-name new-name
```

## Common Branching Strategies

### Feature Branch Workflow
1. Create a branch for each feature
2. Work on the feature
3. Merge back to main when complete
4. Delete the feature branch

```bash
git checkout -b feature/new-feature
# Make changes and commit
git checkout main
git merge feature/new-feature
git branch -d feature/new-feature
```

### Git Flow
- `main` - Production code
- `develop` - Development branch
- `feature/*` - New features
- `hotfix/*` - Emergency fixes
- `release/*` - Release preparation

## Best Practices

1. **Use Descriptive Names**: `feature/user-login`, `bugfix/null-pointer`
2. **Keep Branches Short-Lived**: Merge or delete after use
3. **Branch from Updated Main**: Always start from latest code
4. **One Feature Per Branch**: Keep changes focused
5. **Regular Commits**: Commit frequently on feature branches

## Exercise

Try creating a branch, making changes, and merging:

```bash
# Create and switch to new branch
git checkout -b practice-branch

# Make some changes to a file
echo "Practice change" >> practice.txt
git add practice.txt
git commit -m "Add practice file"

# Switch back to main and merge
git checkout main
git merge practice-branch

# Clean up
git branch -d practice-branch
```
