# Working on ReysCorner

This is a standalone Hugo 0.152.2 blog. Read README.md and docs/architecture.md
before changing its structure; read docs/development.md for checks/deployment.

- Keep authored copy in content/ and identity/navigation in config.yaml.
- Reuse partials in layouts/partials/. Page templates compose components.
- Keep CSS/JS in assets/ and use existing tokens; Hugo owns minification and
  fingerprinting. Keep fonts and decorative art self-hosted in static/.
- Preserve post URLs, base-path-aware links, RSS, search, accessibility, and
  responsive wrapping. Do not reintroduce a theme or unnecessary runtime tooling.
- Run bash scripts/check.sh for changes affecting rendering or links and review
  mobile/desktop behavior for UI changes.
- Do not commit build output or previews. Preserve unrelated Tailscale preview
  artifacts. Publishing occurs on push to main; publish only when requested.

- Never commit private preview hostnames, tailnet domains/IPs, absolute local
  paths, credentials, or local environment files. Use generic examples in docs
  and keep machine-specific notes in ignored .local/.

- Use Conventional Commit messages and PR titles (for example feat(blog): ...).
  Keep review comments concrete and focused on actionable findings.
- Write PR bodies with What/Why/How sections, short prose, and clear bullets.
  Define outcomes and visible UX behavior explicitly. For UI changes, attach
  matching before/after screenshots to the PR body with gh pr edit --attach.
  Keep screenshot files out of commits and private machine details out of images.
