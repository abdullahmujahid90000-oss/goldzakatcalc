#!/usr/bin/env python3
"""Build Urdu pages 1-3: Salary Calculator, GOSI, EOS"""

OUT = "/sessions/clever-inspiring-albattani/mnt/outputs/ur"
import os
os.makedirs(OUT, exist_ok=True)

# Shared nav/footer/CSS for all Urdu pages
UR_NAV_CSS = """
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Jameel Noori Nastaleeq','Noto Nastaliq Urdu','Segoe UI',Tahoma,sans-serif;background:#f8fafc;color:#1a202c;line-height:1.9;direction:rtl}
    nav{background:#fff;border-bottom:2px solid #e2e8f0;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.06)}
    .nav-inner{max-width:1200px;margin:0 auto;padding:0 16px;display:flex;align-items:center;gap:4px;flex-wrap:wrap;min-height:52px;direction:rtl}
    .nav-logo{font-weight:700;font-size:1rem;color:#1a56db;text-decoration:none;margin-left:10px;white-space:nowrap;font-family:'Segoe UI',sans-serif}
    nav a{color:#374151;text-decoration:none;padding:6px 10px;border-radius:6px;font-size:.85rem;white-space:nowrap;transition:background .15s}
    nav a:hover,nav a.active{background:#eff6ff;color:#1a56db}
    .lang-switcher{margin-right:auto;display:flex;gap:4px;direction:ltr}
    .lang-switcher a{background:#f1f5f9;color:#374151;padding:4px 10px;border-radius:6px;font-size:.8rem;font-weight:600;text-decoration:none;border:1px solid #e2e8f0}
    .lang-switcher a:hover{background:#eff6ff;color:#1a56db}
    .lang-switcher a.active-lang{background:#1a56db;color:#fff;border-color:#1a56db}
    .hero{background:linear-gradient(135deg,#1a56db 0%,#1e40af 60%,#065f46 100%);color:#fff;padding:48px 16px 40px;text-align:center}
    .hero h1{font-size:clamp(1.5rem,3.5vw,2.3rem);font-weight:800;margin-bottom:10px;line-height:1.4}
    .hero p{font-size:1rem;opacity:.9;max-width:680px;margin:0 auto 16px}
    .hero-badges{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;font-size:.82rem;margin-bottom:0}
    .hero-badges span{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.3);padding:4px 12px;border-radius:20px}
    main{max-width:920px;margin:0 auto;padding:28px 16px 48px}
    .card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:22px 24px;margin-bottom:20px}
    h2{font-size:1.15rem;font-weight:700;color:#1a202c;margin-bottom:14px}
    label{display:block;font-size:.88rem;font-weight:600;color:#374151;margin-bottom:4px;margin-top:12px}
    input,select{width:100%;padding:10px 12px;border:1px solid #d1d5db;border-radius:8px;font-size:.95rem;font-family:inherit;background:#fff;color:#1a202c;direction:rtl}
    input:focus,select:focus{outline:none;border-color:#1a56db;box-shadow:0 0 0 3px rgba(26,86,219,.1)}
    .btn{display:inline-block;padding:11px 28px;background:#1a56db;color:#fff;border:none;border-radius:8px;font-size:1rem;font-weight:700;cursor:pointer;margin-top:14px;width:100%;font-family:inherit}
    .btn:hover{background:#1e40af}
    .result-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;padding:20px;margin-top:18px;display:none}
    .result-box.show{display:block}
    .res-row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #dcfce7;font-size:.92rem}
    .res-row:last-child{border:none;font-weight:700;font-size:1.05rem;color:#166534}
    .res-label{color:#374151}
    .res-val{font-weight:700;color:#1a56db;font-family:'Segoe UI',sans-serif}
    .res-row:last-child .res-val{color:#166534}
    .info-box{background:#eff6ff;border-right:4px solid #1a56db;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:.88rem;color:#1e40af;border-left:none}
    .warn-box{background:#fefce8;border-right:4px solid #ca8a04;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:.88rem;border-left:none}
    details{border:1px solid #e2e8f0;border-radius:10px;margin-bottom:8px;background:#fff}
    summary{padding:13px 16px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;font-size:.92rem}
    summary::-webkit-details-marker{display:none}
    summary::before{content:'+';font-size:1.2rem;color:#1a56db;margin-left:8px}
    details[open] summary::before{content:'−'}
    .faq-answer{padding:0 16px 12px;font-size:.88rem;color:#374151;line-height:1.8}
    footer{background:#1a202c;color:#e2e8f0;padding:32px 16px 20px;direction:rtl}
    .footer-inner{max-width:1200px;margin:0 auto}
    .footer-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:22px;margin-bottom:20px}
    .footer-col h4{font-size:.82rem;font-weight:700;color:#fff;margin-bottom:10px;text-transform:uppercase}
    .footer-col a{display:block;color:#94a3b8;text-decoration:none;font-size:.8rem;margin-bottom:5px}
    .footer-col a:hover{color:#fff}
    .footer-bottom{border-top:1px solid #2d3748;padding-top:12px;font-size:.77rem;color:#6b7280}
    #ck{position:fixed;bottom:0;left:0;right:0;background:#1a202c;color:#e2e8f0;padding:12px 20px;display:flex;flex-wrap:wrap;align-items:center;gap:10px;z-index:999;font-size:.83rem;direction:rtl}
    #ck a{color:#60a5fa}
    #ck button{padding:6px 14px;border-radius:5px;border:none;cursor:pointer;font-size:.82rem;font-weight:600}
"""

UR_NAV_TEMPLATE = """<nav>
  <div class="nav-inner">
    <a href="https://www.saudiutilityhub.com/ur/" class="nav-logo">🇸🇦 Saudi Utility Hub</a>
    <a href="https://www.saudiutilityhub.com/ur/salary-calculator.html">تنخواہ</a>
    <a href="https://www.saudiutilityhub.com/ur/gosi-calculator.html">گوسی</a>
    <a href="https://www.saudiutilityhub.com/ur/eos-calculator.html">آخری سروس</a>
    <a href="https://www.saudiutilityhub.com/ur/iqama-calculator.html">اقامہ</a>
    <a href="https://www.saudiutilityhub.com/ur/salary-slip.html">تنخواہ سلپ</a>
    <a href="https://www.saudiutilityhub.com/ur/noc-letter.html">این او سی</a>
    <a href="https://www.saudiutilityhub.com/ur/remittance.html">رقم بھیجیں</a>
    <a href="https://www.saudiutilityhub.com/ur/vat-calculator.html">ویٹ</a>
    <div class="lang-switcher">
      <a href="{EN_URL}">EN</a>
      <a href="{AR_URL}">عربي</a>
      <a href="#" class="active-lang">اردو</a>
    </div>
  </div>
</nav>"""

UR_FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>تنخواہ کے اوزار</h4>
        <a href="https://www.saudiutilityhub.com/ur/salary-calculator.html">تنخواہ کیلکولیٹر</a>
        <a href="https://www.saudiutilityhub.com/ur/gosi-calculator.html">گوسی کیلکولیٹر</a>
        <a href="https://www.saudiutilityhub.com/ur/eos-calculator.html">آخری سروس گریجویٹی</a>
        <a href="https://www.saudiutilityhub.com/ur/salary-slip.html">تنخواہ سلپ</a>
        <a href="https://www.saudiutilityhub.com/ur/salary-certificate.html">تنخواہ سرٹیفکیٹ</a>
      </div>
      <div class="footer-col">
        <h4>ویزہ اور اقامہ</h4>
        <a href="https://www.saudiutilityhub.com/ur/iqama-calculator.html">اقامہ ٹریکر</a>
        <a href="https://www.saudiutilityhub.com/ur/noc-letter.html">این او سی لیٹر</a>
        <a href="https://www.saudiutilityhub.com/ur/iqama-transfer.html">اقامہ ٹرانسفر</a>
        <a href="https://www.saudiutilityhub.com/ur/family-visa.html">فیملی وزٹ ویزہ</a>
      </div>
      <div class="footer-col">
        <h4>پیسہ بھیجیں</h4>
        <a href="https://www.saudiutilityhub.com/ur/remittance.html">ریمیٹنس موازنہ</a>
        <a href="https://www.saudiutilityhub.com/ur/vat-calculator.html">ویٹ کیلکولیٹر</a>
      </div>
      <div class="footer-col">
        <h4>دیگر زبانیں</h4>
        <a href="https://www.saudiutilityhub.com/">English</a>
        <a href="https://www.saudiutilityhub.com/ar/">عربي</a>
      </div>
    </div>
    <div class="footer-bottom">© 2026 Saudi Utility Hub · ریاض، سعودی عرب · تمام حسابات تخمینی ہیں۔</div>
  </div>
</footer>
<div id="ck">
  <span>🍪 ہم اشتہارات اور ٹریفک کے لیے کوکیز استعمال کرتے ہیں۔ <a href="https://www.saudiutilityhub.com/privacy.html">پرائیویسی پالیسی</a></span>
  <button onclick="document.getElementById('ck').style.display='none';localStorage.setItem('ck','1')" style="background:#1a56db;color:#fff">قبول کریں</button>
  <button onclick="document.getElementById('ck').style.display='none'" style="background:#374151;color:#e2e8f0">انکار</button>
</div>
<script>if(localStorage.getItem('ck'))document.getElementById('ck').style.display='none'</script>"""

def make_nav(en_url, ar_url):
    return UR_NAV_TEMPLATE.replace("{EN_URL}", en_url).replace("{AR_URL}", ar_url)

# ============================================================
# PAGE 1: Urdu Salary Calculator
# ============================================================
p1 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>سعودی عرب تنخواہ کیلکولیٹر 2026 — گوسی کٹوتی اور نیٹ تنخواہ</title>
  <meta name="description" content="سعودی عرب میں اپنی اصل تنخواہ معلوم کریں۔ گوسی کٹوتی، الاؤنسز اور نیٹ تنخواہ کا حساب لگائیں۔ پاکستانی اور تمام غیر ملکی ملازمین کے لیے۔ 2026 کی تازہ ترین شرحیں۔">
  <meta name="keywords" content="سعودی عرب تنخواہ کیلکولیٹر, گوسی کٹوتی, نیٹ تنخواہ سعودی عرب, پاکستانی تنخواہ سعودی, salary calculator urdu saudi arabia">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/salary-calculator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/salary-calculator.html">
  <meta property="og:title" content="سعودی عرب تنخواہ کیلکولیٹر 2026 اردو">
  <meta property="og:description" content="اپنی نیٹ تنخواہ، گوسی کٹوتی اور تمام الاؤنسز کا فوری حساب لگائیں۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/salary-calculator.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/salary-calculator.html">
  <link rel="alternate" hreflang="ar" href="https://www.saudiutilityhub.com/ar/salary-calculator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/salary-calculator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"سعودی عرب تنخواہ کیلکولیٹر","url":"https://www.saudiutilityhub.com/ur/salary-calculator.html","description":"سعودی عرب میں نیٹ تنخواہ اور گوسی کٹوتی کا حساب لگائیں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {{"@type":"Question","name":"سعودی عرب میں تنخواہ سے کتنی کٹوتی ہوتی ہے؟","acceptedAnswer":{{"@type":"Answer","text":"پاکستانی اور دیگر غیر ملکی ملازمین کی تنخواہ سے کوئی کٹوتی نہیں ہوتی۔ صرف سعودی ملازمین کی تنخواہ سے گوسی 9.75 فیصد کٹتی ہے۔"}}}},
    {{"@type":"Question","name":"سعودی عرب میں گوسی کیا ہے؟","acceptedAnswer":{{"@type":"Answer","text":"گوسی سعودی عرب کا سوشل انشورنس نظام ہے۔ سعودی ملازمین کی بنیادی تنخواہ اور رہائش الاؤنس کا 9.75 فیصد کٹتا ہے۔ زیادہ سے زیادہ حد 45,000 ریال ماہانہ ہے۔"}}}},
    {{"@type":"Question","name":"سعودی عرب میں کم از کم تنخواہ کتنی ہے؟","acceptedAnswer":{{"@type":"Answer","text":"2026 میں سعودی ملازمین کی کم از کم تنخواہ 4,000 ریال ماہانہ ہے۔ غیر ملکی ملازمین کے لیے کوئی قانونی کم از کم تنخواہ نہیں ہے، لیکن عام طور پر پیشہ اور ویزہ کیٹیگری کے مطابق طے ہوتی ہے۔"}}}}
  ]}}
  </script>
  <style>{UR_NAV_CSS}</style>
</head>
<body>
{make_nav("https://www.saudiutilityhub.com/salary-calculator.html","https://www.saudiutilityhub.com/ar/salary-calculator.html")}
<section class="hero">
  <h1>💼 سعودی عرب تنخواہ کیلکولیٹر 2026</h1>
  <p>اپنی نیٹ تنخواہ، گوسی کٹوتی اور تمام الاؤنسز کا فوری حساب لگائیں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span>
    <span>🔒 رجسٹریشن نہیں</span>
    <span>📅 2026 شرحیں</span>
    <span>⚡ فوری نتیجہ</span>
  </div>
</section>
<main>
  <div class="info-box">
    <strong>پاکستانی ملازمین کے لیے:</strong> آپ کی تنخواہ سے کوئی گوسی یا انکم ٹیکس نہیں کاٹا جاتا۔ آپ کی مکمل تنخواہ آپ کی ہے۔ صرف سعودی شہریوں پر 9.75% گوسی لاگو ہوتی ہے۔
  </div>
  <div class="card">
    <h2>📝 تنخواہ کی تفصیل درج کریں</h2>
    <label>بنیادی تنخواہ (ریال)</label>
    <input type="number" id="basic" placeholder="مثلاً 3000" min="0">
    <label>رہائش الاؤنس (ریال)</label>
    <input type="number" id="housing" placeholder="مثلاً 1000" min="0">
    <label>ٹرانسپورٹ الاؤنس (ریال)</label>
    <input type="number" id="transport" placeholder="مثلاً 500" min="0">
    <label>دیگر الاؤنسز (ریال)</label>
    <input type="number" id="other" placeholder="مثلاً 200" min="0">
    <label>قومیت</label>
    <select id="nationality">
      <option value="expat">غیر ملکی (پاکستانی، ہندوستانی، بنگلہ دیشی وغیرہ)</option>
      <option value="saudi">سعودی شہری</option>
    </select>
    <button class="btn" onclick="calcSalary()">حساب لگائیں</button>
  </div>
  <div class="result-box" id="salResult">
    <h2 style="color:#166534;margin-bottom:14px">✅ آپ کی تنخواہ کا حساب</h2>
    <div class="res-row"><span class="res-label">بنیادی تنخواہ</span><span class="res-val" id="r_basic"></span></div>
    <div class="res-row"><span class="res-label">رہائش الاؤنس</span><span class="res-val" id="r_housing"></span></div>
    <div class="res-row"><span class="res-label">ٹرانسپورٹ الاؤنس</span><span class="res-val" id="r_transport"></span></div>
    <div class="res-row"><span class="res-label">دیگر الاؤنسز</span><span class="res-val" id="r_other"></span></div>
    <div class="res-row"><span class="res-label">کل مجموعی تنخواہ</span><span class="res-val" id="r_gross"></span></div>
    <div class="res-row"><span class="res-label">گوسی کٹوتی</span><span class="res-val" id="r_gosi"></span></div>
    <div class="res-row"><span class="res-label">🏦 نیٹ تنخواہ (ہاتھ میں)</span><span class="res-val" id="r_net"></span></div>
  </div>
  <div class="card">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>پاکستانی ملازم کی تنخواہ سے کوئی کٹوتی ہوتی ہے؟</summary><div class="faq-answer">نہیں۔ پاکستانی اور تمام غیر ملکی ملازمین کی تنخواہ سے نہ گوسی کٹتی ہے نہ انکم ٹیکس۔ آپ کی پوری تنخواہ آپ کو ملتی ہے۔</div></details>
    <details><summary>گوسی کیا ہے اور کس پر لاگو ہوتی ہے؟</summary><div class="faq-answer">گوسی (GOSI) سعودی عرب کا سوشل انشورنس پروگرام ہے۔ صرف سعودی شہری ملازمین پر 9.75% شرح سے لاگو ہوتی ہے، زیادہ سے زیادہ حد 45,000 ریال ماہانہ ہے۔</div></details>
    <details><summary>سعودی عرب میں تنخواہ کے ساتھ کون سے الاؤنسز ملتے ہیں؟</summary><div class="faq-answer">عام طور پر رہائش الاؤنس (بنیادی تنخواہ کا 25-30%)، ٹرانسپورٹ الاؤنس (750-1000 ریال)، اور کبھی کبھی کھانے یا موبائل الاؤنس بھی شامل ہوتے ہیں۔</div></details>
    <details><summary>سعودی عرب میں تنخواہ کب ملتی ہے؟</summary><div class="faq-answer">WPS (Wage Protection System) کے تحت ہر ماہ کی 10 تاریخ سے پہلے تنخواہ ادا کرنا لازمی ہے۔ تاخیر پر آجر کو جرمانہ ہو سکتا ہے۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
function fmt(n){{return 'SAR '+n.toLocaleString('en-US',{{minimumFractionDigits:2,maximumFractionDigits:2}});}}
function calcSalary(){{
  const basic=parseFloat(document.getElementById('basic').value)||0;
  const housing=parseFloat(document.getElementById('housing').value)||0;
  const transport=parseFloat(document.getElementById('transport').value)||0;
  const other=parseFloat(document.getElementById('other').value)||0;
  const isSaudi=document.getElementById('nationality').value==='saudi';
  const gross=basic+housing+transport+other;
  const gosiBase=Math.min(basic+housing,45000);
  const gosi=isSaudi?gosiBase*0.0975:0;
  const net=gross-gosi;
  document.getElementById('r_basic').textContent=fmt(basic);
  document.getElementById('r_housing').textContent=fmt(housing);
  document.getElementById('r_transport').textContent=fmt(transport);
  document.getElementById('r_other').textContent=fmt(other);
  document.getElementById('r_gross').textContent=fmt(gross);
  document.getElementById('r_gosi').textContent=isSaudi?'-'+fmt(gosi):'SAR 0.00 (غیر ملکی - کٹوتی نہیں)';
  document.getElementById('r_net').textContent=fmt(net);
  const r=document.getElementById('salResult');
  r.classList.add('show');r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/salary-calculator.html","w",encoding="utf-8") as f: f.write(p1)
print("✓ ur/salary-calculator.html")

# ============================================================
# PAGE 2: Urdu GOSI Calculator
# ============================================================
p2 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>گوسی کیلکولیٹر سعودی عرب 2026 — GOSI حساب اردو میں</title>
  <meta name="description" content="سعودی عرب میں گوسی کا حساب اردو میں لگائیں۔ ملازم 9.75% اور آجر 11.75% کٹوتی۔ زیادہ سے زیادہ حد 45,000 ریال۔ پاکستانی ملازمین کے لیے مکمل گائیڈ 2026۔">
  <meta name="keywords" content="گوسی کیلکولیٹر, GOSI calculator urdu, سعودی گوسی حساب, گوسی کٹوتی سعودی عرب, پاکستانی گوسی سعودی">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/gosi-calculator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/gosi-calculator.html">
  <meta property="og:title" content="گوسی کیلکولیٹر سعودی عرب 2026 اردو">
  <meta property="og:description" content="گوسی کی کٹوتی کا فوری حساب — 9.75% ملازم، 11.75% آجر، 45,000 ریال حد۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/gosi-calculator.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/gosi-calculator.html">
  <link rel="alternate" hreflang="ar" href="https://www.saudiutilityhub.com/ar/gosi-calculator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/gosi-calculator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"گوسی کیلکولیٹر","url":"https://www.saudiutilityhub.com/ur/gosi-calculator.html","description":"سعودی گوسی کٹوتی کا حساب اردو میں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{UR_NAV_CSS}
    .gosi-table{{width:100%;border-collapse:collapse;font-size:.88rem;margin-top:14px}}
    .gosi-table th{{background:#1a56db;color:#fff;padding:10px 12px;text-align:right}}
    .gosi-table td{{padding:9px 12px;border-bottom:1px solid #e2e8f0}}
    .gosi-table tr:hover td{{background:#f8fafc}}
  </style>
</head>
<body>
{make_nav("https://www.saudiutilityhub.com/gosi-calculator.html","https://www.saudiutilityhub.com/ar/gosi-calculator.html")}
<section class="hero">
  <h1>🏛️ گوسی کیلکولیٹر — سعودی عرب 2026</h1>
  <p>گوسی کٹوتی کا فوری حساب اردو میں — ملازم اور آجر دونوں کی رقم معلوم کریں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span><span>📅 2026 شرحیں</span><span>⚡ فوری نتیجہ</span>
  </div>
</section>
<main>
  <div class="info-box">
    <strong>پاکستانی ملازمین:</strong> آپ پر گوسی لاگو نہیں ہوتی۔ گوسی صرف سعودی شہری ملازمین سے کاٹی جاتی ہے۔ یہ کیلکولیٹر آپ کے سعودی ساتھیوں یا خود اگر آپ سعودی ہیں تو استعمال کریں۔
  </div>
  <div class="card">
    <h2>🧮 گوسی حساب</h2>
    <label>بنیادی تنخواہ (ریال)</label>
    <input type="number" id="gBasic" placeholder="مثلاً 5000" min="0">
    <label>رہائش الاؤنس (ریال)</label>
    <input type="number" id="gHousing" placeholder="مثلاً 2000" min="0">
    <label>ملازم کی قسم</label>
    <select id="gType">
      <option value="saudi">سعودی شہری</option>
      <option value="expat">غیر ملکی (گوسی نہیں)</option>
    </select>
    <button class="btn" onclick="calcGosi()">گوسی حساب لگائیں</button>
  </div>
  <div class="result-box" id="gosiResult">
    <h2 style="color:#166534;margin-bottom:14px">✅ گوسی کا حساب</h2>
    <div class="res-row"><span class="res-label">بنیادی تنخواہ + رہائش</span><span class="res-val" id="g_base"></span></div>
    <div class="res-row"><span class="res-label">گوسی کی بنیاد (زیادہ سے زیادہ 45,000)</span><span class="res-val" id="g_cap"></span></div>
    <div class="res-row"><span class="res-label">ملازم کی کٹوتی (9.75%)</span><span class="res-val" id="g_emp"></span></div>
    <div class="res-row"><span class="res-label">آجر کا حصہ (11.75%)</span><span class="res-val" id="g_er"></span></div>
    <div class="res-row"><span class="res-label">کل گوسی (21.5%)</span><span class="res-val" id="g_total"></span></div>
  </div>
  <div class="card">
    <h2>📊 گوسی شرحیں 2026</h2>
    <table class="gosi-table">
      <tr><th>قسم</th><th>شرح</th><th>حد</th></tr>
      <tr><td>ملازم کی کٹوتی</td><td><strong>9.75%</strong></td><td>45,000 ریال</td></tr>
      <tr><td>آجر کا حصہ</td><td><strong>11.75%</strong></td><td>45,000 ریال</td></tr>
      <tr><td>کل گوسی</td><td><strong>21.5%</strong></td><td>45,000 ریال</td></tr>
      <tr><td>غیر ملکی ملازم</td><td><strong>0%</strong></td><td>کوئی کٹوتی نہیں</td></tr>
    </table>
    <p style="margin-top:10px;font-size:.8rem;color:#6b7280">گوسی صرف بنیادی تنخواہ اور رہائش الاؤنس پر لاگو ہوتی ہے، دیگر الاؤنسز پر نہیں۔</p>
  </div>
  <div class="card">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>گوسی کس تنخواہ پر لاگو ہوتی ہے؟</summary><div class="faq-answer">گوسی صرف بنیادی تنخواہ اور رہائش الاؤنس کے مجموعے پر لاگو ہوتی ہے۔ ٹرانسپورٹ، کھانا یا دیگر الاؤنسز گوسی کی بنیاد میں شامل نہیں ہوتے۔</div></details>
    <details><summary>اگر تنخواہ 45,000 ریال سے زیادہ ہو تو؟</summary><div class="faq-answer">گوسی کی زیادہ سے زیادہ حد 45,000 ریال ہے۔ اگر بنیادی تنخواہ اور رہائش الاؤنس مل کر 45,000 سے زیادہ ہوں تو گوسی صرف 45,000 پر ہی لگے گی۔</div></details>
    <details><summary>غیر ملکی ملازم کو گوسی واپس ملتی ہے؟</summary><div class="faq-answer">نہیں، غیر ملکی ملازمین گوسی نہیں دیتے اس لیے واپسی کا سوال نہیں۔ صرف سعودی شہری گوسی میں حصہ لیتے ہیں اور ریٹائرمنٹ پر فائدہ اٹھاتے ہیں۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
function fmt(n){{return 'SAR '+n.toLocaleString('en-US',{{minimumFractionDigits:2}});}}
function calcGosi(){{
  const basic=parseFloat(document.getElementById('gBasic').value)||0;
  const housing=parseFloat(document.getElementById('gHousing').value)||0;
  const isSaudi=document.getElementById('gType').value==='saudi';
  const rawBase=basic+housing;
  const gosiBase=Math.min(rawBase,45000);
  const empAmt=isSaudi?gosiBase*0.0975:0;
  const erAmt=isSaudi?gosiBase*0.1175:0;
  const total=empAmt+erAmt;
  document.getElementById('g_base').textContent=fmt(rawBase);
  document.getElementById('g_cap').textContent=fmt(gosiBase);
  document.getElementById('g_emp').textContent=isSaudi?fmt(empAmt):'SAR 0 (غیر ملکی)';
  document.getElementById('g_er').textContent=isSaudi?fmt(erAmt):'SAR 0 (غیر ملکی)';
  document.getElementById('g_total').textContent=isSaudi?fmt(total):'SAR 0 (غیر ملکی)';
  const r=document.getElementById('gosiResult');
  r.classList.add('show');r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/gosi-calculator.html","w",encoding="utf-8") as f: f.write(p2)
print("✓ ur/gosi-calculator.html")

# ============================================================
# PAGE 3: Urdu EOS Calculator
# ============================================================
p3 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>آخری سروس گریجویٹی کیلکولیٹر سعودی عرب 2026 — مکافأة نهاية الخدمة اردو</title>
  <meta name="description" content="سعودی عرب میں آخری سروس گریجویٹی کا حساب اردو میں لگائیں۔ آرٹیکل 84 فارمولا، استعفیٰ اور برطرفی دونوں صورتوں کا حساب۔ پاکستانی ملازمین کے لیے 2026۔">
  <meta name="keywords" content="آخری سروس گریجویٹی سعودی عرب, EOS calculator urdu, مکافأة نهاية الخدمة, پاکستانی ملازم گریجویٹی, سعودی عرب نوکری چھوڑنا حساب">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/eos-calculator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/eos-calculator.html">
  <meta property="og:title" content="آخری سروس گریجویٹی کیلکولیٹر 2026 اردو">
  <meta property="og:description" content="سعودی عرب میں آخری سروس کا حساب — استعفیٰ یا برطرفی، سال 1 سے 20 تک کا فارمولا۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/eos-calculator.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">
  <link rel="alternate" hreflang="ar" href="https://www.saudiutilityhub.com/ar/eos-calculator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"آخری سروس گریجویٹی کیلکولیٹر","url":"https://www.saudiutilityhub.com/ur/eos-calculator.html","description":"سعودی عرب آخری سروس گریجویٹی کا حساب اردو میں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{UR_NAV_CSS}</style>
</head>
<body>
{make_nav("https://www.saudiutilityhub.com/ksa-eos-calculator.html","https://www.saudiutilityhub.com/ar/eos-calculator.html")}
<section class="hero">
  <h1>🤝 آخری سروس گریجویٹی کیلکولیٹر 2026</h1>
  <p>سعودی لیبر لاء آرٹیکل 84 کے مطابق اپنی گریجویٹی کا صحیح حساب لگائیں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span><span>📅 2026 قانون</span><span>⚡ فوری نتیجہ</span>
  </div>
</section>
<main>
  <div class="info-box">
    <strong>اہم:</strong> گریجویٹی صرف بنیادی تنخواہ پر حساب ہوتی ہے، رہائش یا ٹرانسپورٹ الاؤنس پر نہیں۔ 2 سال سے کم ملازمت میں استعفیٰ دینے پر گریجویٹی نہیں ملتی۔
  </div>
  <div class="card">
    <h2>🧮 گریجویٹی حساب</h2>
    <label>بنیادی آخری تنخواہ (ریال) — صرف بنیادی، الاؤنس نہیں</label>
    <input type="number" id="eosSalary" placeholder="مثلاً 3000" min="0">
    <label>ملازمت کے سال</label>
    <input type="number" id="eosYears" placeholder="مثلاً 5" min="0" max="50" step="0.5">
    <label>جانے کی وجہ</label>
    <select id="eosReason">
      <option value="termination">برطرفی (آجر نے نکالا)</option>
      <option value="resignation">استعفیٰ (خود چھوڑا)</option>
      <option value="contract">معاہدہ ختم ہوا</option>
    </select>
    <button class="btn" onclick="calcEOS()">گریجویٹی حساب لگائیں</button>
  </div>
  <div class="result-box" id="eosResult">
    <h2 style="color:#166534;margin-bottom:14px">✅ آپ کی گریجویٹی</h2>
    <div class="res-row"><span class="res-label">بنیادی تنخواہ</span><span class="res-val" id="e_sal"></span></div>
    <div class="res-row"><span class="res-label">ملازمت کے سال</span><span class="res-val" id="e_yrs"></span></div>
    <div class="res-row"><span class="res-label">پہلے 5 سال کی گریجویٹی</span><span class="res-val" id="e_first"></span></div>
    <div class="res-row"><span class="res-label">5 سال کے بعد کی گریجویٹی</span><span class="res-val" id="e_after"></span></div>
    <div class="res-row"><span class="res-label">💰 کل گریجویٹی</span><span class="res-val" id="e_total"></span></div>
    <div id="e_note" style="margin-top:10px;font-size:.85rem;color:#92400e;background:#fef3c7;padding:10px;border-radius:6px"></div>
  </div>
  <div class="card">
    <h2>📋 گریجویٹی فارمولا — آرٹیکل 84</h2>
    <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:14px;font-size:.88rem;line-height:2">
      <strong>پہلے 5 سال:</strong> ہر سال کے لیے آدھی ماہانہ تنخواہ<br>
      <strong>5 سال کے بعد:</strong> ہر سال کے لیے پوری ماہانہ تنخواہ<br>
      <strong>برطرفی:</strong> مکمل گریجویٹی ملتی ہے<br>
      <strong>استعفیٰ (2-5 سال):</strong> ایک تہائی گریجویٹی<br>
      <strong>استعفیٰ (5-10 سال):</strong> دو تہائی گریجویٹی<br>
      <strong>استعفیٰ (10+ سال):</strong> مکمل گریجویٹی
    </div>
  </div>
  <div class="card">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>کیا استعفیٰ دینے پر گریجویٹی ملتی ہے؟</summary><div class="faq-answer">ہاں، لیکن شرائط کے ساتھ۔ 2 سال سے کم: کوئی گریجویٹی نہیں۔ 2-5 سال: ایک تہائی۔ 5-10 سال: دو تہائی۔ 10 سال سے زیادہ: مکمل گریجویٹی۔</div></details>
    <details><summary>گریجویٹی کا حساب کس تنخواہ سے ہوتا ہے؟</summary><div class="faq-answer">صرف بنیادی تنخواہ (Basic Salary) سے۔ رہائش، ٹرانسپورٹ یا کسی بھی قسم کا الاؤنس گریجویٹی میں شامل نہیں ہوتا۔</div></details>
    <details><summary>آجر گریجویٹی نہ دے تو کیا کریں؟</summary><div class="faq-answer">پہلے کمپنی HR سے بات کریں۔ اگر بات نہ بنے تو MHRSD (وزارت محنت) کی ویب سائٹ musaned.com.sa یا qiwa.sa پر شکایت درج کریں۔ یہ آپ کا قانونی حق ہے۔</div></details>
    <details><summary>معاہدہ ختم ہونے پر مکمل گریجویٹی ملتی ہے؟</summary><div class="faq-answer">ہاں۔ اگر آجر معاہدہ تجدید نہ کرے تو یہ برطرفی کے برابر ہے اور آپ کو مکمل گریجویٹی ملنی چاہیے۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
function fmt(n){{return 'SAR '+n.toLocaleString('en-US',{{minimumFractionDigits:2}});}}
function calcEOS(){{
  const sal=parseFloat(document.getElementById('eosSalary').value)||0;
  const yrs=parseFloat(document.getElementById('eosYears').value)||0;
  const reason=document.getElementById('eosReason').value;
  if(sal<=0||yrs<=0){{alert('براہ کرم تنخواہ اور سال درج کریں');return;}}
  const first5=Math.min(yrs,5)*(sal/2);
  const after5=yrs>5?(yrs-5)*sal:0;
  const rawTotal=first5+after5;
  let multiplier=1;
  let note='';
  if(reason==='resignation'){{
    if(yrs<2){{multiplier=0;note='2 سال سے کم ملازمت میں استعفیٰ دینے پر گریجویٹی نہیں ملتی۔';}}
    else if(yrs<5){{multiplier=1/3;note='2-5 سال استعفیٰ: صرف ایک تہائی گریجویٹی ملتی ہے۔';}}
    else if(yrs<10){{multiplier=2/3;note='5-10 سال استعفیٰ: دو تہائی گریجویٹی ملتی ہے۔';}}
    else{{note='10 سال سے زیادہ استعفیٰ: مکمل گریجویٹی ملتی ہے۔';}}
  }}
  const finalTotal=rawTotal*multiplier;
  document.getElementById('e_sal').textContent=fmt(sal);
  document.getElementById('e_yrs').textContent=yrs+' سال';
  document.getElementById('e_first').textContent=fmt(first5*multiplier);
  document.getElementById('e_after').textContent=fmt(after5*multiplier);
  document.getElementById('e_total').textContent=fmt(finalTotal);
  document.getElementById('e_note').textContent=note;
  const r=document.getElementById('eosResult');
  r.classList.add('show');r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/eos-calculator.html","w",encoding="utf-8") as f: f.write(p3)
print("✓ ur/eos-calculator.html")
print("Batch 1 complete.")
