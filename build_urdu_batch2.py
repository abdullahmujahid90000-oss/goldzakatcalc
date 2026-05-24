#!/usr/bin/env python3
"""Build Urdu pages 4-6: Iqama Tracker, Salary Slip, NOC Letter"""

OUT = "/sessions/clever-inspiring-albattani/mnt/outputs/ur"
import os
os.makedirs(OUT, exist_ok=True)

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
    .hero-badges{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;font-size:.82rem}
    .hero-badges span{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.3);padding:4px 12px;border-radius:20px}
    main{max-width:920px;margin:0 auto;padding:28px 16px 48px}
    .card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:22px 24px;margin-bottom:20px}
    h2{font-size:1.15rem;font-weight:700;color:#1a202c;margin-bottom:14px}
    label{display:block;font-size:.88rem;font-weight:600;color:#374151;margin-bottom:4px;margin-top:12px}
    input,select,textarea{width:100%;padding:10px 12px;border:1px solid #d1d5db;border-radius:8px;font-size:.95rem;font-family:inherit;background:#fff;color:#1a202c;direction:rtl}
    input[type=date]{direction:ltr;text-align:right}
    input:focus,select:focus{outline:none;border-color:#1a56db;box-shadow:0 0 0 3px rgba(26,86,219,.1)}
    .btn{display:inline-block;padding:11px 28px;background:#1a56db;color:#fff;border:none;border-radius:8px;font-size:1rem;font-weight:700;cursor:pointer;margin-top:14px;width:100%;font-family:inherit}
    .btn:hover{background:#1e40af}
    .btn-green{background:#059669}.btn-green:hover{background:#047857}
    .result-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;padding:20px;margin-top:18px;display:none}
    .result-box.show{display:block}
    .res-row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #dcfce7;font-size:.92rem}
    .res-row:last-child{border:none;font-weight:700;font-size:1.05rem;color:#166534}
    .res-label{color:#374151}
    .res-val{font-weight:700;color:#1a56db;font-family:'Segoe UI',sans-serif}
    .res-row:last-child .res-val{color:#166534}
    .info-box{background:#eff6ff;border-right:4px solid #1a56db;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:.88rem;color:#1e40af;border-left:none}
    .warn-box{background:#fefce8;border-right:4px solid #ca8a04;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:.88rem;border-left:none}
    .danger-box{background:#fee2e2;border-right:4px solid #dc2626;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:.88rem;border-left:none}
    details{border:1px solid #e2e8f0;border-radius:10px;margin-bottom:8px;background:#fff}
    summary{padding:13px 16px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;font-size:.92rem}
    summary::-webkit-details-marker{display:none}
    summary::before{content:'+';font-size:1.2rem;color:#1a56db;margin-left:8px}
    details[open] summary::before{content:'−'}
    .faq-answer{padding:0 16px 12px;font-size:.88rem;color:#374151;line-height:1.8}
    .doc-preview{background:#fff;border:2px solid #e2e8f0;border-radius:8px;padding:24px 28px;font-size:.88rem;line-height:2;margin-top:14px;white-space:pre-wrap;font-family:'Courier New',monospace;direction:ltr;text-align:left}
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
    @media print{nav,.hero,footer,#ck,.btn,.btn-green{display:none!important}.doc-preview{border:1px solid #999}}
"""

UR_FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>تنخواہ کے اوزار</h4>
        <a href="https://www.saudiutilityhub.com/ur/salary-calculator.html">تنخواہ کیلکولیٹر</a>
        <a href="https://www.saudiutilityhub.com/ur/gosi-calculator.html">گوسی کیلکولیٹر</a>
        <a href="https://www.saudiutilityhub.com/ur/eos-calculator.html">آخری سروس</a>
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

def nav(en, ar):
    return f"""<nav>
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
      <a href="{en}">EN</a>
      <a href="{ar}">عربي</a>
      <a href="#" class="active-lang">اردو</a>
    </div>
  </div>
</nav>"""

# ============================================================
# PAGE 4: Iqama Tracker
# ============================================================
p4 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>اقامہ میعاد ختم ہونے کا کیلکولیٹر 2026 — سعودی اقامہ تجدید فیس اردو</title>
  <meta name="description" content="اپنے اقامہ کی میعاد ختم ہونے میں کتنے دن باقی ہیں معلوم کریں۔ تجدید فیس 650 ریال، تاخیر جرمانہ 500 ریال ماہانہ۔ پاکستانی ملازمین کے لیے اردو میں۔">
  <meta name="keywords" content="اقامہ میعاد کیلکولیٹر, اقامہ تجدید فیس, اقامہ ختم ہونا سعودی, iqama expiry urdu, پاکستانی اقامہ سعودی عرب 2026">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/iqama-calculator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/iqama-calculator.html">
  <meta property="og:title" content="اقامہ میعاد کیلکولیٹر سعودی عرب 2026 اردو">
  <meta property="og:description" content="اقامہ ختم ہونے کے دن، تجدید فیس اور تاخیر جرمانہ معلوم کریں۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/iqama-calculator.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">
  <link rel="alternate" hreflang="ar" href="https://www.saudiutilityhub.com/ar/iqama-calculator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"اقامہ میعاد کیلکولیٹر","url":"https://www.saudiutilityhub.com/ur/iqama-calculator.html","description":"سعودی اقامہ میعاد اور تجدید فیس کا حساب اردو میں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{UR_NAV_CSS}
    .days-big{{font-size:3rem;font-weight:800;text-align:center;padding:20px;border-radius:10px;margin:14px 0}}
    .days-safe{{background:#dcfce7;color:#166534}}
    .days-warn{{background:#fef3c7;color:#92400e}}
    .days-danger{{background:#fee2e2;color:#991b1b}}
  </style>
</head>
<body>
{nav("https://www.saudiutilityhub.com/iqama-expiry-calculator.html","https://www.saudiutilityhub.com/ar/iqama-calculator.html")}
<section class="hero">
  <h1>🪪 اقامہ میعاد کیلکولیٹر 2026</h1>
  <p>اقامہ ختم ہونے میں کتنے دن باقی ہیں — تجدید فیس اور تاخیر جرمانہ معلوم کریں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span><span>📅 2026 شرحیں</span><span>⚡ فوری نتیجہ</span>
  </div>
</section>
<main>
  <div class="warn-box">⚠️ اقامہ میعاد ختم ہونے کے بعد ہر مہینے <strong>500 ریال جرمانہ</strong> لگتا ہے۔ بروقت تجدید کریں۔</div>
  <div class="card">
    <h2>📅 اقامہ کی تاریخ درج کریں</h2>
    <label>اقامہ ختم ہونے کی تاریخ (ہجری تاریخ کو پہلے میلادی میں بدلیں)</label>
    <input type="date" id="iqDate">
    <label>کیا اقامہ پہلے سے ختم ہو چکا ہے؟</label>
    <select id="expired">
      <option value="no">نہیں — ابھی باقی ہے</option>
      <option value="yes">ہاں — میعاد گزر چکی ہے</option>
    </select>
    <div id="expiredDiv" style="display:none">
      <label>کتنے مہینے گزر چکے ہیں؟</label>
      <input type="number" id="expMonths" min="1" max="60" placeholder="مثلاً 3">
    </div>
    <button class="btn" onclick="calcIqama()">حساب لگائیں</button>
  </div>
  <div class="result-box" id="iqResult">
    <div id="iq_days_box"></div>
    <div class="res-row"><span class="res-label">تجدید فیس (سالانہ)</span><span class="res-val">SAR 650</span></div>
    <div class="res-row"><span class="res-label">تاخیر جرمانہ (اگر لاگو)</span><span class="res-val" id="iq_fine"></span></div>
    <div class="res-row"><span class="res-label">💰 کل ادائیگی</span><span class="res-val" id="iq_total"></span></div>
    <div id="iq_advice" style="margin-top:12px;font-size:.87rem;padding:12px;border-radius:8px"></div>
  </div>
  <div class="card">
    <h2>📋 اقامہ تجدید کا طریقہ — Absher</h2>
    <div style="font-size:.88rem;line-height:2.2">
      <strong>مرحلہ 1:</strong> absher.sa پر لاگ ان کریں<br>
      <strong>مرحلہ 2:</strong> "خدمات" میں "اقامہ تجدید" منتخب کریں<br>
      <strong>مرحلہ 3:</strong> 650 ریال ادا کریں (کریڈٹ/ڈیبٹ کارڈ)<br>
      <strong>مرحلہ 4:</strong> تجدید شدہ اقامہ 3-7 دن میں مل جائے گا<br>
      <strong>نوٹ:</strong> تجدید عام طور پر آجر کرتا ہے، خود بھی کر سکتے ہیں
    </div>
  </div>
  <div class="card">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>اقامہ ختم ہونے پر کتنا جرمانہ ہے؟</summary><div class="faq-answer">500 ریال فی مہینہ جرمانہ ہے۔ اگر 3 مہینے تاخیر ہو تو 1,500 ریال جرمانہ + 650 ریال تجدید فیس = 2,150 ریال ادا کرنے ہوں گے۔</div></details>
    <details><summary>کیا میں خود اقامہ تجدید کر سکتا ہوں؟</summary><div class="faq-answer">ہاں، Absher پر آجر کی اجازت سے تجدید ہو سکتی ہے۔ لیکن فیس عام طور پر آجر ادا کرتا ہے۔ اگر آجر نہ کرے تو MHRSD سے مدد لی جا سکتی ہے۔</div></details>
    <details><summary>اقامہ ختم ہو تو سعودی عرب سے نکل سکتے ہیں؟</summary><div class="faq-answer">ہاں، لیکن واپسی پر مسائل ہو سکتے ہیں۔ ایئرپورٹ پر جرمانہ ادا کرنا پڑ سکتا ہے۔ نکلنے سے پہلے آجر سے بات کریں۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
document.getElementById('expired').addEventListener('change',function(){{
  document.getElementById('expiredDiv').style.display=this.value==='yes'?'block':'none';
}});
function calcIqama(){{
  const dateVal=document.getElementById('iqDate').value;
  const isExpired=document.getElementById('expired').value==='yes';
  const expMonths=parseInt(document.getElementById('expMonths').value)||0;
  let daysLeft=0,fine=0;
  if(!isExpired){{
    if(!dateVal){{alert('براہ کرم تاریخ درج کریں');return;}}
    const exp=new Date(dateVal);const now=new Date();
    daysLeft=Math.round((exp-now)/(1000*60*60*24));
    fine=0;
  }}else{{
    daysLeft=-(expMonths*30);
    fine=expMonths*500;
  }}
  const renewal=650;const total=renewal+fine;
  let daysBox='',daysClass='',advice='',advStyle='';
  if(daysLeft>90){{daysClass='days-safe';daysBox=daysLeft+' دن باقی';advice='✅ آپ کا اقامہ محفوظ ہے۔ 90 دن سے پہلے تجدید کا منصوبہ بنائیں۔';advStyle='background:#dcfce7;color:#166534;';}}
  else if(daysLeft>30){{daysClass='days-warn';daysBox=daysLeft+' دن باقی';advice='⚠️ جلد تجدید کروائیں — 30 دن سے کم رہ گئے ہیں۔';advStyle='background:#fef3c7;color:#92400e;';}}
  else if(daysLeft>0){{daysClass='days-danger';daysBox=daysLeft+' دن باقی — فوری تجدید!';advice='🚨 بہت کم وقت باقی ہے۔ آج ہی آجر سے بات کریں۔';advStyle='background:#fee2e2;color:#991b1b;';}}
  else{{daysClass='days-danger';daysBox='میعاد ختم — '+(expMonths||0)+' مہینے گزر گئے';advice='🚨 آپ کا اقامہ ختم ہو چکا ہے۔ فوری طور پر آجر سے یا MHRSD سے رابطہ کریں۔';advStyle='background:#fee2e2;color:#991b1b;';}}
  document.getElementById('iq_days_box').innerHTML=`<div class="days-big ${{daysClass}}">${{daysBox}}</div>`;
  document.getElementById('iq_fine').textContent=fine>0?'SAR '+fine.toLocaleString():'کوئی جرمانہ نہیں';
  document.getElementById('iq_total').textContent='SAR '+total.toLocaleString();
  document.getElementById('iq_advice').innerHTML=advice;
  document.getElementById('iq_advice').style.cssText=advStyle+'padding:12px;border-radius:8px;';
  const r=document.getElementById('iqResult');r.classList.add('show');r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/iqama-calculator.html","w",encoding="utf-8") as f: f.write(p4)
print("✓ ur/iqama-calculator.html")

# ============================================================
# PAGE 5: Salary Slip Generator (Urdu)
# ============================================================
p5 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>تنخواہ سلپ بنانے کا آلہ سعودی عرب 2026 — مفت پرنٹ ایبل پے سلپ اردو</title>
  <meta name="description" content="سعودی عرب کے لیے مفت تنخواہ سلپ بنائیں۔ گوسی، الاؤنسز اور تمام کٹوتیاں شامل۔ پرنٹ کریں یا PDF بنائیں۔ پاکستانی ملازمین کے لیے اردو میں 2026۔">
  <meta name="keywords" content="تنخواہ سلپ سعودی عرب, salary slip urdu, پے سلپ پاکستانی, تنخواہ رسید سعودی, payslip generator urdu saudi">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/salary-slip.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/salary-slip.html">
  <meta property="og:title" content="تنخواہ سلپ بنانے کا آلہ 2026 اردو">
  <meta property="og:description" content="مفت تنخواہ سلپ بنائیں — گوسی، الاؤنسز، پرنٹ ایبل۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/salary-slip.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/salary-slip-generator.html">
  <link rel="alternate" hreflang="ar" href="https://www.saudiutilityhub.com/ar/salary-slip-generator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/salary-slip-generator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"تنخواہ سلپ جنریٹر","url":"https://www.saudiutilityhub.com/ur/salary-slip.html","description":"سعودی عرب کے لیے تنخواہ سلپ بنائیں اردو میں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{UR_NAV_CSS}
    #slip{{background:#fff;border:2px solid #1a56db;border-radius:10px;padding:24px 28px;margin-top:16px;direction:ltr;text-align:left;font-family:'Segoe UI',Arial,sans-serif;font-size:.88rem;display:none}}
    #slip.show{{display:block}}
    .slip-header{{text-align:center;border-bottom:2px solid #1a56db;padding-bottom:12px;margin-bottom:14px}}
    .slip-co{{font-size:1.1rem;font-weight:700;color:#1a56db}}
    .slip-title{{font-size:.85rem;color:#6b7280;margin-top:2px}}
    .slip-grid{{display:grid;grid-template-columns:1fr 1fr;gap:6px 24px;margin-bottom:14px;font-size:.82rem}}
    .slip-grid span{{color:#6b7280}}
    .slip-grid strong{{color:#1a202c}}
    .slip-table{{width:100%;border-collapse:collapse;margin-bottom:12px}}
    .slip-table th{{background:#f1f5f9;padding:8px 10px;font-size:.8rem;text-align:left;border-bottom:2px solid #e2e8f0}}
    .slip-table td{{padding:7px 10px;border-bottom:1px solid #f1f5f9;font-size:.82rem}}
    .slip-total{{background:#1a56db;color:#fff;font-weight:700}}
    .slip-total td{{padding:10px}}
  </style>
</head>
<body>
{nav("https://www.saudiutilityhub.com/salary-slip-generator.html","https://www.saudiutilityhub.com/ar/salary-slip-generator.html")}
<section class="hero">
  <h1>🧾 تنخواہ سلپ بنانے کا آلہ 2026</h1>
  <p>اپنی یا ملازم کی تنخواہ سلپ مفت بنائیں — پرنٹ کریں یا PDF محفوظ کریں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span><span>🖨️ پرنٹ ایبل</span><span>⚡ فوری</span>
  </div>
</section>
<main>
  <div class="card">
    <h2>🏢 کمپنی کی تفصیل</h2>
    <label>کمپنی کا نام</label>
    <input type="text" id="co" placeholder="مثلاً Al Madar Trading Co.">
    <label>مہینہ اور سال</label>
    <input type="month" id="slipMonth" style="direction:ltr">
  </div>
  <div class="card">
    <h2>👤 ملازم کی تفصیل</h2>
    <label>ملازم کا نام</label>
    <input type="text" id="empN" placeholder="مثلاً Muhammad Ahmed">
    <label>عہدہ</label>
    <input type="text" id="empJ" placeholder="مثلاً Accountant">
    <label>اقامہ نمبر</label>
    <input type="text" id="empIq" placeholder="مثلاً 2012345678">
    <label>قومیت</label>
    <select id="empNat">
      <option value="expat">غیر ملکی (پاکستانی، ہندوستانی وغیرہ)</option>
      <option value="saudi">سعودی شہری</option>
    </select>
  </div>
  <div class="card">
    <h2>💰 تنخواہ کی تفصیل (ریال)</h2>
    <label>بنیادی تنخواہ</label>
    <input type="number" id="sBasic" placeholder="مثلاً 3000" min="0">
    <label>رہائش الاؤنس</label>
    <input type="number" id="sHousing" placeholder="مثلاً 1000" min="0">
    <label>ٹرانسپورٹ الاؤنس</label>
    <input type="number" id="sTransport" placeholder="مثلاً 500" min="0">
    <label>دیگر الاؤنسز</label>
    <input type="number" id="sOther" placeholder="مثلاً 0" min="0">
    <label>دیگر کٹوتیاں (اگر کوئی ہو)</label>
    <input type="number" id="sDeduct" placeholder="مثلاً 0" min="0">
    <button class="btn" onclick="genSlip()">تنخواہ سلپ بنائیں</button>
  </div>

  <div id="slip">
    <div class="slip-header">
      <div class="slip-co" id="s_co"></div>
      <div class="slip-title">SALARY SLIP / تنخواہ سلپ — <span id="s_month"></span></div>
    </div>
    <div class="slip-grid">
      <div><span>Employee: </span><strong id="s_emp"></strong></div>
      <div><span>Iqama No: </span><strong id="s_iq"></strong></div>
      <div><span>Designation: </span><strong id="s_job"></strong></div>
      <div><span>Nationality: </span><strong id="s_nat"></strong></div>
    </div>
    <table class="slip-table">
      <tr><th>Earnings / آمدنی</th><th>Amount (SAR)</th><th>Deductions / کٹوتیاں</th><th>Amount (SAR)</th></tr>
      <tr><td>Basic Salary</td><td id="s_basic"></td><td>GOSI (9.75%)</td><td id="s_gosi"></td></tr>
      <tr><td>Housing Allowance</td><td id="s_hs"></td><td>Other Deductions</td><td id="s_od"></td></tr>
      <tr><td>Transport Allowance</td><td id="s_tr"></td><td></td><td></td></tr>
      <tr><td>Other Allowances</td><td id="s_ot"></td><td></td><td></td></tr>
      <tr class="slip-total"><td><strong>GROSS SALARY</strong></td><td id="s_gross"></td><td><strong>TOTAL DEDUCTIONS</strong></td><td id="s_totded"></td></tr>
    </table>
    <div style="background:#1a56db;color:#fff;padding:12px 14px;border-radius:8px;text-align:center;font-size:1.1rem;font-weight:700">
      NET PAY / نیٹ تنخواہ: SAR <span id="s_net"></span>
    </div>
    <div style="margin-top:16px;font-size:.78rem;color:#6b7280;text-align:center">
      This is a computer-generated salary slip. Verify details with HR. | یہ کمپیوٹر سے بنی تنخواہ سلپ ہے۔
    </div>
  </div>
  <button class="btn btn-green" id="printBtn" style="display:none;margin-top:12px" onclick="window.print()">🖨️ پرنٹ کریں</button>

  <div class="card" style="margin-top:20px">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>تنخواہ سلپ کس لیے ضروری ہے؟</summary><div class="faq-answer">بینک اکاؤنٹ کھولنے، قرضہ لینے، ویزہ درخواست، گھر کرائے پر لینے اور بعض اوقات فیملی ویزہ کے لیے تنخواہ سلپ مانگی جاتی ہے۔</div></details>
    <details><summary>پاکستانی ملازم کی تنخواہ سے کیا کٹتا ہے؟</summary><div class="faq-answer">کچھ نہیں — پاکستانی اور تمام غیر ملکی ملازمین کی تنخواہ سے نہ گوسی کٹتی ہے نہ انکم ٹیکس۔ آپ کو مکمل گراس تنخواہ ملتی ہے۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
function fmt2(n){{return parseFloat(n||0).toFixed(2);}}
function genSlip(){{
  const co=document.getElementById('co').value||'Company Name';
  const mo=document.getElementById('slipMonth').value;
  const empN=document.getElementById('empN').value||'Employee Name';
  const empJ=document.getElementById('empJ').value||'Designation';
  const empIq=document.getElementById('empIq').value||'—';
  const isSaudi=document.getElementById('empNat').value==='saudi';
  const basic=parseFloat(document.getElementById('sBasic').value)||0;
  const housing=parseFloat(document.getElementById('sHousing').value)||0;
  const transport=parseFloat(document.getElementById('sTransport').value)||0;
  const other=parseFloat(document.getElementById('sOther').value)||0;
  const otherDed=parseFloat(document.getElementById('sDeduct').value)||0;
  const gross=basic+housing+transport+other;
  const gosiBase=Math.min(basic+housing,45000);
  const gosi=isSaudi?gosiBase*0.0975:0;
  const totalDed=gosi+otherDed;
  const net=gross-totalDed;
  document.getElementById('s_co').textContent=co;
  document.getElementById('s_month').textContent=mo;
  document.getElementById('s_emp').textContent=empN;
  document.getElementById('s_iq').textContent=empIq;
  document.getElementById('s_job').textContent=empJ;
  document.getElementById('s_nat').textContent=isSaudi?'Saudi':'Non-Saudi (Expat)';
  document.getElementById('s_basic').textContent=fmt2(basic);
  document.getElementById('s_hs').textContent=fmt2(housing);
  document.getElementById('s_tr').textContent=fmt2(transport);
  document.getElementById('s_ot').textContent=fmt2(other);
  document.getElementById('s_gosi').textContent=fmt2(gosi);
  document.getElementById('s_od').textContent=fmt2(otherDed);
  document.getElementById('s_gross').textContent=fmt2(gross);
  document.getElementById('s_totded').textContent=fmt2(totalDed);
  document.getElementById('s_net').textContent=fmt2(net);
  document.getElementById('slip').classList.add('show');
  document.getElementById('printBtn').style.display='block';
  document.getElementById('slip').scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/salary-slip.html","w",encoding="utf-8") as f: f.write(p5)
print("✓ ur/salary-slip.html")

# ============================================================
# PAGE 6: NOC Letter Generator (Urdu)
# ============================================================
p6 = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>این او سی لیٹر بنانے کا آلہ سعودی عرب 2026 — مفت NOC خط اردو</title>
  <meta name="description" content="سعودی عرب کے لیے مفت این او سی لیٹر بنائیں۔ ویزہ درخواست، بینک، اقامہ ٹرانسفر اور سفر کے لیے۔ پرنٹ ایبل NOC سرٹیفکیٹ اردو میں 2026۔">
  <meta name="keywords" content="این او سی لیٹر سعودی عرب, NOC letter urdu saudi, no objection certificate urdu, این او سی سرٹیفکیٹ پاکستانی, اقامہ ٹرانسفر این او سی">
  <link rel="canonical" href="https://www.saudiutilityhub.com/ur/noc-letter.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/ur/noc-letter.html">
  <meta property="og:title" content="این او سی لیٹر جنریٹر سعودی عرب 2026 اردو">
  <meta property="og:description" content="مفت NOC لیٹر بنائیں — ویزہ، بینک، اقامہ ٹرانسفر، سفر۔ فوری پرنٹ ایبل۔">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="ur" href="https://www.saudiutilityhub.com/ur/noc-letter.html">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"این او سی لیٹر جنریٹر","url":"https://www.saudiutilityhub.com/ur/noc-letter.html","description":"سعودی عرب کے لیے این او سی لیٹر اردو میں بنائیں","inLanguage":"ur","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{UR_NAV_CSS}</style>
</head>
<body>
{nav("https://www.saudiutilityhub.com/noc-letter-generator.html","#")}
<section class="hero">
  <h1>📋 این او سی لیٹر جنریٹر 2026</h1>
  <p>ویزہ، بینک، اقامہ ٹرانسفر یا سفر کے لیے مفت این او سی لیٹر بنائیں</p>
  <div class="hero-badges">
    <span>✅ بالکل مفت</span><span>🖨️ پرنٹ ایبل</span><span>⚡ فوری</span>
  </div>
</section>
<main>
  <div class="info-box">
    <strong>این او سی کیا ہے؟</strong> این او سی (عدم اعتراض سرٹیفکیٹ) آجر کا وہ خط ہے جس میں وہ کہتا ہے کہ اسے کوئی اعتراض نہیں کہ ملازم فلاں کام کرے۔ ویزہ، بینک اکاؤنٹ اور اقامہ ٹرانسفر کے لیے ضروری ہے۔
  </div>
  <div class="card">
    <h2>🏢 کمپنی کی تفصیل</h2>
    <label>کمپنی کا نام</label>
    <input type="text" id="nCo" placeholder="مثلاً Al Faisal Trading Company">
    <label>کمپنی کا پتہ</label>
    <input type="text" id="nAddr" placeholder="مثلاً King Fahd Road, Riyadh, Saudi Arabia">
    <label>دستخط کرنے والے کا نام</label>
    <input type="text" id="nSig" placeholder="مثلاً Mohammed Al-Rashidi">
    <label>عہدہ</label>
    <input type="text" id="nSigT" placeholder="مثلاً HR Manager">
  </div>
  <div class="card">
    <h2>👤 ملازم کی تفصیل</h2>
    <label>ملازم کا نام</label>
    <input type="text" id="nEmp" placeholder="مثلاً Ahmed Khan">
    <label>قومیت</label>
    <input type="text" id="nNat" placeholder="مثلاً Pakistani">
    <label>پاسپورٹ نمبر</label>
    <input type="text" id="nPP" placeholder="مثلاً AB1234567">
    <label>اقامہ نمبر</label>
    <input type="text" id="nIq" placeholder="مثلاً 2012345678">
    <label>عہدہ</label>
    <input type="text" id="nJob" placeholder="مثلاً Senior Accountant">
  </div>
  <div class="card">
    <h2>📄 این او سی کی وجہ</h2>
    <label>این او سی کس مقصد کے لیے چاہیے؟</label>
    <select id="nPurp">
      <option value="visa">فیملی / ٹورسٹ ویزہ درخواست</option>
      <option value="bank">بینک اکاؤنٹ / قرضہ درخواست</option>
      <option value="transfer">اقامہ ٹرانسفر / نئی نوکری</option>
      <option value="travel">خروج اعادہ ویزہ / سفر</option>
      <option value="property">مکان کرایہ / رہائش</option>
    </select>
    <label>خط کی تاریخ</label>
    <input type="date" id="nDate" style="direction:ltr">
    <button class="btn" onclick="genNOC()">این او سی لیٹر بنائیں</button>
  </div>
  <div class="result-box" id="nocResult">
    <h2 style="color:#166534;margin-bottom:10px">✅ این او سی لیٹر تیار ہے</h2>
    <div class="warn-box">کمپنی کے سرکاری لیٹر ہیڈ پر پرنٹ کریں، پھر مہر اور دستخط کروائیں۔</div>
    <div class="doc-preview" id="nocText"></div>
    <button class="btn btn-green" style="margin-top:12px" onclick="window.print()">🖨️ پرنٹ کریں</button>
    <button class="btn" style="margin-top:8px" onclick="navigator.clipboard.writeText(document.getElementById('nocText').textContent);alert('کاپی ہو گیا!')">📋 کاپی کریں</button>
  </div>
  <div class="card">
    <h2>❓ اکثر پوچھے جانے والے سوالات</h2>
    <details><summary>این او سی لیٹر کب ضروری ہے؟</summary><div class="faq-answer">فیملی ویزہ، ٹورسٹ ویزہ، بینک قرضہ، اقامہ ٹرانسفر، مکان کرائے، اور بیرون ملک ویزہ درخواست کے وقت این او سی ضروری ہوتا ہے۔</div></details>
    <details><summary>این او سی کتنے دن میں بنتی ہے؟</summary><div class="faq-answer">یہ آلہ فوری بناتا ہے۔ آجر سے اصل دستخط اور مہر لینے میں 1-3 دن لگ سکتے ہیں۔</div></details>
    <details><summary>کیا یہ این او سی قانونی طور پر قابل قبول ہے؟</summary><div class="faq-answer">یہ ٹیمپلیٹ ہے۔ قانونی قبولیت تب ہوگی جب آجر کی مہر اور اختیاری دستخط ہوں۔ بغیر مہر کے این او سی قابل قبول نہیں ہوتا۔</div></details>
  </div>
</main>
{UR_FOOTER}
<script>
document.getElementById('nDate').value=new Date().toISOString().split('T')[0];
const purposeMap={{
  visa:'apply for a family/tourist visa at the relevant embassy',
  bank:'open a bank account and apply for financial products',
  transfer:'transfer their Iqama sponsorship to a new employer',
  travel:'travel outside Saudi Arabia on an exit re-entry visa',
  property:'enter into a property rental agreement'
}};
function genNOC(){{
  const co=document.getElementById('nCo').value.trim();
  const addr=document.getElementById('nAddr').value.trim();
  const sig=document.getElementById('nSig').value.trim();
  const sigT=document.getElementById('nSigT').value.trim();
  const emp=document.getElementById('nEmp').value.trim();
  const nat=document.getElementById('nNat').value.trim();
  const pp=document.getElementById('nPP').value.trim();
  const iq=document.getElementById('nIq').value.trim();
  const job=document.getElementById('nJob').value.trim();
  const purp=purposeMap[document.getElementById('nPurp').value];
  const dateStr=new Date(document.getElementById('nDate').value).toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}});
  if(!co||!emp||!sig){{alert('براہ کرم کمپنی کا نام، ملازم کا نام اور دستخط کرنے والے کا نام درج کریں');return;}}
  const txt=`${{co}}
${{addr||'Riyadh, Saudi Arabia'}}

Date: ${{dateStr}}

                    NO OBJECTION CERTIFICATE
                    (عدم اعتراض سرٹیفکیٹ)

To Whom It May Concern,

This is to certify that Mr./Ms. ${{emp}}${{nat?', a national of '+nat:''}} is currently employed at ${{co}} as ${{job||'___'}}.

Passport No.: ${{pp||'___'}}
Iqama No.:    ${{iq||'___'}}

We hereby confirm that our company has NO OBJECTION to the above-named employee to ${{purp}}.

This certificate is issued upon the employee's request and is valid for 30 days from the date of issue.

Sincerely,


_______________________________
${{sig}}
${{sigT||'Authorized Signatory'}}
${{co}}

[Official Company Stamp]`;
  document.getElementById('nocText').textContent=txt;
  const r=document.getElementById('nocResult');r.classList.add('show');r.scrollIntoView({{behavior:'smooth'}});
}}
</script>
</body></html>"""

with open(f"{OUT}/noc-letter.html","w",encoding="utf-8") as f: f.write(p6)
print("✓ ur/noc-letter.html")
print("Batch 2 complete.")
