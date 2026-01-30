# Publishing to GitHub - Quick Guide

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `meme-generator` (or your choice)
3. Description: "A retro-futuristic meme generator with drag-to-position text"
4. Choose **Public** or **Private**
5. **DO NOT** check "Initialize with README" (we already have one)
6. Click **"Create repository"**

## Step 2: Connect and Push

After creating the repository, GitHub will show you commands. Run these in your terminal:

```bash
cd "y:\My Drive\projects\cursor\cursor tester\meme-generator"

# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/meme-generator.git

# Push your code
git branch -M main
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:YOUR_USERNAME/meme-generator.git
git branch -M main
git push -u origin main
```

## Troubleshooting

- **Authentication required**: You may need to use a Personal Access Token instead of password
- **Branch name**: If GitHub uses `main` instead of `master`, run `git branch -M main` first
- **Already exists**: If remote already exists, use `git remote set-url origin <URL>`
