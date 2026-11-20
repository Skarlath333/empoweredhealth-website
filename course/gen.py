"""Generates the course pages src/learn.html and src/learn-mNN.html from the module content in course/modules_*.py.

Run: python3 course/gen.py && python3 build.py
"""
from html import escape
from pathlib import Path
import sys

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from modules_a import MODULES as A  # noqa: E402
from modules_b import MODULES as B  # noqa: E402

MODULES = A + B
SRC = HERE.parent / "src"

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


def page(idx, m):
    n = m["num"]
    prev_m = MODULES[idx - 1] if idx > 0 else None
    next_m = MODULES[idx + 1] if idx + 1 < len(MODULES) else None
    nav = "\n".join(f'        <li><a href="#{lid}">{escape(t)}</a></li>' for lid, t, _ in m["lessons"])
    lessons = "\n\n".join(
        f'      <section class="lesson" id="{lid}">\n        <div class="eyebrow">Lesson {k} of {len(m["lessons"])}</div>\n        <h2>{escape(t)}</h2>\n{body}\n      </section>'
        for k, (lid, t, body) in enumerate(m["lessons"], 1))
    objectives = "\n".join(f"          <li>{o}</li>" for o in m["objectives"])
    pearls = "\n".join(f"          <li>{p}</li>" for p in m["pearls"])
    flags = "\n".join(f"          <li>{p}</li>" for p in m["redflags"])
    quizzes = "\n".join(quiz(n, i, q) for i, q in enumerate(m["quiz"], 1))
    refs = "\n".join(f"          <li>{r}</li>" for r in m["refs"])
    prev_link = (f'<a class="btn ghost" href="{{base}}learn/{prev_m["slug"]}/">&larr; Module {prev_m["num"]}</a>'
                 if prev_m else '<a class="btn ghost" href="{base}learn/">All modules</a>')
    next_link = (f'<a class="btn" href="{{base}}learn/{next_m["slug"]}/">Next: {escape(next_m["title"])} &rarr;</a>'
                 if next_m else '<a class="btn" href="{base}learn/">Back to all modules</a>')
    case_q, case_a = m["case"]
    h_title, h_body = m["handout"]
    return f"""title: {m["title"]} | Root Cause Clinical Course
description: {m["summary"]} Module {n} of the free Empowered Health functional medicine course for providers, with a patient handout.
path: learn/{m["slug"]}/index.html

<section class="hero small">
  <div class="wrap">
    <div class="eyebrow" style="color:#cfe6a8">Module {n} of {len(MODULES)} · {len(m["lessons"])} lessons · {m["minutes"]} min</div>
    <h1>{escape(m["title"])}</h1>
  </div>
</section>

<section>
  <div class="wrap lesson-layout">
    <aside class="lesson-nav">
      <h4>Module {n}</h4>
      <div class="progress" aria-label="Module {n} of {len(MODULES)}"><span style="width:{round(n / len(MODULES) * 100)}%"></span></div>
      <ol>
{nav}
      </ol>
      <ul class="lesson-extras">
        <li><a href="#review">Case and self-check</a></li>
        <li><a href="#handout">Patient handout</a></li>
      </ul>
      <p style="margin-top:8px"><a href="{{base}}learn/">&larr; All modules</a></p>
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

      <p class="disclaimer">General education for licensed clinicians and the public. Not medical advice, and not a substitute for clinical judgment, current guidelines, or a visit with a licensed provider. Drug doses and guidance change; check current labeling and guidelines before prescribing. <a href="{{booking}}" target="_blank" rel="noopener">Book a visit with Empowered Health</a>.</p>
    </article>
  </div>
</section>
{QUIZ_JS}
"""


def index():
    total = sum(m["minutes"] for m in MODULES)
    cards = "\n".join(
        f'      <a class="module" href="{m["slug"]}/"><span class="num">Module {m["num"]}</span><h3>{escape(m["title"])}</h3><p>{escape(m["summary"])}</p><span class="meta">{len(m["lessons"])} lessons · {m["minutes"]} min · patient handout</span></a>'
        for m in MODULES)
    handouts = "\n".join(
        f'        <li><a href="{m["slug"]}/#handout">{escape(m["handout"][0])}</a></li>' for m in MODULES)
    return f"""title: Root Cause Clinical Course for Providers | Empowered Health
description: A free functional medicine course for clinicians from Empowered Health: evidence-based, root-cause care for metabolic, gut, thyroid, hormone, sleep and stress concerns, with patient handouts.
path: learn/index.html

<section class="hero small">
  <div class="wrap">
    <div class="eyebrow" style="color:#cfe6a8">Free course for clinicians</div>
    <h1>Root Cause Clinical Course: Functional Medicine for Providers</h1>
    <p>{len(MODULES)} evidence-focused modules (about {round(total / 60)} hours) for NPs, PAs, physicians and nurses who want to bring root-cause thinking into everyday practice. Every module ends with a plain-language patient handout you can share.</p>
    <div class="actions">
      <a class="btn" href="{MODULES[0]["slug"]}/">Start Module 1</a>
      <a class="btn light" href="#patients">I'm a patient</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Course modules</h2>
    <p class="lead">Each module has short lessons with workup tables, clinical pearls, red flags for referral, a case, self-check questions, current guideline references, and a printable patient handout. Free, no sign-up, at your own pace.</p>
    <div class="modules">
{cards}
    </div>

    <div id="patients" class="patient-callout">
      <h3>For patients</h3>
      <p>Each module ends with a short handout written for you, in plain language:</p>
      <ul class="handout-list">
{handouts}
      </ul>
      <p>Questions about your own health? <a href="{{booking}}" target="_blank" rel="noopener">Book a visit with Empowered Health</a>.</p>
    </div>
    <p class="course-note">This course is for general education. It is not medical advice, does not replace clinical judgment or current guidelines, and does not offer continuing education credit.</p>
  </div>
</section>
"""


def main():
    for old in SRC.glob("learn-m*.html"):
        old.unlink()
    (SRC / "learn.html").write_text(index())
    for i, m in enumerate(MODULES):
        (SRC / f"learn-m{m['num']:02d}.html").write_text(page(i, m))
    print(f"wrote learn.html and {len(MODULES)} module pages")


if __name__ == "__main__":
    main()
