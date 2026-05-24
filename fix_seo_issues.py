#!/usr/bin/env python3
"""
Fix all SEO issues across saudiutilityhub.com:
1. Fix canonical URLs missing www (saudiutilityhub.com → www.saudiutilityhub.com)
2. Fix canonical URLs missing .html extension
3. Fix canonical pointing to wrong URL (saudi-work-visa-types-2026.html pointing to /blog/)
4. Add missing canonical tags
5. Add missing og:image tags
6. Add missing hreflang tags
7. Shorten title tags that are over 60 chars
"""

import os
import re

SITES = "/sessions/zealous-great-noether/mnt/Sites"
BASE = "https://www.saudiutilityhub.com"
OG_IMAGE = "https://www.saudiutilityhub.com/og-image.png"

fixed = 0
skipped = 0

def get_page_url(filepath):
    """Convert local file path to canonical URL."""
    rel = filepath.replace(SITES, "").lstrip("/")
    # Convert index.html to trailing slash
    if rel == "index.html":
        return f"{BASE}/"
    if rel.endswith("/index.html"):
        folder = rel[:-len("index.html")]
        return f"{BASE}/{folder}"
    return f"{BASE}/{rel}"

def fix_canonical(content, url):
    """Fix or add canonical tag."""
    # Fix wrong domain (missing www)
    content = re.sub(
        r'<link rel="canonical" href="https://saudiutilityhub\.com([^"]*)"',
        lambda m: f'<link rel="canonical" href="https://www.saudiutilityhub.com{m.group(1)}"',
        content
    )
    # Fix missing .html extension in canonical (e.g. /ur/muqeem-visa-check without .html)
    def fix_ext(m):
        href = m.group(1)
        # If it doesn't end with / or .html or .xml, and has no extension, add .html
        if not href.endswith('/') and not href.endswith('.html') and '.' not in href.split('/')[-1]:
            href = href + '.html'
        return f'<link rel="canonical" href="{href}"'
    content = re.sub(r'<link rel="canonical" href="([^"]+)"', fix_ext, content)

    # Fix the one page pointing to wrong URL
    content = re.sub(
        r'<link rel="canonical" href="https://www\.saudiutilityhub\.com/blog/saudi-work-visa-types-2026\.html[^"]*"',
        f'<link rel="canonical" href="{url}"',
        content
    )

    # Add canonical if missing
    if 'rel="canonical"' not in content:
        canonical_tag = f'<link rel="canonical" href="{url}">'
        content = re.sub(r'(<meta name="description"[^>]*>)', rf'\1\n  {canonical_tag}', content, count=1)
        if 'rel="canonical"' not in content:
            content = re.sub(r'(</head>)', f'  {canonical_tag}\n\\1', content, count=1)
    return content

def fix_og_image(content):
    """Add missing og:image tag."""
    if 'og:image' not in content:
        og_img = f'  <meta property="og:image" content="{OG_IMAGE}">\n  <meta name="twitter:image" content="{OG_IMAGE}">'
        # Insert after og:description or og:title
        if 'og:description' in content:
            content = re.sub(r'(<meta property="og:description"[^>]*>)', rf'\1\n{og_img}', content, count=1)
        elif 'og:title' in content:
            content = re.sub(r'(<meta property="og:title"[^>]*>)', rf'\1\n{og_img}', content, count=1)
        else:
            content = re.sub(r'(</head>)', f'{og_img}\n\\1', content, count=1)
    return content

def fix_og_url(content, url):
    """Fix missing og:url or wrong og:url."""
    if 'og:url' not in content:
        og_url = f'  <meta property="og:url" content="{url}">'
        if 'og:type' in content:
            content = re.sub(r'(<meta property="og:type"[^>]*>)', rf'\1\n{og_url}', content, count=1)
        else:
            content = re.sub(r'(</head>)', f'{og_url}\n\\1', content, count=1)
    return content

def shorten_title(content, filepath):
    """Shorten title tags over 60 chars."""
    m = re.search(r'<title>([^<]+)</title>', content)
    if not m:
        return content
    title = m.group(1)
    if len(title) <= 60:
        return content

    # Remove " | Saudi Utility Hub" suffix first
    shortened = re.sub(r'\s*[|—]\s*Saudi Utility Hub\s*$', '', title).strip()
    # If still too long, truncate smartly at word boundary
    if len(shortened) > 60:
        # Try removing year
        shortened = re.sub(r'\s+20(25|26)\s*', ' ', shortened).strip()
    if len(shortened) > 60:
        # Hard cut at 57 + ...
        shortened = shortened[:57].rsplit(' ', 1)[0] + '...'

    content = re.sub(r'<title>[^<]+</title>', f'<title>{shortened}</title>', content, count=1)
    return content

def get_hreflang_block(url, filepath):
    """Generate hreflang block based on page location."""
    rel = filepath.replace(SITES, "").lstrip("/")

    # Determine language and matching pages
    if rel.startswith("ar/"):
        page = rel[3:]  # strip ar/
        en_url = f"{BASE}/{page}" if page != "index.html" else f"{BASE}/"
        ar_url = url
        ur_base = rel.replace("ar/", "ur/")
        # only add ur hreflang if we know the page exists (skip for now, add en+ar+x-default)
        return f'''  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="ar" href="{ar_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">'''
    elif rel.startswith("ur/"):
        page = rel[3:]  # strip ur/
        en_url = f"{BASE}/{page}" if page != "index.html" else f"{BASE}/"
        ur_url = url
        return f'''  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="ur" href="{ur_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">'''
    elif rel.startswith("blog/"):
        # Blog pages - just self-referencing hreflang
        return f'''  <link rel="alternate" hreflang="en" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">'''
    else:
        # Root EN page
        ar_url = f"{BASE}/ar/{rel}" if rel != "index.html" else f"{BASE}/ar/"
        ur_url = f"{BASE}/ur/{rel}" if rel != "index.html" else f"{BASE}/ur/"
        return f'''  <link rel="alternate" hreflang="en" href="{url}">
  <link rel="alternate" hreflang="ar" href="{ar_url}">
  <link rel="alternate" hreflang="ur" href="{ur_url}">
  <link rel="alternate" hreflang="x-default" href="{url}">'''

def fix_hreflang(content, url, filepath):
    """Add hreflang if missing."""
    if 'hreflang' not in content:
        block = get_hreflang_block(url, filepath)
        # Insert before </head>
        content = re.sub(r'(</head>)', f'{block}\n\\1', content, count=1)
    return content

def fix_og_title(content):
    """Add og:title if missing."""
    if 'og:title' not in content:
        m = re.search(r'<title>([^<]+)</title>', content)
        if m:
            og_title = f'  <meta property="og:title" content="{m.group(1)}">'
            content = re.sub(r'(<meta property="og:type"[^>]*>)', rf'\1\n{og_title}', content, count=1)
    return content

def fix_og_description(content):
    """Add og:description if missing."""
    if 'og:description' not in content:
        m = re.search(r'<meta name="description" content="([^"]+)"', content)
        if m:
            og_desc = f'  <meta property="og:description" content="{m.group(1)}">'
            if 'og:title' in content:
                content = re.sub(r'(<meta property="og:title"[^>]*>)', rf'\1\n{og_desc}', content, count=1)
    return content

# Process all HTML files
all_files = []
for root, dirs, files in os.walk(SITES):
    # Skip git dir
    dirs[:] = [d for d in dirs if d != '.git']
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

print(f"Found {len(all_files)} HTML files")

for filepath in sorted(all_files):
    try:
        with open(filepath, 'r', encoding='utf-8') as fh:
            original = fh.read()

        content = original
        url = get_page_url(filepath)

        # Skip 404 page - no canonical needed
        if '404.html' in filepath:
            continue

        # Apply all fixes
        content = fix_canonical(content, url)
        content = fix_og_title(content)
        content = fix_og_description(content)
        content = fix_og_image(content)
        content = fix_og_url(content, url)
        content = fix_hreflang(content, url, filepath)
        content = shorten_title(content, filepath)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as fh:
                fh.write(content)
            rel = filepath.replace(SITES, "")
            print(f"  FIXED: {rel}")
            fixed += 1
        else:
            skipped += 1

    except Exception as e:
        print(f"  ERROR: {filepath}: {e}")

print(f"\nDone. Fixed: {fixed}, Unchanged: {skipped}")
