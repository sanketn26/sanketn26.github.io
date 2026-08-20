from pathlib import Path


COURSE_SITEMAPS = (
    "https://sanketn26.github.io/learn-security/sitemap.xml",
    "https://sanketn26.github.io/learn-ml/sitemap.xml",
    "https://sanketn26.github.io/AIEngineering/sitemap.xml",
    "https://sanketn26.github.io/interview-prep/sitemap.xml",
)


def on_post_build(config, **kwargs):
    """Turn MkDocs' sitemap into an index covering every course site."""
    site_dir = Path(config.site_dir)
    generated_sitemap = site_dir / "sitemap.xml"
    pages_sitemap = site_dir / "sitemap-pages.xml"

    generated_sitemap.replace(pages_sitemap)

    sitemap_urls = (f"{config.site_url}sitemap-pages.xml", *COURSE_SITEMAPS)
    entries = "\n".join(
        f"  <sitemap><loc>{url}</loc></sitemap>" for url in sitemap_urls
    )
    sitemap_index = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</sitemapindex>\n"
    )
    generated_sitemap.write_text(sitemap_index, encoding="utf-8")

    compressed_sitemap = site_dir / "sitemap.xml.gz"
    if compressed_sitemap.exists():
        compressed_sitemap.unlink()
