#!/usr/bin/env python3
"""Validate generated internal links, anchors, assets, feeds, and search URLs.

No dependencies or network requests; external article citations are excluded.
"""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.errors = []
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        for key in ("href", "src", "data-index"):
            if attrs.get(key):
                self.links.append(attrs[key])


def check_site(root, base):
    root = root.resolve()
    base = base.rstrip("/") + "/"
    origin = urlsplit(base)
    pages = {path: Page(path.read_text()) for path in root.rglob("*.html")}
    errors = []
    references = 0

    def check(source, link):
        nonlocal references
        references += 1
        relative = source.relative_to(root).as_posix()
        source_url = urljoin(base, relative)
        target = urlsplit(urljoin(source_url, link))
        if target.scheme not in ("http", "https") or target.netloc != origin.netloc:
            return
        if not target.path.startswith(origin.path):
            errors.append(f"{relative}: escapes site base: {link}")
            return
        local = (root / unquote(target.path[len(origin.path):])).resolve()
        if not local.is_relative_to(root):
            errors.append(f"{relative}: escapes output directory: {link}")
            return
        if local.is_dir():
            local /= "index.html"
        if not local.is_file():
            errors.append(f"{relative}: missing destination: {link}")
        elif target.fragment and local in pages:
            if unquote(target.fragment) not in pages[local].ids:
                errors.append(f"{relative}: missing anchor: {link}")

    if not pages:
        errors.append("No generated HTML found")
    for path, page in pages.items():
        errors.extend(f"{path.relative_to(root)}: {error}" for error in page.errors)
        if page.h1_count != 1:
            errors.append(f"{path.relative_to(root)}: expected one h1, got {page.h1_count}")
        for link in page.links:
            check(path, link)
    for path in root.rglob("*.css"):
        for link in re.findall(r'url\([\'\"]?([^\)\'\"]+)', path.read_text()):
            check(path, link.strip())
    for path in root.rglob("*.xml"):
        try:
            for element in ET.parse(path).iter():
                if element.tag.split("}")[-1] in ("loc", "link", "guid", "url"):
                    if element.text:
                        check(path, element.text.strip())
                if element.attrib.get("href"):
                    check(path, element.attrib["href"])
        except ET.ParseError as error:
            errors.append(f"{path.relative_to(root)}: invalid XML: {error}")
    index = root / "index.json"
    try:
        entries = json.loads(index.read_text())
        seen = set()
        for entry in entries:
            url = entry["permalink"]
            if not url.startswith(base):
                errors.append(f"index.json: search result escapes site base: {url}")
            if url in seen:
                errors.append(f"index.json: duplicate result: {url}")
            seen.add(url)
            check(index, url)
    except (OSError, ValueError, KeyError) as error:
        errors.append(f"index.json: invalid search index: {error}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Passed: {len(pages)} pages, {references} internal/asset references; anchors, feeds, and search index valid.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path("public"))
    parser.add_argument("--base-url", required=True)
    args = parser.parse_args()
    sys.exit(check_site(args.directory, args.base_url))
