"""Wound and Foot Care Course, modules 6 to 10. See wound_a.py for sources."""
from modules_a import table

MODULES = [
# ---------------------------------------------------------------- 6
dict(
    num=6, slug="advanced-therapies", minutes=28,
    title="Advanced wound therapies",
    summary="Negative pressure wound therapy, skin substitutes and placental membranes, grafts, hyperbaric oxygen and other adjuncts.",
    objectives=[
        "Select patients for negative pressure wound therapy and apply it correctly.",
        "Know when cellular and tissue-based products, grafts and hyperbaric oxygen fit.",
        "Prepare the patient and wound so advanced therapies succeed.",
    ],
    lessons=[
        ("npwt", "Negative pressure wound therapy", """        <p>NPWT removes drainage, reduces edema, draws wound edges together and promotes granulation. It fits deep wounds with moderate to heavy drainage, dehisced surgical wounds, and graft fixation.</p>
        <p><strong>Before starting:</strong> treat osteomyelitis and untreated infection, debride necrotic tissue (a practical rule of thumb is at least 60% granulation in the bed), and confirm no exposed vessels, untreated cancer in the wound, or unexplored fistula. Use caution with anticoagulation.</p>
        <ol>
          <li>Cut the foam to fit the wound bed, without overlapping intact skin.</li>
          <li><strong>Windowpane</strong> the surrounding skin with strips of drape (or hydrocolloid) to prevent maceration.</li>
          <li>Place the foam, then cover with drape laid flat with no wrinkles or channels.</li>
          <li>Cut a small hole over the foam and apply the suction pad.</li>
          <li>Start at 125 mmHg continuous (common default), and check for a tight seal.</li>
          <li>Change about three times a week; check under tubing for device pressure injuries.</li>
        </ol>
        <p>Single-use, portable NPWT systems suit smaller, lower-drainage wounds and closed incisions.</p>"""),
        ("ctp", "Skin substitutes, grafts and other adjuncts", """""" + table(["Therapy", "Examples", "Best fit"], [
            ["Cellular and tissue-based products (skin substitutes)", "Bilayered living cell constructs, fish skin, dermal matrices", "Diabetic foot and venous ulcers that stall despite good standard care"],
            ["Placental membranes", "Dehydrated amniotic and chorionic membranes", "Same; rich in growth factors; need adequate perfusion"],
            ["Autologous skin grafts", "Split-thickness grafts by a surgeon", "Large clean wounds after failed conservative care"],
            ["Growth factor gel", "Becaplermin", "Neuropathic diabetic foot ulcers with good blood flow"],
            ["Hyperbaric oxygen", "Chamber-based therapy", "Selected Wagner grade 3+ diabetic foot ulcers, radiation injury, some refractory osteomyelitis"],
            ["Electrical stimulation, ultrasound mist", "Pulsed current, low-frequency ultrasound", "Adjuncts for stalled wounds and biofilm"],
        ]) + """
        <p><strong>Make them count.</strong> Advanced products fail on wounds with poor perfusion, uncontrolled infection, ongoing pressure or poor nutrition. Fix those first. Document at least 4 weeks of failed standard care with measurements, since payers and Medicare coverage policies for skin substitutes require it, and get prior authorization where needed. Coverage rules for skin substitutes are changing, so check current Medicare and payer policies before applying.</p>"""),
    ],
    pearls=[
        "Windowpane the edges and get a flat, tight seal. Most NPWT failures are leaks.",
        "Advanced products amplify good care. They don't replace offloading, perfusion and nutrition.",
        "Measure and document weekly so you can show a stall before moving to advanced therapy.",
    ],
    redflags=[
        "Bleeding into the NPWT canister: stop therapy and evaluate immediately.",
        "Untreated osteomyelitis or exposed vessels: NPWT is not appropriate.",
        "Graft failure or infection after a skin substitute: reassess perfusion, infection and pressure.",
    ],
    case=("A clean, granulating stage 4 sacral wound (80% granulation, heavy drainage) has no signs of osteomyelitis on MRI. The patient is on a low air loss mattress and eating well.",
          "A good NPWT candidate. Windowpane the edges, cut foam to the bed, seal flat, run 125 mmHg continuous, and change three times a week while keeping pressure off the sacrum. Track weekly measurements."),
    quiz=[
        ("Which must be addressed before starting NPWT?",
         ["Untreated osteomyelitis", "Mild drainage", "Granulation tissue"], 0,
         "Osteomyelitis and untreated infection must be treated before NPWT."),
        ("Why do skin substitutes often fail?",
         ["They are applied too early in clean wounds", "Ongoing pressure, poor perfusion, infection or poor nutrition", "Too much granulation"], 1,
         "Advanced products need the same foundations as any wound: offloading, perfusion, infection control and nutrition."),
    ],
    refs=[
        "Apelqvist J, et al. EWMA Document: Negative Pressure Wound Therapy. J Wound Care. 2017.",
        "IWGDF guideline on interventions to enhance healing of foot ulcers in people with diabetes. 2023.",
        "Lavery LA, et al. WHS guidelines update: diabetic foot ulcer treatment guidelines. Wound Repair Regen. 2024.",
        "Centers for Medicare &amp; Medicaid Services. Local Coverage Determinations for skin substitute grafts/cellular and tissue-based products (check current versions).",
    ],
    handout=("Advanced wound treatments", """        <p>If a wound isn't healing with standard care, we may suggest:</p>
        <ul>
          <li><strong>A wound vac</strong> (negative pressure therapy): a small pump with a sealed dressing that pulls fluid out and helps new tissue grow. Keep the pump on and call us if it alarms and you can't fix the seal.</li>
          <li><strong>Skin substitutes or membranes:</strong> thin sheets placed on the wound to help it close. They may need insurance approval.</li>
          <li><strong>Skin grafts or hyperbaric oxygen</strong> for certain wounds.</li>
        </ul>
        <p>These work best when pressure is off the wound, blood flow is good, and you're eating enough protein.</p>
        <p><strong>Call us right away</strong> if you see bright red blood in the wound vac tubing or canister.</p>"""),
),
# ---------------------------------------------------------------- 7
dict(
    num=7, slug="infection-complications", minutes=34,
    title="Infection and complications",
    summary="Recognizing infection, choosing antibiotics, treating osteomyelitis, fixing stalled wounds, and when to refer.",
    objectives=[
        "Distinguish colonization from local and systemic infection.",
        "Choose antibiotics and cultures based on severity, and know when to admit.",
        "Manage stalled wounds, epibole, odor and other complications, and refer early.",
    ],
    lessons=[
        ("infection", "Recognizing infection", """        <p>All chronic wounds carry bacteria. Treat infection, not colonization.</p>
""" + table(["Level", "Signs", "Action"], [
            ["Local infection", "Two or more of: warmth, redness or swelling over 2 cm beyond the edge (diabetic foot: 0.5 to 2 cm is mild), new or increased pain, purulence, new odor after cleansing, friable tissue, stalled healing", "Culture (Levine or tissue), topical antimicrobials, oral antibiotics, debride"],
            ["Deep or spreading", "Redness beyond 2 cm, lymphangitis, abscess, deep tissue or bone involvement", "Oral or IV antibiotics; imaging; surgical consult for drainage"],
            ["Systemic", "Fever or low temperature, chills, fast heart rate or breathing, low blood pressure, confusion, high white count", "Emergency evaluation, blood cultures, IV antibiotics, admission"],
        ]) + """
        <p>Neuropathy, PAD, steroids and older age blunt the signs. A diabetic foot infection may show only rising glucose or a new smell.</p>"""),
        ("antibiotics", "Antibiotics and osteomyelitis", """""" + table(["Setting", "Common options", "Notes"], [
            ["Outpatient, mild to moderate", "Cephalexin or amoxicillin-clavulanate; doxycycline or trimethoprim-sulfamethoxazole when MRSA is a concern; clindamycin as an alternative", "Usually 1 to 2 weeks for soft tissue; check kidney function and interactions (TMP-SMX with warfarin and ACE inhibitors)"],
            ["Inpatient, moderate to severe", "Vancomycin plus cefepime or piperacillin-tazobactam, with metronidazole when anaerobes are likely", "Narrow to culture results; reserve carbapenems for resistant organisms"],
        ]) + """
        <p><strong>Osteomyelitis:</strong> confirm with MRI and, ideally, bone biopsy for culture before long-term antibiotics. Staphylococcus aureus is the most common cause. Involve infectious disease and podiatry or surgery. About 6 weeks of therapy is typical when no infected bone is removed; IWGDF/IDSA 2023 supports oral agents with good bone penetration in many cases, and much shorter courses after complete resection: a few days with clean bone margins, or about 3 weeks if infected bone remains at the margin. Surgical removal of dead bone is often needed.</p>
        <p>Antibiotics treat infection; they don't replace debridement, drainage, offloading or revascularization.</p>"""),
        ("complications", "Stalled wounds, complications and referrals", """""" + table(["Problem", "Likely causes", "What to do"], [
            ["Stalled wound", "Pressure, poor nutrition, weight loss, infection, biofilm, ischemia, edema, wrong diagnosis", "Reassess everything; consider biopsy; change approach after 2 to 4 weeks without progress"],
            ["Epibole (rolled edges)", "Edges curl under and stop migrating", "Open the edges: sharp debridement or silver nitrate, then moist healing"],
            ["Odor", "Infection, necrotic tissue, anaerobes", "Debride, cleanse with Dakin's, charcoal or cadexomer iodine dressings, topical metronidazole (off-label)"],
            ["Anemia", "Iron, B12 or folate deficiency; chronic disease", "Identify and treat the cause"],
            ["Surgical dehiscence", "Infection, tension, poor nutrition", "Contact the surgeon; close follow-up"],
            ["Hypergranulation", "Excess moisture, friction", "Reduce moisture; foam; silver nitrate if needed"],
        ]) + """
        <p><strong>Refer early:</strong> vascular surgery (abnormal ABI, ischemic wounds), infectious disease or the hospital (systemic infection, osteomyelitis, failed oral therapy), general or plastic surgery (large debridement, flaps, exposed hardware), and podiatry (foot and ankle wounds, Charcot foot, surgical offloading). Build relationships with good home health agencies and dietitians too.</p>
        <p>Be cautious with any plan that debrides aggressively at every visit without measurable progress. The goal is healing, not ongoing treatment; get a second opinion when wounds stall for months.</p>"""),
    ],
    pearls=[
        "Culture when you see infection, not to \"see what grows.\"",
        "Rising glucose in a diabetic patient with a foot wound can be the first sign of infection.",
        "When you talk with families, overestimate healing time rather than underestimate it.",
    ],
    redflags=[
        "Fever, low blood pressure, confusion or rapidly spreading redness: emergency care.",
        "Crepitus, gas on X-ray, or pain out of proportion: possible necrotizing infection; emergency surgery.",
        "Exposed bone or positive probe-to-bone: osteomyelitis workup and specialist referral.",
    ],
    case=("A patient with a stage 4 ischial wound has a new foul odor, 3 cm of surrounding redness and warmth, and purulent drainage, but no fever and normal vital signs.",
          "This is a local, possibly deep, infection. Get a Levine or tissue culture after cleansing, debride necrotic tissue, start an oral agent covering staph and strep (and anaerobes if odor and necrosis suggest them), and use antimicrobial dressings. Because it's a stage 4 wound over bone, evaluate for osteomyelitis with ESR, CRP and MRI. Escalate if systemic signs appear."),
    quiz=[
        ("When should a chronic wound be cultured?",
         ["At every visit", "When there are clinical signs of infection or unexplained deterioration", "Never"], 1,
         "Routine cultures pick up colonizers. Culture when infection is suspected."),
        ("What should you do about rolled, closed wound edges (epibole)?",
         ["Nothing", "Open the edges with sharp debridement or silver nitrate", "Apply a hydrocolloid"], 1,
         "Rolled edges stop epithelial migration; reopening them restarts healing."),
    ],
    refs=[
        "Senneville E, et al. IWGDF/IDSA guidelines on the diagnosis and treatment of diabetes-related foot infections. Clin Infect Dis. 2023.",
        "Stevens DL, et al. IDSA practice guidelines for skin and soft tissue infections. Clin Infect Dis. 2014.",
        "International Wound Infection Institute. Wound Infection in Clinical Practice: Principles of Best Practice. 2022.",
        "Gariani K, et al. Six weeks versus twelve weeks of antibiotic therapy for diabetic foot osteomyelitis. Clin Infect Dis. 2021.",
    ],
    handout=("Signs of wound infection", """        <p><strong>Call us the same day</strong> if you notice:</p>
        <ul>
          <li>Redness or warmth spreading around the wound</li>
          <li>More pain, swelling or drainage</li>
          <li>Pus, or a bad smell that stays after cleaning</li>
          <li>The wound getting bigger or deeper</li>
          <li>Higher blood sugars than usual if you have diabetes</li>
        </ul>
        <p><strong>Go to the emergency room or call 911</strong> for fever with chills, red streaks moving up the arm or leg, confusion, fast heartbeat, or feeling very sick.</p>
        <p>If you're given antibiotics, take every dose, and keep doing your wound care.</p>"""),
),
# ---------------------------------------------------------------- 8
dict(
    num=8, slug="prevention-nutrition", minutes=36,
    title="Prevention and nutrition",
    summary="Repositioning, support surfaces, heel and device protection, skin care, incontinence care, nutrition, hydration and weight.",
    objectives=[
        "Build a pressure injury prevention plan with repositioning and the right support surfaces.",
        "Prevent heel, device and moisture-related injuries.",
        "Assess and support nutrition, hydration and weight for healing.",
    ],
    lessons=[
        ("pressure-prevention", "Pressure relief and support surfaces", """        <p>Consistent pressure relief matters more than any dressing. Highest-risk sites: sacrum and coccyx, ischial tuberosities, buttocks, heels, hips, elbows, ankles, and the plantar foot in diabetes.</p>
        <ul>
          <li>Turn bed-bound patients at least every 2 hours (individualize to skin response and surface), using a 30-degree side-lying tilt and a lift sheet to avoid shear.</li>
          <li>Shift weight in a chair every 15 to 30 minutes, and limit sitting time for patients with sacral or ischial wounds.</li>
          <li>Keep the head of the bed at 30 degrees or lower when possible to reduce sliding.</li>
          <li>Watch body mechanics: patients who always lie on one side or stack their feet need targeted padding.</li>
        </ul>
""" + table(["Surface", "Use"], [
            ["Pillows and wedges", "Basic positioning for everyone"],
            ["Static air or foam overlays", "Moderate risk"],
            ["Low air loss mattress", "Moisture control; moderate to high risk"],
            ["Alternating pressure mattress", "High risk or existing wounds"],
            ["Air-fluidized bed", "Large stage 3 and 4 wounds, flaps"],
            ["Air-cell wheelchair cushion", "High risk or existing ischial or sacral wounds"],
        ])),
        ("skin-devices", "Heels, devices, skin and continence", """        <ul>
          <li><strong>Float the heels:</strong> pillows under the calves or heel-suspension boots so the heels don't touch the bed. Apply barrier film to at-risk heels.</li>
          <li><strong>Devices:</strong> check under oxygen tubing, braces, compression devices, catheters, restraints and NPWT tubing every shift. Pad with silicone foam or moleskin, and remove objects left in beds and chairs.</li>
          <li><strong>Prophylactic dressings:</strong> multilayer silicone foam over the sacrum and heels lowers pressure injury rates in high-risk patients.</li>
          <li><strong>Skin care:</strong> use pH-balanced cleansers (skin's natural pH is about 4.5 to 5.5), avoid harsh soaps and hot water, and moisturize daily.</li>
          <li><strong>Incontinence:</strong> check and change promptly, cleanse gently, apply a zinc or dimethicone barrier, treat diarrhea and constipation, and look for reversible causes. Consider a fecal management system for persistent liquid stool. Use indwelling catheters only when clearly indicated.</li>
          <li><strong>Falls:</strong> clear rugs and clutter, add rails, manage toileting needs, and refer to PT and OT for strength and transfers.</li>
        </ul>"""),
        ("nutrition", "Nutrition, hydration and weight", """""" + table(["Target", "Recommendation", "Notes"], [
            ["Calories", "30 to 35 kcal/kg/day", "Adjust for weight goals"],
            ["Protein", "1.25 to 1.5 g/kg/day", "Check kidney function; individualize in advanced CKD with nephrology and a dietitian"],
            ["Fluids", "About 30 mL/kg/day (2,100 mL for 70 kg)", "Individualize in heart failure, edema or dialysis"],
            ["Arginine, zinc and antioxidants", "Arginine-containing supplements for stage 2 or worse pressure injuries with malnutrition", "Supported by EPUAP/NPIAP guidance"],
            ["Vitamin C", "500 to 1,000 mg/day short-term when intake is poor or deficiency is likely", "Generally safe; avoid high doses with kidney stones"],
            ["Zinc", "Replace only when deficient (for example zinc sulfate 220 mg, which is 50 mg elemental zinc, daily for up to 2 weeks)", "Longer use can cause copper deficiency"],
            ["Vitamin A", "Short courses for patients on steroids or with deficiency", "Avoid high doses in pregnancy and liver disease"],
            ["Vitamin D, iron", "Replace when low", "Base on labs"],
        ]) + """
        <p><strong>Weigh weekly.</strong> Unintended weight loss of 5% in a month or 10% in 6 months signals malnutrition and slows healing. Track meal percentages and offer protein supplements between meals. Refer to a dietitian early for large or complex wounds, and document nutrition interventions: it supports the care plan and explains slow healing.</p>
        <p><strong>Smoking</strong> constricts vessels and slows healing. Offer cessation support at every visit.</p>"""),
    ],
    pearls=[
        "No cushion replaces repositioning, and no dressing replaces offloading.",
        "Float the heels. Complete offloading is the best heel protection.",
        "Weekly weights catch decline before the wound does.",
    ],
    redflags=[
        "Weight loss over 5% in a month or eating less than half of meals: dietitian referral and supplements now.",
        "Swallowing problems or coughing with meals: speech therapy evaluation.",
        "New pressure injury despite a prevention plan: reassess the surface, turning schedule and nutrition.",
    ],
    case=("A 68 kg resident with a stage 3 sacral wound eats half of each meal and has lost 4 kg in a month. Kidney function is normal.",
          "She has lost about 6% of her weight in a month, which is significant. Aim for about 2,000 to 2,400 kcal and 85 to 100 g protein a day; add a high-protein or arginine-containing supplement between meals, involve a dietitian, check for depression, dental or swallowing problems, and weigh weekly. Pair this with an alternating pressure mattress and limited sitting time."),
    quiz=[
        ("What protein intake is generally recommended for adults with pressure injuries and normal kidney function?",
         ["0.6 g/kg/day", "1.25 to 1.5 g/kg/day", "3 g/kg/day"], 1,
         "EPUAP/NPIAP guidance suggests 1.25 to 1.5 g/kg/day for adults with pressure injuries who are malnourished or at risk."),
        ("The best way to prevent heel pressure injuries is to:",
         ["Massage the heels", "Float the heels so they don't touch the bed", "Use a donut cushion"], 1,
         "Heel suspension removes pressure completely; donut cushions concentrate pressure and are not recommended."),
    ],
    refs=[
        "EPUAP/NPIAP/PPPIA. Prevention and Treatment of Pressure Ulcers/Injuries: Quick Reference Guide. 2019, with updates.",
        "Munoz N, et al. The role of nutrition for pressure injury prevention and healing: the 2019 International Clinical Practice Guideline recommendations. Adv Skin Wound Care. 2020.",
        "Cereda E, et al. A nutritional formula enriched with arginine, zinc, and antioxidants for the healing of pressure ulcers: a randomized trial. Ann Intern Med. 2015.",
        "Santamaria N, et al. A randomised controlled trial of the effectiveness of soft silicone multi-layered foam dressings in the prevention of sacral and heel pressure ulcers. Int Wound J. 2015.",
        "White JV, et al. Consensus statement: characteristics recommended for the identification and documentation of adult malnutrition. JPEN. 2012.",
    ],
    handout=("Preventing pressure injuries and eating to heal", """        <ul>
          <li>Change position at least every 2 hours in bed, and shift your weight every 15 to 30 minutes in a chair.</li>
          <li>Keep heels off the bed with a pillow under the calves.</li>
          <li>Keep skin clean and dry. Use a gentle, pH-balanced cleanser and a barrier cream if there's leakage.</li>
          <li>Eat protein at every meal, plus a protein shake between meals if you're not eating well.</li>
          <li>Drink water through the day unless your doctor limits fluids.</li>
          <li>Weigh yourself once a week. Tell us if you're losing weight without trying.</li>
        </ul>
        <p><strong>Caregivers:</strong> look at the skin on the tailbone, hips and heels every day.</p>"""),
),
# ---------------------------------------------------------------- 9
dict(
    num=9, slug="documentation-billing", minutes=30,
    title="Documentation, billing and coding",
    summary="Measuring and describing wounds, documentation that protects you, facility reporting, and common wound care codes.",
    objectives=[
        "Measure and document wounds consistently and completely.",
        "Write notes that show medical necessity and protect you legally.",
        "Use common evaluation, debridement, compression, ABI and NPWT codes correctly.",
    ],
    lessons=[
        ("measuring", "Measuring and describing wounds", """        <ul>
          <li><strong>Measure in centimeters:</strong> length (head to toe) by width (side to side, perpendicular) by depth (deepest point with a sterile applicator).</li>
          <li><strong>Undermining and tunneling:</strong> use the clock face with 12 o'clock toward the head, for example "undermining 2.0 cm from 3 to 6 o'clock."</li>
          <li><strong>Photograph</strong> consistently: same distance and angle, with a measuring guide, following consent and privacy policies.</li>
          <li><strong>Number wounds</strong> the same way on every note. When one heals, document the date and final appearance before renumbering.</li>
        </ul>
""" + table(["Document every visit", ""], [
            ["Size and stage or type", "L x W x D; undermining and tunneling"],
            ["Wound bed", "Tissue type percentages; exposed bone, tendon or hardware"],
            ["Drainage", "Amount, color, consistency, odor after cleansing"],
            ["Edges and surrounding skin", "Maceration, redness, induration, callus, epibole"],
            ["Pain and infection signs", "And actions taken"],
            ["Treatment", "Products, frequency, and why"],
        ])),
        ("legal", "Documentation that protects you", """        <p>Document the barriers to healing and what you did about each one:</p>
        <ul>
          <li>Support surface, heel protection, turning schedule, and any refusals or nonadherence (with education given)</li>
          <li>Nutrition: intake, weights, dietitian involvement, supplements, relevant labs</li>
          <li>Perfusion: pulses, ABI, vascular referrals and their results</li>
          <li>Glycemic control, infection management, PT and OT, and other consults</li>
          <li>Conversations with the patient and family about the diagnosis, plan and expected timeline</li>
        </ul>
        <p><strong>In facilities:</strong> do and document a full skin assessment on admission and readmission. Federal nursing home rules (F686) require care that prevents avoidable pressure injuries, and injuries first found after admission are generally counted as facility-acquired, so early documentation of present-on-admission wounds matters for the patient and the facility.</p>
        <p>Partner with facilities on prevention programs. Most referrals come after wounds are complex, but prevention has the greatest impact and lowers costs. Keep patient outcomes first when balancing cost.</p>"""),
        ("coding", "Billing and coding essentials", """""" + table(["Service", "Common codes", "Notes"], [
            ["Office visits", "99202 to 99205 new; 99211 to 99215 established", "Level by medical decision making or time"],
            ["Nursing facility", "99304 to 99306 initial; 99307 to 99310 subsequent", ""],
            ["Home or residence (including assisted living)", "99341, 99342, 99344, 99345 new; 99347 to 99350 established", ""],
            ["Selective debridement (to dermis)", "97597 first 20 sq cm; 97598 each additional", "Removal of slough or fibrin without subcutaneous tissue"],
            ["Debridement, subcutaneous tissue", "11042 first 20 sq cm; 11045 each additional", "Document depth and tissue removed; deeper codes for muscle (11043) and bone (11044)"],
            ["ABI", "93922 (limited, bilateral); 93923 (complete, multilevel)", "Needs a documented indication and a report"],
            ["Unna boot and multilayer compression", "29580; 29581 (below knee); 29582 (thigh and leg)", "Add RT or LT; often not billable on the same day as debridement of the same leg (check NCCI edits)"],
            ["NPWT, durable equipment", "97605 (50 sq cm or less); 97606 (over 50 sq cm)", "Document total wound surface area"],
        ]) + """
        <p>Use modifiers (for example 59 or the X modifiers, and 25 for a separate E/M on a procedure day) only when documentation supports a distinct service. Debridement is billed by the depth and area of tissue removed, not the wound's stage. Coding rules, NCCI edits and local coverage determinations change every year; verify with current CPT, your Medicare contractor and each payer.</p>"""),
    ],
    pearls=[
        "Measure the same way every time: head-to-toe length, perpendicular width, deepest depth.",
        "Document the barriers to healing and your action on each one.",
        "Bill debridement by the deepest tissue actually removed, and say so in the note.",
    ],
    redflags=[
        "A wound not documented on admission to a facility: assess and document it the same day.",
        "Weeks of identical notes with no change in size or plan: reassess the wound and the plan.",
        "Billing a deeper debridement than the note supports: correct before submitting.",
    ],
    case=("You sharply debride slough and some subcutaneous fat from a 6 cm x 4 cm wound, then apply a multilayer wrap to the same leg.",
          "The debrided area is 24 sq cm with subcutaneous tissue removed, so 11042 plus 11045 for the extra 4 sq cm. Note the depth, tissue type and instrument. The multilayer wrap on the same leg on the same day is usually bundled with the debridement under NCCI edits, so check the edit before billing 29581."),
    quiz=[
        ("Undermining is documented using:",
         ["Inches and compass directions", "Centimeters and clock positions, with 12 o'clock toward the head", "Percent of the wound"], 1,
         "Clock positions oriented to the head make documentation consistent across clinicians."),
        ("Debridement codes are chosen based on:",
         ["The pressure injury stage", "The depth and surface area of tissue actually removed", "The dressing used"], 1,
         "Code by the deepest tissue removed and the area debrided, as documented."),
    ],
    refs=[
        "American Medical Association. CPT 2026 Professional Edition.",
        "Centers for Medicare &amp; Medicaid Services. National Correct Coding Initiative (NCCI) Policy Manual, Chapter 11.",
        "CMS. State Operations Manual, Appendix PP: F686 Treatment/Services to Prevent/Heal Pressure Ulcers.",
        "WOCN Society. Wound documentation guidance.",
    ],
    handout=("Questions to ask about your wound care", """        <ul>
          <li>What kind of wound is this, and what caused it?</li>
          <li>Is it getting smaller? Can I see the measurements?</li>
          <li>What can I do at home to help it heal?</li>
          <li>How long do you expect healing to take?</li>
          <li>What signs mean I should call you?</li>
          <li>Will my insurance cover the dressings or treatments?</li>
        </ul>
        <p>It's normal for chronic wounds to take weeks or months. Ask us any time you're unsure about your care.</p>"""),
),
# ---------------------------------------------------------------- 10
dict(
    num=10, slug="foot-care", minutes=32,
    title="Foot care",
    summary="The diabetic foot exam, toenail care, ingrown toenails, calluses, onychomycosis, and foot care documentation.",
    objectives=[
        "Perform a complete foot exam, including monofilament testing and risk grading.",
        "Trim and reduce toenails, treat simple ingrown nails, and pare calluses safely.",
        "Treat onychomycosis with an honest view of the evidence, and document foot care.",
    ],
    lessons=[
        ("foot-exam", "The foot exam and who needs foot care", """        <p>Foot care keeps feet and nails healthy, prevents injury and infection, and often brings immediate relief. Most patients are older adults, people with diabetes, PAD or neuropathy, and people who can't reach or see their feet. Ingrown toenails also affect younger, active people.</p>
        <p><strong>Exam:</strong> look for ulcers, deformity, redness, swelling, drainage, fissures between toes, callus and nail changes; palpate for pain and heel bogginess; check pulses, temperature and edema. Perform the <strong>10 g monofilament</strong> test (plus vibration or pinprick) at least yearly in diabetes, more often in high-risk feet.</p>
        <p><strong>Key terms:</strong> onychomycosis (fungal nail), hypertrophic nails, paronychia (infected nail fold), corns and calluses, fissures, plantar warts, bunions, and gout (sudden red, hot, painful joint, often the big toe).</p>
        <p><strong>Prevention includes</strong> regular exams, nail and callus care, offloading, proper footwear, diabetes control, and teaching patients and caregivers to check feet daily.</p>"""),
        ("procedures", "Nails, ingrown nails and calluses", """        <p>Get consent first. Position the foot so both you and the patient are comfortable.</p>
        <ul>
          <li><strong>Soaking:</strong> a warm soak softens nails, but don't soak patients with diabetes and neuropathy, significant PAD, or open wounds; use moisture-only cleansing instead.</li>
          <li><strong>Nail trimming and debridement:</strong> trim in small bites, roughly straight across, without cutting into skin; watch for curved "horseshoe" nails and protruding skin. Reduce thickened nails with a rotary burr, using dust extraction and eye protection. File sharp edges.</li>
          <li><strong>Simple ingrown nail:</strong> with clean technique, cut a narrow vertical strip of the offending nail edge back toward the cuticle and lift it out. Many patients tolerate this without anesthesia if done slowly; use a digital block when needed. Use silver nitrate for bleeding (rinse with saline afterward to limit stinging). Refer for partial nail avulsion with matrixectomy for recurrent or infected ingrown nails.</li>
          <li><strong>Callus and corn paring:</strong> pare layer by layer with a scalpel or burr until the tissue softens, pausing to avoid heat. Never pare to bleeding. Address the cause with padding, footwear or orthotics.</li>
          <li><strong>Aftercare:</strong> clean, moisturize the skin but not between the toes, and dress any break in the skin (povidone-iodine or mupirocin for a week). Teach signs of infection.</li>
        </ul>"""),
        ("onychomycosis-docs", "Onychomycosis and documentation", """""" + table(["Option", "Evidence", "Notes"], [
            ["Oral terbinafine", "Most effective (mycological cure around 70%)", "Confirm fungus first (KOH, PAS or culture); check liver tests; interactions"],
            ["Topical efinaconazole or tavaborole", "Modest cure rates", "Daily for about 48 weeks; costly"],
            ["Ciclopirox lacquer", "Low cure rates", "Inexpensive option"],
            ["Mentholated ointment (such as Vicks VapoRub)", "Small pilot study only", "Low-risk, inexpensive option for patients who decline or can't take other treatment; set realistic expectations"],
            ["Regular debridement", "Relieves pain and thickness", "Often the main goal in older adults"],
        ]) + """
        <p><strong>Documentation:</strong> record the exam (pulses, sensation, skin, nails), the class findings that establish medical necessity for routine foot care under Medicare (for example diabetes with neuropathy or PAD, documented with the treating physician when required), the number of nails debrided, lesions pared, and the plan. Common diagnoses include onychomycosis, hypertrophic nails, PAD or atherosclerosis, diabetes with or without neuropathy, difficulty walking, foot pain, hyperkeratosis and ingrown nail. Typical follow-up for routine nail care is every 9 to 10 weeks or as covered; see patients sooner for ingrown nails or calluses as needed.</p>
        <p><strong>Common codes</strong> (verify current rules): 11720 and 11721 (nail debridement, 1 to 5 and 6 or more nails), 11055 to 11057 (paring of corns and calluses by number), 11730 (nail avulsion), and 11750 (nail excision with matrixectomy), with Q modifiers for Medicare class findings.</p>"""),
    ],
    pearls=[
        "Don't soak the feet of patients with diabetic neuropathy or severe PAD.",
        "Take your time trimming. Watch for skin that curves up into the nail line.",
        "Every foot visit is a chance to teach daily foot checks and proper shoes.",
    ],
    redflags=[
        "A hot, red, swollen foot in a patient with neuropathy: consider Charcot foot or infection; offload and refer.",
        "Paronychia with spreading redness, or any foot wound in a patient with diabetes: treat promptly and refer to podiatry as needed.",
        "Dark streaks in a nail or a changing pigmented lesion: refer for evaluation of melanoma.",
    ],
    case=("A 74-year-old with diabetes and neuropathy has thick, yellow, painful toenails and a callus under the second metatarsal head. Pulses are faint.",
          "Skip the soak. Check an ABI given faint pulses. Debride the nails with a burr and pare the callus without drawing blood, then pad and adjust footwear to offload the metatarsal head. Document neuropathy and PAD findings that support medical necessity. Discuss onychomycosis treatment options honestly, and teach daily foot checks. Schedule routine care about every 9 to 10 weeks."),
    quiz=[
        ("Which patient should not have a warm foot soak?",
         ["A healthy 40-year-old with an ingrown nail", "A patient with diabetic neuropathy and PAD", "A runner with a callus"], 1,
         "Neuropathy and poor circulation raise the risk of burns and maceration."),
        ("Which onychomycosis treatment has the highest cure rate?",
         ["Mentholated ointment", "Oral terbinafine", "Ciclopirox lacquer"], 1,
         "Oral terbinafine has the best evidence; confirm the diagnosis and check for contraindications first."),
    ],
    refs=[
        "American Diabetes Association. Standards of Care in Diabetes (current edition): Retinopathy, Neuropathy, and Foot Care.",
        "Schaper NC, et al. IWGDF practical guidelines on the prevention and management of diabetes-related foot disease. 2023.",
        "Gupta AK, Stec N, et al. Onychomycosis: a review. J Eur Acad Dermatol Venereol. 2020.",
        "Derby R, et al. Novel treatment of onychomycosis using over-the-counter mentholated ointment: a clinical case series. J Am Board Fam Med. 2011.",
        "CMS. Medicare Benefit Policy Manual, Chapter 15, Section 290: Foot Care; local coverage determinations for routine foot care.",
    ],
    handout=("Caring for your feet", """        <ul>
          <li>Look at your feet every day, including the bottoms and between your toes. Use a mirror or ask for help.</li>
          <li>Wash and dry your feet daily, especially between the toes. Moisturize the tops and bottoms, but not between the toes.</li>
          <li>Wear shoes and socks that fit, even indoors. Check inside shoes before putting them on.</li>
          <li>Don't cut corns or calluses yourself or use acid corn removers.</li>
          <li>If you have diabetes, don't soak your feet or test water with your feet. Use your hand or elbow.</li>
        </ul>
        <p><strong>Call us</strong> for a sore, blister or cut that isn't healing, redness or swelling, a toenail digging into the skin, or a foot that's suddenly hot or misshapen.</p>"""),
),
]
