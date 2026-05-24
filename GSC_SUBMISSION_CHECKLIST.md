# Google Search Console — Complete Submission Checklist
## SaudiUtilityHub.com — May 2026

---

## STEP 1: Upload All Files to Your Server First

Upload these files **before** submitting to GSC:

### Root folder (/)
| Local filename | Upload as |
|---|---|
| salary-slip-generator.html | /salary-slip-generator.html |
| muqeem-visa-check.html | /muqeem-visa-check.html |
| islamic-finance-calculator.html | /islamic-finance-calculator.html |
| salary-certificate.html | /salary-certificate.html |
| sitemap.xml | /sitemap.xml |

### /blog/ folder
| Local filename | Upload as |
|---|---|
| blog-salary-certificate-guide-2026.html | /blog/salary-certificate-guide-2026.html |

### /ar/ folder (rename files — remove the "ar-" prefix)
| Local filename | Rename to | Upload as |
|---|---|---|
| ar-salary-slip-generator.html | salary-slip-generator.html | /ar/salary-slip-generator.html |
| ar-muqeem-visa-check.html | muqeem-visa-check.html | /ar/muqeem-visa-check.html |
| ar-islamic-finance-calculator.html | islamic-finance-calculator.html | /ar/islamic-finance-calculator.html |
| ar-salary-certificate.html | salary-certificate.html | /ar/salary-certificate.html |

### Homepage + Blog Index — Manual edits required
- Open your **index.html** → paste in blocks from HOMEPAGE_ADDITIONS.html
- Open your **blog/index.html** → paste in card from BLOG_INDEX_CARD.html

---

## STEP 2: Submit Sitemap to Google Search Console

1. Go to: https://search.google.com/search-console
2. Select property: **saudiutilityhub.com**
3. In left sidebar → click **Sitemaps**
4. In "Add a new sitemap" box → type: `sitemap.xml`
5. Click **Submit**
6. Refresh page — status should change to "Success" within minutes

> ✅ Your sitemap covers 45 URLs including all new EN + AR pages.

---

## STEP 3: Request Indexing for Each New Page (do this for all 9)

For each URL below:
1. Go to GSC → **URL Inspection** (top search bar)
2. Paste the URL → press Enter
3. Click **"Request Indexing"**
4. Wait 10 seconds for confirmation → move to next URL

### English pages to request indexing:
- https://www.saudiutilityhub.com/salary-slip-generator.html
- https://www.saudiutilityhub.com/muqeem-visa-check.html
- https://www.saudiutilityhub.com/islamic-finance-calculator.html
- https://www.saudiutilityhub.com/salary-certificate.html
- https://www.saudiutilityhub.com/blog/salary-certificate-guide-2026.html

### Arabic pages to request indexing:
- https://www.saudiutilityhub.com/ar/salary-slip-generator.html
- https://www.saudiutilityhub.com/ar/muqeem-visa-check.html
- https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html
- https://www.saudiutilityhub.com/ar/salary-certificate.html

> ⚡ GSC manual indexing requests typically result in crawling within 24–72 hours.
> Without manual requests, new pages can take 2–8 weeks to appear in search.

---

## STEP 4: Fix Ahrefs Errors in Your Existing Pages

### Fix "Canonical points to redirect" (42 pages)
In Ahrefs → All Issues → "Canonical points to redirect" → click to see all affected pages.

The most likely cause: some pages have `href="/blog"` (no trailing slash) in their canonical or internal links instead of `href="/blog/"` (with trailing slash).

**Quick fix — search and replace in ALL your HTML files:**
- Find: `href="https://www.saudiutilityhub.com/blog"`
- Replace with: `href="https://www.saudiutilityhub.com/blog/"`
- Also find: `href="https://www.saudiutilityhub.com/ar"`
- Replace with: `href="https://www.saudiutilityhub.com/ar/"`

### Fix "404 page" (2 URLs) and "4XX page" (2 URLs)
In Ahrefs → All Issues → "404 page" → note the exact broken URLs.
- If a file is missing: upload it
- If it was renamed: add a redirect in your .htaccess or hosting panel

Most likely 404s are:
- `/blog/salary-certificate-guide-2026.html` — fixed by uploading the blog file above
- An old page that was deleted but still linked from somewhere

### Fix "Orphan page" (1 page)
This is fixed automatically once you:
1. Add the blog article card to blog/index.html (Step 1 above)
2. Add the tools to your homepage (Step 1 above)
Both actions create incoming internal links to previously orphaned pages.

### Fix "Page has links to redirect" (9 pages)
After fixing the trailing slash issues above, re-crawl in Ahrefs.
Most of these will auto-resolve once `/blog` → `/blog/` links are corrected.

---

## STEP 5: Verify Results in Ahrefs (2–3 days after upload)

1. Go to Ahrefs Site Audit → re-crawl your site
2. Expected improvements:
   - "Canonical points to redirect": 42 → near 0
   - "Orphan page": 1 → 0
   - "404 page": 2 → 0 (if blog file uploaded correctly)
   - Health Score: 60 → 75–85

---

## STEP 6: Monitor Rankings (4–8 weeks)

Check these keywords in GSC → **Search Results** → **Queries**:

| Keyword | Expected Timeline |
|---|---|
| salary slip generator Saudi Arabia | 4–6 weeks |
| pay slip generator KSA 2026 | 4–6 weeks |
| muqeem visa check | 4–6 weeks |
| muqeem visa validity check Saudi Arabia | 5–7 weeks |
| Islamic finance calculator Saudi Arabia | 5–8 weeks |
| murabaha calculator KSA | 5–8 weeks |
| salary certificate Saudi Arabia | 4–6 weeks |
| شهادة راتب (salary certificate Arabic) | 5–8 weeks |
| قسيمة راتب (salary slip Arabic) | 5–8 weeks |
| مقيم فحص التأشيرة (Muqeem Arabic) | 5–8 weeks |

> Rankings typically start appearing at position 20–50 first, then climb.
> The Arabic keywords have almost zero competition — expect faster results.

---

## Summary: What You Did

| Action | Impact |
|---|---|
| 9 new pages (EN + AR) | +9 indexed URLs, +9 keyword opportunities |
| Fixed nav/footer on all pages | Resolves redirect warnings in Ahrefs |
| Added FAQPage schema (Islamic Finance) | Enables Google rich snippets |
| Expanded nationality dropdown | Better UX for diverse expat users |
| sitemap.xml (45 URLs) | Faster full-site indexing |
| Homepage + blog index additions | Fixes orphan page, passes link equity |
| GSC manual indexing requests | 24–72hr indexing vs 2–8 week wait |

**Expected Ahrefs Health Score after fixes: 75–85 / 100**
**Expected new organic traffic in 8 weeks: +200–500 visits/month from new pages**

