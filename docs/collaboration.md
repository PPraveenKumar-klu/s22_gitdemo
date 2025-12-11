# Collaboration with Git

Learn how to collaborate effectively with others using Git.

## Setting Up for Collaboration

### Fork and Clone
When contributing to others' projects:
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/your-username/repository.git
cd repository

# Add upstream remote
git remote add upstream https://github.com/original-owner/repository.git
```

### Working with Remotes
```bash
# View remotes
git remote -v

# Fetch from remote
git fetch origin

# Pull changes (fetch + merge)
git pull origin main

# Push changes
git push origin branch-name
```

## Pull Request Workflow

1. **Fork** the repository (on GitHub)
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Make** changes and commit
5. **Push** to your fork
6. **Open** a Pull Request on GitHub
7. **Review** and address feedback
8. **Merge** after approval

```bash
# Complete workflow example
git clone https://github.com/your-username/repo.git
cd repo
git checkout -b feature/my-feature
# Make changes
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
# Open PR on GitHub
```

## Keeping Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream main into your main
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

## Code Review Best Practices

### For Authors
- Keep changes small and focused
- Write clear commit messages
- Respond to feedback constructively
- Test your changes before submitting

### For Reviewers
- Be constructive and respectful
- Focus on the code, not the person
- Explain why, not just what
- Approve promptly when appropriate

## Handling Conflicts

When multiple people edit the same code:

```bash
# Pull latest changes
git pull origin main

# If conflicts occur, Git will mark them
# Edit the conflicted files
# Look for conflict markers: <<<<<<<, =======, >>>>>>>

# After resolving
git add conflicted-file.py
git commit -m "Resolve merge conflict"
git push origin branch-name
```

## Communication

### Commit Messages
```
Format:
<type>: <subject>

<body>

<footer>

Example:
feat: Add user authentication

Implement login and signup functionality using JWT tokens.
Includes password hashing and session management.

Closes #123
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

## Team Workflows

### Centralized Workflow
- Everyone works on `main` branch
- Simple, but risky for production code

### Feature Branch Workflow
- Each feature gets its own branch
- Merge to main after review
- Better for small teams

### Gitflow Workflow
- Structured branching model
- Separate `main` and `develop` branches
- Good for projects with scheduled releases

### Forking Workflow
- Each developer has their own fork
- Changes submitted via pull requests
- Common in open source

## Tips for Successful Collaboration

1. **Communicate Early**: Discuss major changes before implementing
2. **Stay Synced**: Pull changes frequently
3. **Review Thoroughly**: Careful code review prevents bugs
4. **Be Respectful**: Maintain a positive team environment
5. **Document**: Keep README and docs updated
6. **Test**: Ensure changes don't break existing functionality
