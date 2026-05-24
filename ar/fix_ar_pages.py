import re, os

BASE = "/sessions/clever-inspiring-albattani/mnt/outputs/"

# ── STANDARD AR NAV (matches live ar/ homepage nav) ──────────────────────────
def ar_nav(active_href, en_href):
    links = [
        ("https://www.saudiutilityhub.com/ar/", "الرئيسية"),
        ("https://www.saudiutilityhub.com/salary-calculator.html", "الراتب"),
        ("https://www.saudiutilityhub.com/gosi-calculator.html", "GOSI"),
        ("https://www.saudiutilityhub.com/ksa-eos-calculator.html", "نهاية الخدمة"),
        ("https://www.saudiutilityhub.com/gold-zakat-calculator.html", "الزكاة"),
        ("https://www.saudiutilityhub.com/iqama-expiry-calculator.html", "الإقامة"),
        ("https://www.saudiutilityhub.com/ar/blog/", "المدونة"),
    ]
    html = '<nav>\n  <a href="https://www.saudiutilityhub.com/ar/" class="logo">Saudi<span>Utility</span>Hub</a>\n  <ul class="nav-links">\n'
    for href, label in links:
        cls = ' class="active"' if href == active_href else ''
        html += f'    <li><a href="{href}"{cls}>{label}</a></li>\n'
    html += f'  </ul>\n  <a href="{en_href}" style="color:#f0c040;font-size:.85rem;font-weight:600;text-decoration:none;margin-left:auto">English</a>\n</nav>'
    return html

# ── STANDARD AR FOOTER ────────────────────────────────────────────────────────
def ar_footer(en_href):
    return f'''<footer>
  <div class="footer-grid">
    <div class="footer-col">
      <h4>SaudiUtilityHub</h4>
      <p style="font-size:.82rem;line-height:1.6;color:#888">أدوات مجانية للمقيمين في المملكة العربية السعودية.</p>
    </div>
    <div class="footer-col">
      <h4>أدوات الرواتب</h4>
      <a href="https://www.saudiutilityhub.com/salary-calculator.html">حاسبة الراتب</a>
      <a href="https://www.saudiutilityhub.com/ar/salary-slip-generator.html">قسيمة الراتب</a>
      <a href="https://www.saudiutilityhub.com/ar/salary-certificate.html">شهادة الراتب</a>
      <a href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">نهاية الخدمة</a>
      <a href="https://www.saudiutilityhub.com/gosi-calculator.html">حاسبة GOSI</a>
    </div>
    <div class="footer-col">
      <h4>أدوات المقيمين</h4>
      <a href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">حاسبة الإقامة</a>
      <a href="https://www.saudiutilityhub.com/ar/muqeem-visa-check.html">فحص مقيم</a>
      <a href="https://www.saudiutilityhub.com/dependent-levy-calculator.html">رسوم المرافقين</a>
      <a href="https://www.saudiutilityhub.com/traffic-fine-calculator.html">الغرامات المرورية</a>
    </div>
    <div class="footer-col">
      <h4>المالية الإسلامية</h4>
      <a href="https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html">حاسبة المرابحة</a>
      <a href="https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html">حاسبة الإجارة</a>
      <a href="https://www.saudiutilityhub.com/gold-zakat-calculator.html">زكاة الذهب</a>
      <a href="https://www.saudiutilityhub.com/zakat-calculator.html">زكاة المال</a>
    </div>
    <div class="footer-col">
      <h4>المدونة والروابط</h4>
      <a href="https://www.saudiutilityhub.com/ar/blog/">جميع المقالات</a>
      <a href="https://www.saudiutilityhub.com/blog/salary-certificate-guide-2026.html">دليل شهادة الراتب</a>
      <a href="https://www.saudiutilityhub.com/blog/gosi-guide-2026.html">دليل GOSI</a>
      <a href="https://www.saudiutilityhub.com/about.html">عن الموقع</a>
      <a href="https://www.saudiutilityhub.com/privacy.html">سياسة الخصوصية</a>
      <a href="{en_href}">English</a>
    </div>
  </div>
  <div class="footer-bottom" style="text-align:center;padding-top:20px;border-top:1px solid #333;font-size:.8rem;color:#666;margin-top:20px">
    © 2026 SaudiUtilityHub. جميع الحقوق محفوظة. | هذه الأداة للأغراض المعلوماتية فقط.
  </div>
</footer>'''

AR_COOKIE = '''<div class="cookie-bar" id="cookieBar" style="position:fixed;bottom:0;left:0;right:0;background:#1a1a2e;color:#ccc;padding:12px 20px;display:flex;align-items:center;gap:16px;font-size:13px;z-index:999;flex-wrap:wrap;direction:rtl">
  🍪 نستخدم ملفات تعريف الارتباط لإعلانات AdSense والتحليلات. لا نبيع بياناتك أبدًا.
  <a href="https://www.saudiutilityhub.com/privacy.html" style="color:#f0c040">سياسة الخصوصية</a>
  <button onclick="document.getElementById('cookieBar').style.display='none'" style="background:#1a5276;color:#fff;border:none;border-radius:5px;padding:6px 14px;cursor:pointer;font-size:13px">موافق</button>
  <button onclick="document.getElementById('cookieBar').style.display='none'" style="background:transparent;border:1px solid #555;color:#aaa;border-radius:5px;padding:6px 14px;cursor:pointer;font-size:13px">رفض</button>
</div>'''

# Map: AR file → active URL, EN counterpart
ar_pages = [
    {
        "file": "ar-salary-slip-generator.html",
        "active": "https://www.saudiutilityhub.com/ar/salary-slip-generator.html",
        "en": "https://www.saudiutilityhub.com/salary-slip-generator.html",
        "canonical": "https://www.saudiutilityhub.com/ar/salary-slip-generator.html",
        "hreflang_en": "https://www.saudiutilityhub.com/salary-slip-generator.html",
    },
    {
        "file": "ar-muqeem-visa-check.html",
        "active": "https://www.saudiutilityhub.com/ar/muqeem-visa-check.html",
        "en": "https://www.saudiutilityhub.com/muqeem-visa-check.html",
        "canonical": "https://www.saudiutilityhub.com/ar/muqeem-visa-check.html",
        "hreflang_en": "https://www.saudiutilityhub.com/muqeem-visa-check.html",
    },
    {
        "file": "ar-islamic-finance-calculator.html",
        "active": "https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html",
        "en": "https://www.saudiutilityhub.com/islamic-finance-calculator.html",
        "canonical": "https://www.saudiutilityhub.com/ar/islamic-finance-calculator.html",
        "hreflang_en": "https://www.saudiutilityhub.com/islamic-finance-calculator.html",
    },
    {
        "file": "ar-salary-certificate.html",
        "active": "https://www.saudiutilityhub.com/ar/salary-certificate.html",
        "en": "https://www.saudiutilityhub.com/salary-certificate.html",
        "canonical": "https://www.saudiutilityhub.com/ar/salary-certificate.html",
        "hreflang_en": "https://www.saudiutilityhub.com/salary-certificate.html",
    },
]

for p in ar_pages:
    path = BASE + p["file"]
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix canonical (ensure it points to /ar/ path, no trailing slash issues)
    html = re.sub(
        r'<link rel="canonical"[^>]*>',
        f'<link rel="canonical" href="{p["canonical"]}">',
        html
    )

    # 2. Fix/add hreflang for EN counterpart
    if 'hreflang="en"' in html:
        html = re.sub(
            r'<link rel="alternate" hreflang="en"[^>]*>',
            f'<link rel="alternate" hreflang="en" href="{p["hreflang_en"]}">',
            html
        )
    else:
        html = html.replace(
            f'<link rel="canonical" href="{p["canonical"]}">',
            f'<link rel="canonical" href="{p["canonical"]}">\n<link rel="alternate" hreflang="en" href="{p["hreflang_en"]}">\n<link rel="alternate" hreflang="ar" href="{p["canonical"]}">'
        )

    # 3. Fix og:url
    html = re.sub(
        r'<meta property="og:url"[^>]*>',
        f'<meta property="og:url" content="{p["canonical"]}">',
        html
    )

    # 4. Replace nav with standard AR nav
    new_nav = ar_nav(p["active"], p["en"])
    html = re.sub(r'<nav>.*?</nav>', new_nav, html, flags=re.DOTALL)

    # 5. Replace footer with standard AR footer
    new_footer = ar_footer(p["en"])
    html = re.sub(r'<footer>.*?</footer>', new_footer, html, flags=re.DOTALL)

    # 6. Replace or add cookie bar
    if 'cookie-bar' in html:
        html = re.sub(r'<div class="cookie-bar".*?</div>', AR_COOKIE, html, flags=re.DOTALL)
    else:
        html = html.replace('</body>', AR_COOKIE + '\n</body>')

    # 7. Fix lang-bar link to point to exact canonical
    html = re.sub(
        r'(<div class="lang-bar">.*?<a href=")([^"]+)(">[^<]*</a>)',
        lambda m: m.group(1) + p["hreflang_en"] + m.group(3),
        html, flags=re.DOTALL
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Fixed AR: {p['file']}")

print("\nAll 4 AR pages fixed.")
