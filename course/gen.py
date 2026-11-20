"""Generates the course pages in src/ from the module content in course/*.py.

Courses:
  Root Cause Clinical Course   modules_a.py + modules_b.py -> src/learn.html, src/learn-mNN.html  (/learn/)
  Wound and Foot Care Course   wound_a.py + wound_b.py     -> src/wound.html, src/wound-mNN.html  (/learn/wound-care/)

Run: python3 course/gen.py && python3 build.py
"""
from html import escape
from pathlib import Path
import sys

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import modules_a, modules_b, wound_a, wound_b  # noqa: E402,E401

SRC = HERE.parent / "src"

COURSES = [
    dict(key="learn", prefix="learn/", name="Root Cause Clinical Course",
         modules=modules_a.MODULES + modules_b.MODULES),
    dict(key="wound", prefix="learn/wound-care/", name="Wound and Foot Care Course",
         modules=wound_a.MODULES + wound_b.MODULES),
]

QUIZ_JS = """<script>
document.querySelectorAll('form.check').forEach(function (f) {
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var picked = f.querySelector('input:checked');
    var out = f.querySelector('.result');
    if (!picked) { out.textContent = 'Choose an answer first.'; return; }
    var ok = picked.value === f.dataset.answer;
    out.className = 'result ' + (ok ? 'ok' : 'no');
    out.textContent = (ok ? 'Correct. ' : 'Not quite. ') + f.dataset.explain;
  });
});
</script>"""


def quiz(mnum, i, q):
    question, options, answer, explain = q
    labels = "\n".join(
        f'          <label><input type="radio" name="m{mnum}q{i}" value="{j}"> {escape(o)}</label>'
        for j, o in enumerate(options))
    return f"""      <form class="check" data-answer="{answer}" data-explain="{escape(explain)}">
        <fieldset>
          <legend>Question {i}: {escape(question)}</legend>
{labels}
        </fieldset>
        <button class="btn" type="submit">Check answer</button>
        <p class="result" role="status"></p>
      </form>"""


def page(course, idx, m):
    mods = course["modules"]
    pre = course["prefix"]
    n = m["num"]
    prev_m = mods[idx - 1] if idx > 0 else None
    next_m = mods[idx + 1] if idx + 1 < len(mods) else None
    nav = "\n".join(f'        <li><a href="#{lid}">{escape(t)}</a></li>' for lid, t, _ in m["lessons"])
    lessons = "\n\n".join(
        f'      <section class="lesson" id="{lid}">\n        <div class="eyebrow">Lesson {k} of {len(m["lessons"])}</div>\n        <h2>{escape(t)}</h2>\n{body}\n      </section>'
        for k, (lid, t, body) in enumerate(m["lessons"], 1))
    objectives = "\n".join(f"          <li>{o}</li>" for o in m["objectives"])
    pearls = "\n".join(f"          <li>{p}</li>" for p in m["pearls"])
    flags = "\n".join(f"          <li>{p}</li>" for p in m["redflags"])
    quizzes = "\n".join(quiz(n, i, q) for i, q in enumerate(m["quiz"], 1))
    refs = "\n".join(f"          <li>{r}</li>" for r in m["refs"])
    all_link = f'{{base}}{pre}'
    prev_link = (f'<a class="btn ghost" href="{{base}}{pre}{prev_m["slug"]}/">&larr; Module {prev_m["num"]}</a>'
                 if prev_m else f'<a class="btn ghost" href="{all_link}">All modules</a>')
    next_link = (f'<a class="btn" href="{{base}}{pre}{next_m["slug"]}/">Next: {escape(next_m["title"])} &rarr;</a>'
                 if next_m else f'<a class="btn" href="{all_link}">Back to all modules</a>')
    case_q, case_a = m["case"]
    h_title, h_body = m["handout"]
    return f"""title: {m["title"]} | {course["name"]}
description: {m["summary"]} Module {n} of the free Empowered Health {course["name"]} for providers, with a patient handout.
path: {pre}{m["slug"]}/index.html

<section class="hero small">
  <div class="wrap">
    <div class="eyebrow" style="color:#cfe6a8">{course["name"]} · Module {n} of {len(mods)} · {len(m["lessons"])} lessons · {m["minutes"]} min</div>
    <h1>{escape(m["title"])}</h1>
  </div>
</section>

<section>
  <div class="wrap lesson-layout">
    <aside class="lesson-nav">
      <h4>Module {n}</h4>
      <div class="progress" aria-label="Module {n} of {len(mods)}"><span style="width:{round(n / len(mods) * 100)}%"></span></div>
      <ol>
{nav}
      </ol>
      <ul class="lesson-extras">
        <li><a href="#review">Case and self-check</a></li>
        <li><a href="#handout">Patient handout</a></li>
      </ul>
      <p style="margin-top:8px"><a href="{all_link}">&larr; All modules</a></p>
    </aside>

    <article class="prose" style="min-width:0">
      <div class="objectives">
        <h3>Learning objectives</h3>
        <ul>
{objectives}
        </ul>
      </div>

{lessons}

      <div class="pearl">
        <h3>Clinical pearls</h3>
        <ul>
{pearls}
        </ul>
      </div>

      <div class="redflags">
        <h3>Red flags: refer or work up first</h3>
        <ul>
{flags}
        </ul>
      </div>

      <section id="review">
        <div class="case">
          <h3>Case</h3>
          <p>{case_q}</p>
          <details><summary>Show discussion</summary><p>{case_a}</p></details>
        </div>
{quizzes}
      </section>

      <div class="sources">
        <strong>References</strong>
        <ul>
{refs}
        </ul>
      </div>

      <div class="handout" id="handout">
        <div class="eyebrow">Patient handout · plain language</div>
        <h2>{escape(h_title)}</h2>
{h_body}
        <button class="btn ghost" type="button" onclick="window.print()">Print handout</button>
      </div>

      <div class="lesson-pager">
        {prev_link}
        {next_link}
      </div>

      <p class="disclaimer">General education for licensed clinicians and the public. Not medical advice, and not a substitute for clinical judgment, current guidelines, or a visit with a licensed provider. Product names are examples, not endorsements. Drug doses, coding rules and guidance change; check current labeling, payer rules and guidelines before acting. <a href="{{booking}}" target="_blank" rel="noopener">Book a visit with Empowered Health</a>.</p>
    </article>
  </div>
</section>
{QUIZ_JS}
"""


def cards(course):
    return "\n".join(
        f'      <a class="module" href="{m["slug"]}/"><span class="num">Module {m["num"]}</span><h3>{escape(m["title"])}</h3><p>{escape(m["summary"])}</p><span class="meta">{len(m["lessons"])} lessons · {m["minutes"]} min · patient handout</span></a>'
        for m in course["modules"])


def handout_list(course):
    return "\n".join(
        f'        <li><a href="{m["slug"]}/#handout">{escape(m["handout"][0])}</a></li>' for m in course["modules"])


def other_course_card(href, eyebrow, title, text, cta):
    return f"""    <div class="course-cross">
      <div>
        <div class="eyebrow">{eyebrow}</div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>
      <a class="btn ghost" href="{href}">{cta}</a>
    </div>"""


def learn_index(course, wound):
    mods = course["modules"]
    total = sum(m["minutes"] for m in mods)
    return f"""title: Root Cause Clinical Course for Providers | Empowered Health
description: A free functional medicine course for clinicians from Empowered Health: evidence-based, root-cause care for metabolic, gut, thyroid, hormone, sleep and stress concerns, with patient handouts.
path: learn/index.html

<section class="hero small">
  <div class="wrap">
    <div class="eyebrow" style="color:#cfe6a8">Free course for clinicians</div>
    <h1>Root Cause Clinical Course: Functional Medicine for Providers</h1>
    <p>{len(mods)} evidence-focused modules (about {round(total / 60)} hours) for NPs, PAs, physicians and nurses who want to bring root-cause thinking into everyday practice. Every module ends with a plain-language patient handout you can share.</p>
    <div class="actions">
      <a class="btn" href="{mods[0]["slug"]}/">Start Module 1</a>
      <a class="btn light" href="#patients">I'm a patient</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
{other_course_card("wound-care/", "Also free", "Wound and Foot Care Course", f"{len(wound['modules'])} modules on wound assessment, dressings, compression, offloading, infection, documentation and foot care.", "View the wound care course")}
    <h2>Course modules</h2>
    <p class="lead">Each module has short lessons with workup tables, clinical pearls, red flags for referral, a case, self-check questions, current guideline references, and a printable patient handout. Free, no sign-up, at your own pace.</p>
    <div class="modules">
{cards(course)}
    </div>

    <div id="patients" class="patient-callout">
      <h3>For patients</h3>
      <p>Each module ends with a short handout written for you, in plain language:</p>
      <ul class="handout-list">
{handout_list(course)}
      </ul>
      <p>Looking for wound or foot care information? See the <a href="wound-care/#patients">wound and foot care handouts</a>. Questions about your own health? <a href="{{booking}}" target="_blank" rel="noopener">Book a visit with Empowered Health</a>.</p>
    </div>
    <p class="course-note">This course is for general education. It is not medical advice, does not replace clinical judgment or current guidelines, and does not offer continuing education credit.</p>
  </div>
</section>
"""


def wound_index(course, learn):
    mods = course["modules"]
    total = sum(m["minutes"] for m in mods)
    return f"""title: Wound and Foot Care Course for Providers | Empowered Health
description: A free wound and foot care course for clinicians from Empowered Health: wound types, assessment, dressings, compression, offloading, infection, prevention, documentation and foot care, with patient handouts.
path: learn/wound-care/index.html

<section class="hero small">
  <div class="wrap">
    <div class="eyebrow" style="color:#cfe6a8">Free course for clinicians</div>
    <h1>Wound and Foot Care Course</h1>
    <p>{len(mods)} practical modules (about {round(total / 60)} hours) from Heath Tunnell, FNP-BC, CWCN-AP, WCS-C, on assessing, treating and preventing wounds and caring for feet. Every module ends with a plain-language patient handout.</p>
    <div class="actions">
      <a class="btn" href="{mods[0]["slug"]}/">Start Module 1</a>
      <a class="btn light" href="#patients">I'm a patient</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
{other_course_card("../", "Also free", "Root Cause Clinical Course", f"{len(learn['modules'])} modules on functional medicine: nutrition, gut, metabolic health, thyroid, hormones, sleep and labs.", "View the functional medicine course")}
    <h2>Course modules</h2>
    <p class="lead">Each module has short lessons with step-by-step how-tos, decision tables, clinical pearls, red flags for referral, a case, self-check questions, references, and a printable patient handout. Free, no sign-up, at your own pace.</p>
    <div class="modules">
{cards(course)}
    </div>

    <div id="patients" class="patient-callout">
      <h3>For patients and families</h3>
      <p>Each module ends with a short handout written for you, in plain language:</p>
      <ul class="handout-list">
{handout_list(course)}
      </ul>
      <p>Need help with a wound or your feet? <a href="{{booking}}" target="_blank" rel="noopener">Book a visit with Empowered Health</a>. If a wound shows signs of spreading infection, such as fever, spreading redness or confusion, get medical care right away.</p>
    </div>
    <p class="course-note">This course is for general education. It is not medical advice, does not certify anyone to perform wound or foot care, does not replace clinical judgment, current guidelines or payer rules, and does not offer continuing education credit. Product names are examples, not endorsements.</p>
  </div>
</section>
"""


def main():
    for pattern in ("learn-m*.html", "wound-m*.html"):
        for old in SRC.glob(pattern):
            old.unlink()
    learn, wound = COURSES
    (SRC / "learn.html").write_text(learn_index(learn, wound))
    (SRC / "wound.html").write_text(wound_index(wound, learn))
    for course in COURSES:
        for i, m in enumerate(course["modules"]):
            (SRC / f"{course['key']}-m{m['num']:02d}.html").write_text(page(course, i, m))
        print(f"{course['name']}: index and {len(course['modules'])} module pages")


if __name__ == "__main__":
    main()
