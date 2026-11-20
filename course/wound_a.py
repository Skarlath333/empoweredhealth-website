"""Wound and Foot Care Course, modules 1 to 5.

Written from Heath Tunnell's Empowered Health Wound and Foot Care Course deck (2026), checked against
NPIAP/EPUAP, IWGDF/IDSA, WOCN, SVS and ABA guidance. No slide images are reused.
"""
from modules_a import table

MODULES = [
# ---------------------------------------------------------------- 1
dict(
    num=1, slug="foundations", minutes=30,
    title="Foundations of wound care",
    summary="The wound care role, scope and liability, who is at risk, key terms, and how wounds heal.",
    objectives=[
        "Describe the wound care provider's goal: heal the wound by treating what caused it.",
        "Identify high-risk populations and the main liability risks in wound care.",
        "Explain the four phases of healing and why chronic wounds stall.",
    ],
    lessons=[
        ("role", "The wound care role", """        <p>Wound care is the assessment, treatment and prevention of acute and chronic wounds: damage to skin and the tissue beneath it from pressure, trauma, poor circulation, diabetes, infection, cancer, radiation and other causes. An estimated 7 million or more Americans live with a chronic wound, and Medicare alone spends tens of billions of dollars a year on them. Demand is rising with age, diabetes, obesity and vascular disease.</p>
        <p><strong>The goal is not the dressing.</strong> The wound care provider treats the wound and the reasons it formed or won't heal:</p>
        <ul>
          <li>Relieve pressure and offload</li>
          <li>Optimize protein, calories, vitamins and hydration</li>
          <li>Manage diabetes, vascular disease, edema and other comorbidities</li>
          <li>Treat the whole person, including pain, mood and isolation</li>
        </ul>
        <p>Care can happen almost anywhere: clinics, skilled nursing and assisted living facilities, home visits, and hospitals. Wounds also take a heavy toll beyond the skin. Pain, odor and drainage lead many patients to withdraw socially, so ask about mood and daily life.</p>"""),
        ("scope", "Scope, liability and who is at risk", """        <p><strong>Scope.</strong> Basic wound care (assessment, dressing selection, education) is within every NP's scope. Advanced procedures such as conservative sharp debridement, biopsy, incision and drainage, and skin substitute application depend on state rules, collaboration agreements, facility privileges and training. Certifications such as CWCN-AP and WCS-C deepen skills and credibility.</p>
        <p><strong>Liability.</strong> Wound care is a moderate-risk specialty. Carry your own malpractice policy if you own a practice or work in facilities or homes. The most common problems are:</p>
""" + table(["Risk", "How to reduce it"], [
            ["Incomplete documentation", "Measure, photograph and describe every wound every visit; record rationale and response"],
            ["Ignoring the cause", "Document what you did about pressure, nutrition, glucose, perfusion and infection"],
            ["Working outside scope", "Know your state board rules and facility privileges"],
            ["Delayed referral", "Refer early for ischemia, deep infection, osteomyelitis or stalled wounds"],
            ["Poor communication", "Document consent, education, and family updates"],
        ]) + """
        <p><strong>High-risk groups:</strong> older adults, the critically ill, hospice and palliative patients, people with spinal cord injury, the malnourished, infants, sedated patients, dialysis patients, people frequently transported by stretcher, and people with poor hygiene or self-care.</p>"""),
        ("healing", "How wounds heal, and why they stall", """""" + table(["Phase", "Timing", "What happens"], [
            ["Hemostasis", "Minutes", "Platelets and clotting factors form a fibrin clot that stops bleeding and makes a scaffold"],
            ["Inflammation", "About days 1 to 3 (longer in chronic wounds)", "Neutrophils kill bacteria; macrophages clear debris and release growth factors"],
            ["Proliferation", "About days 4 to 24", "Granulation tissue, new vessels, contraction and epithelialization; beefy red granulation is a good sign"],
            ["Remodeling", "3 weeks to 2 years", "Collagen reorganizes; scar reaches only about 80% of the original skin's strength"],
        ]) + """
        <p><strong>Chronic wounds get stuck in inflammation.</strong> Matrix metalloproteinases (MMPs) normally clear damaged matrix, but in chronic wounds levels (especially MMP-2 and MMP-9) run too high. They break down new tissue and growth factors. Collagen and protease-modulating dressings help bind excess protease activity.</p>
        <p><strong>Key terms to know:</strong> granulation (red, cobblestone healthy tissue), slough (yellow to tan nonviable tissue), stable eschar (dry, hard, adherent) versus unstable eschar (soft, boggy, draining), epibole (rolled edges that stop epithelial migration), maceration (white, waterlogged skin), undermining and tunneling (measured in cm by clock position), and biofilm (invisible bacterial communities that stall healing).</p>
        <p><strong>Risk tools:</strong> the Braden Scale scores sensory perception, moisture, activity, mobility, nutrition, and friction and shear (6 to 23). Scores of 18 or less signal risk, and 12 or less is very high risk. Use it alongside, not instead of, clinical judgment.</p>"""),
    ],
    pearls=[
        "Treat the person as a whole, not just the hole in the person.",
        "If you didn't document it, it didn't happen. That applies to education and offloading as much as to measurements.",
        "A wound stuck in inflammation needs its cause fixed, not just a stronger dressing.",
    ],
    redflags=[
        "Signs of systemic infection (fever, low blood pressure, confusion, rising white count): urgent evaluation.",
        "Exposed bone, tendon or hardware: assume deep infection until proven otherwise and involve surgery.",
        "A wound that hasn't shrunk in 2 to 4 weeks of good care: reassess the diagnosis, perfusion and infection.",
    ],
    case=("A new facility patient has a sacral wound that has been dressed with the same foam for two months without change. Her Braden score is 11, she eats about 30% of meals, and she sits up in a chair most of the day.",
          "The dressing isn't the problem. She is at very high risk with poor intake and constant sitting pressure. Address offloading first (time in bed on a pressure-redistributing surface, chair limits), get a dietitian involved and add protein supplements, reassess the wound fully (measurements, tissue types, infection signs), and document each intervention."),
    quiz=[
        ("What is the primary goal of the wound care provider?",
         ["Choose the most advanced dressing", "Treat the wound and the underlying causes that impair healing", "Debride at every visit"], 1,
         "Healing depends on fixing pressure, nutrition, perfusion, infection and comorbidities, not on the dressing alone."),
        ("Which phase are chronic wounds typically stuck in?",
         ["Hemostasis", "Inflammation", "Remodeling"], 1,
         "Chronic wounds often stall in prolonged inflammation with excess protease activity."),
    ],
    refs=[
        "European Pressure Ulcer Advisory Panel, National Pressure Injury Advisory Panel and Pan Pacific Pressure Injury Alliance. Prevention and Treatment of Pressure Ulcers/Injuries: International Guideline. 2019, with updates.",
        "Braden BJ, Bergstrom N. The Braden Scale for Predicting Pressure Sore Risk (bradenscale.com).",
        "Sen CK. Human Wound and Its Burden: Updated 2020 Compendium of Estimates. Adv Wound Care. 2021.",
        "Caley MP, et al. Metalloproteinases and Wound Healing. Adv Wound Care. 2015.",
        "Wound, Ostomy and Continence Nurses Society (WOCN) clinical guidelines.",
    ],
    handout=("Understanding your wound", """        <p>Healing a wound takes more than a bandage. Your body needs:</p>
        <ul>
          <li><strong>Pressure off the wound.</strong> Change positions often, and keep weight off it.</li>
          <li><strong>Good food.</strong> Protein at every meal (eggs, meat, fish, beans, Greek yogurt, protein shakes).</li>
          <li><strong>Water,</strong> unless your doctor has limited your fluids.</li>
          <li><strong>Blood sugar control</strong> if you have diabetes.</li>
          <li><strong>No smoking.</strong> Nicotine cuts blood flow to the wound.</li>
        </ul>
        <p>Chronic wounds can take weeks to months to heal. We'll measure your wound at each visit so you can see progress.</p>
        <p><strong>Get care right away</strong> for fever or chills, redness spreading from the wound, a bad new smell, or new confusion.</p>"""),
),
# ---------------------------------------------------------------- 2
dict(
    num=2, slug="wound-types", minutes=40,
    title="Types of wounds",
    summary="Pressure injury staging, diabetic, arterial and venous ulcers, moisture damage, trauma, burns and other wounds.",
    objectives=[
        "Stage pressure injuries accurately using NPIAP definitions.",
        "Tell diabetic, arterial and venous ulcers apart by location, appearance and pain.",
        "Recognize moisture damage, skin tears, burns and other wound types, and when to refer.",
    ],
    lessons=[
        ("pressure", "Pressure injuries", """        <p>Pressure injuries form over bony prominences from sustained pressure, often with shear (skin stays put while deeper tissue slides, as when a patient slides down in bed). Friction alone causes superficial damage and is not a pressure injury, but it adds to shear.</p>
""" + table(["Stage", "NPIAP description"], [
            ["Stage 1", "Intact skin with non-blanchable redness. In darker skin, look for color change, warmth, firmness or pain."],
            ["Stage 2", "Partial-thickness loss into the dermis: a pink or red shallow wound or an intact or ruptured serum-filled blister. No slough, eschar or granulation."],
            ["Stage 3", "Full-thickness skin loss into fat. Granulation and rolled edges may be present; slough or eschar may be present but don't hide the depth; undermining and tunneling possible."],
            ["Stage 4", "Full-thickness loss exposing fascia, muscle, tendon, ligament, cartilage or bone."],
            ["Unstageable", "Full-thickness loss whose base is obscured by slough or eschar, so depth can't be seen."],
            ["Deep tissue pressure injury", "Intact or non-intact skin with persistent non-blanchable deep red, maroon or purple color, or a blood-filled blister. Can evolve quickly."],
        ]) + """
        <p>Also know medical device-related pressure injuries (under tubing, braces, oxygen cannulas, compression devices) and Kennedy terminal ulcers: sudden butterfly or pear-shaped sacral wounds at the end of life that may not be preventable. Goals shift to comfort, odor and drainage control.</p>"""),
        ("lower-extremity", "Diabetic, arterial and venous ulcers", """""" + table(["", "Diabetic foot ulcer", "Arterial ulcer", "Venous ulcer"], [
            ["Cause", "Neuropathy, pressure and repetitive trauma, often with PAD", "Peripheral arterial disease", "Venous hypertension from incompetent veins"],
            ["Location", "Plantar foot, toes, pressure points", "Toes, forefoot, heels, lateral ankle", "Medial lower leg, gaiter area, near the medial malleolus"],
            ["Look", "Round, punched-out, callused rim", "Punched-out, dry, pale base, often slough or eschar", "Shallow, irregular, moist to heavily draining, beefy red base"],
            ["Skin around it", "Callus; dry skin; deformity", "Shiny, hairless, cool, pale on elevation, rubor when dependent", "Edema, hemosiderin staining, stasis dermatitis, lipodermatosclerosis"],
            ["Pain", "Often painless (neuropathy)", "Severe, worse at night and with elevation", "Aching, better with elevation"],
            ["Key step", "Offload and check perfusion", "ABI and vascular referral", "Compression after ruling out significant PAD"],
        ]) + """
        <p>Venous ulcers are the most common leg ulcers. Many patients have mixed arterial and venous disease, so check perfusion before compressing.</p>"""),
        ("moisture-trauma", "Moisture damage and traumatic wounds", """        <p><strong>Moisture-associated skin damage (MASD)</strong>, including incontinence-associated dermatitis, comes from urine, stool, sweat or wound drainage. Skin is red, shiny, macerated or eroded, often with diffuse edges. It isn't a pressure injury, but it often leads to one on the sacrum and buttocks.</p>
""" + table(["Wound", "Key features", "Notes"], [
            ["Skin tear (ISTAP)", "Type 1 no skin loss (flap repositionable); type 2 partial flap loss; type 3 total flap loss", "Fragile skin of older adults and steroid users; from tape, bumps, transfers"],
            ["Abrasion", "Scraped, raw, weeping, painful", "Usually heals well with simple care"],
            ["Contusion", "Closed injury with discoloration", "Watch large or expanding bruises in anticoagulated patients for hematoma, compartment syndrome or fracture"],
            ["Laceration", "Cut through skin, often deep", "May need closure; check tetanus status"],
            ["Blood-filled blister", "Dark, tense blister from shear or trauma", "May be a deep tissue injury; usually leave intact"],
        ])),
        ("burns-other", "Burns and other wounds", """""" + table(["Burn depth", "Appearance", "Pain"], [
            ["Superficial (first degree)", "Red, dry, no blisters", "Painful"],
            ["Superficial partial thickness", "Pink, moist, blisters, blanches", "Very painful"],
            ["Deep partial thickness", "Mottled red and white, less blanching", "Less painful"],
            ["Full thickness (third degree)", "White, leathery or charred, dry", "Often painless"],
        ]) + """
        <p><strong>Refer to a burn center</strong> (American Burn Association criteria) for partial-thickness burns over 10% of body surface area, any full-thickness burn, burns of the face, hands, feet, genitalia, perineum or major joints, electrical, chemical or inhalation injuries, and burns in patients with significant comorbidities or in children without appropriate care. Estimate area with the Rule of Nines or a Lund-Browder chart.</p>
        <p><strong>Other wounds:</strong> surgical incisions (watch for infection and dehiscence), osteomyelitis (bone infection, often under diabetic foot ulcers and stage 4 pressure injuries; the wound won't heal until it's treated), fistulas and abscesses, malignant wounds, and wounds from autoimmune disease such as pyoderma gangrenosum or vasculitis. Biopsy atypical or non-healing wounds.</p>"""),
    ],
    pearls=[
        "If you can't see the wound base because of slough or eschar, it's unstageable. Don't guess the stage.",
        "Pain at night that eases when the leg hangs down points to arterial disease.",
        "A wound in an unusual spot or with an unusual look that won't heal deserves a biopsy.",
    ],
    redflags=[
        "Cold, pale, pulseless foot or new black toes: urgent vascular evaluation.",
        "Burns meeting burn center criteria, or any inhalation, electrical or chemical burn.",
        "Rapidly spreading purple discoloration, crepitus or pain out of proportion: possible necrotizing infection, emergency care.",
    ],
    case=("A 78-year-old with diabetes has a shallow, painless, round ulcer under the first metatarsal head with a thick callus rim. Pedal pulses are faint.",
          "This is a diabetic (neuropathic) foot ulcer, possibly with PAD given faint pulses. Offload the area, debride the callus, check an ABI (and toe pressures if vessels may be non-compressible), probe to bone and consider an X-ray to look for osteomyelitis, and refer to vascular if perfusion is poor."),
    quiz=[
        ("A wound covered by slough so the base can't be seen is staged as:",
         ["Stage 2", "Stage 3", "Unstageable"], 2,
         "When slough or eschar hides the depth, the pressure injury is unstageable until the base can be seen."),
        ("Which ulcer is typically on the medial lower leg with heavy drainage and hemosiderin staining?",
         ["Arterial", "Venous", "Diabetic"], 1,
         "Venous ulcers sit in the gaiter area with edema, staining and moderate to heavy drainage."),
    ],
    refs=[
        "Edsberg LE, et al. Revised National Pressure Ulcer Advisory Panel Pressure Injury Staging System. J Wound Ostomy Continence Nurs. 2016.",
        "LeBlanc K, et al. Best practice recommendations for the prevention and management of skin tears (ISTAP). Adv Skin Wound Care. 2018.",
        "Gray M, et al. Incontinence-associated dermatitis: a consensus. J Wound Ostomy Continence Nurs. 2007, with updates.",
        "American Burn Association. Guidelines for Burn Patient Referral. 2022.",
        "Schaper NC, et al. IWGDF practical guidelines on the prevention and management of diabetes-related foot disease. 2023.",
        "O'Donnell TF, et al. Management of venous leg ulcers: SVS and AVF clinical practice guidelines. J Vasc Surg. 2014.",
    ],
    handout=("Pressure injuries (bedsores)", """        <p>Pressure injuries happen when skin is pressed between a bone and a bed or chair for too long. They often form on the tailbone, hips, heels and elbows.</p>
        <ul>
          <li><strong>Watch for:</strong> red or dark skin that doesn't fade when pressed, blisters, or open spots.</li>
          <li><strong>Move often.</strong> Change position at least every 2 hours in bed, and shift weight every 15 to 30 minutes in a chair.</li>
          <li><strong>Float the heels</strong> on a pillow under the calves so heels don't touch the bed.</li>
          <li><strong>Keep skin clean and dry,</strong> and use a barrier cream if there's leakage of urine or stool.</li>
        </ul>
        <p><strong>Call us</strong> if you see a new sore, dark purple skin, or a sore that's getting bigger.</p>"""),
),
# ---------------------------------------------------------------- 3
dict(
    num=3, slug="assessment", minutes=34,
    title="Assessment and diagnostic testing",
    summary="History, head-to-toe skin checks, tissue types, labs, wound cultures, the ankle-brachial index, and imaging for osteomyelitis.",
    objectives=[
        "Perform a complete wound history and head-to-toe skin assessment.",
        "Order labs and cultures that change management, using proper technique.",
        "Perform and interpret an ankle-brachial index and choose imaging for osteomyelitis.",
    ],
    lessons=[
        ("history-exam", "History and skin assessment", """        <p>Many wounds look alike but have different causes. The history usually tells you which: diabetes, vascular disease, smoking, steroids, recent surgery, mobility, continence, intake and weight trends, and how the wound started.</p>
        <p><strong>Head-to-toe skin assessment</strong> at every new visit:</p>
        <ul>
          <li>All bony prominences: sacrum, coccyx, ischia, hips, heels, ankles, elbows, occiput, ears</li>
          <li>Skin folds, under the breasts and abdomen, and the perineum</li>
          <li>Under every device: oxygen tubing, braces, catheters, compression devices, NPWT tubing</li>
          <li>Legs and feet: hair loss, color, temperature, pulses, edema, staining</li>
          <li>Where and how the patient lives: bed- or chair-bound, support surfaces, who helps them</li>
        </ul>
        <p>In darker skin, redness is hard to see. Use temperature, firmness, swelling and pain. Check blanching: redness that blanches is reactive; non-blanchable redness is a stage 1 injury.</p>
        <p><strong>Tissue types:</strong> estimate the percentage of each in the wound bed (for example 60% granulation, 30% slough, 10% epithelial): dermal, granulation, slough, unstable eschar, stable eschar, epithelial tissue, and skin flaps.</p>"""),
        ("labs-culture", "Labs and wound cultures", """""" + table(["Lab", "Why"], [
            ["CBC", "Infection, anemia (poor oxygen delivery), platelets before debridement"],
            ["CMP", "Kidney function (protein and drug dosing), glucose, albumin"],
            ["A1c", "Diabetes and glycemic control"],
            ["CRP and ESR", "Inflammation; a very high ESR raises concern for osteomyelitis"],
            ["Iron studies, B12, folate", "When anemia is present"],
            ["Vitamin D, zinc", "When deficiency is suspected"],
            ["PT/INR", "Anticoagulated patients, before sharp debridement"],
        ]) + """
        <p>Albumin and prealbumin fall with inflammation and illness, so they are markers of severity and risk rather than precise measures of nutrition. Pair them with intake and weight.</p>
        <p><strong>Culture only when infection is suspected</strong> (increased pain, spreading redness, warmth, purulence, odor, sudden deterioration, or stalled healing), not on every chronic wound. Use the <strong>Levine technique</strong>: cleanse with saline, don't swab necrotic tissue or old drainage, then rotate a swab over 1 cm<sup>2</sup> of viable tissue for 5 seconds with enough pressure to express fluid. Tissue samples after debridement are better still.</p>"""),
        ("abi-imaging", "Ankle-brachial index and imaging", """        <p><strong>How to perform an ABI:</strong> rest the patient supine for 5 to 10 minutes. Measure systolic pressure with a handheld Doppler in both arms (brachial), then at each ankle using the dorsalis pedis and posterior tibial arteries. For each leg, divide the higher ankle pressure by the higher arm pressure.</p>
""" + table(["ABI", "Meaning", "Action"], [
            ["Over 1.40", "Non-compressible, calcified vessels (common in diabetes and kidney disease)", "Get toe pressures or toe-brachial index and arterial duplex"],
            ["1.00 to 1.40", "Normal", "Compression generally safe"],
            ["0.91 to 0.99", "Borderline", "Treat risk factors; monitor"],
            ["0.50 to 0.90", "PAD (mild to moderate)", "Vascular referral; reduced compression only with care"],
            ["Under 0.50", "Severe PAD", "Urgent vascular referral; no compression"],
        ]) + """
        <p><strong>Osteomyelitis workup:</strong> probe to bone, ESR and CRP, and plain X-rays first (they may be normal early). MRI is the best imaging test. Nuclear medicine scans are an option when MRI isn't possible. Bone biopsy with culture and histology is the reference standard and guides antibiotics.</p>"""),
    ],
    pearls=[
        "Look under every device during every skin check.",
        "Don't culture a wound that doesn't look infected. You'll grow colonizers and treat the wrong thing.",
        "An ABI over 1.40 is not reassuring. It means you need toe pressures.",
    ],
    redflags=[
        "ABI under 0.50, rest pain or gangrene: urgent vascular referral.",
        "Probe-to-bone positive wound or bone exposed: work up for osteomyelitis.",
        "A wound with systemic signs of infection: same-day evaluation.",
    ],
    case=("A 70-year-old smoker has a painful, dry, punched-out ulcer on the lateral ankle and a mild venous-looking edema. You plan to start compression. Her ABI is 0.62.",
          "Her ABI shows moderate PAD, so standard high compression is unsafe. Refer to vascular surgery, keep the wound dry and protected while perfusion is assessed, and use only reduced, carefully monitored compression if vascular agrees. Strongly support smoking cessation."),
    quiz=[
        ("Which wound culture technique is preferred for a swab?",
         ["Swab the eschar", "Levine technique over viable tissue after cleansing", "Swab the old dressing"], 1,
         "The Levine technique samples viable tissue after cleansing, which better reflects infecting organisms."),
        ("An ABI of 1.6 in a patient with diabetes most likely means:",
         ["Excellent circulation", "Calcified, non-compressible vessels; get toe pressures", "Venous disease"], 1,
         "High ABIs reflect calcified arteries and can hide real PAD."),
    ],
    refs=[
        "Gerhard-Herman MD, et al. 2016 AHA/ACC Guideline on the Management of Patients With Lower Extremity Peripheral Artery Disease. Circulation. 2017.",
        "Aboyans V, et al. Measurement and interpretation of the ankle-brachial index: AHA Scientific Statement. Circulation. 2012.",
        "Senneville E, et al. IWGDF/IDSA guidelines on the diagnosis and treatment of diabetes-related foot infections. Clin Infect Dis. 2023.",
        "Levine NS, et al. The quantitative swab culture and smear. J Trauma. 1976.",
        "EPUAP/NPIAP/PPPIA. International Guideline: skin and tissue assessment. 2019.",
    ],
    handout=("What to expect at your wound visit", """        <ul>
          <li>We'll ask how the wound started and about your health, medicines and diet.</li>
          <li>We'll check your skin from head to toe, including your heels and backside.</li>
          <li>We'll measure the wound and may take a photo to track healing.</li>
          <li>For leg or foot wounds, we may check blood pressure at your ankles to make sure enough blood is reaching the wound.</li>
          <li>We may order blood work, a culture (a swab of the wound), or an X-ray or MRI.</li>
        </ul>
        <p><strong>Bring to your visit:</strong> a list of your medicines and supplements, and the names of the dressings you've been using.</p>"""),
),
# ---------------------------------------------------------------- 4
dict(
    num=4, slug="dressings-debridement", minutes=36,
    title="Dressings, products and debridement",
    summary="A simple dry-versus-wet, shallow-versus-deep framework, a practical product toolkit, and choosing a debridement method.",
    objectives=[
        "Classify wounds as dry or wet and shallow or deep to choose a dressing.",
        "Build a small, reliable product toolkit and adapt to each facility's formulary.",
        "Choose and limit debridement appropriately.",
    ],
    lessons=[
        ("framework", "The dry/wet, shallow/deep framework", """        <p>Most wounds fit one of four boxes. The box tells you whether to add moisture, remove moisture, or keep things dry.</p>
""" + table(["Wound", "Goal", "Common choices"], [
            ["Dry shallow (stable eschar, minimal drainage)", "Keep dry and protected", "Povidone-iodine or skin barrier film painted three to four times daily; leave stable eschar alone"],
            ["Wet shallow (partial thickness, moderate to heavy drainage)", "Absorb drainage, protect skin", "Antimicrobial foam (for example Hydrofera Blue), silver alginate, hydrocolloid for light drainage; zinc barrier on surrounding skin"],
            ["Dry deep (stage 3 or 4, little drainage)", "Add moisture, debride autolytically", "Medical-grade honey or hydrogel on gauze lightly packed, foam cover; collagen once clean"],
            ["Wet deep (stage 3 or 4, heavy drainage)", "Control moisture and bioburden, then maintain", "Quarter- to half-strength Dakin's moistened gauze for 1 to 2 weeks, then silver alginate or antimicrobial foam; consider NPWT"],
        ]) + """
        <p><strong>Exception:</strong> in arterial wounds without adequate blood flow, and in frail or end-of-life patients, keep wounds dry with stable eschar rather than moist, even if deep.</p>"""),
        ("toolkit", "A practical product toolkit", """        <p>Every facility has a different formulary. Know a few products well, learn each facility's equivalents, and adapt. A reliable core kit:</p>
""" + table(["Category", "Examples", "Use"], [
            ["Antiseptic paints and solutions", "Povidone-iodine, sodium hypochlorite (Dakin's), skin barrier film", "Dry stable eschar; reduce bioburden; protect skin"],
            ["Antimicrobial foam", "Methylene blue and gentian violet foam (Hydrofera Blue)", "Wet shallow or deep wounds; some versions stay on up to 3 to 7 days"],
            ["Alginates and silver alginates", "Calcium alginate, silver alginate", "Moderate to heavy drainage, minor bleeding, bioburden"],
            ["Hydrocolloids", "DuoDERM", "Shallow, light drainage; up to 7 days"],
            ["Collagen", "Collagen with or without silver", "Clean, stalled wounds; binds excess proteases"],
            ["Honey and hydrogels", "Medical-grade honey, hydrogel, silver hydrogel", "Dry wounds; autolytic debridement"],
            ["Foams and absorbers", "Bordered silicone foam, super-absorbent pads, ABD pads", "Cover dressings; prophylaxis over bony prominences"],
            ["Barriers", "Zinc oxide pastes, barrier films", "MASD; protecting surrounding skin"],
            ["Nonadherent", "Petrolatum or bismuth gauze (Xeroform)", "Skin tears, wet abrasions, graft sites"],
            ["Antifungals", "Nystatin powder or cream; oral fluconazole for extensive yeast", "Candida in folds and around wounds"],
            ["Compression", "Elastic wraps, Unna boot, 2- to 4-layer systems, stockings", "Venous disease once arterial flow is confirmed"],
        ])),
        ("debridement", "Debridement: when and how", """""" + table(["Method", "How", "Best for"], [
            ["Sharp (conservative)", "Scalpel, curette or scissors by a trained provider", "Fast removal of slough, callus and nonviable tissue; within scope and privileges"],
            ["Autolytic", "Moisture-retentive dressings let the body's enzymes work", "Small amounts of slough; patients who can't tolerate sharp debridement"],
            ["Enzymatic", "Collagenase ointment (Santyl)", "Slough and soft eschar"],
            ["Mechanical", "Irrigation, monofilament pads, ultrasonic mist", "Loose debris; avoid repeated wet-to-dry gauze, which is painful and nonselective"],
            ["Biological", "Sterile medical maggots", "Selective debridement when other methods fail"],
        ]) + """
        <p><strong>Less is often more.</strong> Debride when there is loose necrotic tissue, slough, callus or biofilm and when it will help healing, not at every visit to make a wound look clean. Over-debridement removes healthy tissue, causes pain, and is a common reason wounds stall.</p>
        <p><strong>Don't debride</strong> stable, dry eschar on heels or in ischemic limbs, or wounds without adequate blood flow, until perfusion is addressed. Check anticoagulation and platelets before sharp debridement.</p>"""),
    ],
    pearls=[
        "Ask two questions first: is it dry or wet, and is it shallow or deep?",
        "Stable, dry eschar on a heel or an ischemic limb is a natural dressing. Leave it alone.",
        "Pick a few products you know well and learn every facility's equivalents.",
    ],
    redflags=[
        "Pain, bleeding or exposed structures during debridement beyond what you expected: stop and reassess.",
        "Eschar that becomes soft, boggy, draining or surrounded by redness: it's no longer stable; evaluate for infection.",
        "Debriding a foot or leg wound with unknown perfusion: check the ABI first.",
    ],
    case=("A stage 4 sacral wound has heavy drainage, 50% slough, and macerated edges. The facility carries Dakin's, silver alginate, foam and zinc paste.",
          "It's a wet deep wound. Start with Dakin's-moistened gauze and an absorptive cover once or twice daily for 1 to 2 weeks to reduce drainage and bioburden, protect the edges with zinc paste, and debride slough selectively. Then switch to silver alginate or antimicrobial foam and consider NPWT once the bed is clean and granulating. Fix the pressure and nutrition at the same time."),
    quiz=[
        ("A dry, stable eschar on the heel of a frail patient with poor circulation should usually be:",
         ["Sharply debrided", "Kept dry and protected, and left in place", "Covered with hydrogel"], 1,
         "Stable heel eschar, especially with poor perfusion, acts as a natural cover and is usually left intact."),
        ("Which wound most needs moisture added?",
         ["Wet shallow", "Dry deep with good blood flow", "Heavily draining venous ulcer"], 1,
         "Dry deep wounds with adequate perfusion heal best with moist wound healing."),
    ],
    refs=[
        "Kirshen C, Woo K, Ayello EA, Sibbald RG. Debridement: a vital component of wound bed preparation. Adv Skin Wound Care. 2006.",
        "Schultz GS, et al. Wound bed preparation: a systematic approach to wound management. Wound Repair Regen. 2003.",
        "Wound, Ostomy and Continence Nurses Society. Guideline for Management of Wounds in Patients With Lower-Extremity Arterial Disease. 2014.",
        "EPUAP/NPIAP/PPPIA. International Guideline: wound dressings and debridement. 2019.",
    ],
    handout=("Caring for your dressing at home", """        <ul>
          <li>Wash your hands before and after touching the dressing.</li>
          <li>Change it only as often as we told you. Some dressings stay on for several days.</li>
          <li>Keep it dry when you bathe unless we said otherwise.</li>
          <li>If the dressing leaks or falls off, replace it the same day.</li>
          <li>Don't put creams, peroxide or home remedies on the wound unless we recommend them.</li>
        </ul>
        <p><strong>A dark, dry scab is sometimes left on purpose.</strong> It can protect the wound underneath. Tell us if it gets soft, starts draining, or the skin around it turns red.</p>"""),
),
# ---------------------------------------------------------------- 5
dict(
    num=5, slug="treatment-by-type", minutes=44,
    title="Treatment by wound type",
    summary="Step-by-step care for pressure injuries, venous and arterial ulcers, diabetic foot ulcers, skin tears, abrasions and minor burns.",
    objectives=[
        "Treat each pressure injury stage, starting with the cause.",
        "Apply compression safely for venous ulcers and manage arterial wounds with vascular input.",
        "Offload diabetic foot ulcers and treat skin tears, abrasions and minor burns.",
    ],
    lessons=[
        ("pressure-tx", "Pressure injuries by stage", """""" + table(["Stage", "Local care", "Always"], [
            ["Stage 1", "Barrier cream or film; prophylactic silicone foam", "Offload, change the support surface, address nutrition"],
            ["Stage 2", "Hydrocolloid or foam for light drainage; antimicrobial foam or silver alginate for more", "Offload; manage moisture and incontinence"],
            ["Stage 3", "Choose by moisture: honey or hydrogel if dry; Dakin's then silver alginate or antimicrobial foam if wet; collagen when clean", "Aggressive offloading; protein and calories"],
            ["Stage 4", "As stage 3, often NPWT once clean; consider advanced products", "Rule out osteomyelitis; specialty support surface"],
            ["Unstageable", "Dry and stable on heels or ischemic limbs: keep dry. Otherwise debride slough or soft eschar to stage it", "Determine perfusion and prognosis"],
            ["Deep tissue injury", "Protect with barrier film or povidone-iodine; no debridement", "Immediate pressure relief; watch closely for evolution"],
        ])),
        ("venous-arterial", "Venous and arterial ulcers", """        <p><strong>Venous ulcers: compression is the treatment.</strong> Confirm arterial flow first (ABI).</p>
        <ul>
          <li>ABI 0.8 or higher: full compression (about 40 mmHg at the ankle) with multilayer systems or an Unna boot.</li>
          <li>ABI 0.5 to 0.8: reduced compression only, with vascular input.</li>
          <li>ABI under 0.5, or uncontrolled heart failure: no compression.</li>
        </ul>
        <p><strong>Practical sequence:</strong> antimicrobial foam or silver alginate on the wound, absorbent pad, then wrap from the toes to just below the knee. Change daily or three times a week. Use an <strong>Unna boot</strong> (zinc paste gauze, then rolled gauze and an elastic or cohesive wrap) for weeping legs. After 1 to 2 weeks, step up to multilayer compression; once healed, fit 20 to 40 mmHg stockings for life to prevent recurrence. Coordinate diuretics for fluid overload with the patient's primary clinician. Refer to vascular for venous ablation, which speeds healing and reduces recurrence (EVRA trial).</p>
        <p><strong>Arterial ulcers: perfusion first.</strong> Refer to vascular surgery for ABI under 0.9 with a wound. Locally, paint with povidone-iodine to keep a dry, stable eschar and prevent infection until blood flow is restored. Trim eschar edges only as they lift. Don't compress, soak, or aggressively debride an ischemic wound. Necrotic toes: keep dry and involve vascular early.</p>"""),
        ("diabetic", "Diabetic foot ulcers", """        <p><strong>Offloading is the cornerstone.</strong> No dressing heals a wound that's still being walked on.</p>
""" + table(["Step", "What to do"], [
            ["Offload", "Total contact cast or a non-removable knee-high walker is best for plantar forefoot ulcers; removable walkers or custom shoes otherwise"],
            ["Debride", "Sharp debridement of callus and slough, usually weekly"],
            ["Perfusion", "ABI and toe pressures; vascular referral if inadequate"],
            ["Infection", "Assess every visit; probe to bone and X-ray if deep (see Module 7)"],
            ["Local care", "Clean, then collagen with an antimicrobial foam or alginate based on drainage; change daily to three times a week"],
            ["Systemic", "Glycemic control, smoking cessation, nutrition"],
        ]) + """
        <p>When standard care fails to shrink the wound by about 40 to 50% in 4 weeks, consider advanced therapies (Module 6) and recheck perfusion and infection.</p>"""),
        ("skin-tears-burns", "Skin tears, abrasions and minor burns", """        <p><strong>Skin tears:</strong> clean gently, realign the flap with a moist cotton swab, and secure with skin closure strips or a silicone contact layer (no sutures in fragile skin). Cover with petrolatum gauze or silicone foam, and mark an arrow showing which way to remove the dressing so the flap isn't lifted. Change two to three times a week. Once the flap adheres, protect with barrier film. Pad bed rails and wheelchairs and moisturize skin twice daily.</p>
        <p><strong>Abrasions:</strong> irrigate with saline. Dry abrasions: povidone-iodine to form a protective scab. Wet abrasions: petrolatum gauze or zinc barrier, with foam if needed.</p>
        <p><strong>Minor burns</strong> (superficial and small partial thickness): cool with running water for about 20 minutes, don't pop intact blisters, and cover with a nonadherent or antimicrobial dressing. Silver sulfadiazine is still used but can slow epithelialization; avoid it on the face, in sulfa allergy and in pregnancy near term. Refer per burn center criteria (Module 2).</p>"""),
    ],
    pearls=[
        "Compression heals venous ulcers. Teach patients the wraps feel tight at first and get easier as swelling falls.",
        "In arterial wounds, dry stable eschar is your friend until blood flow is fixed.",
        "Mark skin-tear dressings with an arrow so the next person removes them the right way.",
    ],
    redflags=[
        "Compression causing numbness, color change or new pain: remove it and recheck perfusion.",
        "A diabetic foot that is hot, red and swollen without a wound: consider acute Charcot foot; offload and refer.",
        "Necrotic toes, rest pain, or a non-healing ischemic wound: vascular surgery now.",
    ],
    case=("An 82-year-old has a weeping venous ulcer with 3+ pitting edema. ABI is 0.95 in both legs. She has stable heart failure.",
          "Arterial flow is adequate, so compression is safe; coordinate with her cardiology or primary clinician given heart failure. Use silver alginate or antimicrobial foam, an absorbent pad, and an Unna boot with rolled gauze and an elastic wrap, changed three times a week. Elevate legs, review diuretics, step up to multilayer compression as weeping settles, then fit stockings after healing and refer for venous evaluation."),
    quiz=[
        ("Before applying full compression to a venous ulcer, you should:",
         ["Check an ABI to confirm adequate arterial flow", "Culture the wound", "Start antibiotics"], 0,
         "Compression can cause ischemic injury when arterial disease is significant."),
        ("What is the cornerstone of diabetic foot ulcer treatment?",
         ["Silver dressings", "Offloading pressure from the wound", "Daily wet-to-dry gauze"], 1,
         "Offloading, ideally with a total contact cast or non-removable walker for plantar ulcers, matters most."),
    ],
    refs=[
        "O'Donnell TF, et al. Management of venous leg ulcers: SVS and AVF clinical practice guidelines. J Vasc Surg. 2014.",
        "Gohel MS, et al. A randomized trial of early endovenous ablation in venous ulceration (EVRA). N Engl J Med. 2018.",
        "Bus SA, et al. IWGDF guidelines on offloading foot ulcers in persons with diabetes. 2023.",
        "Sheehan P, et al. Percent change in wound area of diabetic foot ulcers over a 4-week period is a robust predictor of complete healing. Diabetes Care. 2003.",
        "WOCN Society. Guideline for Management of Wounds in Patients With Lower-Extremity Arterial Disease. 2014.",
        "LeBlanc K, et al. ISTAP best practice recommendations for skin tears. 2018.",
        "Conte MS, et al. Global vascular guidelines on the management of chronic limb-threatening ischemia. J Vasc Surg. 2019.",
    ],
    handout=("Leg and foot wounds", """        <p><strong>If you have swollen legs and a venous wound:</strong></p>
        <ul>
          <li>Wear your wraps or stockings as directed. They feel tight at first and get easier as swelling goes down.</li>
          <li>Raise your legs above your heart for 30 minutes a few times a day.</li>
          <li>Walk if you can. Calf muscles help push blood back up.</li>
        </ul>
        <p><strong>If you have diabetes and a foot wound:</strong></p>
        <ul>
          <li>Keep weight off the wound. Wear the boot or shoe we give you every time you stand or walk, even at home.</li>
          <li>Check both feet every day with a mirror or a helper.</li>
          <li>Keep your blood sugar in your target range.</li>
        </ul>
        <p><strong>Take your wraps off and call us</strong> if your toes become numb, cold, blue or more painful.</p>"""),
),
]
