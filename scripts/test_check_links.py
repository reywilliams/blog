"""Regression checks for nested preview routes across navigation and XML feeds."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "check_links", Path(__file__).with_name("check-links.py")
)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PreviewLinks(unittest.TestCase):
    base = "https://preview.example.test/preview/blog/"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "index.html").write_text('<h1>Writing</h1><main id="main"></main>')
        (self.root / "index.json").write_text(json.dumps([]))

    def run_check(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return checker.check_site(self.root, self.base)

    def test_valid_nested_routes_and_fragments(self):
        (self.root / "index.html").write_text(
            '<h1>Writing</h1><main id="main"></main>'
            '<a href="/preview/blog/#main">Writing</a>'
        )
        (self.root / "sitemap.xml").write_text(
            f'<urlset><url><loc>{self.base}</loc></url></urlset>'
        )
        self.assertEqual(self.run_check(), 0)

    def test_navigation_cannot_escape_preview(self):
        (self.root / "index.html").write_text('<h1>Writing</h1><a href="/">Writing</a>')
        self.assertEqual(self.run_check(), 1)

    def test_sitemap_cannot_escape_preview(self):
        (self.root / "sitemap.xml").write_text(
            '<urlset><url><loc>https://preview.example.test/posts/missing/</loc></url></urlset>'
        )
        self.assertEqual(self.run_check(), 1)

    def test_feed_self_link_cannot_escape_preview(self):
        (self.root / "index.xml").write_text(
            '<rss xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            '<atom:link href="https://preview.example.test/index.xml"/>'
            '</channel></rss>'
        )
        self.assertEqual(self.run_check(), 1)

    def test_missing_heading_anchor_is_rejected(self):
        (self.root / "index.html").write_text('<h1>Writing</h1><a href="#missing">Section</a>')
        self.assertEqual(self.run_check(), 1)


if __name__ == "__main__":
    unittest.main()
