# Shared CSS, nav, footer, scripts — sourced by page scripts
SHARED_CSS='<style>
:root{--green:#0a7c3e;--green-dark:#065a2d;--green-light:#e8f5ee;--gold:#c9a227;--text:#1a1a2e;--muted:#5a6375;--border:#e2e8f0;--bg:#f4f7f4;--white:#fff;--shadow:0 2px 12px rgba(0,0,0,.07);--radius:12px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;color:var(--text);background:var(--bg);line-height:1.65;font-size:15px;}
a{text-decoration:none;color:inherit;}
nav{background:var(--green-dark);position:sticky;top:0;z-index:200;box-shadow:0 2px 10px rgba(0,0,0,.25);}
.nav-inner{max-width:1100px;margin:0 auto;padding:0 20px;display:flex;align-items:center;height:54px;gap:2px;}
.nav-brand{color:#fff;font-weight:800;font-size:1rem;padding-right:14px;white-space:nowrap;flex-shrink:0;}
.nav-links{display:flex;align-items:center;gap:0;flex:1;overflow-x:auto;}
.nav-links a{color:rgba(255,255,255,.82);font-size:.81rem;padding:18px 8px;white-space:nowrap;transition:color .15s;border-bottom:2px solid transparent;}
.nav-links a:hover,.nav-links a.active{color:#fff;border-bottom-color:#ffd166;}
.nav-ar{background:rgba(255,255,255,.13);color:#ffd166!important;border:1px solid rgba(255,255,255,.2);border-radius:6px;padding:5px 12px!important;font-weight:700!important;margin-right:8px;border-bottom:none!important;}
.page-wrap{max-width:860px;margin:0 auto;padding:24px 20px 48px;}
.breadcrumb{font-size:13px;color:var(--muted);margin-bottom:14px;}
.breadcrumb a{color:var(--muted);}
.breadcrumb a:hover{color:var(--green);}
h1{font-size:1.7rem;font-weight:800;line-height:1.25;margin-bottom:6px;}
h2{font-size:1.15rem;font-weight:700;margin:28px 0 10px;color:var(--green-dark);}
h3{font-size:1rem;font-weight:700;margin:18px 0 6px;}
p{margin-bottom:12px;font-size:.95rem;line-height:1.7;}
.page-meta{color:var(--muted);font-size:.82rem;margin-bottom:20px;}
.ad-slot{background:#f0f4f8;border-radius:8px;min-height:90px;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:11px;margin:18px 0;text-align:center;}
.calc-card{background:var(--white);border-radius:var(--radius);border:1.5px solid var(--border);padding:24px;margin-bottom:16px;box-shadow:var(--shadow);}
.field{margin-bottom:14px;}
.field label{display:block;font-size:12px;font-weight:700;color:var(--muted);margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px;}
.field input,.field select{width:100%;padding:11px 13px;border:1.5px solid var(--border);border-radius:8px;font-size:.95rem;font-family:inherit;color:var(--text);background:var(--white);transition:border-color .15s;}
.field input:focus,.field select:focus{outline:none;border-color:var(--green);box-shadow:0 0 0 3px rgba(10,124,62,.1);}
.field-hint{font-size:11px;color:#aaa;margin-top:3px;}
.fields-2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media(max-width:520px){.fields-2{grid-template-columns:1fr;}}
.calc-btn{width:100%;margin-top:6px;background:var(--green);color:#fff;border:none;padding:13px 20px;border-radius:10px;font-size:1rem;font-weight:700;cursor:pointer;transition:background .15s;}
.calc-btn:hover{background:var(--green-dark);}
.results{margin-top:18px;display:none;}
.results.show{display:block;}
.result-hero{background:linear-gradient(135deg,var(--green-dark),var(--green));color:#fff;border-radius:var(--radius);padding:22px;text-align:center;margin-bottom:14px;}
.result-hero .big{font-size:2.4rem;font-weight:800;display:block;margin:6px 0;}
.result-hero .lbl{font-size:13px;opacity:.85;}
.result-hero .sub{font-size:12px;opacity:.7;margin-top:4px;}
.result-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;}
@media(max-width:480px){.result-grid{grid-template-columns:1fr;}}
.rg-item{background:#f8fafc;border:1px solid var(--border);border-radius:8px;padding:12px 14px;}
.rg-item .rl{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;display:block;margin-bottom:3px;}
.rg-item .rv{font-size:1.1rem;font-weight:700;color:var(--green-dark);}
.rg-item.neg .rv{color:#e53e3e;}
.rg-item.pos .rv{color:var(--green);}
.info-box{background:#eaf7ef;border-left:4px solid var(--green);padding:13px 16px;border-radius:6px;font-size:.88rem;margin:14px 0;line-height:1.6;}
.warn-box{background:#fef9e7;border:1px solid #f0c040;border-radius:6px;padding:12px 16px;font-size:.85rem;color:#7d6608;margin:14px 0;line-height:1.6;}
table.data-tbl{width:100%;border-collapse:collapse;background:var(--white);border-radius:10px;overflow:hidden;margin:12px 0;box-shadow:var(--shadow);}
.data-tbl th{background:var(--green-dark);color:#fff;padding:10px 13px;text-align:left;font-size:.82rem;}
.data-tbl td{padding:9px 13px;border-bottom:1px solid #f0f0f0;font-size:.88rem;}
.data-tbl tr:last-child td{border-bottom:none;}
.data-tbl .total-row td{background:var(--green-light);font-weight:700;color:var(--green-dark);}
.faq-item{border:1.5px solid var(--border);border-radius:var(--radius);margin-bottom:8px;background:var(--white);box-shadow:var(--shadow);}
.faq-q{padding:14px 18px;font-weight:600;cursor:pointer;font-size:.9rem;display:flex;justify-content:space-between;align-items:center;gap:10px;user-select:none;}
.faq-q:hover{background:var(--green-light);}
.faq-icon{width:22px;height:22px;background:var(--green-light);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--green);font-size:1rem;font-weight:700;flex-shrink:0;transition:transform .25s,background .2s;}
.faq-item.open .faq-icon{transform:rotate(45deg);background:var(--green);color:#fff;}
.faq-a{display:none;padding:4px 18px 16px;font-size:.87rem;color:var(--muted);line-height:1.7;}
.faq-item.open .faq-a{display:block;}
.faq-a a{color:var(--green);font-weight:600;}
.tool-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(155px,1fr));gap:8px;margin:12px 0;}
.tool-link{background:var(--white);border:1.5px solid var(--border);border-radius:8px;padding:10px 13px;color:var(--green-dark);font-size:.83rem;font-weight:700;display:block;transition:all .15s;}
.tool-link:hover{background:var(--green-light);border-color:var(--green);}
.site-footer{background:var(--green-dark);color:rgba(255,255,255,.75);padding:36px 20px 16px;margin-top:40px;}
.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:22px;max-width:1100px;margin:0 auto 20px;}
.footer-grid h4{color:#fff;font-size:.8rem;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px;}
.footer-grid a{display:block;color:rgba(255,255,255,.6);font-size:.79rem;margin-bottom:5px;}
.footer-grid a:hover{color:#fff;}
.footer-bottom{text-align:center;font-size:.72rem;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:14px;max-width:1100px;margin:0 auto;}
.footer-bottom a{color:rgba(255,255,255,.4);}
#cookie-bar{position:fixed;bottom:0;left:0;right:0;background:#1a1a2e;color:rgba(255,255,255,.88);padding:13px 20px;display:flex;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap;font-size:.8rem;z-index:9000;box-shadow:0 -3px 16px rgba(0,0,0,.2);}
#cookie-bar a{color:#6ee7a7;text-decoration:underline;}
.cb-btn{border:none;border-radius:7px;padding:7px 16px;cursor:pointer;font-size:.8rem;font-weight:700;font-family:inherit;}
.cb-accept{background:var(--green);color:#fff;}
.cb-decline{background:transparent;color:rgba(255,255,255,.5);border:1px solid rgba(255,255,255,.2)!important;}
#back-top{position:fixed;bottom:76px;right:18px;width:40px;height:40px;background:var(--green);color:#fff;border:none;border-radius:50%;cursor:pointer;font-size:1.1rem;display:none;align-items:center;justify-content:center;box-shadow:0 3px 10px rgba(0,0,0,.2);z-index:8000;}
#back-top.show{display:flex;}
#back-top:hover{background:var(--green-dark);}
@media(max-width:600px){h1{font-size:1.35rem;}.nav-links a{padding:16px 5px;font-size:.75rem;}}
</style>'
echo "shared CSS defined"
