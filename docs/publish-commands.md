# Publish Commands

After creating an empty public GitHub repository named `clinical-ui-skills`, run from this folder:

```bash
git init
git add .
git commit -m "Release Clinical UI Skills v0.1.0"
git branch -M main
git remote add origin <PASTE_THE_GITHUB_REMOTE_YOU_CREATED>
git push -u origin main

git tag -a v0.1.0 -m "Clinical UI Skills v0.1.0"
git push origin v0.1.0
```

Then create the GitHub Release from tag `v0.1.0` using `RELEASE_NOTES_v0.1.0.md`, set `assets/social-preview.png` as the repository social preview, and confirm the `Validate` Action is green.

Do not copy the angle-bracket placeholder literally; GitHub shows the exact remote URL in the repository's **Code** menu.
