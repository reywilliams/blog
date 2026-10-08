# ReysCorner

A standalone Hugo blog at [blog.reywilliams.com](https://blog.reywilliams.com/),
using the visual language of [reywilliams.com](https://reywilliams.com/).
There is no theme dependency or frontend package manager.

## Local development

Use Hugo **0.152.2**, matching CI, and Python 3.9+ for validation.

```sh
hugo server --bind 0.0.0.0 --port 1313
```

Open http://localhost:1313/. Hugo rebuilds when content, components, or styles change.

```sh
bash scripts/check.sh
```

This builds and checks both the production domain root and a nested preview path.
Set `HUGO_BIN=/path/to/hugo` if the pinned version is not on your PATH.

## Common updates

| Change                                                     | Edit                        |
| ---------------------------------------------------------- | --------------------------- |
| Write a post                                               | `content/posts/`            |
| Homepage introduction                                      | `content/_index.md`         |
| About page                                                 | `content/whoami.md`         |
| Site name, author, personal site, navigation, date formats | `config.yaml`               |
| Colors and fonts                                           | `assets/css/tokens.css`     |
| Header, footer, metadata                                   | `layouts/partials/layout/`  |
| Writing rows                                               | `layouts/partials/writing/` |
| Article header, tags, previous/next links                  | `layouts/partials/article/` |
| Article body formatting                                    | `assets/css/prose.css`      |
| Search behavior                                            | `assets/js/search.js`       |

Create a post with `hugo new content/posts/my-post.md`. Add a `description` for
its homepage excerpt. Start body headings at `##` and nest subsections with
`###` or `####`. For posts with images, use a page bundle:
`content/posts/my-post/index.md`, with images in the same directory and relative
Markdown image paths. Set `draft: true` while writing; preview drafts using
`hugo server -D`. Existing posts remain at `/posts/<slug>/`.

Read [architecture](docs/architecture.md) for component boundaries and
[development](docs/development.md) for previews, checks, and publishing.
