#!/usr/bin/env python3
"""Build 10 Urdu blog articles for saudiutilityhub.com/ur/blog/"""

import os

OUT = "/sessions/clever-inspiring-albattani/mnt/outputs/ur/blog"
os.makedirs(OUT, exist_ok=True)

DOMAIN = "https://www.saudiutilityhub.com"

# Shared CSS + nav builder
CSS = """
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Noto Nastaliq Urdu','Jameel Noori Nastaleeq','Segoe UI',Tahoma,sans-serif;direction:rtl;background:#f8f9fa;color:#1a1a2e;font-size:17px;line-height:2.1}
    nav{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);padding:0 20px;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.3)}
    .nav-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;flex-wrap:wrap;gap:4px;padding:10px 0}
    .nav-logo{font-size:18px;font-weight:700;color:#00d4aa;text-decoration:none;margin-left:16px;font-family:'Segoe UI',sans-serif}
    nav a{color:#cdd6f4;text-decoration:none;padding:5px 10px;border-radius:6px;font-size:14px;transition:background .2s}
    nav a:hover{background:rgba(255,255,255,.1);color:#fff}
    .lang-switcher{margin-right:auto;display:flex;gap:4px;align-items:center}
    .lang-switcher a{padding:3px 10px;border-radius:12px;border:1px solid rgba(255,255,255,.2);font-size:13px}
    .active-lang{background:#00d4aa!important;color:#1a1a2e!important;font-weight:700;border-color:#00d4aa!important}
    .hero{background:linear-gradient(135deg,#1a1a2e 0%,#0f3460 60%,#533483 100%);color:#fff;padding:50px 20px 40px}
    .hero h1{font-size:1.9rem;margin-bottom:12px;line-height:1.5}
    .hero-meta{font-size:13px;opacity:.75;margin-top:8px}
    .hero-meta span{margin:0 10px}
    article{max-width:820px;margin:0 auto;padding:36px 20px 60px}
    h2{font-size:1.4rem;color:#0f3460;margin:32px 0 12px;padding-right:12px;border-right:4px solid #00d4aa}
    h3{font-size:1.2rem;color:#1a1a2e;margin:24px 0 10px}
    p{margin-bottom:16px;color:#333}
    .info-box{background:#e8f4fd;border-right:4px solid #2196F3;padding:16px 20px;border-radius:8px;margin:20px 0;font-size:15px;color:#1a1a2e}
    .info-box strong{color:#1565c0}
    .warning-box{background:#fff8e1;border-right:4px solid #FFC107;padding:16px 20px;border-radius:8px;margin:20px 0;font-size:15px}
    .success-box{background:#f1f8e9;border-right:4px solid #4CAF50;padding:16px 20px;border-radius:8px;margin:20px 0;font-size:15px}
    .tip-box{background:#f3e5f5;border-right:4px solid #9c27b0;padding:16px 20px;border-radius:8px;margin:20px 0;font-size:15px}
    .step-list{counter-reset:step;list-style:none;margin:16px 0 24px}
    .step-list li{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid #eee;align-items:flex-start}
    .step-list li:last-child{border-bottom:none}
    .step-num{background:#1a1a2e;color:#fff;min-width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-family:'Segoe UI',sans-serif;font-size:14px;flex-shrink:0}
    ul.check{list-style:none;margin:12px 0 20px;padding-right:8px}
    ul.check li{padding:6px 0;padding-right:28px;position:relative;color:#333}
    ul.check li::before{content:'✓';color:#00d4aa;font-weight:700;position:absolute;right:0}
    table.data{width:100%;border-collapse:collapse;margin:20px 0;font-size:15px}
    table.data th{background:#1a1a2e;color:#fff;padding:12px;text-align:right}
    table.data td{padding:10px 12px;border-bottom:1px solid #eee}
    table.data tr:hover td{background:#f8f9fa}
    .cta-box{background:linear-gradient(135deg,#1a1a2e,#0f3460);color:#fff;border-radius:16px;padding:28px;text-align:center;margin:32px 0}
    .cta-box h3{color:#00d4aa;margin-bottom:10px;font-size:1.3rem}
    .cta-box a{display:inline-block;background:#00d4aa;color:#1a1a2e;padding:12px 28px;border-radius:10px;text-decoration:none;font-weight:700;margin-top:12px;font-size:16px}
    .tag{display:inline-block;background:#e3f2fd;color:#1565c0;padding:2px 10px;border-radius:12px;font-size:12px;margin:2px}
    .author-box{background:#f8f9fa;border-radius:12px;padding:20px;margin:32px 0;display:flex;gap:16px;align-items:center}
    .author-avatar{width:50px;height:50px;border-radius:50%;background:#1a1a2e;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0}
    .related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin:20px 0}
    .related-card{background:#fff;border-radius:12px;padding:16px;text-decoration:none;color:#1a1a2e;border:2px solid #e0e0e0;transition:border-color .2s}
    .related-card:hover{border-color:#00d4aa}
    .related-card .r-icon{font-size:1.8rem;margin-bottom:8px}
    .related-card .r-title{font-weight:700;font-size:15px}
    footer{background:#1a1a2e;color:#cdd6f4;text-align:center;padding:30px 20px;font-size:14px}
    footer a{color:#00d4aa;text-decoration:none;margin:0 8px}
    @media(max-width:600px){.hero h1{font-size:1.5rem}}
"""

def nav_html(en_url, ar_url):
    return f"""<nav>
  <div class="nav-inner">
    <a href="{DOMAIN}/ur/" class="nav-logo">🇸🇦 Saudi Utility Hub</a>
    <a href="{DOMAIN}/ur/salary-calculator.html">تنخواہ</a>
    <a href="{DOMAIN}/ur/gosi-calculator.html">گوسی</a>
    <a href="{DOMAIN}/ur/eos-calculator.html">آخری سروس</a>
    <a href="{DOMAIN}/ur/iqama-calculator.html">اقامہ</a>
    <a href="{DOMAIN}/ur/remittance.html">ریمیٹنس</a>
    <a href="{DOMAIN}/ur/blog/">بلاگ</a>
    <div class="lang-switcher">
      <a href="{en_url}">EN</a>
      <a href="{ar_url}">عربي</a>
      <a href="#" class="active-lang">اردو</a>
    </div>
  </div>
</nav>"""

FOOTER = f"""<footer>
  <p>© 2025 Saudi Utility Hub — سعودی عرب میں پاکستانیوں کے لیے مفت ٹولز</p>
  <div style="margin-top:12px;">
    <a href="{DOMAIN}/ur/">اردو ہوم</a>
    <a href="{DOMAIN}/ur/blog/">تمام مضامین</a>
    <a href="{DOMAIN}/ur/salary-calculator.html">تنخواہ کیلکولیٹر</a>
    <a href="{DOMAIN}/">English Site</a>
  </div>
</footer>"""

def page(title, meta_desc, keywords, canonical, en_url, ar_url, pub_date, read_time, tags, body_html):
    return f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title} | Saudi Utility Hub</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="ar" href="{ar_url}">
  <link rel="alternate" hreflang="ur" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="article">
  <meta property="article:published_time" content="{pub_date}">
  <style>{CSS}</style>
</head>
<body>
{nav_html(en_url, ar_url)}
{body_html}
{FOOTER}
</body>
</html>"""

# ============================================================
# ARTICLE 1 — Iqama Renewal
# ============================================================
a1_body = f"""
<div class="hero">
  <h1>🪪 اقامہ تجدید کا مکمل طریقہ 2025 — فیس، دستاویزات اور آن لائن طریقہ</h1>
  <p style="opacity:.85;font-size:1rem;">سعودی عرب میں اقامہ کی میعاد ختم ہونے سے پہلے یہ گائیڈ ضرور پڑھیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 7 منٹ مطالعہ</span><span>👤 Saudi Utility Hub</span></div>
</div>
<article>
  <div class="info-box">
    <strong>📌 مختصر خلاصہ:</strong> اقامہ تجدید کی فیس SAR 650 فی سال ہے۔ میعاد ختم ہونے پر ہر ماہ SAR 500 جرمانہ لگتا ہے۔ آن لائن Absher یا Muqeem سے تجدید ہو سکتی ہے۔
  </div>

  <h2>اقامہ کیا ہے اور تجدید کیوں ضروری ہے؟</h2>
  <p>اقامہ (Iqama) سعودی عرب میں غیر ملکیوں کا سرکاری رہائشی شناختی کارڈ ہے۔ یہ آپ کی قانونی حیثیت کا ثبوت ہے — نوکری، بینک اکاؤنٹ، گاڑی خریدنے اور بچوں کے سکول داخلے سب کے لیے ضروری ہے۔ اقامہ کی میعاد عموماً ایک یا دو سال ہوتی ہے اور میعاد ختم ہونے سے پہلے تجدید لازمی ہے۔</p>

  <h2>💰 اقامہ تجدید فیس 2025</h2>
  <table class="data">
    <thead><tr><th>مدت</th><th>فیس</th><th>اضافی چارجز</th></tr></thead>
    <tbody>
      <tr><td>1 سال تجدید</td><td>SAR 650</td><td>—</td></tr>
      <tr><td>2 سال تجدید</td><td>SAR 1,300</td><td>—</td></tr>
      <tr><td>میعاد ختم — 1 ماہ دیر</td><td>SAR 650 + 500</td><td>جرمانہ SAR 500/ماہ</td></tr>
      <tr><td>میعاد ختم — 3 ماہ دیر</td><td>SAR 650 + 1,500</td><td>جرمانہ SAR 1,500</td></tr>
    </tbody>
  </table>
  <div class="warning-box">⚠️ <strong>خبردار:</strong> اگر اقامہ 6 ماہ سے زیادہ میعاد ختم ہو جائے تو ملک بدری (deportation) کا خطرہ ہوتا ہے۔ فوری تجدید کریں!</div>

  <h2>📋 تجدید کے لیے ضروری دستاویزات</h2>
  <ul class="check">
    <li>موجودہ اقامہ (اصل)</li>
    <li>پاسپورٹ (کم از کم 6 ماہ کی میعاد باقی)</li>
    <li>کفیل (آجر) کا تعاون / منظوری</li>
    <li>میڈیکل انشورنس (لازمی)</li>
    <li>GOSI رجسٹریشن (نئی ملازمتوں کے لیے)</li>
  </ul>

  <h2>💻 آن لائن اقامہ تجدید — مرحلہ وار طریقہ</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div><strong>Absher پر لاگ ان کریں</strong><br><span style="color:#555">absher.sa پر اپنے نمبر اور OTP سے لاگ ان کریں۔</span></div></li>
    <li><div class="step-num">2</div><div><strong>"اقامہ تجدید" آپشن منتخب کریں</strong><br><span style="color:#555">Individuals → Iqama Services → Renew Iqama</span></div></li>
    <li><div class="step-num">3</div><div><strong>مدت منتخب کریں</strong><br><span style="color:#555">1 سال یا 2 سال — 2 سال لینا عموماً بہتر ہے (کم جھنجھٹ)</span></div></li>
    <li><div class="step-num">4</div><div><strong>فیس ادا کریں</strong><br><span style="color:#555">Mada ڈیبٹ کارڈ، Visa یا STC Pay سے ادائیگی۔</span></div></li>
    <li><div class="step-num">5</div><div><strong>ڈیجیٹل اقامہ ڈاؤن لوڈ کریں</strong><br><span style="color:#555">تجدید کے بعد Absher ایپ میں نئی اقامہ محفوظ ہو جاتی ہے۔</span></div></li>
  </ol>

  <h2>📱 Muqeem سے اقامہ تجدید</h2>
  <p>اگر آپ کا کفیل کاروباری ادارہ ہے تو Muqeem.sa پورٹل سے بھی تجدید ممکن ہے۔ یہ پورٹل عموماً HR اور آجر استعمال کرتے ہیں۔ ملازم خود Absher استعمال کرے تو بہتر ہے۔</p>

  <div class="success-box">✅ <strong>مفید ٹپ:</strong> اقامہ کی میعاد ختم ہونے سے <strong>2 ماہ پہلے</strong> تجدید شروع کریں۔ Absher پر رمائنڈر سیٹ کریں۔</div>

  <h2>اقامہ تجدید میں مسائل — عام سوالات</h2>
  <h3>کیا میں خود اقامہ تجدید کر سکتا ہوں؟</h3>
  <p>ہاں، آپ Absher ایپ سے خود تجدید کر سکتے ہیں بشرطیکہ کفیل کی طرف سے کوئی پابندی نہ ہو اور میڈیکل انشورنس فعال ہو۔</p>
  <h3>کفیل نے اقامہ تجدید کرنے سے انکار کر دیا تو کیا کریں؟</h3>
  <p>یہ آپ کا قانونی حق ہے۔ Qiwa.sa پر شکایت درج کروائیں یا وزارت محنت (Ministry of Human Resources) سے رابطہ کریں۔ کفیل کا تجدید سے انکار قانون کی خلاف ورزی ہے۔</p>
  <h3>میڈیکل انشورنس نہ ہو تو؟</h3>
  <p>اقامہ تجدید کے لیے میڈیکل انشورنس لازمی ہے۔ اگر آجر نے نہیں دی تو وہ قانوناً ذمہ دار ہے۔ شکایت Qiwa پر کریں۔</p>

  <div class="cta-box">
    <h3>🪪 اقامہ کب ختم ہوگی؟ ابھی چیک کریں</h3>
    <p>ہمارے مفت کیلکولیٹر سے باقی دن اور جرمانے جانیں</p>
    <a href="{DOMAIN}/ur/iqama-calculator.html">اقامہ کیلکولیٹر استعمال کریں ←</a>
  </div>

  <h2>نتیجہ</h2>
  <p>اقامہ تجدید ایک آسان عمل ہے اگر آپ وقت پر کریں۔ میعاد ختم ہونے سے پہلے تجدید کریں، جرمانوں سے بچیں اور اپنی قانونی حیثیت محفوظ رکھیں۔ کوئی سوال ہو تو ہمارے ٹولز استعمال کریں۔</p>

  <div class="author-box">
    <div class="author-avatar">✍️</div>
    <div><strong>Saudi Utility Hub ٹیم</strong><br><span style="font-size:14px;color:#555">سعودی عرب میں پاکستانیوں کی مدد کے لیے مفت معلومات اور ٹولز</span></div>
  </div>

  <div style="margin-top:16px;">
    <span class="tag">اقامہ</span><span class="tag">تجدید</span><span class="tag">سعودی عرب</span><span class="tag">پاکستانی</span>
  </div>

  <h2 style="margin-top:32px;">متعلقہ ٹولز</h2>
  <div class="related-grid">
    <a href="{DOMAIN}/ur/iqama-calculator.html" class="related-card"><div class="r-icon">🪪</div><div class="r-title">اقامہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/iqama-transfer.html" class="related-card"><div class="r-icon">🔄</div><div class="r-title">اقامہ ٹرانسفر</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 2 — GOSI Guide for Pakistanis
# ============================================================
a2_body = f"""
<div class="hero">
  <h1>🏛️ گوسی (GOSI) کیا ہے؟ پاکستانی ملازمین کے لیے مکمل گائیڈ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">کیا آپ کی تنخواہ سے گوسی کٹتا ہے؟ — سچ جانیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 6 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="success-box">
    <strong>✅ پاکستانیوں کے لیے اچھی خبر:</strong> سعودی عرب میں غیر ملکی (expatriate) ملازمین کی تنخواہ سے کوئی GOSI نہیں کٹتا! صرف سعودی شہریوں پر لاگو ہوتا ہے۔
  </div>

  <h2>GOSI کیا ہے؟</h2>
  <p>GOSI یعنی General Organization for Social Insurance (عمومی ادارہ برائے سماجی بیمہ) سعودی عرب کا سرکاری ادارہ ہے جو ملازمین کی سماجی سیکیورٹی کا انتظام کرتا ہے۔ یہ بڑھاپے، معذوری اور موت کی صورت میں مالی تحفظ فراہم کرتا ہے۔</p>

  <h2>📊 GOSI کی شرح 2025</h2>
  <table class="data">
    <thead><tr><th>زمرہ</th><th>ملازم کی کٹوتی</th><th>آجر کا حصہ</th><th>کل</th></tr></thead>
    <tbody>
      <tr><td>سعودی ملازم</td><td>9.75%</td><td>11.75%</td><td>21.5%</td></tr>
      <tr><td>غیر ملکی (پاکستانی وغیرہ)</td><td><strong>0%</strong></td><td>2% (صرف حادثاتی)</td><td>2%</td></tr>
    </tbody>
  </table>
  <p>غیر ملکی ملازمین پر صرف <strong>حادثاتی بیمہ (Occupational Hazard)</strong> کے لیے آجر 2% ادا کرتا ہے — یہ رقم آپ کی تنخواہ سے نہیں کٹتی، آجر کے حساب سے جاتی ہے۔</p>

  <h2>GOSI کا حساب کیسے ہوتا ہے؟</h2>
  <p>سعودی ملازمین کے لیے GOSI کا حساب <strong>بنیادی تنخواہ + ہاؤسنگ الاؤنس</strong> پر ہوتا ہے، زیادہ سے زیادہ SAR 45,000 بنیاد پر۔</p>
  <div class="info-box">
    <strong>مثال (سعودی ملازم):</strong><br>
    بنیادی تنخواہ: SAR 8,000 + ہاؤسنگ: SAR 3,200 = SAR 11,200<br>
    ملازم کی کٹوتی: 11,200 × 9.75% = <strong>SAR 1,092</strong><br>
    آجر کا حصہ: 11,200 × 11.75% = <strong>SAR 1,316</strong>
  </div>

  <h2>کیا GOSI واپس مل سکتا ہے؟</h2>
  <p>سعودی ملازمین جو ملک چھوڑتے ہیں یا ریٹائر ہوتے ہیں، وہ اپنے GOSI جمع شدہ رقم نکال سکتے ہیں۔ غیر ملکیوں کا کوئی GOSI بیلنس نہیں ہوتا۔</p>

  <h2>GOSI رجسٹریشن ضروری کیوں ہے؟</h2>
  <p>چاہے آپ پاکستانی ہوں، آپ کے آجر کو آپ کو GOSI میں رجسٹر کرنا لازمی ہے۔ یہ <strong>اقامہ تجدید</strong> کے لیے ضروری شرط ہے۔ اگر آجر نے GOSI رجسٹریشن نہیں کی تو یہ قانون کی خلاف ورزی ہے۔</p>

  <div class="tip-box">💡 <strong>GOSI چیک کریں:</strong> gosi.gov.sa پر اپنا GOSI نمبر اور سٹیٹس چیک کر سکتے ہیں۔</div>

  <div class="cta-box">
    <h3>🧮 اپنی خالص تنخواہ جانیں</h3>
    <p>تنخواہ کیلکولیٹر سے دیکھیں کہ GOSI کے بعد کتنا ملے گا</p>
    <a href="{DOMAIN}/ur/gosi-calculator.html">گوسی کیلکولیٹر کھولیں ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/gosi-calculator.html" class="related-card"><div class="r-icon">🏛️</div><div class="r-title">گوسی کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/eos-calculator.html" class="related-card"><div class="r-icon">🎯</div><div class="r-title">آخری سروس</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 3 — End of Service (EOS) Guide
# ============================================================
a3_body = f"""
<div class="hero">
  <h1>🎯 سعودی عرب میں آخری سروس (End of Service) کا حساب — مکمل گائیڈ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">نوکری چھوڑنے یا نکالے جانے پر کتنی رقم ملے گی؟ قانونی حق جانیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 8 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="info-box">
    <strong>📌 خلاصہ:</strong> سعودی لیبر لاء آرٹیکل 84 کے تحت ہر ملازم کو سروس کے اختتام پر گریجویٹی (End of Service) کا حق ہے۔ یہ رقم تنخواہ پر نہیں، بنیادی تنخواہ پر ملتی ہے۔
  </div>

  <h2>آخری سروس (EOS) کیا ہے؟</h2>
  <p>آخری سروس یا End of Service Benefit (EOSB) وہ رقم ہے جو کسی بھی ملازم کو نوکری ختم ہونے پر ملتی ہے — چاہے نوکری چھوڑی ہو، آجر نے نکالا ہو، یا معاہدہ ختم ہوا ہو۔ یہ سعودی لیبر قانون کے تحت آپ کا قانونی حق ہے۔</p>

  <h2>📐 EOS کا فارمولا (آرٹیکل 84)</h2>
  <table class="data">
    <thead><tr><th>سروس کی مدت</th><th>فی سال رقم</th></tr></thead>
    <tbody>
      <tr><td>پہلے 5 سال</td><td>½ مہینے کی بنیادی تنخواہ فی سال</td></tr>
      <tr><td>5 سال کے بعد</td><td>1 مہینے کی بنیادی تنخواہ فی سال</td></tr>
    </tbody>
  </table>

  <h2>استعفیٰ کی صورت میں کٹوتی</h2>
  <p>اگر ملازم نے خود نوکری چھوڑی ہو تو پوری رقم نہیں ملتی:</p>
  <table class="data">
    <thead><tr><th>سروس کی مدت</th><th>ملنے والی فیصد</th></tr></thead>
    <tbody>
      <tr><td>2 سال سے کم</td><td>کچھ نہیں</td></tr>
      <tr><td>2 سے 5 سال</td><td>⅓ (ایک تہائی)</td></tr>
      <tr><td>5 سے 10 سال</td><td>⅔ (دو تہائی)</td></tr>
      <tr><td>10 سال سے زیادہ</td><td>مکمل رقم</td></tr>
    </tbody>
  </table>
  <div class="warning-box">⚠️ اگر آجر نے نوکری سے نکالا ہو تو کسی بھی مدت میں مکمل رقم ملے گی۔</div>

  <h2>🔢 حساب کی مثال</h2>
  <div class="info-box">
    <strong>مثال:</strong> بنیادی تنخواہ SAR 5,000، سروس 7 سال، آجر نے نکالا<br><br>
    پہلے 5 سال: 5,000 × ½ × 5 = <strong>SAR 12,500</strong><br>
    بعد کے 2 سال: 5,000 × 1 × 2 = <strong>SAR 10,000</strong><br>
    <strong>کل: SAR 22,500</strong>
  </div>

  <h2>EOS میں کیا شامل ہوتا ہے؟</h2>
  <ul class="check">
    <li>بنیادی تنخواہ (Basic Salary) پر حساب</li>
    <li>باقی سالانہ چھٹیاں (Annual Leave) ادائیگی</li>
    <li>نوٹس پیریڈ کی تنخواہ (اگر نہیں دی گئی)</li>
  </ul>
  <p>ہاؤسنگ، ٹرانسپورٹ اور دیگر الاؤنس EOS میں شامل نہیں ہوتے۔</p>

  <h2>EOS نہ دینے پر کیا کریں؟</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div>Qiwa.sa پر لاگ ان کریں اور شکایت درج کروائیں</div></li>
    <li><div class="step-num">2</div><div>وزارت محنت (Ministry of HR) میں مقدمہ دائر کریں</div></li>
    <li><div class="step-num">3</div><div>عدالت عمل (Labor Court) سے رجوع کریں</div></li>
  </ol>

  <div class="cta-box">
    <h3>🎯 اپنی EOS ابھی حساب کریں</h3>
    <a href="{DOMAIN}/ur/eos-calculator.html">آخری سروس کیلکولیٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/eos-calculator.html" class="related-card"><div class="r-icon">🎯</div><div class="r-title">EOS کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/noc-letter.html" class="related-card"><div class="r-icon">✉️</div><div class="r-title">NOC جنریٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 4 — Remittance Guide
# ============================================================
a4_body = f"""
<div class="hero">
  <h1>💸 سعودی عرب سے پاکستان پیسے بھیجنے کے 5 بہترین طریقے 2025</h1>
  <p style="opacity:.85;font-size:1rem;">بہترین ریٹ، کم فیس — ہر ماہ ہزاروں روپے بچائیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 7 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="info-box">
    <strong>💡 اہم بات:</strong> SAR 1,000 بھیجنے پر مختلف سروسز میں PKR 3,000–5,000 کا فرق ہو سکتا ہے۔ صحیح سروس چنیں اور پیسے بچائیں!
  </div>

  <h2>1. Wise (وائز) — سب سے کم فیس</h2>
  <p>Wise دنیا کی سب سے شفاف ریمیٹنس سروس ہے۔ mid-market ریٹ (بینک ریٹ) استعمال کرتی ہے اور فیس صرف 0.4–0.8% ہے۔</p>
  <ul class="check">
    <li>SAR 1,000 پر تقریباً SAR 6–8 فیس</li>
    <li>پاکستان بینک اکاؤنٹ، JazzCash، Easypaisa سپورٹ</li>
    <li>1–2 کاری دنوں میں ٹرانسفر</li>
    <li>موبائل ایپ دستیاب</li>
  </ul>

  <h2>2. Al Rajhi Bank — فوری ٹرانسفر</h2>
  <p>Al Rajhi سعودی عرب کا سب سے بڑا بینک ہے اور پاکستان میں براہ راست ٹرانسفر کرتا ہے۔</p>
  <ul class="check">
    <li>فوری یا اگلے دن ٹرانسفر</li>
    <li>Urpay ایپ سے بھیج سکتے ہیں</li>
    <li>فیس SAR 10–15</li>
    <li>پاکستان کے تمام بینکوں کو بھیج سکتے ہیں</li>
  </ul>

  <h2>3. STC Pay — آسان موبائل ٹرانسفر</h2>
  <p>STC Pay سعودی عرب کی مقبول ترین موبائل والیٹ سروس ہے۔</p>
  <ul class="check">
    <li>فوری ٹرانسفر</li>
    <li>STC سم نہ ہو تو بھی استعمال ممکن</li>
    <li>JazzCash اور Easypaisa میں براہ راست</li>
  </ul>

  <h2>4. Western Union — کیش پک آپ</h2>
  <p>اگر وصول کنندہ کا بینک اکاؤنٹ نہیں ہے تو Western Union بہترین ہے۔ پاکستان میں نزدیکی برانچ سے نقد وصول کر سکتے ہیں۔</p>

  <h2>5. Exchange House — برانچ سے براہ راست</h2>
  <p>سعودی عرب میں AL-Mujib، SAMBA اور دیگر exchange houses موجود ہیں جہاں سے کم فیس پر ٹرانسفر ممکن ہے۔</p>

  <h2>📊 موازنہ جدول (SAR 1,000 کے لیے)</h2>
  <table class="data">
    <thead><tr><th>سروس</th><th>فیس</th><th>وقت</th><th>PKR تقریباً</th></tr></thead>
    <tbody>
      <tr><td>Wise</td><td>SAR 6–8</td><td>1–2 دن</td><td>PKR 73,500+</td></tr>
      <tr><td>Al Rajhi</td><td>SAR 12</td><td>فوری</td><td>PKR 72,800+</td></tr>
      <tr><td>STC Pay</td><td>SAR 15</td><td>فوری</td><td>PKR 72,500+</td></tr>
      <tr><td>Western Union</td><td>SAR 20–25</td><td>فوری</td><td>PKR 71,500+</td></tr>
    </tbody>
  </table>

  <div class="tip-box">💡 <strong>ماہانہ ٹپ:</strong> مہینے کے آخر میں ریٹ عموماً بہتر ہوتا ہے جب زیادہ لوگ بھیجتے ہیں اور مقابلہ بڑھ جاتا ہے۔</div>

  <div class="cta-box">
    <h3>💸 ابھی بہترین ریٹ چیک کریں</h3>
    <a href="{DOMAIN}/ur/remittance.html">ریمیٹنس موازنہ ٹول ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/remittance.html" class="related-card"><div class="r-icon">💸</div><div class="r-title">ریمیٹنس موازنہ</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/vat-calculator.html" class="related-card"><div class="r-icon">🧾</div><div class="r-title">ویٹ کیلکولیٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 5 — Traffic Fines
# ============================================================
a5_body = f"""
<div class="hero">
  <h1>🚦 سعودی عرب میں ٹریفک جرمانے — مکمل فہرست اور ادائیگی کا طریقہ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">Absher اور Najm سے جرمانے چیک کریں اور ادا کریں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 6 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="warning-box">
    ⚠️ <strong>اہم:</strong> بغیر ادائیگی کے جرمانے گاڑی کی نمبر پلیٹ بلاک ہو سکتی ہے اور اقامہ تجدید میں مسئلہ ہو سکتا ہے۔
  </div>

  <h2>📋 عام ٹریفک جرمانوں کی فہرست</h2>
  <table class="data">
    <thead><tr><th>خلاف ورزی</th><th>جرمانہ (SAR)</th></tr></thead>
    <tbody>
      <tr><td>سیٹ بیلٹ نہ لگانا (ڈرائیور)</td><td>150</td></tr>
      <tr><td>سیٹ بیلٹ نہ لگانا (مسافر)</td><td>150</td></tr>
      <tr><td>سرخ بتی سے گزرنا</td><td>3,000</td></tr>
      <tr><td>تیز رفتاری (20 km/h سے زیادہ)</td><td>300–3,000</td></tr>
      <tr><td>موبائل فون استعمال کرنا</td><td>500</td></tr>
      <tr><td>غلط پارکنگ</td><td>150–500</td></tr>
      <tr><td>لائسنس کے بغیر گاڑی چلانا</td><td>5,000</td></tr>
      <tr><td>گاڑی کا انشورنس نہ ہونا</td><td>5,000</td></tr>
      <tr><td>رجسٹریشن ختم ہو جانا</td><td>500</td></tr>
      <tr><td>خطرناک ڈرائیونگ</td><td>3,000+</td></tr>
    </tbody>
  </table>

  <h2>جرمانے کیسے چیک کریں؟</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div><strong>Absher.sa</strong> پر لاگ ان کریں → Vehicles → Traffic Violations</div></li>
    <li><div class="step-num">2</div><div><strong>Najm.sa</strong> ویب سائٹ پر گاڑی نمبر سے چیک کریں</div></li>
    <li><div class="step-num">3</div><div>MOI (وزارت داخلہ) ایپ سے بھی چیک ممکن ہے</div></li>
  </ol>

  <h2>جرمانہ کیسے ادا کریں؟</h2>
  <ul class="check">
    <li>Absher ایپ میں آن لائن ادائیگی (Mada/Visa)</li>
    <li>STC Pay سے براہ راست ادائیگی</li>
    <li>سعودی بینک کی شاخ پر نقد</li>
    <li>Najm.sa پورٹل سے آن لائن</li>
  </ul>

  <div class="tip-box">💡 کچھ جرمانوں پر 30 دن کے اندر ادائیگی پر <strong>50% رعایت</strong> مل سکتی ہے۔ جلد ادا کریں!</div>

  <h2>جرمانہ نہ دینے کے نتائج</h2>
  <ul class="check">
    <li>گاڑی کی نمبر پلیٹ بلاک — گاڑی نہیں بیچ سکتے</li>
    <li>Absher پر سروسز بند ہو سکتی ہیں</li>
    <li>ائیرپورٹ پر روک لیا جا سکتا ہے</li>
    <li>اقامہ تجدید میں مسئلہ</li>
  </ul>

  <div class="cta-box">
    <h3>🚦 ٹریفک فائن کیلکولیٹر</h3>
    <p>اپنے جرمانوں کا مکمل حساب لگائیں</p>
    <a href="{DOMAIN}/traffic-fine-calculator.html">ٹریفک فائن کیلکولیٹر (EN) ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/iqama-calculator.html" class="related-card"><div class="r-icon">🪪</div><div class="r-title">اقامہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/vat-calculator.html" class="related-card"><div class="r-icon">🧾</div><div class="r-title">ویٹ کیلکولیٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 6 — Family Visit Visa
# ============================================================
a6_body = f"""
<div class="hero">
  <h1>👨‍👩‍👧 سعودی عرب فیملی ویزٹ ویزہ 2025 — مکمل گائیڈ، اخراجات اور درخواست کا طریقہ</h1>
  <p style="opacity:.85;font-size:1rem;">اپنے خاندان کو سعودی عرب بلائیں — آسان اور تیز طریقہ</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 8 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="info-box">
    <strong>📌 ضروری شرط:</strong> فیملی ویزٹ ویزہ کے لیے آپ کی اقامہ کم از کم 3 ماہ کی میعاد باقی ہونی چاہیے اور تنخواہ SAR 3,000+ ہونی چاہیے۔
  </div>

  <h2>فیملی ویزٹ ویزہ کیا ہے؟</h2>
  <p>یہ ویزہ سعودی عرب میں رہنے والے غیر ملکیوں کو اپنے خاندان (والدین، بیوی، بچے، بھائی بہن) کو عارضی دورے کے لیے بلانے کی اجازت دیتا ہے۔ عموماً 90 دن کا ہوتا ہے۔</p>

  <h2>💰 اخراجات 2025</h2>
  <table class="data">
    <thead><tr><th>فیس کی قسم</th><th>رقم</th></tr></thead>
    <tbody>
      <tr><td>ویزہ فیس (پاکستانی)</td><td>SAR 300 (تقریباً)</td></tr>
      <tr><td>میڈیکل انشورنس (90 دن)</td><td>SAR 100–200</td></tr>
      <tr><td>MOFA سروس فیس</td><td>SAR 50–100</td></tr>
      <tr><td>کل تخمینہ فی شخص</td><td><strong>SAR 450–600</strong></td></tr>
    </tbody>
  </table>

  <h2>📋 ضروری دستاویزات</h2>
  <ul class="check">
    <li>درخواست دہندہ کی اقامہ (کاپی)</li>
    <li>پاسپورٹ (کم از کم 6 ماہ میعاد)</li>
    <li>تنخواہ سرٹیفکیٹ (آجر سے)</li>
    <li>خاندانی تعلق کا ثبوت (نکاح نامہ، پیدائشی سرٹیفکیٹ)</li>
    <li>میڈیکل انشورنس</li>
    <li>ذاتی ضمانت (Personal Guarantee)</li>
  </ul>

  <h2>درخواست کا طریقہ — MOFA پورٹل</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div><strong>visa.mofa.gov.sa</strong> پر لاگ ان کریں (Absher اکاؤنٹ سے)</div></li>
    <li><div class="step-num">2</div><div>"Visit Visa" آپشن منتخب کریں اور درخواست دہندہ کی معلومات بھریں</div></li>
    <li><div class="step-num">3</div><div>دستاویزات اپ لوڈ کریں اور فیس ادا کریں</div></li>
    <li><div class="step-num">4</div><div>ویزہ نمبر حاصل کریں — پاکستان میں پاسپورٹ پر لگائیں (VFS سے)</div></li>
    <li><div class="step-num">5</div><div>مہمان سعودی عرب پہنچنے پر اندراج (Tasjeel) کروائیں</div></li>
  </ol>

  <h2>اہم ہدایات</h2>
  <ul class="check">
    <li>ویزہ ملنے کے بعد 90 دن میں سفر کرنا ضروری ہے</li>
    <li>میعاد ختم ہونے پر توسیع ممکن ہے (Absher سے)</li>
    <li>مہمان کا اقامہ نہیں بنتا — صرف عارضی رہائش</li>
    <li>خروج نہائی (ملک چھوڑنے کی اجازت) ضروری ہے</li>
  </ul>

  <div class="warning-box">⚠️ اگر مہمان میعاد گزار کر رہے تو SAR 500/ماہ جرمانہ اور ملک بدری کا خطرہ۔ واپسی کا ٹکٹ پہلے بک کروائیں!</div>

  <div class="cta-box">
    <h3>📜 تنخواہ سرٹیفکیٹ چاہیے؟</h3>
    <p>فیملی ویزہ کے لیے سرٹیفکیٹ فوری بنائیں</p>
    <a href="{DOMAIN}/ur/salary-certificate.html">سرٹیفکیٹ جنریٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/salary-certificate.html" class="related-card"><div class="r-icon">📜</div><div class="r-title">تنخواہ سرٹیفکیٹ</div></a>
    <a href="{DOMAIN}/ur/noc-letter.html" class="related-card"><div class="r-icon">✉️</div><div class="r-title">NOC جنریٹر</div></a>
    <a href="{DOMAIN}/ur/iqama-calculator.html" class="related-card"><div class="r-icon">🪪</div><div class="r-title">اقامہ کیلکولیٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 7 — Qiwa Portal Guide
# ============================================================
a7_body = f"""
<div class="hero">
  <h1>💼 Qiwa پورٹل — سعودی عرب میں پاکستانی ملازمین کے لیے مکمل گائیڈ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">اقامہ ٹرانسفر، معاہدہ چیک، شکایت — سب Qiwa سے</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 7 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="info-box">
    <strong>Qiwa.sa</strong> سعودی عرب کا سرکاری مزدور پورٹل ہے جسے وزارت محنت چلاتی ہے۔ 2021 کے بعد سے زیادہ تر مزدور خدمات یہاں سے لی جاتی ہیں۔
  </div>

  <h2>Qiwa پر کیا کیا جا سکتا ہے؟</h2>
  <ul class="check">
    <li>ملازمت کا معاہدہ (Contract) دیکھیں اور ڈاؤن لوڈ کریں</li>
    <li>اقامہ ٹرانسفر (کفیل تبدیل) کی درخواست</li>
    <li>آجر کے خلاف شکایت درج کروائیں</li>
    <li>کام کی اجازت (Work Permit) کی تجدید</li>
    <li>تنخواہ کی عدم ادائیگی کی شکایت</li>
    <li>ملازمت کی شرائط دیکھیں</li>
  </ul>

  <h2>Qiwa پر رجسٹریشن کا طریقہ</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div>qiwa.sa پر جائیں اور "Individuals" منتخب کریں</div></li>
    <li><div class="step-num">2</div><div>Absher اکاؤنٹ سے لاگ ان کریں (OTP آئے گا)</div></li>
    <li><div class="step-num">3</div><div>اقامہ نمبر تصدیق کریں</div></li>
    <li><div class="step-num">4</div><div>ڈیش بورڈ پر آپ کی تمام ملازمت معلومات نظر آئیں گی</div></li>
  </ol>

  <h2>معاہدہ کیسے چیک کریں؟</h2>
  <p>Qiwa پر لاگ ان کریں → My Services → Employment Contract → آپ کا معاہدہ نظر آئے گا۔ اگر معاہدہ موجود نہیں یا غلط ہے تو آجر کو Qiwa کے ذریعے درست کرنے کا کہیں۔</p>

  <h2>تنخواہ نہ ملنے پر شکایت</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div>Qiwa → Labour Complaints → New Complaint</div></li>
    <li><div class="step-num">2</div><div>خلاف ورزی کی قسم منتخب کریں: "Non-payment of Wages"</div></li>
    <li><div class="step-num">3</div><div>تاریخیں اور رقم درج کریں</div></li>
    <li><div class="step-num">4</div><div>شکایت جمع کروائیں — 3–5 کاری دن میں جواب آئے گا</div></li>
  </ol>

  <div class="success-box">✅ <strong>اچھی خبر:</strong> 2021 کے نئے قوانین کے تحت اگر آجر تنخواہ نہیں دیتا تو Qiwa کے ذریعے کفیل کی اجازت کے بغیر بھی ٹرانسفر ممکن ہے!</div>

  <h2>Qiwa موبائل ایپ</h2>
  <p>Android اور iOS دونوں پر Qiwa ایپ دستیاب ہے۔ ایپ سے تمام سروسز فون پر ہی مل جاتی ہیں۔</p>

  <div class="cta-box">
    <h3>🔄 اقامہ ٹرانسفر کا حساب لگائیں</h3>
    <a href="{DOMAIN}/ur/iqama-transfer.html">اقامہ ٹرانسفر کیلکولیٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/iqama-transfer.html" class="related-card"><div class="r-icon">🔄</div><div class="r-title">اقامہ ٹرانسفر</div></a>
    <a href="{DOMAIN}/ur/noc-letter.html" class="related-card"><div class="r-icon">✉️</div><div class="r-title">NOC جنریٹر</div></a>
    <a href="{DOMAIN}/ur/eos-calculator.html" class="related-card"><div class="r-icon">🎯</div><div class="r-title">آخری سروس</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 8 — Driving License Conversion
# ============================================================
a8_body = f"""
<div class="hero">
  <h1>🚗 سعودی عرب میں پاکستانی ڈرائیونگ لائسنس تبدیل — مکمل گائیڈ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">ٹیسٹ دینا ہوگا یا نہیں؟ — مکمل معلومات</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 6 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="warning-box">
    ⚠️ <strong>پاکستانی لائسنس کے لیے:</strong> پاکستانی ڈرائیونگ لائسنس براہ راست سعودی لائسنس میں تبدیل نہیں ہوتا۔ ٹیسٹ دینا پڑتا ہے۔
  </div>

  <h2>کن ممالک کا لائسنس بغیر ٹیسٹ تبدیل ہوتا ہے؟</h2>
  <p>صرف چند ممالک کے ڈرائیونگ لائسنس بغیر ٹیسٹ کے تبدیل ہو سکتے ہیں:</p>
  <ul class="check">
    <li>تمام GCC ممالک (UAE، بحرین وغیرہ)</li>
    <li>امریکہ، کینیڈا، آسٹریلیا، برطانیہ</li>
    <li>یورپی یونین کے ممالک</li>
    <li>جاپان، کوریا</li>
  </ul>
  <p>پاکستان، ہندوستان، بنگلہ دیش، فلپائن — ان سب کو <strong>ٹیسٹ دینا پڑتا ہے۔</strong></p>

  <h2>💰 اخراجات</h2>
  <table class="data">
    <thead><tr><th>خدمت</th><th>فیس</th></tr></thead>
    <tbody>
      <tr><td>ڈرائیونگ سکول (تقریباً)</td><td>SAR 1,500–3,000</td></tr>
      <tr><td>نظری امتحان (Theory Test)</td><td>SAR 50</td></tr>
      <tr><td>عملی امتحان (Practical Test)</td><td>SAR 100</td></tr>
      <tr><td>لائسنس فیس</td><td>SAR 400</td></tr>
      <tr><td>Eye Test</td><td>SAR 50–100</td></tr>
    </tbody>
  </table>

  <h2>مرحلہ وار طریقہ</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div><strong>سرکاری ڈرائیونگ سکول</strong> میں داخلہ لیں (Moroor سے منظور شدہ)</div></li>
    <li><div class="step-num">2</div><div>نظری (Theory) کلاسیں مکمل کریں — عربی یا انگریزی میں</div></li>
    <li><div class="step-num">3</div><div>Moroor.sa پر نظری امتحان بک کریں</div></li>
    <li><div class="step-num">4</div><div>نظری پاس کریں پھر عملی امتحان دیں</div></li>
    <li><div class="step-num">5</div><div>دونوں پاس — لائسنس فیس ادا کریں، لائسنس مل جائے گا</div></li>
  </ol>

  <h2>ضروری دستاویزات</h2>
  <ul class="check">
    <li>اقامہ (اصل اور کاپی)</li>
    <li>پاسپورٹ</li>
    <li>پاسپورٹ سائز تصویر</li>
    <li>Eye Test سرٹیفکیٹ (Moroor منظور شدہ آنکھ کا ڈاکٹر)</li>
    <li>پاکستانی ڈرائیونگ لائسنس (اگر ہو)</li>
  </ul>

  <div class="tip-box">💡 <strong>ٹپ:</strong> نظری امتحان کے لیے Saudi Driving Test سوالات انگریزی میں Moroor ایپ پر مل جاتے ہیں۔ مطالعہ کریں — ٹیسٹ آسان ہے!</div>

  <div class="cta-box">
    <h3>📜 اقامہ اور دستاویزات تیار ہیں؟</h3>
    <a href="{DOMAIN}/ur/iqama-calculator.html">اقامہ کیلکولیٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/iqama-calculator.html" class="related-card"><div class="r-icon">🪪</div><div class="r-title">اقامہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/noc-letter.html" class="related-card"><div class="r-icon">✉️</div><div class="r-title">NOC جنریٹر</div></a>
    <a href="{DOMAIN}/ur/salary-certificate.html" class="related-card"><div class="r-icon">📜</div><div class="r-title">تنخواہ سرٹیفکیٹ</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 9 — Exit Re-entry Visa
# ============================================================
a9_body = f"""
<div class="hero">
  <h1>✈️ سعودی عرب Exit Re-entry ویزہ — مکمل گائیڈ 2025</h1>
  <p style="opacity:.85;font-size:1rem;">پاکستان جانے سے پہلے یہ ضرور پڑھیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 6 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="info-box">
    <strong>📌 Exit Re-entry ویزہ:</strong> یہ وہ اجازت ہے جو آپ کو سعودی عرب سے باہر جا کر واپس آنے کی اجازت دیتی ہے۔ بغیر اس کے سعودی عرب چھوڑنا اقامہ کینسل کرا سکتا ہے۔
  </div>

  <h2>Exit Re-entry ویزہ کیا ہے؟</h2>
  <p>جب آپ سعودی عرب سے باہر سفر کرتے ہیں (چھٹی، پاکستان وغیرہ) تو آپ کو Exit Re-entry Visa کی ضرورت ہوتی ہے تاکہ واپس آ سکیں۔ بغیر اس کے نکلنا Final Exit (خروج نہائی) کہلاتا ہے — پھر واپسی ممکن نہیں۔</p>

  <h2>Exit Re-entry Visa کے اقسام</h2>
  <table class="data">
    <thead><tr><th>قسم</th><th>استعمال</th><th>مدت</th></tr></thead>
    <tbody>
      <tr><td>Single Exit Re-entry</td><td>ایک بار باہر اور واپس</td><td>3–6 ماہ</td></tr>
      <tr><td>Multiple Exit Re-entry</td><td>کئی بار آنا جانا</td><td>1–2 سال</td></tr>
      <tr><td>Final Exit (خروج نہائی)</td><td>ہمیشہ کے لیے نکلنا</td><td>—</td></tr>
    </tbody>
  </table>

  <h2>💰 فیس</h2>
  <p>2021 کے بعد سے <strong>Exit Re-entry Visa مفت</strong> ہے۔ پہلے SAR 200–400 لگتے تھے۔</p>

  <h2>کیسے لیں؟ — Absher سے</h2>
  <ol class="step-list">
    <li><div class="step-num">1</div><div>Absher.sa → Individuals → My Services → Exit/Re-entry Visa</div></li>
    <li><div class="step-num">2</div><div>Single یا Multiple منتخب کریں</div></li>
    <li><div class="step-num">3</div><div>واپسی کی آخری تاریخ منتخب کریں</div></li>
    <li><div class="step-num">4</div><div>فوری منظوری — ڈیجیٹل ویزہ Absher میں محفوظ</div></li>
  </ol>

  <div class="warning-box">
    ⚠️ <strong>خبردار:</strong>
    <ul style="margin-top:8px;padding-right:16px;">
      <li>Exit Re-entry کی میعاد گزر گئی اور واپس نہیں آئے تو اقامہ کینسل</li>
      <li>Final Exit لے لی تو واپس نئی ملازمت کے ویزہ پر ہی آ سکتے ہیں</li>
      <li>آجر کی منظوری ضروری ہو سکتی ہے (پرانے قوانین میں)</li>
    </ul>
  </div>

  <h2>2021 کے نئے قوانین</h2>
  <p>2021 کے اصلاحات کے بعد ملازمین کو Exit Re-entry لینے کے لیے آجر کی اجازت کی ضرورت نہیں رہی — آپ خود Absher سے لے سکتے ہیں۔ یہ پاکستانی ملازمین کے لیے بہت بڑی تبدیلی ہے۔</p>

  <div class="success-box">✅ <strong>اچھی خبر:</strong> اب آپ بغیر آجر کی اجازت کے پاکستان جا سکتے ہیں — بس Exit Re-entry Absher سے لیں!</div>

  <div class="cta-box">
    <h3>🪪 اقامہ کی میعاد چیک کریں</h3>
    <p>سفر سے پہلے اقامہ چیک کرنا ضروری ہے</p>
    <a href="{DOMAIN}/ur/iqama-calculator.html">اقامہ کیلکولیٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/iqama-calculator.html" class="related-card"><div class="r-icon">🪪</div><div class="r-title">اقامہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/iqama-transfer.html" class="related-card"><div class="r-icon">🔄</div><div class="r-title">اقامہ ٹرانسفر</div></a>
    <a href="{DOMAIN}/ur/noc-letter.html" class="related-card"><div class="r-icon">✉️</div><div class="r-title">NOC جنریٹر</div></a>
  </div>
</article>"""

# ============================================================
# ARTICLE 10 — Worker Rights
# ============================================================
a10_body = f"""
<div class="hero">
  <h1>⚖️ سعودی عرب میں پاکستانی ملازمین کے قانونی حقوق 2025</h1>
  <p style="opacity:.85;font-size:1rem;">اپنے حقوق جانیں — استحصال سے بچیں</p>
  <div class="hero-meta"><span>📅 جنوری 2025</span><span>⏱️ 9 منٹ مطالعہ</span></div>
</div>
<article>
  <div class="success-box">
    <strong>✅ یاد رکھیں:</strong> سعودی لیبر قانون تمام ملازمین — چاہے سعودی ہوں یا غیر ملکی — کو یکساں بنیادی حقوق دیتا ہے۔ آپ کے حقوق کا دفاع آپ کا فرض ہے!
  </div>

  <h2>1. تنخواہ کا حق</h2>
  <p>ہر ملازم کو وقت پر (مہینے کے آخر تک) مکمل تنخواہ ملنا لازمی ہے۔ Wage Protection System (WPS) کے تحت آجر کو ملازمین کی تنخواہ بینک کے ذریعے دینی ہوتی ہے۔ اگر تنخواہ نہ ملے تو Qiwa.sa پر فوری شکایت کریں۔</p>

  <h2>2. آخری سروس (EOS) کا حق</h2>
  <p>ہر ملازم جو 2 سال یا اس سے زیادہ کام کرے اسے آخری سروس ملنی چاہیے۔ یہ قانوناً لازمی ہے — آجر انکار نہیں کر سکتا۔</p>

  <h2>3. سالانہ چھٹیوں کا حق</h2>
  <table class="data">
    <thead><tr><th>سروس کی مدت</th><th>سالانہ چھٹیاں</th></tr></thead>
    <tbody>
      <tr><td>5 سال سے کم</td><td>21 دن</td></tr>
      <tr><td>5 سال یا زیادہ</td><td>30 دن</td></tr>
    </tbody>
  </table>
  <p>اگر چھٹیاں نہیں لیں تو نوکری ختم ہونے پر باقی چھٹیوں کی تنخواہ ملنا لازمی ہے۔</p>

  <h2>4. کام کے اوقات کا حق</h2>
  <ul class="check">
    <li>روزانہ 8 گھنٹے سے زیادہ کام نہیں کرا سکتے</li>
    <li>رمضان میں 6 گھنٹے سے زیادہ نہیں</li>
    <li>اضافی کام پر اوور ٹائم دینا لازمی (25–50% اضافہ)</li>
    <li>ہفتے میں کم از کم 1 دن آرام</li>
  </ul>

  <h2>5. محفوظ کام کا حق</h2>
  <p>آجر کا فرض ہے کہ محفوظ کام کا ماحول دے۔ اگر کام کی جگہ خطرناک ہو یا حادثہ ہو تو آجر ذمہ دار ہے۔ حادثاتی بیمہ (GOSI Occupational Hazard) آجر ادا کرتا ہے۔</p>

  <h2>6. ناجائز برطرفی کے خلاف حق</h2>
  <p>آجر بغیر وجہ فوری نہیں نکال سکتا۔ اگر بغیر نوٹس نکالا جائے تو آپ نوٹس پیریڈ کی تنخواہ کے حق دار ہیں۔</p>

  <h2>📞 شکایت کہاں کریں؟</h2>
  <table class="data">
    <thead><tr><th>مسئلہ</th><th>کہاں رابطہ کریں</th></tr></thead>
    <tbody>
      <tr><td>تنخواہ نہ ملنا</td><td>Qiwa.sa → Labour Complaints</td></tr>
      <tr><td>EOS نہ ملنا</td><td>Qiwa یا Labour Court</td></tr>
      <tr><td>اقامہ مسائل</td><td>Absher یا Jawazat</td></tr>
      <tr><td>جسمانی تشدد / بدسلوکی</td><td>پولیس 911 یا سفارت خانہ</td></tr>
      <tr><td>پاکستانی سفارت خانہ (ریاض)</td><td>+966-11-4600405</td></tr>
    </tbody>
  </table>

  <div class="tip-box">💡 <strong>مشورہ:</strong> اپنے ملازمت معاہدے کی کاپی ہمیشہ اپنے پاس رکھیں اور Qiwa پر آن لائن بھی چیک کریں۔</div>

  <h2>اہم پاکستانی سفارتی معلومات</h2>
  <ul class="check">
    <li><strong>ریاض سفارت خانہ:</strong> +966-11-4600405</li>
    <li><strong>جدہ قنصل خانہ:</strong> +966-12-6651010</li>
    <li><strong>OISL (اوورسیز پاکستانیوں کی مدد):</strong> overseas.gov.pk</li>
  </ul>

  <div class="cta-box">
    <h3>🎯 اپنی EOS حساب کریں</h3>
    <p>جانیں آپ کتنی رقم کے حق دار ہیں</p>
    <a href="{DOMAIN}/ur/eos-calculator.html">آخری سروس کیلکولیٹر ←</a>
  </div>

  <div class="related-grid">
    <a href="{DOMAIN}/ur/eos-calculator.html" class="related-card"><div class="r-icon">🎯</div><div class="r-title">EOS کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/salary-calculator.html" class="related-card"><div class="r-icon">🧮</div><div class="r-title">تنخواہ کیلکولیٹر</div></a>
    <a href="{DOMAIN}/ur/iqama-transfer.html" class="related-card"><div class="r-icon">🔄</div><div class="r-title">اقامہ ٹرانسفر</div></a>
  </div>
</article>"""

# ============================================================
# Define all articles
# ============================================================
articles = [
    {
        "slug": "iqama-tajdeed-guide",
        "title": "اقامہ تجدید کا مکمل طریقہ 2025 — فیس، دستاویزات اور آن لائن طریقہ",
        "meta_desc": "سعودی عرب میں اقامہ تجدید کا مکمل طریقہ: فیس SAR 650، ضروری دستاویزات، Absher سے آن لائن تجدید اور جرمانوں سے بچنے کے طریقے۔",
        "keywords": "اقامہ تجدید, iqama renewal, اقامہ فیس 2025, Absher اقامہ, اقامہ تجدید طریقہ",
        "en_url": f"{DOMAIN}/blog/iqama-renewal-guide.html",
        "ar_url": f"{DOMAIN}/ar/blog/iqama-tajdeed.html",
        "pub_date": "2025-01-10",
        "read_time": "7",
        "tags": "اقامہ, تجدید, سعودی عرب",
        "body": a1_body,
    },
    {
        "slug": "gosi-guide-pakistanis",
        "title": "گوسی (GOSI) کیا ہے؟ پاکستانی ملازمین کے لیے مکمل گائیڈ 2025",
        "meta_desc": "سعودی عرب میں GOSI کیا ہے؟ کیا پاکستانیوں کی تنخواہ سے گوسی کٹتا ہے؟ 2025 کی شرح، حساب کا طریقہ اور مکمل معلومات اردو میں۔",
        "keywords": "گوسی سعودی عرب, GOSI پاکستانی, GOSI rate 2025, گوسی کٹوتی, پاکستانی ملازم گوسی",
        "en_url": f"{DOMAIN}/gosi-calculator.html",
        "ar_url": f"{DOMAIN}/ar/gosi-calculator.html",
        "pub_date": "2025-01-12",
        "read_time": "6",
        "tags": "گوسی, GOSI, پاکستانی ملازمین",
        "body": a2_body,
    },
    {
        "slug": "eos-guide-urdu",
        "title": "سعودی عرب میں آخری سروس (End of Service) کا حساب — مکمل گائیڈ 2025",
        "meta_desc": "سعودی عرب میں آخری سروس (EOS) کا حساب کیسے لگائیں؟ آرٹیکل 84 فارمولا، استعفیٰ اور برطرفی کی صورت میں رقم کا حساب اردو میں۔",
        "keywords": "آخری سروس سعودی عرب, end of service Pakistan, EOS calculator urdu, سروس گریجویٹی, آرٹیکل 84",
        "en_url": f"{DOMAIN}/end-of-service-calculator.html",
        "ar_url": f"{DOMAIN}/ar/eos-calculator.html",
        "pub_date": "2025-01-15",
        "read_time": "8",
        "tags": "آخری سروس, EOS, سعودی لیبر قانون",
        "body": a3_body,
    },
    {
        "slug": "remittance-guide-pakistan",
        "title": "سعودی عرب سے پاکستان پیسے بھیجنے کے 5 بہترین طریقے 2025",
        "meta_desc": "Wise، Al Rajhi، STC Pay، Western Union — سعودی عرب سے پاکستان ریمیٹنس کا موازنہ۔ SAR to PKR بہترین ریٹ، کم فیس، فوری ٹرانسفر۔",
        "keywords": "سعودی عرب سے پاکستان پیسے بھیجنا, SAR to PKR, Wise سعودی عرب, Al Rajhi ریمیٹنس, ریمیٹنس گائیڈ",
        "en_url": f"{DOMAIN}/remittance-fee-compare.html",
        "ar_url": f"{DOMAIN}/ar/remittance.html",
        "pub_date": "2025-01-18",
        "read_time": "7",
        "tags": "ریمیٹنس, پاکستان, SAR to PKR",
        "body": a4_body,
    },
    {
        "slug": "traffic-fines-guide",
        "title": "سعودی عرب میں ٹریفک جرمانے — مکمل فہرست اور ادائیگی 2025",
        "meta_desc": "سعودی عرب کے تمام ٹریفک جرمانوں کی فہرست اردو میں۔ Absher اور Najm سے جرمانے چیک کریں اور آن لائن ادا کریں۔ 2025 کی تازہ فیس۔",
        "keywords": "سعودی عرب ٹریفک جرمانہ, traffic fine Saudi Arabia, Najm جرمانہ, Absher ٹریفک, ٹریفک فائن اردو",
        "en_url": f"{DOMAIN}/traffic-fine-calculator.html",
        "ar_url": f"{DOMAIN}/ar/traffic-fines.html",
        "pub_date": "2025-01-20",
        "read_time": "6",
        "tags": "ٹریفک, جرمانہ, Najm",
        "body": a5_body,
    },
    {
        "slug": "family-visit-visa-guide",
        "title": "سعودی عرب فیملی ویزٹ ویزہ 2025 — مکمل گائیڈ، اخراجات اور درخواست",
        "meta_desc": "سعودی عرب فیملی ویزٹ ویزہ کیسے لیں؟ MOFA پورٹل سے درخواست، فیس، دستاویزات اور ضروری شرائط اردو میں — 2025 کی تازہ معلومات۔",
        "keywords": "فیملی ویزٹ ویزہ سعودی عرب, family visit visa Pakistan, MOFA ویزہ, سعودی ویزٹ ویزہ 2025",
        "en_url": f"{DOMAIN}/family-visit-visa-guide.html",
        "ar_url": f"{DOMAIN}/ar/family-visa.html",
        "pub_date": "2025-01-22",
        "read_time": "8",
        "tags": "فیملی ویزہ, MOFA, سعودی عرب",
        "body": a6_body,
    },
    {
        "slug": "qiwa-portal-guide",
        "title": "Qiwa پورٹل — پاکستانی ملازمین کے لیے مکمل گائیڈ 2025",
        "meta_desc": "Qiwa.sa پورٹل سے اقامہ ٹرانسفر، معاہدہ چیک، تنخواہ شکایت — پاکستانی ملازمین کے لیے مکمل گائیڈ اردو میں۔",
        "keywords": "Qiwa پورٹل اردو, Qiwa پاکستانی گائیڈ, qiwa.sa استعمال, اقامہ ٹرانسفر Qiwa, Qiwa شکایت",
        "en_url": f"{DOMAIN}/blog/qiwa-portal-guide.html",
        "ar_url": f"{DOMAIN}/ar/blog/qiwa-guide.html",
        "pub_date": "2025-01-25",
        "read_time": "7",
        "tags": "Qiwa, مزدور حقوق, سعودی عرب",
        "body": a7_body,
    },
    {
        "slug": "driving-license-conversion",
        "title": "سعودی عرب میں پاکستانی ڈرائیونگ لائسنس تبدیل — مکمل گائیڈ 2025",
        "meta_desc": "پاکستانی ڈرائیونگ لائسنس سعودی عرب میں کیسے تبدیل کریں؟ ٹیسٹ کی ضرورت، اخراجات، ضروری دستاویزات اردو میں۔",
        "keywords": "پاکستانی لائسنس سعودی عرب, driving license conversion Saudi, سعودی ڈرائیونگ لائسنس پاکستانی",
        "en_url": f"{DOMAIN}/driving-license-conversion.html",
        "ar_url": f"{DOMAIN}/ar/driving-license.html",
        "pub_date": "2025-01-28",
        "read_time": "6",
        "tags": "ڈرائیونگ لائسنس, سعودی عرب, پاکستانی",
        "body": a8_body,
    },
    {
        "slug": "exit-reentry-visa-guide",
        "title": "سعودی عرب Exit Re-entry ویزہ — مکمل گائیڈ 2025",
        "meta_desc": "سعودی عرب Exit Re-entry ویزہ کیا ہے؟ Absher سے کیسے لیں، Final Exit سے فرق، اور 2021 کے نئے قوانین اردو میں۔",
        "keywords": "exit re-entry visa Saudi Arabia, خروج عودہ سعودی, Absher ایگزٹ ویزہ, پاکستان جانا سعودی عرب",
        "en_url": f"{DOMAIN}/blog/exit-reentry-visa.html",
        "ar_url": f"{DOMAIN}/ar/blog/exit-visa.html",
        "pub_date": "2025-02-01",
        "read_time": "6",
        "tags": "ایگزٹ ویزہ, سفر, سعودی عرب",
        "body": a9_body,
    },
    {
        "slug": "worker-rights-saudi",
        "title": "سعودی عرب میں پاکستانی ملازمین کے قانونی حقوق 2025",
        "meta_desc": "سعودی عرب میں پاکستانی ملازمین کے قانونی حقوق — تنخواہ، چھٹیاں، EOS، محفوظ کام کا ماحول اور شکایت کا طریقہ اردو میں۔",
        "keywords": "سعودی عرب مزدور حقوق, پاکستانی ملازم حقوق, لیبر قانون سعودی عرب اردو, Qiwa شکایت, سعودی کفیل حقوق",
        "en_url": f"{DOMAIN}/blog/worker-rights-saudi.html",
        "ar_url": f"{DOMAIN}/ar/blog/worker-rights.html",
        "pub_date": "2025-02-05",
        "read_time": "9",
        "tags": "مزدور حقوق, لیبر قانون, پاکستانی",
        "body": a10_body,
    },
]

# ============================================================
# Write all article files
# ============================================================
written = []
for art in articles:
    canonical = f"{DOMAIN}/ur/blog/{art['slug']}.html"
    html = page(
        title=art["title"],
        meta_desc=art["meta_desc"],
        keywords=art["keywords"],
        canonical=canonical,
        en_url=art["en_url"],
        ar_url=art["ar_url"],
        pub_date=art["pub_date"],
        read_time=art["read_time"],
        tags=art["tags"],
        body_html=art["body"],
    )
    out_path = f"{OUT}/{art['slug']}.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    written.append(art["slug"])
    print(f"✓ {art['slug']}.html")

print(f"\nDone! {len(written)} articles written to {OUT}")
