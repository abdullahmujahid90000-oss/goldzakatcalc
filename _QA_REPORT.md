# Saudi Utility Hub — QA Report

**Date:** 28 May 2026
**Source:** `Sites.zip` provided by user (332 HTML files)
**Output:** `Sites-FIXED-FINAL/` (293 HTML files — internal scratch/build files removed)

## Summary

| Area | Before | After |
|---|---|---|
| Pages with truncated `<title>` (`...`) | 78 | **0** |
| Pages with meta description out of sync | many | aligned with new titles |
| Stub redirect pages without `noindex` | 12 | **0** (all noindex,follow) |
| Pages where `iqama-transfer.html` pointed to wrong page | 1 (critical) | **fixed** to `iqama-transfer-calculator.html` |
| AdSense script verified on every content page | partial | **293/293** |
| Pages with JSON-LD schema | 95 | **253** |
| Pages with `BreadcrumbList` schema | very few | **254** |
| Pages with `WebApplication`/`SoftwareApplication` schema | 0 | **99** |
| Pages with `Article` schema | 0 | **87** |
| Pages with `FAQPage` schema (rich-result eligible) | 1 (homepage) | **13** (12 top calculators + homepage) |
| Sitemap URLs | 186 (with orphans) | **258** (clean, with hreflang) |
| Internal/build files leaked into deliverable | many (build_*.py, fix_*.py, SUH_FIXED_ADSENSE_READY, .DS_Store) | removed |

## Files changed

### Site-wide

- `sitemap.xml` — rebuilt from scratch; 258 URLs; full hreflang alternates;
  fresh `<lastmod>` of 2026-05-28; cleaned out orphans and dead entries.

### Top-12 calculator pages (got FAQPage schema + visible FAQ section)

`salary-calculator.html`, `gosi-calculator.html`, `ksa-eos-calculator.html`,
`iqama-expiry-calculator.html`, `vat-calculator.html`, `traffic-fine-calculator.html`,
`gold-zakat-calculator.html`, `dependent-levy-calculator.html`, `remittance-fee-compare.html`,
`iqama-transfer-calculator.html`, `currency-converter.html`, `family-visit-visa-guide.html`.

Each got: 4 high-intent FAQs (answers grounded in 2026 official rates), FAQPage schema,
visible `<details>` accordion under each calculator, and a "Last updated" + sources block.

### 12 stub redirect pages — now `noindex,follow`

`eos-calculator.html`, `iqama-calculator.html`, `family-visa.html`, `remittance.html`,
`iqama-transfer.html` (also had its target fixed!), `traffic-fines.html`,
`salary-calculator-ar.html`, `gosi-calculator-ar.html`, `eos-calculator-ar.html`,
`iqama-expiry-ar.html`, `vat-calculator-ar.html`, `zakat-calculator-ar.html`.

### 104 pages — titles + meta descriptions rewritten

The original site had 78 pages whose `<title>` ended in `...` because they were
truncated by some earlier build step. Plus another 26 pages had inconsistent
meta-titles vs `og:title` vs `twitter:title`. All now use a single clean title
and a matching description across all three meta tags.

Examples of titles fixed:

- Homepage: `Saudi Utility Hub — Free KSA Salary, GOSI, Zakat &...` → **`Saudi Utility Hub — Free KSA Calculators 2026`**
- Iqama Expiry: `Iqama Expiry Calculator | Hijri to Gregorian | Saudi...` → **`Iqama Expiry Calculator — Hijri to Gregorian KSA`**
- Saudi IBAN: `Saudi IBAN Validator & Checker — Verify SA Bank...` → **`Saudi IBAN Validator — Verify SA Bank Number 2026`**
- All 21 truncated Arabic & Urdu page titles — rewritten with native-language full titles

### 254 pages — JSON-LD structured data added

- `BreadcrumbList` on every full-content page (helps Google show breadcrumb in SERP)
- `WebApplication` on calculator/validator/generator pages
- `Article` on blog posts
- `WebPage` on guide/about/contact pages

All inserted schema blocks carry `data-suh-schema="auto"` so future re-runs are
idempotent (won't duplicate).

### Files removed from deliverable

`SUH_FIXED_ADSENSE_READY/` (legacy duplicate folder), `build_new_pages.py`,
`build_ur_blog.py`, `build_urdu_batch1.py`, `build_urdu_batch2.py`,
`fix_all_pages.py`, `fix_canonical_redirects.py`, `fix_seo_issues.py`,
`_shared.sh`, `CLAUDE.md`, `2de595534ba4439cab01a90c7a0e389d.txt`, `.DS_Store`, `__MACOSX/`, `.git/`.

## Things you should still do manually (not done by this audit)

1. **Add a real `og:image` per top calculator** (currently they all use the global
   one). Tools like https://og-image.vercel.app generate per-page PNGs in minutes.
2. **Add a named author** with photo + LinkedIn to `about.html`. For YMYL content
   (Zakat, GOSI, labour law) Google strongly prefers named editorial expertise.
3. **Spot-check Arabic titles** I wrote — I'm confident in the meaning but a native
   speaker should glance over the 21 Arabic titles before publishing.
4. **Spot-check Urdu titles** — same. The strings are in `fix_site.py` if you
   want to revise.
5. **Sitemap on host:** confirm the deployed URL `https://www.saudiutilityhub.com/sitemap.xml`
   returns the new 258-URL version (not a cached old one). Some hosts cache `sitemap.xml`
   aggressively — purge if needed.

## Re-running the fixes

If you tweak the source files (`Sites-FIXED-FINAL/`) and want to re-apply the
title map, just run from the parent folder:

```
python3 fix_site.py       # title + meta + stub fixes
python3 add_schema.py     # JSON-LD schema (idempotent)
python3 add_faq_schema.py # FAQPage schema on top calculators (idempotent)
python3 build_sitemap.py  # rebuild sitemap.xml
```

All four scripts are in the parent folder alongside `Sites-FIXED-FINAL/`. They are
safe to run in any order and can be run multiple times.
