#!/usr/bin/env python3
"""
fix_canonical_redirects.py
==========================
Fixes "canonical points to redirect" Ahrefs errors across ALL pages on saudiutilityhub.com.

The problem:
  Ahrefs flags pages where the <link rel="canonical"> tag points to a URL that
  redirects (e.g., trailing-slash version /blog/ redirecting to /blog or vice versa).
  This tells Google the canonical is unreliable, lowering trust & score.

What this script does:
  1. Scans every .html file in the folder you point it at
  2. Finds <link rel="canonical" href="..."> tags
  3. Removes trailing slashes from canonical URLs UNLESS the URL is the root domain
     (https://www.saudiutilityhub.com/ stays as-is — root slash is correct)
  4. Fixes og:url to match the corrected canonical
  5. Also fixes any href="https://www.saudiutilityhub.com/blog/" internal links
     in <a> tags to remove the trailing slash (consistent linking)

Usage:
  python3 fix_canonical_redirects.py /path/to/your/site/files

  Example (if your files are in the current folder):
    python3 fix_canonical_redirects.py .

  Example (if you extracted your site to ~/Desktop/saudisite):
    python3 fix_canonical_redirects.py ~/Desktop/saudisite

The script NEVER modifies:
  - https://www.saudiutilityhub.com/  (root canonical, slash is correct)
  - External URLs (gosi.gov.sa, google.com, etc.)
  - Non-HTML files

A backup of each changed file is saved as filename.html.bak before editing.
"""

import os
import re
import sys
import shutil
from pathlib import Path

DOMAIN = "https://www.saudiutilityhub.com"
ROOT_CANONICAL = DOMAIN + "/"  # The ONE URL where trailing slash is correct

def fix_trailing_slash(url: str) -> str:
    """Remove trailing slash from URL unless it's the bare root domain."""
    if url == ROOT_CANONICAL or url == DOMAIN:
        return url  # Never touch the root
    if url.startswith(DOMAIN) and url.endswith("/") and len(url) > len(ROOT_CANONICAL):
        return url.rstrip("/")
    return url

def process_file(filepath: Path, dry_run: bool = False) -> bool:
    """Process a single HTML file. Returns True if changes were made."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"  ✗ Cannot read {filepath.name}: {e}")
        return False

    original = content
    changes = []

    # --- Fix canonical tag ---
    def fix_canonical_tag(m):
        url = m.group(1)
        fixed = fix_trailing_slash(url)
        if fixed != url:
            changes.append(f"canonical: {url}  →  {fixed}")
        return f'<link rel="canonical" href="{fixed}"'

    content = re.sub(
        r'<link\s+rel="canonical"\s+href="([^"]+)"',
        fix_canonical_tag,
        content,
        flags=re.IGNORECASE
    )

    # Also handle reversed attribute order
    content = re.sub(
        r'<link\s+href="([^"]+)"\s+rel="canonical"',
        lambda m: f'<link rel="canonical" href="{fix_trailing_slash(m.group(1))}"',
        content,
        flags=re.IGNORECASE
    )

    # --- Fix og:url ---
    def fix_og_url(m):
        url = m.group(1)
        fixed = fix_trailing_slash(url)
        if fixed != url:
            changes.append(f"og:url:   {url}  →  {fixed}")
        return f'<meta property="og:url" content="{fixed}"'

    content = re.sub(
        r'<meta\s+property="og:url"\s+content="([^"]+)"',
        fix_og_url,
        content,
        flags=re.IGNORECASE
    )

    # --- Fix hreflang alternate links (non-root) ---
    def fix_hreflang(m):
        prefix = m.group(1)  # everything up to href="
        url = m.group(2)
        suffix = m.group(3)  # closing part
        fixed = fix_trailing_slash(url)
        if fixed != url:
            changes.append(f"hreflang: {url}  →  {fixed}")
        return f'{prefix}"{fixed}"{suffix}'

    content = re.sub(
        r'(<link[^>]+hreflang="[^"]*"[^>]+href=)"([^"]+)"([^>]*>)',
        fix_hreflang,
        content,
        flags=re.IGNORECASE
    )
    # Also handle href before hreflang
    content = re.sub(
        r'(<link[^>]+href=)"([^"]+)"([^>]*hreflang="[^"]*"[^>]*>)',
        fix_hreflang,
        content,
        flags=re.IGNORECASE
    )

    # --- Fix internal <a href> links with trailing slash (non-root, non-blog-index) ---
    # We keep /blog/ intact since that's the blog index directory URL
    # But /blog/some-article/ should be /blog/some-article.html (no slash needed)
    # This regex targets .html pages linked with a trailing slash
    def fix_internal_link(m):
        url = m.group(1)
        # Only fix .html URLs that somehow got a trailing slash
        if url.endswith(".html/"):
            fixed = url.rstrip("/")
            changes.append(f"a href:   {url}  →  {fixed}")
            return f'href="{fixed}"'
        return m.group(0)

    content = re.sub(
        r'href="(https://www\.saudiutilityhub\.com/[^"]+\.html/)"',
        fix_internal_link,
        content,
        flags=re.IGNORECASE
    )

    if content == original:
        return False  # No changes

    if dry_run:
        print(f"  [DRY RUN] Would fix {filepath.name}:")
        for c in changes:
            print(f"    • {c}")
        return True

    # Backup original
    backup = filepath.with_suffix(".html.bak")
    shutil.copy2(filepath, backup)

    # Write fixed version
    filepath.write_text(content, encoding="utf-8")
    print(f"  ✓ Fixed {filepath.name} ({len(changes)} change(s))")
    for c in changes:
        print(f"    • {c}")
    return True


def main():
    # Parse args
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not args:
        print("Usage: python3 fix_canonical_redirects.py <folder> [--dry-run]")
        print("Example: python3 fix_canonical_redirects.py .")
        sys.exit(1)

    folder = Path(args[0]).expanduser().resolve()
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a directory.")
        sys.exit(1)

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Scanning: {folder}")
    print("=" * 60)

    html_files = sorted(folder.rglob("*.html"))
    if not html_files:
        print("No .html files found.")
        sys.exit(0)

    print(f"Found {len(html_files)} HTML file(s)\n")

    fixed_count = 0
    skipped_count = 0

    for f in html_files:
        # Skip backup files
        if f.suffix == ".bak":
            continue
        result = process_file(f, dry_run=dry_run)
        if result:
            fixed_count += 1
        else:
            skipped_count += 1

    print("\n" + "=" * 60)
    if dry_run:
        print(f"[DRY RUN COMPLETE] Would fix: {fixed_count} | No changes needed: {skipped_count}")
        print("Run without --dry-run to apply changes.")
    else:
        print(f"Done! Fixed: {fixed_count} | Already correct: {skipped_count}")
        if fixed_count > 0:
            print("\nNext steps:")
            print("1. Upload the fixed .html files to your server (replace old versions)")
            print("2. In Ahrefs: Site Audit → Re-crawl")
            print("3. In Google Search Console: submit sitemap.xml again")
            print("4. Backups saved as .html.bak — delete them after verifying")


if __name__ == "__main__":
    main()
