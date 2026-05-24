#!/usr/bin/env python3
"""Build 6 new zero-competition SEO pages for saudiutilityhub.com"""

import os

OUT = "/sessions/clever-inspiring-albattani/mnt/outputs"

NAV = """<nav>
  <div class="nav-inner">
    <a href="https://www.saudiutilityhub.com/" class="nav-logo">🇸🇦 Saudi Utility Hub</a>
    <a href="https://www.saudiutilityhub.com/">Home</a>
    <a href="https://www.saudiutilityhub.com/salary-calculator.html">Salary</a>
    <a href="https://www.saudiutilityhub.com/gosi-calculator.html">GOSI</a>
    <a href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">EOS</a>
    <a href="https://www.saudiutilityhub.com/gold-zakat-calculator.html">Zakat</a>
    <a href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">Iqama</a>
    <a href="https://www.saudiutilityhub.com/remittance-fee-compare.html">Remittance</a>
    <a href="https://www.saudiutilityhub.com/vat-calculator.html">VAT</a>
    <a href="https://www.saudiutilityhub.com/traffic-fine-calculator.html">Traffic</a>
    <a href="https://www.saudiutilityhub.com/blog/">Blog</a>
    <a href="https://www.saudiutilityhub.com/ar/" class="ar-link">عربي</a>
  </div>
</nav>"""

NAV_CSS = """
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Segoe UI',Arial,sans-serif;background:#f8fafc;color:#1a202c;line-height:1.6}
    nav{background:#fff;border-bottom:2px solid #e2e8f0;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.06)}
    .nav-inner{max-width:1200px;margin:0 auto;padding:0 16px;display:flex;align-items:center;gap:4px;flex-wrap:wrap;min-height:52px}
    .nav-logo{font-weight:700;font-size:1.1rem;color:#1a56db;text-decoration:none;margin-right:8px;white-space:nowrap}
    nav a{color:#374151;text-decoration:none;padding:6px 10px;border-radius:6px;font-size:.88rem;white-space:nowrap;transition:background .15s}
    nav a:hover,nav a.active{background:#eff6ff;color:#1a56db}
    nav a.ar-link{background:#f0fdf4;color:#166534;font-weight:600}
    .hero{background:linear-gradient(135deg,#1a56db 0%,#1e40af 60%,#065f46 100%);color:#fff;padding:44px 16px 36px;text-align:center}
    .hero h1{font-size:clamp(1.5rem,3.5vw,2.2rem);font-weight:800;margin-bottom:10px}
    .hero p{font-size:1rem;opacity:.9;max-width:680px;margin:0 auto}
    main{max-width:900px;margin:0 auto;padding:32px 16px 48px}
    .card{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:24px;margin-bottom:24px}
    h2{font-size:1.2rem;font-weight:700;color:#1a202c;margin-bottom:16px}
    label{display:block;font-size:.88rem;font-weight:600;color:#374151;margin-bottom:4px;margin-top:12px}
    input,select,textarea{width:100%;padding:10px 12px;border:1px solid #d1d5db;border-radius:8px;font-size:.95rem;font-family:inherit;background:#fff;color:#1a202c}
    input:focus,select:focus,textarea:focus{outline:none;border-color:#1a56db;box-shadow:0 0 0 3px rgba(26,86,219,.1)}
    .btn{display:inline-block;padding:11px 28px;background:#1a56db;color:#fff;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer;transition:background .15s;margin-top:16px}
    .btn:hover{background:#1e40af}
    .btn-green{background:#059669}.btn-green:hover{background:#047857}
    .result{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:20px;margin-top:20px;display:none}
    .result.show{display:block}
    .doc-preview{background:#fff;border:2px solid #e2e8f0;border-radius:8px;padding:28px 32px;font-size:.9rem;line-height:1.8;margin-top:16px;white-space:pre-wrap;font-family:'Courier New',monospace}
    .print-btn{background:#059669;color:#fff;border:none;padding:9px 20px;border-radius:6px;cursor:pointer;font-size:.88rem;font-weight:600;margin-top:12px}
    details{border:1px solid #e2e8f0;border-radius:10px;margin-bottom:8px;background:#fff}
    summary{padding:14px 18px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;font-size:.95rem}
    summary::-webkit-details-marker{display:none}
    summary::after{content:'+';font-size:1.2rem;color:#1a56db}
    details[open] summary::after{content:'−'}
    .faq-answer{padding:0 18px 14px;font-size:.9rem;color:#374151;line-height:1.6}
    .badge{display:inline-block;padding:3px 10px;border-radius:12px;font-size:.75rem;font-weight:600}
    .badge-green{background:#dcfce7;color:#166534}
    .badge-blue{background:#dbeafe;color:#1e40af}
    .badge-red{background:#fee2e2;color:#991b1b}
    table{width:100%;border-collapse:collapse;font-size:.88rem}
    th{background:#1a56db;color:#fff;padding:10px 12px;text-align:left}
    td{padding:9px 12px;border-bottom:1px solid #e2e8f0}
    tr:hover td{background:#f8fafc}
    footer{background:#1a202c;color:#e2e8f0;padding:32px 16px 20px}
    .footer-inner{max-width:1200px;margin:0 auto}
    .footer-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:24px;margin-bottom:20px}
    .footer-col h4{font-size:.85rem;font-weight:700;color:#fff;margin-bottom:10px;text-transform:uppercase}
    .footer-col a{display:block;color:#94a3b8;text-decoration:none;font-size:.82rem;margin-bottom:5px}
    .footer-col a:hover{color:#fff}
    .footer-bottom{border-top:1px solid #2d3748;padding-top:12px;font-size:.78rem;color:#6b7280}
    .info-box{background:#eff6ff;border-left:4px solid #1a56db;padding:14px 16px;border-radius:0 8px 8px 0;margin:16px 0;font-size:.9rem}
    .warn-box{background:#fefce8;border-left:4px solid #ca8a04;padding:14px 16px;border-radius:0 8px 8px 0;margin:16px 0;font-size:.9rem}
    .step{display:flex;gap:14px;margin-bottom:16px;align-items:flex-start}
    .step-num{background:#1a56db;color:#fff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;margin-top:2px}
    .step-body h3{font-size:.97rem;font-weight:700;margin-bottom:4px}
    .step-body p{font-size:.88rem;color:#4b5563}
    @media print{nav,.hero,footer,#cookie-bar,.print-btn,.btn{display:none!important}.doc-preview{border:1px solid #999;padding:20px}}
"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>💼 Finance Tools</h4>
        <a href="https://www.saudiutilityhub.com/salary-calculator.html">Salary Calculator</a>
        <a href="https://www.saudiutilityhub.com/gosi-calculator.html">GOSI Calculator</a>
        <a href="https://www.saudiutilityhub.com/ksa-eos-calculator.html">EOS Gratuity</a>
        <a href="https://www.saudiutilityhub.com/salary-slip-generator.html">Salary Slip</a>
        <a href="https://www.saudiutilityhub.com/salary-certificate.html">Salary Certificate</a>
        <a href="https://www.saudiutilityhub.com/noc-letter-generator.html">NOC Letter</a>
        <a href="https://www.saudiutilityhub.com/experience-letter-generator.html">Experience Letter</a>
      </div>
      <div class="footer-col">
        <h4>🪪 Expat Tools</h4>
        <a href="https://www.saudiutilityhub.com/iqama-expiry-calculator.html">Iqama Tracker</a>
        <a href="https://www.saudiutilityhub.com/iqama-transfer-calculator.html">Iqama Transfer Cost</a>
        <a href="https://www.saudiutilityhub.com/muqeem-visa-check.html">Muqeem Visa Check</a>
        <a href="https://www.saudiutilityhub.com/family-visit-visa-guide.html">Family Visit Visa</a>
        <a href="https://www.saudiutilityhub.com/driving-license-conversion.html">Driving License Convert</a>
        <a href="https://www.saudiutilityhub.com/traffic-fine-calculator.html">Traffic Fines</a>
      </div>
      <div class="footer-col">
        <h4>🏦 Banking</h4>
        <a href="https://www.saudiutilityhub.com/saudi-iban-validator.html">IBAN Validator</a>
        <a href="https://www.saudiutilityhub.com/remittance-fee-compare.html">Remittance Compare</a>
        <a href="https://www.saudiutilityhub.com/currency-converter.html">Currency Converter</a>
        <a href="https://www.saudiutilityhub.com/pakistan-remittance.html">SAR to PKR</a>
        <a href="https://www.saudiutilityhub.com/islamic-finance-calculator.html">Islamic Finance</a>
      </div>
      <div class="footer-col">
        <h4>📝 Blog</h4>
        <a href="https://www.saudiutilityhub.com/blog/">All Articles</a>
        <a href="https://www.saudiutilityhub.com/blog/gosi-guide-2026.html">GOSI Guide</a>
        <a href="https://www.saudiutilityhub.com/blog/eos-guide-2026.html">EOS Guide</a>
        <a href="https://www.saudiutilityhub.com/blog/salary-certificate-guide-2026.html">Salary Certificate</a>
      </div>
      <div class="footer-col">
        <h4>ℹ️ About</h4>
        <a href="https://www.saudiutilityhub.com/about.html">About Us</a>
        <a href="https://www.saudiutilityhub.com/contact.html">Contact</a>
        <a href="https://www.saudiutilityhub.com/privacy.html">Privacy Policy</a>
        <a href="https://www.saudiutilityhub.com/terms.html">Terms of Use</a>
        <a href="https://www.saudiutilityhub.com/ar/">عربي</a>
      </div>
    </div>
    <div class="footer-bottom">© 2026 Saudi Utility Hub · Riyadh, Saudi Arabia · Calculations are estimates only.</div>
  </div>
</footer>
<div id="cookie-bar" style="position:fixed;bottom:0;left:0;right:0;background:#1a202c;color:#e2e8f0;padding:12px 20px;display:flex;flex-wrap:wrap;align-items:center;gap:10px;z-index:999;font-size:.83rem">
  <span>🍪 We use cookies for ads and analytics. <a href="https://www.saudiutilityhub.com/privacy.html" style="color:#60a5fa">Privacy Policy</a></span>
  <button onclick="document.getElementById('cookie-bar').style.display='none';localStorage.setItem('ck','1')" style="background:#1a56db;color:#fff;border:none;padding:6px 14px;border-radius:5px;cursor:pointer;font-weight:600">Accept</button>
  <button onclick="document.getElementById('cookie-bar').style.display='none'" style="background:#374151;color:#e2e8f0;border:none;padding:6px 14px;border-radius:5px;cursor:pointer">Decline</button>
</div>
<script>if(localStorage.getItem('ck'))document.getElementById('cookie-bar').style.display='none'</script>"""

# ============================================================
# PAGE 1: NOC Letter Generator
# ============================================================
noc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Free NOC Letter Generator Saudi Arabia 2026 — No Objection Certificate Template</title>
  <meta name="description" content="Generate a free No Objection Certificate (NOC) letter for Saudi Arabia. Instant printable template for visa applications, bank accounts, job transfer, and more. Updated 2026.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <meta property="og:title" content="Free NOC Letter Generator Saudi Arabia 2026">
  <meta property="og:description" content="Generate a printable No Objection Certificate for Saudi Arabia — visa, bank, job transfer, or travel. Free, instant, bilingual.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/noc-letter-generator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"NOC Letter Generator Saudi Arabia","url":"https://www.saudiutilityhub.com/noc-letter-generator.html","description":"Free No Objection Certificate generator for Saudi Arabia — visa, bank, job transfer, and travel purposes.","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {{"@type":"Question","name":"What is an NOC letter in Saudi Arabia?","acceptedAnswer":{{"@type":"Answer","text":"A No Objection Certificate (NOC) is an official letter from your employer confirming they have no objection to you performing a specific action — such as applying for a visa, changing jobs, opening a bank account, or travelling. It must be on company letterhead with an official stamp."}}}},
    {{"@type":"Question","name":"When do I need an NOC in Saudi Arabia?","acceptedAnswer":{{"@type":"Answer","text":"Common situations: family visit visa application, tourist visa for a third country, bank account or loan application, sponsor transfer (Iqama transfer), property rental, educational enrollment."}}}},
    {{"@type":"Question","name":"Is an NOC letter legally required?","acceptedAnswer":{{"@type":"Answer","text":"It depends on the purpose. For sponsor transfer it is legally required. For visa applications and bank accounts it is a strong supporting document that most institutions request."}}}}
  ]}}
  </script>
  <style>{NAV_CSS}</style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>📋 Free NOC Letter Generator — Saudi Arabia 2026</h1>
  <p>Generate a professional No Objection Certificate instantly. Fill in your details, download, print, and submit.</p>
</section>
<main>
  <div class="info-box">
    <strong>What is an NOC?</strong> A No Objection Certificate (شهادة عدم ممانعة) is an official letter from your employer confirming they have no objection to a specific action. Required for visa applications, bank accounts, sponsor transfers, and more.
  </div>

  <div class="card">
    <h2>🏢 Employer / Company Details</h2>
    <label>Company Name (English)</label>
    <input type="text" id="compName" placeholder="e.g. Al Madar Trading Co. Ltd." value="">
    <label>Company Name (Arabic) — optional</label>
    <input type="text" id="compNameAr" placeholder="مثال: شركة المدار للتجارة" dir="rtl" value="">
    <label>Company Address</label>
    <input type="text" id="compAddr" placeholder="e.g. King Fahd Road, Riyadh 12345, Saudi Arabia" value="">
    <label>Commercial Registration (CR) Number — optional</label>
    <input type="text" id="crNum" placeholder="e.g. 1010123456" value="">
    <label>Authorized Signatory Name</label>
    <input type="text" id="sigName" placeholder="e.g. Mohammed Al-Rashidi" value="">
    <label>Signatory Job Title</label>
    <input type="text" id="sigTitle" placeholder="e.g. HR Manager / General Manager" value="">
  </div>

  <div class="card">
    <h2>👤 Employee Details</h2>
    <label>Employee Full Name</label>
    <input type="text" id="empName" placeholder="e.g. Ahmed Khan" value="">
    <label>Nationality</label>
    <input type="text" id="empNat" placeholder="e.g. Pakistani" value="">
    <label>Passport Number</label>
    <input type="text" id="passNum" placeholder="e.g. AB1234567" value="">
    <label>Iqama Number</label>
    <input type="text" id="iqamaNum" placeholder="e.g. 2012345678" value="">
    <label>Job Title</label>
    <input type="text" id="empTitle" placeholder="e.g. Senior Accountant" value="">
    <label>Employment Start Date</label>
    <input type="date" id="empStart" value="">
  </div>

  <div class="card">
    <h2>📄 NOC Purpose</h2>
    <label>Purpose of NOC</label>
    <select id="nocPurpose">
      <option value="visa">Family / Tourist Visa Application</option>
      <option value="bank">Bank Account / Loan Application</option>
      <option value="transfer">Sponsor / Iqama Transfer</option>
      <option value="travel">Personal Travel / Exit Re-Entry Visa</option>
      <option value="education">Educational Enrollment</option>
      <option value="property">Property Rental</option>
      <option value="custom">Custom Purpose</option>
    </select>
    <div id="customPurposeDiv" style="display:none">
      <label>Custom Purpose (describe briefly)</label>
      <input type="text" id="customPurpose" placeholder="e.g. applying for a second job">
    </div>
    <label>Letter Date</label>
    <input type="date" id="letterDate" value="">
    <label>NOC Valid Until (optional)</label>
    <input type="date" id="validUntil" value="">
    <button class="btn" onclick="generateNOC()">Generate NOC Letter</button>
  </div>

  <div class="result" id="nocResult">
    <h2 style="margin-bottom:12px;color:#166534">✅ Your NOC Letter is Ready</h2>
    <div class="warn-box">Print this letter on your company's official letterhead paper, then have it stamped and signed by the authorized person.</div>
    <div class="doc-preview" id="nocText"></div>
    <button class="print-btn" onclick="printNOC()">🖨️ Print NOC Letter</button>
    <button class="print-btn" style="background:#1a56db;margin-left:8px" onclick="copyNOC()">📋 Copy Text</button>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>What is an NOC letter in Saudi Arabia?</summary><div class="faq-answer">A No Objection Certificate (NOC / شهادة عدم ممانعة) is an official letter from your employer confirming they have no objection to a specific action. It must be on company letterhead with an official stamp and authorized signature.</div></details>
    <details><summary>When do I need an NOC in Saudi Arabia?</summary><div class="faq-answer">Common situations include: family or tourist visa applications, bank account or loan applications, sponsor (Iqama) transfer, property rental agreements, educational enrollment, and applying for an exit re-entry visa.</div></details>
    <details><summary>Does the NOC need to be in Arabic?</summary><div class="faq-answer">For Saudi government offices, Arabic is preferred. For embassies and banks, English is usually accepted. For best results, include both languages or get the English version officially translated.</div></details>
    <details><summary>Is this NOC legally binding?</summary><div class="faq-answer">This tool generates a standard template. The document only becomes legally effective once it is signed by an authorized company representative and stamped with the official company seal. Always verify requirements with the receiving institution.</div></details>
  </div>
</main>
{FOOTER}
<script>
  // Set today's date as default
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('letterDate').value = today;
  
  document.getElementById('nocPurpose').addEventListener('change', function() {{
    document.getElementById('customPurposeDiv').style.display = this.value === 'custom' ? 'block' : 'none';
  }});

  const purposes = {{
    visa: "apply for a family / tourist visa at the relevant embassy or consulate",
    bank: "open a bank account and/or apply for financial products at a bank of their choice",
    transfer: "transfer their Iqama sponsorship to another employer within the Kingdom of Saudi Arabia",
    travel: "travel outside the Kingdom of Saudi Arabia and return on an exit re-entry visa",
    education: "enroll in an educational or professional development program",
    property: "enter into a property rental agreement",
    custom: null
  }};

  function generateNOC() {{
    const fields = {{
      compName: document.getElementById('compName').value.trim(),
      compNameAr: document.getElementById('compNameAr').value.trim(),
      compAddr: document.getElementById('compAddr').value.trim(),
      crNum: document.getElementById('crNum').value.trim(),
      sigName: document.getElementById('sigName').value.trim(),
      sigTitle: document.getElementById('sigTitle').value.trim(),
      empName: document.getElementById('empName').value.trim(),
      empNat: document.getElementById('empNat').value.trim(),
      passNum: document.getElementById('passNum').value.trim(),
      iqamaNum: document.getElementById('iqamaNum').value.trim(),
      empTitle: document.getElementById('empTitle').value.trim(),
      empStart: document.getElementById('empStart').value,
      letterDate: document.getElementById('letterDate').value,
      validUntil: document.getElementById('validUntil').value,
    }};
    const purposeKey = document.getElementById('nocPurpose').value;
    let purposeText = purposeKey === 'custom'
      ? document.getElementById('customPurpose').value.trim()
      : purposes[purposeKey];
    if(!purposeText) purposeText = 'proceed with their personal matter';
    if(!fields.compName || !fields.empName || !fields.sigName) {{
      alert('Please fill in at least: Company Name, Employee Name, and Signatory Name.');
      return;
    }}
    const dateStr = fields.letterDate ? new Date(fields.letterDate).toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}}) : 'Date: ___________';
    const startStr = fields.empStart ? new Date(fields.empStart).toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}}) : '___________';
    const validStr = fields.validUntil ? new Date(fields.validUntil).toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}}) : '___________';
    const crLine = fields.crNum ? `CR No: ${{fields.crNum}}` : '';
    const arLine = fields.compNameAr ? `${{fields.compNameAr}}` : '';
    const text = `${{arLine ? arLine + '\\n' : ''}}${{fields.compName}}
${{fields.compAddr}}${{crLine ? '\\n' + crLine : ''}}

Date: ${{dateStr}}

                           NO OBJECTION CERTIFICATE
                           (شهادة عدم ممانعة)

To Whom It May Concern,

This is to certify that Mr./Ms. ${{fields.empName}}${{fields.empNat ? ', a national of ' + fields.empNat : ''}}, is currently employed at ${{fields.compName}} in the capacity of ${{fields.empTitle || '___________'}} since ${{startStr}}.

Passport No.: ${{fields.passNum || '___________'}}
Iqama No.:    ${{fields.iqamaNum || '___________'}}

We hereby confirm that our company has no objection to the above-named employee to ${{purposeText}}.

This letter is issued upon the employee's request and is valid${{fields.validUntil ? ' until ' + validStr : ' for 30 days from the date of issue'}}. We wish him/her all the best in his/her endeavours.

Yours sincerely,


_______________________________
${{fields.sigName}}
${{fields.sigTitle || 'Authorized Signatory'}}
${{fields.compName}}

[Official Company Stamp Here]`;
    document.getElementById('nocText').textContent = text;
    const r = document.getElementById('nocResult');
    r.classList.add('show');
    r.scrollIntoView({{behavior:'smooth'}});
  }}

  function printNOC() {{ window.print(); }}
  function copyNOC() {{
    navigator.clipboard.writeText(document.getElementById('nocText').textContent);
    alert('NOC text copied to clipboard!');
  }}
</script>
</body>
</html>"""

with open(f"{OUT}/noc-letter-generator.html", "w", encoding="utf-8") as f:
    f.write(noc)
print("✓ noc-letter-generator.html")

# ============================================================
# PAGE 2: Experience Letter Generator
# ============================================================
exp = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Free Experience Letter Generator Saudi Arabia 2026 — Work Experience Certificate Template</title>
  <meta name="description" content="Generate a free work experience letter for Saudi Arabia in seconds. Bilingual Arabic/English template. Required for job applications, visa, and bank purposes. Updated 2026.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/experience-letter-generator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/experience-letter-generator.html">
  <meta property="og:title" content="Free Experience Letter Generator Saudi Arabia 2026">
  <meta property="og:description" content="Instant printable work experience certificate for Saudi Arabia. Free bilingual template for expats.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/experience-letter-generator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/experience-letter-generator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"Experience Letter Generator Saudi Arabia","url":"https://www.saudiutilityhub.com/experience-letter-generator.html","description":"Free work experience certificate generator for Saudi Arabia.","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{NAV_CSS}</style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>📜 Free Experience Letter Generator — Saudi Arabia 2026</h1>
  <p>Create an official work experience certificate instantly. Required for new jobs, visa applications, and bank purposes.</p>
</section>
<main>
  <div class="info-box">
    An Experience Letter (خطاب خبرة عمل) officially confirms your employment history — your role, duration, and performance. Required by most employers, embassies, and banks when you're changing jobs or applying for services.
  </div>

  <div class="card">
    <h2>🏢 Company Details</h2>
    <label>Company Name (English)</label>
    <input type="text" id="cName" placeholder="e.g. Saudi Petroleum Services Corp.">
    <label>Company Address</label>
    <input type="text" id="cAddr" placeholder="e.g. Dhahran Road, Al Khobar 31952, Saudi Arabia">
    <label>HR / Authorized Signatory Name</label>
    <input type="text" id="hrName" placeholder="e.g. Khalid Al-Otaibi">
    <label>Signatory Title</label>
    <input type="text" id="hrTitle" placeholder="e.g. Human Resources Manager">
  </div>

  <div class="card">
    <h2>👤 Employee Details</h2>
    <label>Employee Full Name</label>
    <input type="text" id="eName" placeholder="e.g. Muhammad Tariq">
    <label>Nationality</label>
    <input type="text" id="eNat" placeholder="e.g. Pakistani">
    <label>Passport Number</label>
    <input type="text" id="ePP" placeholder="e.g. AB1234567">
    <label>Iqama Number</label>
    <input type="text" id="eIq" placeholder="e.g. 2012345678">
    <label>Job Title / Designation</label>
    <input type="text" id="eJob" placeholder="e.g. Civil Engineer">
    <label>Department</label>
    <input type="text" id="eDept" placeholder="e.g. Construction & Projects">
    <label>Employment Start Date</label>
    <input type="date" id="eStart">
    <label>Last Working Date</label>
    <input type="date" id="eEnd">
    <label>Reason for Leaving</label>
    <select id="eReason">
      <option value="resignation">Resignation</option>
      <option value="contract">Contract End / Non-Renewal</option>
      <option value="mutual">Mutual Agreement</option>
      <option value="currently">Currently Employed (for reference)</option>
    </select>
    <label>Final Salary (SAR) — optional</label>
    <input type="number" id="eSalary" placeholder="e.g. 8500">
  </div>

  <div class="card">
    <h2>📄 Letter Options</h2>
    <label>Letter Date</label>
    <input type="date" id="lDate">
    <label>Performance Note</label>
    <select id="ePerfNote">
      <option value="excellent">Excellent — Outstanding performance and dedication</option>
      <option value="good">Good — Reliable and professional</option>
      <option value="neutral">Neutral — Standard factual letter only</option>
    </select>
    <button class="btn" onclick="generateExp()">Generate Experience Letter</button>
  </div>

  <div class="result" id="expResult">
    <h2 style="margin-bottom:12px;color:#166534">✅ Experience Letter Ready</h2>
    <div class="warn-box">Print on official company letterhead. Get it stamped and signed before submission.</div>
    <div class="doc-preview" id="expText"></div>
    <button class="print-btn" onclick="window.print()">🖨️ Print Letter</button>
    <button class="print-btn" style="background:#1a56db;margin-left:8px" onclick="navigator.clipboard.writeText(document.getElementById('expText').textContent);alert('Copied!')">📋 Copy Text</button>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>What must an experience letter include in Saudi Arabia?</summary><div class="faq-answer">Under Saudi Labour Law it must include: employee name, nationality, Iqama/passport number, job title, start and end dates, reason for leaving (if applicable), and company stamp + authorized signature on official letterhead.</div></details>
    <details><summary>Can I use this letter for a new Saudi employer?</summary><div class="faq-answer">Yes. Present this letter to your new employer along with your Iqama and passport. Most Saudi companies require an experience letter from your previous employer as part of the hiring process.</div></details>
    <details><summary>Is experience letter required for visa application?</summary><div class="faq-answer">Many embassies — particularly US, UK, Schengen, and Canada — require a current employment letter for visa applications from Saudi Arabia. This generator covers both "currently employed" and "past employment" versions.</div></details>
    <details><summary>How long should the letter be valid?</summary><div class="faq-answer">Experience letters typically have no expiry for employment history purposes. For visa applications, embassies usually require the letter to be dated within 3 months of the application.</div></details>
  </div>
</main>
{FOOTER}
<script>
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('lDate').value = today;
  document.getElementById('eEnd').value = today;

  const reasonMap = {{
    resignation: 'upon his/her own resignation',
    contract: 'due to the end of the employment contract',
    mutual: 'by mutual agreement between both parties',
    currently: null
  }};
  const perfMap = {{
    excellent: 'During the tenure, {{name}} demonstrated excellent professional skills, dedication, and commitment. We wish {{pronoun}} great success in future endeavors.',
    good: 'Throughout the employment period, {{name}} was a reliable and professional team member. We wish {{pronoun}} all the best.',
    neutral: ''
  }};

  function fmt(d) {{
    if(!d) return '___________';
    return new Date(d).toLocaleDateString('en-US',{{year:'numeric',month:'long',day:'numeric'}});
  }}

  function generateExp() {{
    const cn = document.getElementById('cName').value.trim();
    const ca = document.getElementById('cAddr').value.trim();
    const hr = document.getElementById('hrName').value.trim();
    const ht = document.getElementById('hrTitle').value.trim();
    const en = document.getElementById('eName').value.trim();
    const enat = document.getElementById('eNat').value.trim();
    const epp = document.getElementById('ePP').value.trim();
    const eiq = document.getElementById('eIq').value.trim();
    const ej = document.getElementById('eJob').value.trim();
    const ed = document.getElementById('eDept').value.trim();
    const es = document.getElementById('eStart').value;
    const ee = document.getElementById('eEnd').value;
    const er = document.getElementById('eReason').value;
    const esal = document.getElementById('eSalary').value;
    const ld = document.getElementById('lDate').value;
    const pn = document.getElementById('ePerfNote').value;

    if(!cn || !en || !hr) {{ alert('Please fill in Company Name, Employee Name, and Signatory Name.'); return; }}

    const isCurrent = er === 'currently';
    const deptLine = ed ? ` in the ${{ed}} Department` : '';
    const salLine = esal ? `\\nFinal Basic Salary: SAR ${{parseInt(esal).toLocaleString()}} per month` : '';
    const reasonLine = !isCurrent ? `His/Her employment has ended ${{reasonMap[er]}} on ${{fmt(ee)}}.` : 'He/She continues to be an active employee of our organization.';
    const perfText = perfMap[pn].replace(/\\{{name\\}}/g, en).replace(/\\{{pronoun\\}}/g, 'him/her');

    const text = `${{cn}}
${{ca}}

Date: ${{fmt(ld)}}

                        TO WHOM IT MAY CONCERN
                   EXPERIENCE CERTIFICATE / LETTER

This is to certify that Mr./Ms. ${{en}}${{enat ? ', a national of ' + enat : ''}}, ${{isCurrent ? 'is currently employed' : 'was employed'}} with ${{cn}}${{deptLine}} as ${{ej || '___________'}} since ${{fmt(es)}}.${{!isCurrent ? '' : ''}}

Passport No.: ${{epp || '___________'}}
Iqama No.:    ${{eiq || '___________'}}${{salLine}}

${{reasonLine}}

${{perfText}}

This certificate is issued on the employee's request for use wherever required.


_______________________________
${{hr}}
${{ht || 'Authorized Signatory'}}
${{cn}}

[Official Company Stamp Here]`;
    document.getElementById('expText').textContent = text;
    const r = document.getElementById('expResult');
    r.classList.add('show');
    r.scrollIntoView({{behavior:'smooth'}});
  }}
</script>
</body>
</html>"""

with open(f"{OUT}/experience-letter-generator.html", "w", encoding="utf-8") as f:
    f.write(exp)
print("✓ experience-letter-generator.html")

# ============================================================
# PAGE 3: Iqama Transfer Cost Calculator
# ============================================================
iqtrans = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Iqama Transfer Cost Calculator Saudi Arabia 2026 — Sponsor Change Fees</title>
  <meta name="description" content="Calculate exact Iqama transfer (sponsor change) fees in Saudi Arabia 2026. SAR 2,000 first transfer, SAR 4,000 second. Eligibility check + full fee breakdown.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/iqama-transfer-calculator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/iqama-transfer-calculator.html">
  <meta property="og:title" content="Iqama Transfer Cost Calculator Saudi Arabia 2026">
  <meta property="og:description" content="Exact Iqama transfer fees 2026. First transfer SAR 2,000 · Second SAR 4,000 · Third+ SAR 6,000. Eligibility + full breakdown.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/iqama-transfer-calculator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/iqama-transfer-calculator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"Iqama Transfer Cost Calculator","url":"https://www.saudiutilityhub.com/iqama-transfer-calculator.html","description":"Calculate Iqama sponsor transfer fees in Saudi Arabia 2026.","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{NAV_CSS}
    .fee-row{{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e2e8f0;font-size:.93rem}}
    .fee-row:last-child{{border:none;font-weight:700;font-size:1rem;color:#1a56db}}
    .eligibility{{padding:14px;border-radius:8px;margin-top:16px;font-weight:600}}
    .elig-yes{{background:#dcfce7;color:#166534;border:1px solid #86efac}}
    .elig-no{{background:#fee2e2;color:#991b1b;border:1px solid #fca5a5}}
  </style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>🔄 Iqama Transfer Cost Calculator — Saudi Arabia 2026</h1>
  <p>Calculate the exact fee to transfer your sponsorship (Iqama) to a new employer in Saudi Arabia.</p>
</section>
<main>
  <div class="info-box">
    <strong>Sponsor Transfer (نقل الكفالة)</strong> allows you to move your Iqama from your current employer to a new one. The fee depends on how many times you've transferred before. All transfers must be done through <strong>Qiwa platform</strong>.
  </div>

  <div class="card">
    <h2>🧮 Calculate Your Transfer Cost</h2>
    <label>How many times have you transferred sponsor before?</label>
    <select id="transferCount">
      <option value="0">This is my FIRST transfer</option>
      <option value="1">I have transferred ONCE before (this will be 2nd)</option>
      <option value="2">I have transferred TWICE before (this will be 3rd+)</option>
    </select>
    <label>Years employed with CURRENT sponsor</label>
    <input type="number" id="yearsWithSponsor" min="0" max="40" step="0.5" placeholder="e.g. 2.5" value="1">
    <label>Do you have outstanding violations or penalties on Absher?</label>
    <select id="hasViolations">
      <option value="no">No — clean record</option>
      <option value="yes">Yes — I have unpaid fines or violations</option>
      <option value="unknown">Not sure</option>
    </select>
    <label>Remaining Iqama validity (months)</label>
    <input type="number" id="iqamaMonths" min="0" max="12" step="1" placeholder="e.g. 6" value="6">
    <button class="btn" onclick="calcTransfer()">Calculate Transfer Cost</button>
  </div>

  <div class="result" id="transferResult">
    <h2 style="color:#166534;margin-bottom:16px">💰 Transfer Cost Breakdown</h2>
    <div id="eligDiv" class="eligibility"></div>
    <div style="margin-top:16px" id="feeBreakdown"></div>
    <div class="warn-box" style="margin-top:16px" id="warningDiv"></div>
  </div>

  <div class="card">
    <h2>📋 Iqama Transfer Fee Table 2026</h2>
    <table>
      <tr><th>Transfer Number</th><th>Fee (SAR)</th><th>Fee (USD approx.)</th></tr>
      <tr><td>1st Transfer</td><td><strong>SAR 2,000</strong></td><td>~$533</td></tr>
      <tr><td>2nd Transfer</td><td><strong>SAR 4,000</strong></td><td>~$1,066</td></tr>
      <tr><td>3rd Transfer &amp; beyond</td><td><strong>SAR 6,000</strong></td><td>~$1,599</td></tr>
      <tr><td>Iqama Renewal after transfer</td><td><strong>SAR 650</strong></td><td>~$173</td></tr>
      <tr><td>Qiwa service fee</td><td><strong>SAR 51.75</strong></td><td>~$14</td></tr>
    </table>
    <p style="margin-top:10px;font-size:.82rem;color:#6b7280">Fees effective 2026. Paid by the new employer or shared by agreement. Verify on <a href="https://qiwa.sa" target="_blank">qiwa.sa</a></p>
  </div>

  <div class="card">
    <h2>✅ Eligibility Requirements</h2>
    <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Valid Iqama</h3><p>Your Iqama must be valid (not expired). Renew before applying for transfer.</p></div></div>
    <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Minimum 1 Year with Current Sponsor</h3><p>You must have worked at least 12 months with your current sponsor unless they consent to early transfer.</p></div></div>
    <div class="step"><div class="step-num">3</div><div class="step-body"><h3>No Outstanding Violations</h3><p>Clear all traffic fines, Absher violations, and any unpaid fees before applying.</p></div></div>
    <div class="step"><div class="step-num">4</div><div class="step-body"><h3>New Job Offer via Qiwa</h3><p>The new employer must issue a contract offer through the Qiwa platform for the transfer to proceed.</p></div></div>
    <div class="step"><div class="step-num">5</div><div class="step-body"><h3>No Active Iqama Violation (هروب)</h3><p>You must not have an active absconding (هروب) report filed against you.</p></div></div>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>Can my new employer pay the transfer fee?</summary><div class="faq-answer">Yes. By law and common practice, the new employer usually covers the transfer fee as part of the hiring offer. You can negotiate this in your job offer. Always confirm in writing before proceeding.</div></details>
    <details><summary>How long does an Iqama transfer take?</summary><div class="faq-answer">If all conditions are met, the transfer is processed instantly through Qiwa. If the current employer must consent, it can take 1–30 days depending on their cooperation or if you use the MHRSD mediation channel.</div></details>
    <details><summary>Can I transfer without my current employer's approval?</summary><div class="faq-answer">Yes, in certain cases. Under the Saudi Labour Reform Initiative, if you've completed 12 months of service, you may request a transfer without explicit employer approval through Qiwa. MHRSD may intervene if the employer objects without valid reason.</div></details>
    <details><summary>What is the Qiwa platform?</summary><div class="faq-answer">Qiwa (qiwa.sa) is Saudi Arabia's official platform for managing labour contracts, Iqama transfers, and employer-employee agreements. Both the employee and the new employer must have Qiwa accounts to complete the transfer.</div></details>
  </div>
</main>
{FOOTER}
<script>
  function calcTransfer() {{
    const tc = parseInt(document.getElementById('transferCount').value);
    const yrs = parseFloat(document.getElementById('yearsWithSponsor').value) || 0;
    const viol = document.getElementById('hasViolations').value;
    const months = parseInt(document.getElementById('iqamaMonths').value) || 0;

    const fees = [2000, 4000, 6000];
    const transferFee = fees[Math.min(tc, 2)];
    const qiwaFee = 51.75;
    const renewalFee = months < 3 ? 650 : 0;
    const total = transferFee + qiwaFee + renewalFee;

    // Eligibility
    let eligText = '';
    let eligClass = 'elig-yes';
    const issues = [];
    if(yrs < 1) issues.push('You have worked less than 12 months — employer consent may be required');
    if(viol === 'yes') issues.push('You have outstanding violations — clear these first on Absher');
    if(months < 1) issues.push('Your Iqama appears expired — renew before transferring');

    if(issues.length === 0) {{
      eligText = '✅ You appear eligible for sponsor transfer. Proceed via Qiwa platform.';
    }} else {{
      eligClass = 'elig-no';
      eligText = '⚠️ Potential issues found:<br>• ' + issues.join('<br>• ');
    }}

    document.getElementById('eligDiv').className = 'eligibility ' + eligClass;
    document.getElementById('eligDiv').innerHTML = eligText;

    const breakdown = `
      <div class="fee-row"><span>Sponsor Transfer Fee (${{tc===0?'1st':tc===1?'2nd':'3rd+'}} transfer)</span><span>SAR ${{transferFee.toLocaleString()}}</span></div>
      <div class="fee-row"><span>Qiwa Platform Fee</span><span>SAR ${{qiwaFee.toFixed(2)}}</span></div>
      ${{renewalFee > 0 ? '<div class="fee-row"><span>Iqama Renewal (recommended — under 3 months left)</span><span>SAR ' + renewalFee + '</span></div>' : ''}}
      <div class="fee-row"><span>TOTAL ESTIMATED COST</span><span>SAR ${{total.toLocaleString('en-US',{{minimumFractionDigits:2}})}}</span></div>
    `;
    document.getElementById('feeBreakdown').innerHTML = breakdown;

    const warnText = tc === 0
      ? 'This is your first transfer. The fee of SAR 2,000 is commonly covered by the new employer — negotiate this before signing your contract.'
      : tc === 1
      ? 'Second transfer costs SAR 4,000. Discuss with your new employer who will cover this fee.'
      : 'Third or subsequent transfers cost SAR 6,000. Ensure your new employer confirms they will cover this cost in writing.';
    document.getElementById('warningDiv').textContent = warnText;

    const r = document.getElementById('transferResult');
    r.classList.add('show');
    r.scrollIntoView({{behavior:'smooth'}});
  }}
</script>
</body>
</html>"""

with open(f"{OUT}/iqama-transfer-calculator.html", "w", encoding="utf-8") as f:
    f.write(iqtrans)
print("✓ iqama-transfer-calculator.html")

# ============================================================
# PAGE 4: Saudi IBAN Validator
# ============================================================
iban = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Saudi IBAN Validator &amp; Checker 2026 — Verify SA Bank Account Numbers Free</title>
  <meta name="description" content="Validate any Saudi Arabia IBAN number instantly. Check format, length, bank code, and checksum. Free IBAN checker for Al Rajhi, SNB, Riyad Bank and all Saudi banks.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/saudi-iban-validator.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/saudi-iban-validator.html">
  <meta property="og:title" content="Saudi IBAN Validator 2026 — Free IBAN Checker">
  <meta property="og:description" content="Validate Saudi IBAN numbers instantly. Check format, bank code, and MOD97 checksum. All Saudi banks supported.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/saudi-iban-validator.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/saudi-iban-validator.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebApplication","name":"Saudi IBAN Validator","url":"https://www.saudiutilityhub.com/saudi-iban-validator.html","description":"Validate Saudi Arabia IBAN numbers — format, bank code, and checksum verification.","applicationCategory":"UtilityApplication","operatingSystem":"Any","offers":{{"@type":"Offer","price":"0","priceCurrency":"SAR"}}}}
  </script>
  <style>{NAV_CSS}
    .iban-input{{font-size:1.3rem;letter-spacing:2px;text-transform:uppercase;font-family:'Courier New',monospace;text-align:center;padding:14px}}
    .valid-box{{background:#dcfce7;border:2px solid #86efac;border-radius:10px;padding:20px;margin-top:16px}}
    .invalid-box{{background:#fee2e2;border:2px solid #fca5a5;border-radius:10px;padding:20px;margin-top:16px}}
    .check-row{{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid #e2e8f0;font-size:.9rem}}
    .check-row:last-child{{border:none}}
    .ck-pass{{color:#166534;font-weight:700;font-size:1rem}}
    .ck-fail{{color:#991b1b;font-weight:700;font-size:1rem}}
    .iban-parts{{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px;margin-top:12px}}
    .iban-part{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px;text-align:center}}
    .iban-part .label{{font-size:.72rem;color:#6b7280;text-transform:uppercase;font-weight:600;margin-bottom:4px}}
    .iban-part .value{{font-size:1rem;font-weight:700;font-family:'Courier New',monospace;color:#1a56db}}
  </style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>🏦 Saudi IBAN Validator — Free Checker 2026</h1>
  <p>Instantly validate any Saudi Arabia IBAN number. Checks format, length, bank code, and MOD97 checksum.</p>
</section>
<main>
  <div class="card">
    <h2>🔍 Enter Saudi IBAN Number</h2>
    <p style="font-size:.88rem;color:#6b7280;margin-bottom:12px">Saudi IBANs start with <strong>SA</strong> and are exactly <strong>24 characters</strong> long. Example: SA0380000000608010167519</p>
    <input type="text" id="ibanInput" class="iban-input" maxlength="30" placeholder="SA XX XXXX XXXX XXXX XXXX" oninput="this.value=this.value.toUpperCase().replace(/\\s/g,'')">
    <button class="btn" onclick="validateIBAN()" style="width:100%;margin-top:12px">✅ Validate IBAN</button>
  </div>

  <div id="ibanResult" style="display:none">
    <div id="ibanStatus"></div>
    <div class="card" style="margin-top:16px">
      <h2>📊 IBAN Breakdown</h2>
      <div class="iban-parts" id="ibanParts"></div>
      <div style="margin-top:16px" id="ibanChecks"></div>
    </div>
  </div>

  <div class="card">
    <h2>🏛️ Saudi Bank Codes Reference</h2>
    <table>
      <tr><th>Bank Code</th><th>Bank Name</th></tr>
      <tr><td>10</td><td>Al Rajhi Bank</td></tr>
      <tr><td>20</td><td>Arab National Bank (ANB)</td></tr>
      <tr><td>30</td><td>Saudi National Bank (SNB / Al Ahli)</td></tr>
      <tr><td>40</td><td>Bank Al Jazira</td></tr>
      <tr><td>45</td><td>Bank AlBilad</td></tr>
      <tr><td>55</td><td>Alinma Bank</td></tr>
      <tr><td>60</td><td>Riyad Bank</td></tr>
      <tr><td>65</td><td>Saudi British Bank (SABB)</td></tr>
      <tr><td>80</td><td>Saudi Investment Bank (SAIB)</td></tr>
      <tr><td>05</td><td>Saudi Fransi Bank</td></tr>
    </table>
  </div>

  <div class="card">
    <h2>📐 Saudi IBAN Format Explained</h2>
    <div class="iban-parts" style="grid-template-columns:repeat(4,1fr)">
      <div class="iban-part"><div class="label">Characters 1–2</div><div class="value">SA</div><div style="font-size:.75rem;margin-top:4px;color:#6b7280">Country Code</div></div>
      <div class="iban-part"><div class="label">Characters 3–4</div><div class="value">XX</div><div style="font-size:.75rem;margin-top:4px;color:#6b7280">Check Digits</div></div>
      <div class="iban-part"><div class="label">Characters 5–6</div><div class="value">XX</div><div style="font-size:.75rem;margin-top:4px;color:#6b7280">Bank Code</div></div>
      <div class="iban-part"><div class="label">Characters 7–24</div><div class="value">XXXXXXXXXX</div><div style="font-size:.75rem;margin-top:4px;color:#6b7280">Account Number</div></div>
    </div>
    <p style="margin-top:12px;font-size:.85rem;color:#6b7280">Total length: exactly 24 characters. No spaces or dashes when used in banking systems.</p>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>What is an IBAN and why do I need it in Saudi Arabia?</summary><div class="faq-answer">IBAN (International Bank Account Number) is the Saudi standard for all bank transfers. All Saudi banks use 24-character IBANs starting with SA. You need your IBAN to receive your salary, send international transfers, and set up direct debits.</div></details>
    <details><summary>Where can I find my Saudi IBAN?</summary><div class="faq-answer">Log in to your bank's mobile app → Account Details → IBAN. Alternatively, check your bank statement, visit a branch, or use your bank's ATM. You can also find it on the SAMA official IBAN checker at sama.gov.sa.</div></details>
    <details><summary>Is this validator connected to real bank data?</summary><div class="faq-answer">This tool validates the IBAN format, length, bank code, and MOD97 mathematical checksum — the same checks used by banks. It does NOT verify whether the account is active or belongs to a specific person. For full verification, use your bank's official service.</div></details>
    <details><summary>How do I find my IBAN without a bank statement?</summary><div class="faq-answer">Use your bank's mobile app (Al Rajhi App, SNB AlAhli, etc.) → tap your account → Account Number / IBAN. You can also dial your bank's customer service or visit any branch with your Iqama.</div></details>
  </div>
</main>
{FOOTER}
<script>
  const bankCodes = {{
    '05': 'Saudi Fransi Bank', '10': 'Al Rajhi Bank', '20': 'Arab National Bank (ANB)',
    '30': 'Saudi National Bank (SNB)', '40': 'Bank Al Jazira', '45': 'Bank AlBilad',
    '55': 'Alinma Bank', '60': 'Riyad Bank', '65': 'Saudi British Bank (SABB)',
    '80': 'Saudi Investment Bank (SAIB)'
  }};

  function mod97(iban) {{
    const rearranged = iban.slice(4) + iban.slice(0, 4);
    const digits = rearranged.split('').map(c => {{
      const code = c.charCodeAt(0);
      return code >= 65 ? (code - 55).toString() : c;
    }}).join('');
    let remainder = 0;
    for(let i = 0; i < digits.length; i++) {{
      remainder = (remainder * 10 + parseInt(digits[i])) % 97;
    }}
    return remainder;
  }}

  function validateIBAN() {{
    const raw = document.getElementById('ibanInput').value.replace(/\\s/g, '').toUpperCase();
    const result = document.getElementById('ibanResult');
    const status = document.getElementById('ibanStatus');
    const parts = document.getElementById('ibanParts');
    const checks = document.getElementById('ibanChecks');
    result.style.display = 'block';

    const isCorrectPrefix = raw.startsWith('SA');
    const isCorrectLength = raw.length === 24;
    const bankCode = raw.length >= 6 ? raw.slice(4, 6) : '??';
    const bankName = bankCodes[bankCode] || 'Unknown Bank';
    const isKnownBank = !!bankCodes[bankCode];
    const checkDigits = raw.length >= 4 ? raw.slice(2, 4) : '??';
    const accountNum = raw.length >= 7 ? raw.slice(6) : '??';
    let checksumOk = false;
    if(isCorrectLength && isCorrectPrefix) {{
      try {{ checksumOk = mod97(raw) === 1; }} catch(e) {{}}
    }}

    const allOk = isCorrectPrefix && isCorrectLength && isKnownBank && checksumOk;

    status.innerHTML = allOk
      ? `<div class="valid-box"><strong style="font-size:1.1rem;color:#166534">✅ Valid Saudi IBAN</strong><br><span style="font-size:.9rem">Bank: <strong>${{bankName}}</strong></span></div>`
      : `<div class="invalid-box"><strong style="font-size:1.1rem;color:#991b1b">❌ Invalid IBAN</strong><br><span style="font-size:.9rem">Please check the number and try again.</span></div>`;

    parts.innerHTML = `
      <div class="iban-part"><div class="label">Country</div><div class="value">${{raw.slice(0,2)||'--'}}</div></div>
      <div class="iban-part"><div class="label">Check Digits</div><div class="value">${{checkDigits}}</div></div>
      <div class="iban-part"><div class="label">Bank Code</div><div class="value">${{bankCode}}</div></div>
      <div class="iban-part"><div class="label">Account Number</div><div class="value" style="font-size:.85rem">${{accountNum}}</div></div>
    `;

    checks.innerHTML = `
      <div class="check-row"><span class="${{isCorrectPrefix?'ck-pass':'ck-fail'}}">${{isCorrectPrefix?'✅':'❌'}}</span><span>Starts with SA (Saudi Arabia country code)</span></div>
      <div class="check-row"><span class="${{isCorrectLength?'ck-pass':'ck-fail'}}">${{isCorrectLength?'✅':'❌'}}</span><span>Correct length: ${{raw.length}} / 24 characters${{!isCorrectLength?' — '+(raw.length<24?'too short':'too long'):''}}</span></div>
      <div class="check-row"><span class="${{isKnownBank?'ck-pass':'ck-fail'}}">${{isKnownBank?'✅':'⚠️'}}</span><span>Bank code ${{bankCode}}: ${{bankName}}</span></div>
      <div class="check-row"><span class="${{checksumOk?'ck-pass':'ck-fail'}}">${{checksumOk?'✅':'❌'}}</span><span>MOD97 checksum: ${{checksumOk?'Passed':'Failed — number may contain a typo'}}</span></div>
    `;

    result.scrollIntoView({{behavior:'smooth'}});
  }}

  document.getElementById('ibanInput').addEventListener('keydown', function(e) {{
    if(e.key === 'Enter') validateIBAN();
  }});
</script>
</body>
</html>"""

with open(f"{OUT}/saudi-iban-validator.html", "w", encoding="utf-8") as f:
    f.write(iban)
print("✓ saudi-iban-validator.html")

# ============================================================
# PAGE 5: Family Visit Visa Guide
# ============================================================
famvisa = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Saudi Arabia Family Visit Visa 2026 — Complete Guide, Cost &amp; How to Apply</title>
  <meta name="description" content="Complete guide to Saudi Arabia family visit visa 2026. How to apply on MOFA, cost, requirements, processing time, duration, and common mistakes to avoid.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/family-visit-visa-guide.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/family-visit-visa-guide.html">
  <meta property="og:title" content="Saudi Arabia Family Visit Visa 2026 — Complete Guide">
  <meta property="og:description" content="How to get a family visit visa for Saudi Arabia. MOFA application, fees, documents, processing time, and dos &amp; don'ts.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/family-visit-visa-guide.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/family-visit-visa-guide.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"HowTo","name":"How to Apply for Saudi Arabia Family Visit Visa 2026","description":"Step-by-step guide to apply for a family visit visa for Saudi Arabia through the MOFA portal.","step":[
    {{"@type":"HowToStep","name":"Create MOFA Account","text":"Go to visa.mofa.gov.sa and register your account using your Iqama number and a valid email."}},
    {{"@type":"HowToStep","name":"Select Visa Type","text":"Choose 'Family Visit Visa' and enter your relative's passport details, nationality, and relationship."}},
    {{"@type":"HowToStep","name":"Purchase Health Insurance","text":"Buy mandatory health insurance during the application — BUPA Saudi or other approved providers."}},
    {{"@type":"HowToStep","name":"Pay Visa Fee","text":"Pay the visa fee by credit card. Fees range from SAR 300–800 depending on nationality."}},
    {{"@type":"HowToStep","name":"Receive Visa Approval","text":"The approved visa is emailed to you usually within 1–5 business days. Your relative uses it to apply at the Saudi embassy or enter on arrival if eligible."}}
  ]}}
  </script>
  <style>{NAV_CSS}
    .cost-card{{background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:16px 20px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center}}
    .cost-label{{font-weight:600;font-size:.93rem}}
    .cost-amount{{font-size:1.05rem;font-weight:700;color:#1a56db}}
  </style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>✈️ Saudi Arabia Family Visit Visa 2026</h1>
  <p>Complete guide for expats — how to apply, cost, documents, processing time, and everything you need to know.</p>
</section>
<main>
  <div class="info-box">
    <strong>Family Visit Visa (تأشيرة الزيارة العائلية)</strong> allows expatriate residents in Saudi Arabia to invite immediate family members (spouse, children, parents, siblings) to visit them. You — the sponsor — apply on their behalf through the MOFA portal.
  </div>

  <div class="card">
    <h2>💰 Fee Calculator — Family Visit Visa</h2>
    <label>Number of family members visiting</label>
    <input type="number" id="familyCount" min="1" max="10" value="2" style="max-width:120px">
    <label>Nationality of visitors</label>
    <select id="visaNat">
      <option value="300">Pakistan, India, Bangladesh, Philippines, Indonesia, Nepal, Sri Lanka (SAR 300/person)</option>
      <option value="500">Egypt, Jordan, Morocco, Sudan, Yemen (SAR 500/person)</option>
      <option value="800">Other nationalities (SAR 800/person)</option>
    </select>
    <label>Health insurance (per person, approx.)</label>
    <input type="number" id="insuranceAmt" value="150" min="100" max="400">
    <button class="btn" onclick="calcVisaCost()">Calculate Total Cost</button>
    <div id="visaCostResult" style="display:none;margin-top:16px">
      <div class="cost-card"><span class="cost-label">Visa fee</span><span class="cost-amount" id="visaFeeTotal"></span></div>
      <div class="cost-card"><span class="cost-label">Health insurance</span><span class="cost-amount" id="insTotal"></span></div>
      <div class="cost-card" style="background:#eff6ff;border-color:#bfdbfe"><span class="cost-label" style="font-weight:700">TOTAL ESTIMATED COST</span><span class="cost-amount" id="grandTotal"></span></div>
    </div>
  </div>

  <div class="card">
    <h2>📋 Step-by-Step Application Process</h2>
    <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Create MOFA Account</h3><p>Go to <a href="https://visa.mofa.gov.sa" target="_blank">visa.mofa.gov.sa</a> → Register using your Iqama number and valid email address. If you already have an account, log in.</p></div></div>
    <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Select "Family Visit Visa"</h3><p>From the visa services menu, choose Family Visit Visa. Enter each visitor's full name (as in passport), date of birth, nationality, passport number, and relationship to you.</p></div></div>
    <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Purchase Mandatory Health Insurance</h3><p>The system will prompt you to buy approved health insurance for each visitor. BUPA Saudi Arabia and other CCHI-approved insurers are listed. Cost: SAR 100–400 per person depending on age.</p></div></div>
    <div class="step"><div class="step-num">4</div><div class="step-body"><h3>Pay Visa Fee</h3><p>Pay by credit/debit card. Confirm the amount per person based on nationality. The fee is non-refundable once the visa is issued.</p></div></div>
    <div class="step"><div class="step-num">5</div><div class="step-body"><h3>Receive Visa Approval</h3><p>The approved visa is emailed within 1–5 business days. Print it and share with your family member. Some nationalities can use it for visa-on-arrival; others must apply at a Saudi embassy first.</p></div></div>
    <div class="step"><div class="step-num">6</div><div class="step-body"><h3>Visitor Arrives in Saudi Arabia</h3><p>At the airport, the visitor presents their passport and printed visa approval. Entry is granted for the duration specified (usually 30 or 90 days).</p></div></div>
  </div>

  <div class="card">
    <h2>📄 Required Documents</h2>
    <table>
      <tr><th>Document</th><th>Who Provides</th><th>Notes</th></tr>
      <tr><td>Valid Iqama of sponsor</td><td>You (the resident)</td><td>Must be valid, not expired</td></tr>
      <tr><td>Visitor's passport</td><td>Visiting family member</td><td>Minimum 6 months validity</td></tr>
      <tr><td>Proof of relationship</td><td>Both parties</td><td>Marriage certificate, birth certificate, etc.</td></tr>
      <tr><td>Health insurance</td><td>Purchased online during application</td><td>CCHI-approved insurer</td></tr>
      <tr><td>Sponsor's salary certificate</td><td>You (optional but helpful)</td><td>Some countries' embassies require it</td></tr>
    </table>
  </div>

  <div class="card">
    <h2>⚠️ Common Mistakes to Avoid</h2>
    <div class="warn-box">❌ <strong>Don't book flights before visa approval.</strong> Processing can take up to 5 business days. Wait for the email confirmation.</div>
    <div class="warn-box" style="margin-top:8px">❌ <strong>Don't enter visitor's name with nicknames.</strong> Name must match the passport exactly — middle names included.</div>
    <div class="warn-box" style="margin-top:8px">❌ <strong>Don't forget health insurance.</strong> It is now mandatory for all family visit visa applicants without exception.</div>
    <div class="warn-box" style="margin-top:8px">❌ <strong>Don't extend the stay beyond the visa duration</strong> without applying for an extension via Absher. Overstay penalties are SAR 10,000+.</div>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>How long can my family stay on a visit visa?</summary><div class="faq-answer">Usually 90 days on a single entry. Some nationalities are limited to 30 days. You can apply for one extension through Absher Business for an additional 90 days if needed.</div></details>
    <details><summary>Can my family work on a visit visa?</summary><div class="faq-answer">Absolutely not. Working on a visit visa is illegal and can result in deportation, heavy fines for the employer, and a ban on future entry. If family members need to work, they require a proper work/resident visa.</div></details>
    <details><summary>Can I apply for multiple family members at once?</summary><div class="faq-answer">Yes. The MOFA portal allows you to add multiple visitors in one application. Each person pays their own visa fee and health insurance.</div></details>
    <details><summary>My application was rejected — what can I do?</summary><div class="faq-answer">Rejection reasons are not always disclosed. Common reasons include: invalid passport, passport too close to expiry, security flags, or incorrect information. Re-apply after correcting the issue, or contact MOFA helpdesk at 920002814.</div></details>
  </div>
</main>
{FOOTER}
<script>
  function calcVisaCost() {{
    const count = parseInt(document.getElementById('familyCount').value) || 1;
    const feePerPerson = parseInt(document.getElementById('visaNat').value);
    const insPerPerson = parseInt(document.getElementById('insuranceAmt').value) || 150;
    const visaTotal = count * feePerPerson;
    const insTotal = count * insPerPerson;
    const grand = visaTotal + insTotal;
    document.getElementById('visaFeeTotal').textContent = 'SAR ' + visaTotal.toLocaleString();
    document.getElementById('insTotal').textContent = 'SAR ' + insTotal.toLocaleString();
    document.getElementById('grandTotal').textContent = 'SAR ' + grand.toLocaleString();
    document.getElementById('visaCostResult').style.display = 'block';
  }}
</script>
</body>
</html>"""

with open(f"{OUT}/family-visit-visa-guide.html", "w", encoding="utf-8") as f:
    f.write(famvisa)
print("✓ family-visit-visa-guide.html")

# ============================================================
# PAGE 6: Driving License Conversion Guide
# ============================================================
driving = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Saudi Arabia Driving License Conversion 2026 — Expat Guide, Cost &amp; Eligible Countries</title>
  <meta name="description" content="Convert your foreign driving license to Saudi Arabia license 2026. Full guide: eligible countries (47+), cost SAR 350–600, steps, medical test, and which nationalities need to take the test.">
  <link rel="canonical" href="https://www.saudiutilityhub.com/driving-license-conversion.html">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.saudiutilityhub.com/driving-license-conversion.html">
  <meta property="og:title" content="Saudi Arabia Driving License Conversion 2026 — Expat Guide">
  <meta property="og:description" content="Full guide to converting your foreign driving license in Saudi Arabia. Eligible countries, fees, steps, and medical test info.">
  <meta property="og:image" content="https://www.saudiutilityhub.com/og-image.png">
  <link rel="alternate" hreflang="en" href="https://www.saudiutilityhub.com/driving-license-conversion.html">
  <link rel="alternate" hreflang="x-default" href="https://www.saudiutilityhub.com/driving-license-conversion.html">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"HowTo","name":"How to Convert Foreign Driving License to Saudi License 2026","description":"Step-by-step process to convert your foreign driving license to a Saudi Arabian driving license.","step":[
    {{"@type":"HowToStep","name":"Confirm Eligibility","text":"Check if your home country is on the 47+ approved countries list. If yes, no driving test required."}},
    {{"@type":"HowToStep","name":"Get Arabic Translation","text":"Have your foreign license officially translated into Arabic by a certified translator. Cost: ~SAR 100."}},
    {{"@type":"HowToStep","name":"Medical Examination","text":"Visit an approved medical center for eye test and general health check. Cost: ~SAR 100–200."}},
    {{"@type":"HowToStep","name":"Book Absher Appointment","text":"Log in to Absher Individuals → Traffic Services → Book an appointment at your nearest traffic department."}},
    {{"@type":"HowToStep","name":"Submit Documents","text":"Attend appointment with: valid Iqama, original foreign license, Arabic translation, medical certificate, passport copy, and 2 passport photos."}},
    {{"@type":"HowToStep","name":"Receive Saudi License","text":"Your Saudi driving license is issued on the spot or within 1–3 days. Valid for 10 years."}}
  ]}}
  </script>
  <style>{NAV_CSS}
    .country-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px;margin-top:12px}}
    .country-tag{{background:#dcfce7;color:#166534;padding:5px 10px;border-radius:6px;font-size:.82rem;font-weight:600;text-align:center}}
    .country-tag.no-test{{background:#dbeafe;color:#1e40af}}
    .country-tag.test-req{{background:#fee2e2;color:#991b1b}}
    .eligibility-result{{padding:16px;border-radius:10px;margin-top:16px;font-size:.95rem;font-weight:600}}
  </style>
</head>
<body>
{NAV}
<section class="hero">
  <h1>🚗 Saudi Arabia Driving License Conversion 2026</h1>
  <p>Full guide for expats — which countries are eligible, what documents you need, cost, and step-by-step process.</p>
</section>
<main>
  <div class="card">
    <h2>🔍 Check Your Country's Eligibility</h2>
    <label>Select your home country / nationality</label>
    <select id="countryCheck">
      <option value="">-- Select your country --</option>
      <optgroup label="✅ No Driving Test Required">
        <option value="no_test">USA</option>
        <option value="no_test">UK / United Kingdom</option>
        <option value="no_test">Canada</option>
        <option value="no_test">Australia</option>
        <option value="no_test">New Zealand</option>
        <option value="no_test">Germany</option>
        <option value="no_test">France</option>
        <option value="no_test">Italy</option>
        <option value="no_test">Spain</option>
        <option value="no_test">Netherlands</option>
        <option value="no_test">Sweden</option>
        <option value="no_test">Norway</option>
        <option value="no_test">Denmark</option>
        <option value="no_test">Finland</option>
        <option value="no_test">Belgium</option>
        <option value="no_test">Switzerland</option>
        <option value="no_test">Austria</option>
        <option value="no_test">Ireland</option>
        <option value="no_test">Japan</option>
        <option value="no_test">South Korea</option>
        <option value="no_test">Singapore</option>
        <option value="no_test">UAE</option>
        <option value="no_test">Kuwait</option>
        <option value="no_test">Bahrain</option>
        <option value="no_test">Qatar</option>
        <option value="no_test">Oman</option>
        <option value="no_test">Turkey</option>
        <option value="no_test">South Africa</option>
        <option value="no_test">Argentina</option>
        <option value="no_test">Brazil</option>
      </optgroup>
      <optgroup label="⚠️ Driving Test Required">
        <option value="test_req">Pakistan</option>
        <option value="test_req">India</option>
        <option value="test_req">Bangladesh</option>
        <option value="test_req">Philippines</option>
        <option value="test_req">Indonesia</option>
        <option value="test_req">Nepal</option>
        <option value="test_req">Sri Lanka</option>
        <option value="test_req">Egypt</option>
        <option value="test_req">Sudan</option>
        <option value="test_req">Ethiopia</option>
        <option value="test_req">Nigeria</option>
        <option value="test_req">Ghana</option>
        <option value="test_req">Yemen</option>
        <option value="test_req">Other (not on list)</option>
      </optgroup>
    </select>
    <div id="eligResult" style="display:none" class="eligibility-result"></div>
  </div>

  <div class="card">
    <h2>💰 Estimated Cost</h2>
    <table>
      <tr><th>Item</th><th>Cost (SAR)</th></tr>
      <tr><td>Arabic translation of license</td><td>~SAR 100</td></tr>
      <tr><td>Medical examination (eye + general)</td><td>SAR 100–200</td></tr>
      <tr><td>License issuance fee</td><td>SAR 100–300</td></tr>
      <tr><td>Driving school (test required countries)</td><td>SAR 800–2,000</td></tr>
      <tr><td>Theory + practical test fee (if applicable)</td><td>SAR 200–400</td></tr>
      <tr><td style="font-weight:700">Total (no-test countries)</td><td style="font-weight:700;color:#1a56db">SAR 300–600</td></tr>
      <tr><td style="font-weight:700">Total (test required countries)</td><td style="font-weight:700;color:#1a56db">SAR 1,200–2,600</td></tr>
    </table>
  </div>

  <div class="card">
    <h2>📋 Step-by-Step Process</h2>
    <div class="step"><div class="step-num">1</div><div class="step-body"><h3>Confirm Eligibility</h3><p>Check if your home country is on the approved list above. GCC countries, US, UK, EU, Canada, Australia, Japan, South Korea, Singapore — no driving test required.</p></div></div>
    <div class="step"><div class="step-num">2</div><div class="step-body"><h3>Get Arabic Translation</h3><p>Have your foreign license officially translated to Arabic by a certified legal translator. Cost ~SAR 100, takes 1–2 days. Required even if you speak Arabic.</p></div></div>
    <div class="step"><div class="step-num">3</div><div class="step-body"><h3>Medical Examination</h3><p>Visit any approved medical center. You'll get an eye test, blood group check, and general health check. Costs SAR 100–200 and takes under 1 hour. Ask Absher for approved centers near you.</p></div></div>
    <div class="step"><div class="step-num">4</div><div class="step-body"><h3>Book Appointment via Absher</h3><p>Log in to <a href="https://www.absher.sa" target="_blank">absher.sa</a> → Individuals → Traffic Services → Driving License Conversion → Book appointment at your nearest traffic department.</p></div></div>
    <div class="step"><div class="step-num">5</div><div class="step-body"><h3>Attend Appointment with Documents</h3><p>Bring: valid original Iqama, original foreign license, Arabic translation, medical certificate, passport copy (bio page), 2 recent passport-sized photos.</p></div></div>
    <div class="step"><div class="step-num">6</div><div class="step-body"><h3>Receive Saudi Driving License</h3><p>Your Saudi license is issued on the same day or within 1–3 business days. It's valid for 10 years and allows you to drive all over the GCC.</p></div></div>
    <div class="warn-box" style="margin-top:4px">⏰ You must convert your license within <strong>3 months</strong> of receiving your Iqama. You can drive on your foreign license for the first year but conversion is recommended early.</div>
  </div>

  <div class="card">
    <h2>📄 Documents Checklist</h2>
    <table>
      <tr><th>Document</th><th>Required?</th></tr>
      <tr><td>Valid Iqama (original)</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>Original foreign driving license</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>Arabic translation of license</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>Medical certificate (eye + health check)</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>Passport copy (bio data page)</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>2 passport-sized photos</td><td><span class="badge badge-green">Required</span></td></tr>
      <tr><td>Absher appointment confirmation</td><td><span class="badge badge-blue">Recommended</span></td></tr>
      <tr><td>Driving school certificate</td><td><span class="badge badge-red">If test required</span></td></tr>
    </table>
  </div>

  <div class="card">
    <h2>❓ Frequently Asked Questions</h2>
    <details><summary>Can I drive in Saudi Arabia on my foreign license?</summary><div class="faq-answer">Yes, for up to 1 year from arrival. However, if you're a resident (have Iqama), you should convert within 3 months. After 1 year, driving on a foreign license is technically illegal and your insurance may not cover accidents.</div></details>
    <details><summary>My country requires a test — what does the driving test involve?</summary><div class="faq-answer">The test has two parts: (1) Theory test on Saudi traffic rules and signs — multiple choice questions, usually in Arabic/English. (2) Practical driving test in a traffic department yard — you'll be assessed on basic maneuvers and road rules. Most driving schools prepare you for both.</div></details>
    <details><summary>Can I use a Saudi driving license in other GCC countries?</summary><div class="faq-answer">Yes. Saudi driving licenses are recognized across all GCC countries (UAE, Bahrain, Kuwait, Qatar, Oman) without any additional paperwork.</div></details>
    <details><summary>What if my Iqama is renewed — do I need to renew my driving license?</summary><div class="faq-answer">No. Saudi driving licenses are valid for 10 years regardless of Iqama renewal cycles. You only renew the license when it expires.</div></details>
    <details><summary>Is an international driving permit (IDP) accepted in Saudi Arabia?</summary><div class="faq-answer">An IDP is accepted for tourists and short-term visitors. Residents with an Iqama must convert to a Saudi license — an IDP is not a permanent substitute.</div></details>
  </div>
</main>
{FOOTER}
<script>
  document.getElementById('countryCheck').addEventListener('change', function() {{
    const val = this.value;
    const res = document.getElementById('eligResult');
    if(!val) {{ res.style.display='none'; return; }}
    res.style.display = 'block';
    if(val === 'no_test') {{
      res.style.background = '#dcfce7'; res.style.border = '1px solid #86efac'; res.style.color = '#166534';
      res.innerHTML = '✅ <strong>No Driving Test Required!</strong> Your country is on the approved list. You only need Arabic translation of your license + medical check. Estimated total cost: SAR 300–600.';
    }} else {{
      res.style.background = '#fefce8'; res.style.border = '1px solid #fde68a'; res.style.color = '#92400e';
      res.innerHTML = '⚠️ <strong>Driving Test Required.</strong> Your country is not on the exemption list. You will need to complete a driving school course and pass both the theory and practical tests. Estimated total cost: SAR 1,200–2,600.';
    }}
  }});
</script>
</body>
</html>"""

with open(f"{OUT}/driving-license-conversion.html", "w", encoding="utf-8") as f:
    f.write(driving)
print("✓ driving-license-conversion.html")

print("\n✅ All 6 pages built successfully!")
