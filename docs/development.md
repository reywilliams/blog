# Development, previews, and publishing

## Checks

Run `bash scripts/check.sh` after layout, navigation, asset, or content-link
changes. It first runs regression tests for escaped preview routes and invalid
anchors, then uses Hugo 0.152.2 (set `HUGO_BIN` if needed) to build isolated temporary
outputs for both a domain root and `/preview/blog/`. Python's standard library
checker validates generated HTML links, asset paths, heading anchors, duplicate
IDs, one h1 per page, CSS font URLs, XML feeds/sitemaps, and unique search-result
URLs. It does not make network requests or audit third-party citations.

Browser review should cover homepage, articles, archive, tags, About, and Search
at mobile and desktop sizes. Check wrapping, keyboard focus, search results,
contents/footnote links, previous/next navigation, and return-to-writing links.

## Private previews

Set your preview URL and output directory locally. Machine hostnames, private
network domains, absolute home-directory paths, and credentials must stay out
of tracked files. Keep optional local notes in `.local/`, which is ignored.

For example, replace these generic values in your shell:

```sh
BLOG_PREVIEW_URL="https://preview.example.test/preview/blog/"
BLOG_PREVIEW_DIR=".preview/blog"
hugo --gc --minify \
  --baseURL "$BLOG_PREVIEW_URL" \
  --destination "$BLOG_PREVIEW_DIR"
python3 scripts/check-links.py \
  --base-url "$BLOG_PREVIEW_URL" \
  --directory "$BLOG_PREVIEW_DIR"
```

Use your actual private preview URL when building locally. If serving through
Tailscale, connect to the tailnet to review it. The preview is a snapshot;
rebuild after changes. Preserve unrelated artifacts in shared preview directories.
Personal-site links intentionally leave the preview; blog links remain under
its configured base path.

Use `site.Home.RelPermalink` for home links, `.RelPermalink` for page links, and
the shared menu URL partial for menu entries. Do not strip the preview base path.

## CI and publishing

`.github/workflows/hugo.yaml` is the source of truth. Pull requests build and
validate both routes without publishing. Pushes to `main` and manual runs on
`main` validate both routes, build using the Pages base URL, validate the exact
deployment artifact, and publish it through GitHub Pages. Failed checks block
deployment. The build requires only Hugo and Python; unused Go, Node, Sass,
theme checkout, and cache setup have been removed.

Local edits and Tailscale previews do not publish. A push to `main` does. Keep
`public/`, `resources/`, screenshots, and preview output out of commits. To roll
back a published change, revert the source commit and publish through CI.
