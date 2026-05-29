# Saudi Utility Hub — New Pages Package (May 2026)

This package contains **30 new files** to add to your existing site:

- **18 calculator/guide pages** (6 topics × English/Arabic/Urdu)
- **9 blog posts** (3 topics × English/Arabic/Urdu)
- **3 updated homepages** (English, Arabic, Urdu — adds a new "Utility Bills, Residency & Remittance" section above your existing tool cards)
- **1 updated sitemap.xml** (now lists all new URLs with proper hreflang)

## What pages were built

### Tier-1 calculators / guides
1. `sec-electricity-bill-calculator.html` — Saudi Electricity Company (SEC) bill calculator, 2-tier residential tariff + VAT
2. `nwc-water-bill-calculator.html` — National Water Company (NWC) 4-block residential tariff + sewerage + VAT
3. `5-year-resident-id-guide-2026.html` — Comprehensive guide to the new 5-year physical Iqama card
4. `premium-residency-cost-calculator.html` — Compare all Premium Residency categories with cost calculator
5. `bangladesh-remittance.html` — SAR to BDT remittance compare + 2.5% government incentive explainer
6. `philippines-remittance.html` — SAR to PHP remittance compare incl. GCash, PayMaya, cash pickup networks

### Supporting blog posts
- `blog/sec-electricity-bills-saudi-arabia-2026.html` — 8-min deep dive on SEC bills, payment, savings
- `blog/saudi-5-year-resident-id-explained-2026.html` — 7-min explainer on the new card vs residency
- `blog/send-money-saudi-arabia-to-bangladesh-2026.html` — 9-min complete corridor guide

## What's in every page
- Clean **<title>**, **meta description**, **og:image**, **twitter:card**
- Full **hreflang** alternates (en / ar / ur / x-default)
- Working **JavaScript calculator** with results display
- **FAQPage** + **WebApplication/Article** + **BreadcrumbList** JSON-LD schema
- 2× **AdSense responsive ad units** (`pub-5391037132181133`) at top and middle
- **Cookie / GTAG** code matching the rest of your site
- **Footer** with all 30+ internal links updated
- Page sizes: 23–27 KB — well above AdSense's thin-content threshold

## How to deploy

1. **Download** `NEW-PAGES-PACKAGE.zip` and unzip it on your computer.
2. **Open github.dev** by pressing `.` on your goldzakatcalc repo page.
3. **Drag every file** from inside the unzipped folder into the matching folder in your repo:
   - 6 tool HTML files → root
   - `ar/*.html` → `ar/`
   - `ur/*.html` → `ur/`
   - 3 blog files → `blog/`
   - `ar/blog/*` → `ar/blog/`
   - `ur/blog/*` → `ur/blog/`
   - `index.html`, `ar/index.html`, `ur/index.html` → overwrite existing
   - `sitemap.xml` → overwrite existing
4. **Commit & push**.
5. Wait 2 minutes for Vercel to redeploy.

## Post-deploy checklist

1. **Visit a new page in incognito** — e.g. `https://www.saudiutilityhub.com/sec-electricity-bill-calculator.html`
2. **Run Rich Results Test** on it: https://search.google.com/test/rich-results
   - You should see FAQPage + WebApplication results detected.
3. **Resubmit sitemap** in Search Console: https://www.saudiutilityhub.com/sitemap.xml
4. **Request indexing** for the 6 new tool pages via URL Inspection (one at a time, don't spam).
5. **Run Ahrefs site audit** — page count should jump from ~250 to ~280, with all new pages having 0 errors.

## Recommended next pages (when you're ready)

Tier 2 — STC/Mobily/Zain bill calc · Hajj 2026 cost · Umrah visa cost · MOFA attestation cost · Final Exit guide
Tier 3 — Decision trees: "Iqama expired", probation transfer, Qiwa labour complaint, maternity leave
Tier 4 — Document generators: Rental Contract (Ejar), Resignation Letter, Power of Attorney

Tell me which tier you want next and I'll build the same way.
