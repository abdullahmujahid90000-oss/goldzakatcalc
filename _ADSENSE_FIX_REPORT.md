# AdSense Readiness Fix Report — 30 May 2026

All fixes applied in a single pass by Claude.

## What changed

### 1. Hidden /ar/ and /ur/ from search (instant kill of 194 hreflang errors)
- 114 files in `/ar/` set to `<meta name="robots" content="noindex,nofollow">`
- 69 files in `/ur/` set to noindex,nofollow
- 6 root `-ar.html` / `-ur.html` stubs set to noindex,nofollow
- 6 Arabic blog stubs in `/blog/` (eos-guide-ar.html etc.) set to noindex,nofollow
- All hreflang annotations stripped from `/ar/` and `/ur/` pages
- `robots.txt` now contains `Disallow: /ar/` and `Disallow: /ur/`
- These pages stay live for any user who has the direct URL — they just won't appear in Google Search
- AdSense ads still serve on them after approval (AdSense works on any page of the domain)

### 2. Stripped hreflang from English pages (kills 254 hreflang errors)
- 338 `<link rel="alternate" hreflang="...">` tags removed across 307 English files
- Reason: if /ar/ /ur/ are noindexed, hreflang to them is invalid and causes errors

### 3. Upgraded 12 redirect stubs (kills "low word count" + "missing H1" + "meta refresh" warnings)
Files: `eos-calculator.html`, `family-visa.html`, `gosi-calculator-ar.html`, `iqama-calculator.html`, `iqama-expiry-ar.html`, `iqama-transfer.html`, `remittance.html`, `salary-calculator-ar.html`, `traffic-fines.html`, `vat-calculator-ar.html`, `zakat-calculator-ar.html`, `eos-calculator-ar.html`
- Each now has: H1, meta description, OG tags, Twitter card, canonical, noindex
- Still redirects via `meta refresh` to its canonical destination

### 4. Added Open Graph + Twitter cards to every page
- ~630 social-meta tags added across 105 pages
- Every English page now has og:title, og:description, og:url, og:image, og:type, og:site_name, twitter:card, twitter:title, twitter:description, twitter:image

### 5. Rebuilt sitemap.xml
- Old sitemap: 204 entries, 258 /ar/ references, 173 /ur/ references = 635 hreflang inline links
- New sitemap: 116 clean, canonical, indexable English URLs only
- No hreflang annotations in sitemap (since /ar/ /ur/ are noindexed)

### 6. Standardised contact email
- 11 files updated: `hello@saudiutilityhub.com` → `saudiutilityhub@gmail.com`

### 7. Fixed internal links to /ar/ /ur/
- 106 pages had nav links to `/ar` or `/ur` — these now point to `/`
- Eliminates the language switcher UX bug (Arabic nav was linking to English pages anyway)

### 8. robots.txt updated
- Added `Disallow: /ar/` and `Disallow: /ur/`
- Added wildcard `Disallow: /*-ar.html$` and `/*-ur.html$`

## Expected Ahrefs Health Score impact

| Issue | Before | After (expected) |
|-------|--------|------------------|
| Missing reciprocal hreflang | 97 | 0 |
| Hreflang to redirect/broken | 57 | 0 |
| Hreflang to non-canonical | 40 | 0 |
| Self-reference hreflang missing | 60 | 0 (no hreflang at all) |
| Non-canonical in sitemap | 33 | 0 |
| Open Graph tags incomplete | 104 | 0 |
| Twitter card incomplete | 104 | 0 |
| Twitter card missing | 20 | 0 |
| Low word count | 19 | 0 (stubs upgraded) |
| H1 missing | 19 | 0 (stubs upgraded) |
| Meta description missing | 19 | 0 (stubs upgraded) |
| Health Score | 54 (Fair) | ~85–90 (Good) |

## What's NOT done (and why)

These need manual work or are outside script scope:

1. **Domain age** — wait until month 3 (~July 2026) before applying to AdSense per Path B plan
2. **Compression (gzip/brotli)** — GitHub Pages doesn't support this directly. Put Cloudflare in front of saudiutilityhub.com (free) and turn on Brotli in Cloudflare → kills the 19 "Not compressed" warnings
3. **Schema.org validation errors (5)** — need to run https://validator.schema.org on each flagged page; I can do this if you share which 5 pages Ahrefs flagged
4. **404 pages (6)** — Ahrefs report would need to be re-exported to identify the exact URLs; once known, either restore or 301-redirect each one
5. **Translation of /ar/ /ur/ calculators** — long-term; do after AdSense approval

## Next steps (do today)

1. Commit and push this whole folder to your GitHub repo (overwrite existing files)
2. Wait 24h for Google to re-crawl
3. In Google Search Console, re-submit `sitemap.xml`
4. Set up Cloudflare in front of the domain (free) → turn on Brotli, Auto Minify, Always Use HTTPS
5. I'll deliver one new 1,500+ word blog post per day starting now
