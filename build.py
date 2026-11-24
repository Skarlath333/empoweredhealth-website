"""Builds the static Empowered Health site into ./docs (served by GitHub Pages) from the page bodies in ./src.

Run: python3 build.py
Each src/*.html file starts with three lines:
  title: <page title>
  description: <meta description>
  path: <output path, e.g. index.html or hormone-replacement-therapy/index.html>
followed by a blank line and the page body HTML.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "docs"
SITE_URL = "https://www.empoweredhealthtn.com"
BOOKING_URL = "https://empoweredhealth.setmore.com"
# Course sign-ups go to HubSpot (free CRM) through its Forms API. Fill in both from the HubSpot form's share/embed code.
HUBSPOT_PORTAL_ID = ""
HUBSPOT_FORM_ID = ""
SIGNUP_URL = (f"https://api.hsforms.com/submissions/v3/integration/submit/{HUBSPOT_PORTAL_ID}/{HUBSPOT_FORM_ID}"
              if HUBSPOT_PORTAL_ID and HUBSPOT_FORM_ID else "")
# Course pages under learn/ need a sign-up first, except these open pages.
OPEN_LEARN_PAGES = {"learn/index.html", "learn/join/index.html"}
GATE = """<script>try{{if(localStorage.getItem("ehCourseAccess")!=="1"){{location.replace("{base}learn/join/?next="+encodeURIComponent(location.pathname+location.hash))}}}}catch(e){{}}</script>
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:image" content="{site}/assets/logo.webp">
<link rel="icon" href="{base}assets/logo-mark.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Manrope:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/styles.css">
{gate}<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"MedicalBusiness","name":"Empowered Health","url":"{site}/","email":"info@empoweredhealthtn.com","telephone":"+1-865-740-9361","description":"A telehealth-only medical practice serving patients across Tennessee.","areaServed":"Tennessee","sameAs":["https://www.facebook.com/EmpoweredHealthTN/"]}}
</script>
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{base}"><img src="{base}assets/logo-mark.webp" alt="" width="40" height="40">Empowered Health</a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" onclick="var n=document.querySelector('.nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))"><span></span><span></span><span></span></button>
    <nav class="nav">
      <a href="{base}#services">Services</a>
      <a class="nav-learn" href="{base}learn/">For providers</a>
      <a href="{base}hormone-replacement-therapy/">HRT</a>
      <a href="{base}#about">About</a>
      <a href="{base}#team">Team</a>
      <a href="{base}#order">Shop</a>
      <a class="btn" href="{booking}" target="_blank" rel="noopener">Book now</a>
    </nav>
  </div>
</header>
<main>
"""

FOOT = """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><img src="{base}assets/logo-mark.webp" alt="" width="40" height="40">Empowered Health</div>
        <p>A telehealth-only medical practice serving patients across Tennessee, and free clinical education for providers.</p>
      </div>
      <div>
        <h4>Patients</h4>
        <ul>
          <li><a href="{base}#about">About</a></li>
          <li><a href="{base}#services">Services</a></li>
          <li><a href="{base}hormone-replacement-therapy/">Hormone Replacement Therapy</a></li>
          <li><a href="{base}#team">Team</a></li>
          <li><a href="{base}#order">Supplements &amp; Labs</a></li>
        </ul>
      </div>
      <div>
        <h4>Providers</h4>
        <ul>
          <li><a href="{base}learn/">All free courses</a></li>
          <li><a href="{base}learn/functional-medicine/">Root Cause Clinical Course</a></li>
          <li><a href="{base}learn/wound-care/">Wound and Foot Care Course</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="{booking}" target="_blank" rel="noopener">Book an appointment</a></li>
          <li><a href="tel:+18657409361">(865) 740-9361</a></li>
          <li><a href="mailto:info@empoweredhealthtn.com">info@empoweredhealthtn.com</a></li>
          <li><a href="https://www.facebook.com/EmpoweredHealthTN/" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>&copy; <span id="yr">2026</span> Empowered Health. All rights reserved.</span>
      <a href="{base}privacy-policy/">Privacy Policy</a>
      <a href="{base}cookie-policy/">Cookie Policy</a>
      <a href="{base}tracker/" rel="nofollow">Staff</a>
    </div>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();
document.querySelectorAll('.nav a').forEach(function(a){{a.addEventListener('click',function(){{document.querySelector('.nav').classList.remove('open')}})}});</script>
</body>
</html>
"""


REDIRECT = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} | Empowered Health</title>
<link rel="canonical" href="{canonical}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}" + location.hash)</script>
</head>
<body><p>This page moved to <a href="{target}">{target}</a>.</p></body>
</html>
"""


def build():
    for src in sorted(SRC.glob("*.html")):
        text = src.read_text()
        header, body = text.split("\n\n", 1)
        meta = dict(line.split(": ", 1) for line in header.splitlines())
        path = meta["path"]
        if "redirect" in meta:
            out = OUT / path
            out.parent.mkdir(parents=True, exist_ok=True)
            target = meta["redirect"]
            out.write_text(REDIRECT.format(target=target, title=meta["title"], canonical=SITE_URL + target))
            print("wrote", out.relative_to(ROOT), "(redirect)")
            continue
        depth = path.count("/")
        base = meta.get("base") or ("../" * depth if depth else "./")
        canonical = SITE_URL + "/" + (path[: -len("index.html")] if path.endswith("index.html") else path)
        gated = path.startswith("learn/") and path not in OPEN_LEARN_PAGES
        ctx = dict(title=meta["title"], description=meta["description"], canonical=canonical,
                   site=SITE_URL, base=base, booking=BOOKING_URL,
                   gate=GATE.format(base=base) if gated else "")
        html = HEAD.format(**ctx) + body.replace("{base}", base).replace("{booking}", BOOKING_URL).replace("{signup}", SIGNUP_URL) + FOOT.format(**ctx)
        out = OUT / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    build()
