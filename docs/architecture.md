# Architecture

## Content and configuration

Markdown in `content/` is the source of authored page copy. Front matter contains
post titles, dates, descriptions, tags, and optional `showtoc`. Site identity,
asset paths, date formats, and both menus belong in `config.yaml`. Do not hardcode
navigation or author URLs in templates. The homepage introduction belongs in
`content/_index.md`.

## Components

Hugo partials are the components. Page templates select content and compose
partials; partials render only the context they are passed.

- `_default/baseof.html`: document shell and main-content block.
- `partials/layout/`: document metadata, asset pipeline, header, footer.
- `partials/navigation/`: shared menu renderer and base-path-aware URL handling.
  Hugo's resolved `pageRef` URLs must not receive the preview prefix twice.
- `partials/page/`: shared page heading and decorative homepage hero.
- `partials/writing/`: list container and one dated entry. Pass `pages` and
  `headingLevel` to `list.html`; it passes `page` and `headingLevel` to each entry.
  Entry headings sit below their parent heading (h3 below homepage/archives h2).
- `partials/article/`: article heading/metadata, tag links, previous/next links.
- `_default/single.html`: shared article/About presentation. About requires no
  duplicate template; its content uses the default single-page layout.
- `_default/list.html`, `archives.html`, `terms.html`: page-specific composition
  around the shared writing components.
- `_default/search.html`: search form; `_default/index.json`: search data.
- `_default/rss.xml`: local RSS implementation. Feeds include posts only.
- `_default/_markup/`: bundle-aware Markdown image rendering. Article headings
  use Hugo's default renderer. Start Markdown body headings at `##` and nest
  subsections with `###`/`####`; the link checker enforces one page h1.

Current posts use standard Markdown and no custom shortcodes. All required
rendering is local; no PaperMod templates, scripts, or styles are loaded.

## Styles and runtime assets

Authored CSS and JavaScript live in `assets/`, where Hugo concatenates/minifies
CSS and fingerprints CSS/JS URLs for cache invalidation. Production output is
minified; source files stay readable. Fonts and art remain self-hosted in
`static/`. Relative font URLs resolve from the generated `css/` directory.

- `tokens.css`: font declarations and shared color tokens.
- `base.css`: reset, default type/link behavior, focus and skip link.
- `layout.css`: page shell, header, footer, homepage hero.
- `writing.css`: writing list and section heading.
- `article.css`: article header, metadata, contents, tags, previous/next links.
- `prose.css`: Markdown body typography, images, tables, and code blocks.
- `pages.css`: archive, tags, generic page headings, and result lists.
- `search.css`: search form and status.
- `syntax.css`: Hugo-generated Monokai code highlighting.
- `responsive.css`: responsive component overrides and reduced motion, loaded last.

Use the existing components and tokens for changes. Keep readable source, one
h1, visible focus, semantic landmarks, image alt text, and mobile wrapping.
Regenerate syntax colors with `hugo gen chromastyles --style monokai` if needed.

Search is the only application JavaScript. It loads the generated JSON index,
matches all query words against title/body, renders links using DOM APIs, and
announces the result count. It handles loading failures; it is not fuzzy search.
The rest of the blog works without JavaScript.
