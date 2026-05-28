# Saudi Utility Hub — Deployment Notes (Static / GitHub Pages / Vercel)

This package has been audited and patched for AdSense readiness, SEO and indexation.
Read **`_QA_REPORT.md`** for a full list of changes.

## How to deploy

This is a pure static site — no build step needed. Upload everything to your host:

### GitHub Pages
1. Commit the entire folder to your repo's `main` branch (or `gh-pages` branch).
2. In repo Settings → Pages → set "Source" to that branch and `/` as the directory.
3. Custom domain: add `www.saudiutilityhub.com` and enable HTTPS.
4. Add a `CNAME` file at the repo root containing one line: `www.saudiutilityhub.com`

### Vercel
1. `vercel link` then `vercel --prod` from the folder.
2. Add `www.saudiutilityhub.com` in Vercel dashboard → Domains.
3. Vercel will auto-serve `*.html` cleanly.

### Cloudflare Pages
1. Push to GitHub → connect repo to Cloudflare Pages.
2. Build command: (empty). Output directory: `/`.
3. Add the custom domain.

## Stub redirect pages — already handled

The original site had 12 thin "stub" pages that used `<meta http-equiv="refresh">` to
redirect users to the real calculator. Google treats these as low-value duplicate
content and they were silently hurting indexation.

We have NOT deleted them, but every stub now has `<meta name="robots" content="noindex,follow">`
which tells Google to ignore the stub but still follow the link to the real page. This is
the cleanest possible solution on static hosting.

If your host supports server-side 301 redirects (e.g. `vercel.json` rewrites or
Cloudflare Pages `_redirects`), you can additionally use the table below — Google
treats 301 as the strongest signal.

### Redirect mapping (use only if you have server-side redirect support)

| Old URL | 301 → New URL |
|---|---|
| /eos-calculator.html | /ksa-eos-calculator.html |
| /iqama-calculator.html | /iqama-expiry-calculator.html |
| /family-visa.html | /family-visit-visa-guide.html |
| /remittance.html | /remittance-fee-compare.html |
| /iqama-transfer.html | /iqama-transfer-calculator.html |
| /traffic-fines.html | /traffic-fine-calculator.html |
| /salary-calculator-ar.html | /ar/salary-calculator-ar.html |
| /gosi-calculator-ar.html | /ar/gosi-calculator-ar.html |
| /eos-calculator-ar.html | /ar/eos-calculator-ar.html |
| /iqama-expiry-ar.html | /ar/iqama-expiry-ar.html |
| /vat-calculator-ar.html | /ar/vat-calculator-ar.html |
| /zakat-calculator-ar.html | /ar/zakat-calculator-ar.html |

### Vercel `vercel.json` (drop in repo root if using Vercel)

```json
{
  "redirects": [
    { "source": "/eos-calculator.html",       "destination": "/ksa-eos-calculator.html",       "permanent": true },
    { "source": "/iqama-calculator.html",     "destination": "/iqama-expiry-calculator.html",  "permanent": true },
    { "source": "/family-visa.html",          "destination": "/family-visit-visa-guide.html",  "permanent": true },
    { "source": "/remittance.html",           "destination": "/remittance-fee-compare.html",   "permanent": true },
    { "source": "/iqama-transfer.html",       "destination": "/iqama-transfer-calculator.html","permanent": true },
    { "source": "/traffic-fines.html",        "destination": "/traffic-fine-calculator.html",  "permanent": true },
    { "source": "/salary-calculator-ar.html", "destination": "/ar/salary-calculator-ar.html",  "permanent": true },
    { "source": "/gosi-calculator-ar.html",   "destination": "/ar/gosi-calculator-ar.html",    "permanent": true },
    { "source": "/eos-calculator-ar.html",    "destination": "/ar/eos-calculator-ar.html",     "permanent": true },
    { "source": "/iqama-expiry-ar.html",      "destination": "/ar/iqama-expiry-ar.html",       "permanent": true },
    { "source": "/vat-calculator-ar.html",    "destination": "/ar/vat-calculator-ar.html",     "permanent": true },
    { "source": "/zakat-calculator-ar.html",  "destination": "/ar/zakat-calculator-ar.html",   "permanent": true }
  ]
}
```

### Cloudflare Pages `_redirects` (drop in repo root)

```
/eos-calculator.html        /ksa-eos-calculator.html         301
/iqama-calculator.html      /iqama-expiry-calculator.html    301
/family-visa.html           /family-visit-visa-guide.html    301
/remittance.html            /remittance-fee-compare.html     301
/iqama-transfer.html        /iqama-transfer-calculator.html  301
/traffic-fines.html         /traffic-fine-calculator.html    301
/salary-calculator-ar.html  /ar/salary-calculator-ar.html    301
/gosi-calculator-ar.html    /ar/gosi-calculator-ar.html      301
/eos-calculator-ar.html     /ar/eos-calculator-ar.html       301
/iqama-expiry-ar.html       /ar/iqama-expiry-ar.html         301
/vat-calculator-ar.html     /ar/vat-calculator-ar.html       301
/zakat-calculator-ar.html   /ar/zakat-calculator-ar.html     301
```

## Post-deploy checklist (Search Console)

1. Open Google Search Console → **both** `https://www.saudiutilityhub.com/` and
   `https://saudiutilityhub.com/` properties.
2. **Sitemaps** → submit `https://www.saudiutilityhub.com/sitemap.xml`. The new sitemap
   contains 258 URLs (up from 186).
3. **URL Inspection** → run for these top-priority URLs:
   - `/`
   - `/salary-calculator.html`
   - `/gosi-calculator.html`
   - `/ksa-eos-calculator.html`
   - `/iqama-expiry-calculator.html`
   - `/gold-zakat-calculator.html`
   - `/traffic-fine-calculator.html`
   - `/vat-calculator.html`
   - `/remittance-fee-compare.html`
   - `/family-visit-visa-guide.html`
   For each: click "Request indexing." Don't spam — one request per page is enough.
4. **Rich Results Test** → paste `https://www.saudiutilityhub.com/salary-calculator.html`
   into https://search.google.com/test/rich-results — you should see FAQPage and
   WebApplication results.
5. **Mobile-Friendly Test** → run on the homepage.
6. **Core Web Vitals** → wait 28 days for the first report; meanwhile run
   https://pagespeed.web.dev on the homepage.

## AdSense post-deploy

- `ads.txt` is already in place (`pub-5391037132181133`).
- AdSense auto-ads script is present on all 293 content pages.
- Privacy Policy already mentions AdSense + Google Analytics — required for AdSense approval.
- Cookie consent banner already on the site.
- No thin/duplicate content remains (stubs are `noindex`).

If your AdSense status is still "Getting Ready", give Google 1–3 weeks after re-submitting
the sitemap and confirming indexation. If it's "Needs Attention", the most common reasons
post-fix are: (a) too few indexed pages — Google wants ≥10 indexed pages, (b) missing
contact / about content — both are present and detailed here.

## Backlinks — what to do this week

Indexation in our pre-flight check returned **zero pages**. Even with sitemap and
Search Console properly set up, Google often refuses to index sites with zero
inbound links. Build 5–10 contextual backlinks before re-submitting:

1. Post helpful answers (not spam) on:
   - r/saudiarabia and r/expats subreddits
   - Quora questions about GOSI, EOS, Iqama renewal
   - SaudiExpatriates.com forum threads
   - ExpatWoman.com Saudi forum
2. Write one genuine guest post for a Saudi expat blog (KSAExpats, Khaleej Blog)
   linking back to the homepage.
3. Submit the site to free directories: ExpatExplorer, InterNations Saudi Arabia,
   ExpatRiyadh.com, ExpatJeddah.com.
4. List the brand on Crunchbase, Producthunt (free), and DEV.to.

Each backlink improves your chance of being indexed. Most are free and take ~30 minutes.
