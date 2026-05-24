import re, os

BASE = "/sessions/clever-inspiring-albattani/mnt/outputs/"

# ── STANDARD NAV for EN pages (matches live salary-calculator.html) ──────────
def std_nav(active_href, ar_href):
    links = [
        ("https://www.saudiutilityhub.com/", "Home"),
        ("https://www.saudiutilityhub.com/salary-calculator.html", "Salary"),
        ("https://www.saudiutilityhub.com/gosi-calculator.html", "GOSI"),
        ("https://www.saudiutilityhub.com/ksa-eos-calculator.html", "EOS"),
        ("https://www.saudiutilityhub.com/gold-zakat-calculator.html", "Zakat"),
        ("https://www.saudiutilityhub.com/iqama-expiry-calculator.html", "Iqama"),
        ("https://www.saudiutilityhub.com/remittance-fee-compare.html", "Remittance"),
        ("https://www.saudiutilityhub.com/vat-calculator.html", "VAT"),
        ("https://www.saudiutilityhub.com/traffic-fine-calculator.html", "Traffic"),
        ("https://www.saudiutilityhub.com/blog/", "Blog"),
    ]
    html = '<nav>\n  <a href="https://www.saudiutilityhub.com/" class="nav-brand">🇸🇦 Saudi Utility Hub</a>\n'
    for href, label in links:
        cls = ' class="active"' if href == active_href else ''
        html += f'  <a href="{href}"{cls}>{label}</a>\n'
    html += f'  <a href="{ar_href}" class="nav-ar">عربي</a>\n</nav>'
    return html

# ── STANDARD FOOTER for EN pages ─────────────────────────────────────────────
def std_footer(ar_href, copyright_note=""):
    note = copyright_note or "© 2026 Saudi Utility Hub · Calculations are estimates only · <a href=\"mailto:hello@saudiutilityhub.com\" style=\"color:#888\">hello@saudiutilityhub.com</a>"
    return f'''<footer>
  <div class="footer-grid">
    <div class="footer-col">
      <h4>💼 Finance Tools</h4>
      <a href="https://www.saudiutilityhub.com/salary-calculator.html">Salary Calculator</a>
      <a href="https://www.saudiutilityhub.com/salary-slip-generator.html">Pay Slip Generator</a>
      <a href="https://www.saudiutilityhub.com/salary-certificate.html">Salary Certificate</a>
      <a href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">EOS Gratuity</a>
      <a href="https://www.saudiutilityhub.com/gosi-calculator.html">GOSI Calculator</a>
      <a href="https://www.saudiutilityhub.com/vat-calculator.html">VAT Calculator</a>
    </div>
    <div class="footer-col">
      <h4>🪪 Expat Tools</h4>
      <a href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">Iqama Tracker</a>
      <a href="https://www.saudiutilityhub.com/muqeem-visa-check.html">Muqeem Visa Check</a>
      <a href="https://www.saudiutilityhub.com/dependent-levy-calculator.html">Dependent Levy</a>
      <a href="https://www.saudiutilityhub.com/exit-reentry-calculator.html">Exit Visa Cost</a>
      <a href="https://www.saudiutilityhub.com/remittance-fee-compare.html">Remittance Compare</a>
      <a href="https://www.saudiutilityhub.com/traffic-fine-calculator.html">Traffic Fines</a>
    </div>
    <div class="footer-col">
      <h4>💸 Money Transfer</h4>
      <a href="https://www.saudiutilityhub.com/remittance-fee-compare.html">Compare Services</a>
      <a href="https://www.saudiutilityhub.com/pakistan-remittance.html">SAR → PKR</a>
      <a href="https://www.saudiutilityhub.com/currency-converter.html">Currency Converter</a>
    </div>
    <div class="footer-col">
      <h4>🌙 Zakat &amp; Islamic</h4>
      <a href="https://www.saudiutilityhub.com/gold-zakat-calculator.html">Gold Zakat</a>
      <a href="https://www.saudiutilityhub.com/zakat-calculator.html">Cash Zakat</a>
      <a href="https://www.saudiutilityhub.com/islamic-finance-calculator.html">Islamic Finance Calc</a>
      <a href="https://www.saudiutilityhub.com/gold-prices.html">Live Gold Prices</a>
    </div>
    <div class="footer-col">
      <h4>📝 Blog Guides</h4>
      <a href="https://www.saudiutilityhub.com/blog/">All Articles</a>
      <a href="https://www.saudiutilityhub.com/blog/salary-certificate-guide-2026.html">Salary Certificate Guide</a>
      <a href="https://www.saudiutilityhub.com/blog/gosi-guide-2026.html">GOSI Guide 2026</a>
      <a href="https://www.saudiutilityhub.com/blog/eos-guide-2026.html">EOS Guide 2026</a>
      <a href="https://www.saudiutilityhub.com/blog/iqama-renewal-2026.html">Iqama Renewal Guide</a>
    </div>
    <div class="footer-col">
      <h4>ℹ️ Info</h4>
      <a href="https://www.saudiutilityhub.com/about.html">About Us</a>
      <a href="https://www.saudiutilityhub.com/contact.html">Contact</a>
      <a href="https://www.saudiutilityhub.com/privacy.html">Privacy Policy</a>
      <a href="https://www.saudiutilityhub.com/terms.html">Terms of Use</a>
      <a href="{ar_href}">عربي</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>{note}</span>
    <span>📢 Google AdSense &amp; affiliate commissions. Never affects our tools.</span>
  </div>
</footer>'''

# ── COOKIE BAR ────────────────────────────────────────────────────────────────
COOKIE_BAR = '''<div class="cookie-bar" id="cookieBar">
  🍪 We use cookies for Google AdSense ads and analytics. We never sell your data.
  <a href="https://www.saudiutilityhub.com/privacy.html">Privacy Policy</a>
  <button class="decline" onclick="document.getElementById('cookieBar').style.display='none'">Decline</button>
  <button onclick="document.getElementById('cookieBar').style.display='none'">Accept &amp; Continue</button>
</div>'''

# ── NATIONALITY OPTIONS (expanded) ───────────────────────────────────────────
NAT_OPTIONS = '''          <option value="Pakistani">Pakistani</option>
          <option value="Indian">Indian</option>
          <option value="Bangladeshi">Bangladeshi</option>
          <option value="Filipino">Filipino</option>
          <option value="Egyptian">Egyptian</option>
          <option value="Yemeni">Yemeni</option>
          <option value="Syrian">Syrian</option>
          <option value="Indonesian">Indonesian</option>
          <option value="Sudanese">Sudanese</option>
          <option value="Ethiopian">Ethiopian</option>
          <option value="Nepali">Nepali</option>
          <option value="Sri Lankan">Sri Lankan</option>
          <option value="Saudi">Saudi</option>
          <option value="Other">Other</option>'''

def replace_nav(html, active_href, ar_href):
    new_nav = std_nav(active_href, ar_href)
    # Match any <nav>...</nav> block
    html = re.sub(r'<nav>.*?</nav>', new_nav, html, flags=re.DOTALL)
    return html

def replace_footer(html, ar_href, copyright_note=""):
    new_footer = std_footer(ar_href, copyright_note)
    html = re.sub(r'<footer>.*?</footer>', new_footer, html, flags=re.DOTALL)
    return html

def replace_cookie(html):
    html = re.sub(r'<div class="cookie-bar".*?</div>', COOKIE_BAR, html, flags=re.DOTALL)
    return html

def fix_nationality(html):
    old = re.search(r'(<select id="emp-nationality">)(.*?)(</select>)', html, re.DOTALL)
    if old:
        html = html.replace(old.group(0), f'{old.group(1)}\n{NAT_OPTIONS}\n        {old.group(3)}')
    return html

def fix_og_type(html, og_type="website"):
    # Add og:type if missing, or fix it
    if 'og:type' not in html:
        html = html.replace('</head>', f'<meta property="og:type" content="{og_type}">\n</head>')
    return html

def add_faq_schema(html, page_id):
    schemas = {
        'islamic': '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is Islamic finance more expensive than conventional loans?","acceptedAnswer":{"@type":"Answer","text":"The total cost is often similar, but Islamic banks do not charge compounding penalties. The key benefit is Sharia compliance and peace of mind, not necessarily lower cost."}},{"@type":"Question","name":"Can non-Muslims get Islamic finance in Saudi Arabia?","acceptedAnswer":{"@type":"Answer","text":"Yes. Islamic finance in Saudi Arabia is available to all residents regardless of religion. Banks apply it as a legal commercial model."}},{"@type":"Question","name":"What is the difference between Murabaha and a conventional loan?","acceptedAnswer":{"@type":"Answer","text":"In Murabaha, the bank buys the asset and sells it to you at a declared profit margin. In a conventional loan, interest compounds on the outstanding debt. Murabaha profit is fixed upfront."}}]}</script>'''
    }
    if page_id in schemas and schemas[page_id] not in html:
        html = html.replace('</head>', schemas[page_id] + '\n</head>')
    return html

# ── Process each EN page ──────────────────────────────────────────────────────
pages = [
    {
        "file": "salary-slip-generator.html",
        "active": "https://www.saudiutilityhub.com/salary-slip-generator.html",
        "ar":     "https://www.saudiutilityhub.com/ar/salary-slip-generator.html",
        "fix_nat": True,
        "schema_id": None,
    },
    {
        "file": "muqeem-visa-check.html",
        "active": "https://www.saudiutilityhub.com/muqeem-visa-check.html",
        "ar":     "https://www.saudiutilityhub.com/ar/muqeem-visa-check.html",
        "fix_nat": False,
        "schema_id": None,
        "copyright": "© 2026 Saudi Utility Hub · This is a guide site — always verify with official Saudi government portals (muqeem.sa, jawazat.gov.sa, absher.sa) · <a href=\"mailto:hello@saudiutilityhub.com\" style=\"color:#888\">hello@saudiutilityhub.com</a>",
    },
    {
        "file": "islamic-finance-calculator.html",
        "active": "https://www.saudiutilityhub.com/islamic-finance-calculator.html",
        "ar":     "https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html",
        "fix_nat": False,
        "schema_id": "islamic",
    },
    {
        "file": "salary-certificate.html",
        "active": "https://www.saudiutilityhub.com/salary-certificate.html",
        "ar":     "https://www.saudiutilityhub.com/ar/salary-certificate.html",
        "fix_nat": True,
        "schema_id": None,
    },
]

for p in pages:
    path = BASE + p["file"]
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    html = replace_nav(html, p["active"], p["ar"])
    html = replace_footer(html, p["ar"], p.get("copyright", ""))
    html = replace_cookie(html)
    html = fix_og_type(html)
    if p.get("fix_nat"):
        html = fix_nationality(html)
    if p.get("schema_id"):
        html = add_faq_schema(html, p["schema_id"])

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Fixed: {p['file']}")

print("\nAll 4 EN pages fixed.")
