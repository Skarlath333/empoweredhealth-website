"""Course content, modules 6 to 10. Original writing; sources are listed in each module's refs."""
from modules_a import table

MODULES = [
# ---------------------------------------------------------------- 6
dict(
    num=6, slug="menopause", minutes=34,
    title="Perimenopause and menopause hormone therapy",
    summary="Candidacy, routes and doses, risks by age and timing, and monitoring under current guidance.",
    objectives=[
        "Diagnose perimenopause and menopause clinically, and know when testing helps.",
        "Select candidates for hormone therapy using age, timing and contraindications.",
        "Prescribe and monitor estrogen and progestogen, and offer non-hormonal options.",
    ],
    lessons=[
        ("diagnosis", "Perimenopause and diagnosis", """        <p>Menopause is 12 months without a period. Perimenopause, the years before it, brings irregular cycles, hot flashes and night sweats, poor sleep, mood changes, brain fog, joint aches, and vaginal dryness.</p>
        <ul>
          <li><strong>In women 45 and older</strong> with typical symptoms, diagnosis is clinical. FSH swings widely in perimenopause, so a single value is unreliable.</li>
          <li><strong>Under 40:</strong> evaluate for primary ovarian insufficiency (FSH on two occasions, plus TSH, prolactin and hCG). These patients generally need hormone therapy until the average age of menopause.</li>
          <li><strong>Contraception</strong> is still needed in perimenopause, until 12 months without a period for women over 50, or 24 months for women under 50.</li>
          <li><strong>Bleeding after menopause</strong> always needs evaluation of the endometrium.</li>
        </ul>"""),
        ("candidacy", "Candidacy and risks", """        <p>The Menopause Society's 2022 position: for people under 60 or within 10 years of menopause, without contraindications, the benefits of hormone therapy generally outweigh the risks for bothersome vasomotor symptoms and for preventing bone loss.</p>
""" + table(["Risk", "What we know"], [
            ["Breast cancer", "Estrogen plus progestin: small increase with longer use (WHI: under 1 extra case per 1,000 women per year). Estrogen alone after hysterectomy did not increase risk in WHI."],
            ["Blood clots and stroke", "Higher with oral estrogen. Transdermal estradiol appears to carry lower risk in observational data."],
            ["Heart disease", "Starting near menopause appears neutral or favorable; starting 10+ years later or after 60 carries more risk."],
            ["Endometrial cancer", "Unopposed estrogen raises risk. Anyone with a uterus needs a progestogen."],
        ]) + """
        <p><strong>Contraindications:</strong> unexplained vaginal bleeding, breast cancer or another estrogen-sensitive cancer, prior blood clot or stroke, coronary disease, active liver disease, and known high-risk thrombophilia.</p>"""),
        ("prescribing", "Prescribing and monitoring", """""" + table(["Option", "Typical start", "Notes"], [
            ["Transdermal estradiol patch", "0.025 to 0.05 mg/day", "Preferred with clot risk, migraine, or high triglycerides"],
            ["Oral estradiol", "0.5 to 1 mg/day", "Simple and inexpensive"],
            ["Micronized progesterone", "100 mg nightly (continuous) or 200 mg for 12 days a month", "For endometrial protection; may help sleep"],
            ["Low-dose vaginal estrogen", "Cream, tablet or ring", "For genitourinary symptoms; minimal absorption; no progestogen needed; can continue long term"],
        ]) + """
        <ul>
          <li><strong>Dose by symptoms,</strong> not blood levels. Routine estradiol levels aren't needed.</li>
          <li><strong>Use FDA-approved products.</strong> FDA-approved estradiol and progesterone are bioidentical. Compounded hormones and pellets are not FDA-approved, vary in dose, and pellets can produce very high levels.</li>
          <li><strong>Testosterone for women</strong> has one evidence-based use: hypoactive sexual desire disorder after menopause, at doses appropriate for women, with monitoring.</li>
          <li><strong>Duration</strong> is individualized. There's no automatic stop at 65; reassess yearly with mammography and a risk review.</li>
          <li><strong>Non-hormonal options:</strong> fezolinetant (needs liver tests before and during treatment), low-dose paroxetine and other SSRIs or SNRIs, gabapentin, and CBT for hot flashes and sleep.</li>
        </ul>"""),
    ],
    pearls=[
        "Don't order FSH to diagnose perimenopause in a woman over 45 with typical symptoms.",
        "Every patient with a uterus who takes systemic estrogen needs a progestogen.",
        "Vaginal estrogen is low-risk and underused for urinary and vaginal symptoms.",
    ],
    redflags=[
        "Any postmenopausal bleeding, or heavy or prolonged bleeding on hormone therapy.",
        "A new breast lump, or calf pain, chest pain, or shortness of breath on therapy.",
        "Menopause symptoms before 40: evaluate for primary ovarian insufficiency.",
    ],
    case=("A 51-year-old with 10 hot flashes a day, poor sleep and a last period 8 months ago has migraine without aura and a BMI of 33. She has her uterus. She asks about hormone therapy.",
          "She is within 10 years of menopause and under 60, so hormone therapy is reasonable. Transdermal estradiol is preferred given migraine and higher BMI. Add micronized progesterone for endometrial protection. Confirm mammography is current, discuss that she still needs contraception for now, and follow up in about 3 months to adjust the dose."),
    quiz=[
        ("Who is generally the best candidate for systemic hormone therapy?",
         ["A 66-year-old who stopped menstruating 15 years ago", "A 50-year-old within a few years of menopause with bothersome hot flashes and no contraindications", "Anyone with a history of breast cancer"], 1,
         "Benefits generally outweigh risks under 60 or within 10 years of menopause, without contraindications."),
        ("Which progestogen approach protects the endometrium?",
         ["None is needed with a uterus", "Micronized progesterone 100 mg nightly or 200 mg for 12 days a month", "Vaginal estrogen alone"], 1,
         "Systemic estrogen with a uterus requires a progestogen, such as micronized progesterone."),
    ],
    refs=[
        "The 2022 Hormone Therapy Position Statement of The North American Menopause Society. Menopause. 2022.",
        "Manson JE, et al. Menopausal hormone therapy and health outcomes during the intervention and extended poststopping phases of the Women's Health Initiative randomized trials. JAMA. 2013.",
        "The 2023 Nonhormone Therapy Position Statement of The North American Menopause Society. Menopause. 2023.",
        "Davis SR, et al. Global Consensus Position Statement on the Use of Testosterone Therapy for Women. J Clin Endocrinol Metab. 2019.",
        "ACOG Clinical Consensus: Compounded Bioidentical Menopausal Hormone Therapy. 2023.",
        "U.S. FDA. Safety communication on fezolinetant (Veozah) and liver injury, boxed warning. 2024.",
        "Harlow SD, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10. Menopause. 2012.",
    ],
    handout=("Perimenopause and menopause", """        <p>Perimenopause can start in your 40s. Periods change, and hot flashes, night sweats, poor sleep, mood swings and vaginal dryness are common. You don't have to just put up with it.</p>
        <ul>
          <li><strong>Hormone therapy</strong> is safe and effective for many women under 60 or within 10 years of menopause. We'll go over your own risks.</li>
          <li><strong>Other options</strong> include non-hormone medicines and therapy for sleep and hot flashes.</li>
          <li><strong>Vaginal estrogen</strong> is low-dose and helps dryness and urinary symptoms.</li>
          <li><strong>You can still get pregnant</strong> in perimenopause. Keep using birth control until we tell you it's safe to stop.</li>
        </ul>
        <p><strong>Call us</strong> about any bleeding after your periods have stopped for a year, a new breast lump, or leg swelling or chest pain.</p>"""),
),
# ---------------------------------------------------------------- 7
dict(
    num=7, slug="testosterone", minutes=32,
    title="Testosterone therapy in men",
    summary="Diagnosis, fertility counseling, hematocrit and PSA monitoring, and when not to treat.",
    objectives=[
        "Diagnose testosterone deficiency with correct testing and find reversible causes.",
        "Counsel on fertility and choose among treatment forms.",
        "Monitor hematocrit, PSA, and symptoms safely.",
    ],
    lessons=[
        ("diagnosis", "Diagnosing testosterone deficiency", """        <p>Diagnosis needs both symptoms (low libido, erectile dysfunction, fatigue, low mood, loss of muscle) and low levels.</p>
        <ul>
          <li><strong>Test correctly:</strong> total testosterone in the morning (ideally fasting), on two separate days. The AUA uses under 300 ng/dL as a reasonable cutoff.</li>
          <li><strong>Free testosterone</strong> (by equilibrium dialysis or calculated) helps when SHBG is abnormal. Obesity and diabetes lower SHBG; aging and liver disease raise it.</li>
          <li><strong>Check LH</strong> to separate primary (testicular) from secondary (pituitary) causes. If LH is low or normal, check prolactin; consider iron studies and pituitary imaging when testosterone is very low.</li>
          <li><strong>Look for reversible causes:</strong> obesity, sleep apnea, opioids, glucocorticoids, heavy alcohol use, and acute illness. Weight loss alone often raises testosterone.</li>
        </ul>"""),
        ("treatment", "Treatment and fertility", """        <p><strong>Ask about fertility first.</strong> Testosterone therapy suppresses sperm production and can cause infertility. Men who want children soon should not use it; specialists may use hCG or (off-label) clomiphene instead.</p>
""" + table(["Form", "Notes"], [
            ["Gels and solutions", "Steady levels; risk of transfer to women and children (wash hands, cover the site)"],
            ["Injections (cypionate or enanthate, IM or subcutaneous)", "Inexpensive; peaks and troughs; weekly dosing smooths levels"],
            ["Oral testosterone undecanoate", "Taken with food; monitor blood pressure"],
            ["Pellets", "Long-acting; can't be adjusted once placed"],
        ]) + """
        <p><strong>Don't start</strong> with breast or prostate cancer, a palpable prostate nodule or elevated PSA without urology evaluation, elevated hematocrit (around 50% or higher), untreated severe sleep apnea, uncontrolled heart failure, a heart attack or stroke within 6 months, or a near-term wish for fertility.</p>
        <p><strong>Cardiovascular safety:</strong> in the TRAVERSE trial (men 45 to 80 with cardiovascular risk), testosterone gel did not increase major cardiovascular events, but atrial fibrillation, pulmonary embolism, and acute kidney injury were more common.</p>
        <p>Testosterone is a Schedule III controlled substance. Follow current DEA telehealth rules and your state's requirements.</p>"""),
        ("monitoring", "Monitoring", """""" + table(["What", "When", "Action"], [
            ["Testosterone level", "3 to 6 months after starting, then yearly", "AUA target about 450 to 600 ng/dL; draw midway between injections"],
            ["Hematocrit", "Baseline, 3 to 6 months, then yearly", "Over 54%: hold or lower the dose and look for sleep apnea; consider phlebotomy"],
            ["PSA (ages 40 to 69, after shared decision)", "Baseline, 3 to 12 months, then per screening", "Refer to urology for PSA over 4, a rise over 1.4 ng/mL in 12 months, or an abnormal exam"],
            ["Blood pressure, symptoms, sleep apnea symptoms", "Each visit", "Reassess benefit; stop if symptoms don't improve"],
        ]) + """
        <p>Reassess at 3 to 6 months. If symptoms haven't improved despite normal levels, testosterone probably wasn't the cause. Shift the focus back to sleep, mood, weight and vascular health.</p>"""),
    ],
    pearls=[
        "Never diagnose low testosterone from one afternoon level.",
        "Ask every man about fertility plans before starting testosterone.",
        "Rising hematocrit on therapy is a reason to look for sleep apnea.",
    ],
    redflags=[
        "Very low testosterone with low LH, headaches, or visual changes: check prolactin and image the pituitary.",
        "Hematocrit over 54% on therapy.",
        "A palpable prostate nodule or rapidly rising PSA.",
        "Leg swelling, chest pain, or shortness of breath on therapy.",
    ],
    case=("A 34-year-old with low energy has a total testosterone of 262 ng/dL drawn at 4 p.m. His BMI is 36, he snores, and he and his partner hope to have a baby next year.",
          "Repeat a morning level and add LH and SHBG or free testosterone, since obesity lowers SHBG. Screen for sleep apnea. Exogenous testosterone would suppress sperm production, so it's a poor fit with his fertility plans. Prioritize weight loss and sleep apnea treatment, which can raise testosterone, and refer to urology or endocrinology if treatment is still needed."),
    quiz=[
        ("Which is the correct way to confirm low testosterone?",
         ["One random level", "Two morning total testosterone levels plus symptoms", "Salivary testosterone"], 1,
         "Guidelines call for two early-morning measurements in a man with symptoms."),
        ("On testosterone therapy, a hematocrit over 54% should lead to:",
         ["No change", "Holding or lowering the dose and evaluating for sleep apnea", "Increasing the dose"], 1,
         "Erythrocytosis is the most common lab side effect and raises clot risk."),
    ],
    refs=[
        "Mulhall JP, et al. Evaluation and Management of Testosterone Deficiency: AUA Guideline. J Urol. 2018.",
        "Bhasin S, et al. Testosterone Therapy in Men With Hypogonadism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2018.",
        "Lincoff AM, et al. Cardiovascular Safety of Testosterone-Replacement Therapy (TRAVERSE). N Engl J Med. 2023.",
        "U.S. DEA. Telemedicine prescribing of controlled substances: current rules and extensions.",
    ],
    handout=("Low testosterone", """        <p>Low testosterone can cause low sex drive, erection problems, tiredness, and low mood. But these symptoms have many causes, so we test carefully.</p>
        <ul>
          <li><strong>Testing:</strong> blood is drawn in the morning, on two different days.</li>
          <li><strong>Things that lower testosterone:</strong> extra weight, poor sleep or sleep apnea, some pain medicines, and heavy drinking. Fixing these can help on their own.</li>
          <li><strong>Want children?</strong> Tell us. Testosterone treatment can stop sperm production.</li>
          <li><strong>If you start treatment,</strong> you'll need regular blood tests to check your red blood cell count and PSA.</li>
          <li><strong>Using gel?</strong> Wash your hands and cover the area so it doesn't rub off on partners or children.</li>
        </ul>"""),
),
# ---------------------------------------------------------------- 8
dict(
    num=8, slug="stress-sleep-mood", minutes=30,
    title="Stress physiology, sleep and mood",
    summary="The HPA axis without the hype, CBT-I first, screening for depression and anxiety, and mind-body tools.",
    objectives=[
        "Explain the stress response accurately, and test for true adrenal disease when needed.",
        "Treat insomnia with CBT-I first and screen for sleep apnea and restless legs.",
        "Use mind-body tools with evidence alongside standard mental health care.",
    ],
    lessons=[
        ("stress", "Stress physiology without the hype", """        <p>Short-term stress responses (cortisol and adrenaline) are healthy. Long-term activation, sometimes called allostatic load, is linked to high blood pressure, poor sleep, weight gain, insulin resistance, and IBS flares.</p>
        <ul>
          <li><strong>"Adrenal fatigue" is not a recognized diagnosis.</strong> A systematic review found no evidence that it exists, and the Endocrine Society advises against it. Salivary cortisol panels sold for it are not validated.</li>
          <li><strong>Test for real adrenal disease when it's suspected:</strong> morning cortisol and ACTH stimulation for adrenal insufficiency (weight loss, low blood pressure, hyperpigmentation, low sodium); late-night salivary cortisol, 1 mg dexamethasone suppression, or 24-hour urine cortisol for Cushing's syndrome.</li>
          <li><strong>Screen for depression and anxiety.</strong> USPSTF recommends depression screening for all adults and anxiety screening for adults under 65. Use PHQ-9 and GAD-7.</li>
        </ul>
        <p>Patients describing "burnout" are often describing real exhaustion, depression, poor sleep, or anxiety. Name what you find and treat it.</p>"""),
        ("sleep", "Sleep", """        <p>Adults need 7 or more hours. Short sleep worsens blood pressure, glucose, appetite and mood.</p>
""" + table(["Problem", "First-line approach", "Notes"], [
            ["Chronic insomnia", "CBT for insomnia (CBT-I): stimulus control, sleep restriction, cognitive work", "Recommended first by ACP and AASM; digital programs work; sleep hygiene alone isn't enough"],
            ["Obstructive sleep apnea", "STOP-BANG, then home sleep test or polysomnography", "Treat with CPAP, oral appliance, weight loss; GLP-1 therapy can help in obesity"],
            ["Restless legs", "Check ferritin and transferrin saturation", "AASM suggests iron if ferritin 75 ng/mL or lower or saturation under 20%"],
            ["Circadian rhythm problems", "Timed light exposure, low-dose melatonin (0.5 to 3 mg)", "Melatonin products vary widely in actual content"],
        ]) + """
        <p>Avoid long-term benzodiazepines and Z-drugs, especially in older adults (Beers Criteria). Review medications, alcohol, and caffeine after noon.</p>"""),
        ("mind-body", "Mind-body tools", """        <ul>
          <li><strong>Exercise</strong> is an effective treatment for depression. A 2024 network meta-analysis found walking or jogging, yoga and strength training all reduced depressive symptoms, with larger effects at higher intensity.</li>
          <li><strong>Mindfulness-based stress reduction</strong> was as effective as escitalopram for anxiety disorders in a randomized trial.</li>
          <li><strong>Slow breathing</strong> (around 6 breaths a minute for 5 minutes) is a free, quick tool to lower arousal.</li>
          <li><strong>Social connection</strong> matters. The U.S. Surgeon General has called loneliness a public health concern linked to heart disease, dementia and early death.</li>
          <li><strong>Supplements:</strong> evidence is modest. St. John's wort interacts with many drugs, including birth control. Ashwagandha has been linked to rare liver injury and can affect thyroid levels.</li>
        </ul>
        <p>These tools add to, not replace, therapy and medication for moderate to severe depression or anxiety.</p>"""),
    ],
    pearls=[
        "Sleep hygiene handouts alone rarely fix insomnia. Prescribe CBT-I.",
        "Check ferritin in every patient with restless legs.",
        "When a patient asks about adrenal fatigue, screen for depression, sleep apnea, anemia and thyroid disease, and test for true adrenal disease only if signs point to it.",
    ],
    redflags=[
        "Suicidal thoughts: assess the same day. The 988 Suicide &amp; Crisis Lifeline is available by call or text.",
        "Drowsy driving or witnessed apneas: expedite a sleep evaluation.",
        "Weight loss, low blood pressure and salt craving (possible adrenal insufficiency), or easy bruising, purple stretch marks and new hypertension (possible Cushing's).",
    ],
    case=("A 44-year-old teacher says she has \"adrenal fatigue.\" She sleeps 5 hours, wakes at 3 a.m. with racing thoughts, and her PHQ-9 is 12. She brings a salivary cortisol panel.",
          "The panel isn't validated and shouldn't guide treatment. Her PHQ-9 suggests moderate depression, and she has insomnia. Offer CBT-I, discuss therapy and possibly medication for depression, add regular exercise, and check basic labs (CBC, TSH, ferritin). Only test for adrenal disease if she has signs of it."),
    quiz=[
        ("What is the first-line treatment for chronic insomnia?",
         ["Zolpidem", "Cognitive behavioral therapy for insomnia (CBT-I)", "High-dose melatonin"], 1,
         "ACP and AASM recommend CBT-I as first-line treatment for chronic insomnia."),
        ("Restless legs syndrome should prompt a check of:",
         ["Vitamin C", "Ferritin and transferrin saturation", "Reverse T3"], 1,
         "Low iron stores worsen restless legs, and iron treatment can help."),
    ],
    refs=[
        "Cadegiani FA, Kater CE. Adrenal fatigue does not exist: a systematic review. BMC Endocr Disord. 2016.",
        "U.S. Preventive Services Task Force. Screening for Depression and Suicide Risk in Adults; Screening for Anxiety Disorders in Adults. JAMA. 2023.",
        "Qaseem A, et al. Management of Chronic Insomnia Disorder in Adults: ACP Clinical Practice Guideline. Ann Intern Med. 2016.",
        "Edinger JD, et al. Behavioral and psychological treatments for chronic insomnia disorder in adults: AASM clinical practice guideline. J Clin Sleep Med. 2021.",
        "Winkelman JW, et al. The treatment of restless legs syndrome and periodic limb movement disorder: AASM clinical practice guideline. J Clin Sleep Med. 2024.",
        "Erland LAE, Saxena PK. Melatonin natural health products and supplements: presence of serotonin and significant variability of melatonin content. J Clin Sleep Med. 2017.",
        "Noetel M, et al. Effect of exercise for depression: systematic review and network meta-analysis. BMJ. 2024.",
        "Hoge EA, et al. Mindfulness-Based Stress Reduction vs Escitalopram for anxiety disorders. JAMA Psychiatry. 2022.",
        "American Geriatrics Society 2023 Updated Beers Criteria. J Am Geriatr Soc. 2023.",
    ],
    handout=("Better sleep, less stress", """        <ul>
          <li>Go to bed and get up at the same time every day.</li>
          <li>Use your bed only for sleep and sex. If you can't sleep after about 20 minutes, get up and do something calm until you feel sleepy.</li>
          <li>Get outside light in the morning, and dim screens in the evening.</li>
          <li>Skip caffeine after noon and limit alcohol, which breaks up sleep.</li>
          <li>Move every day. Walking counts and helps mood.</li>
          <li>Try slow breathing: in for 4, out for 6, for 5 minutes.</li>
        </ul>
        <p><strong>Tell us</strong> if you snore loudly, feel sleepy while driving, or have felt down or anxious most days for 2 weeks or more.</p>
        <p><strong>If you are thinking about hurting yourself,</strong> call or text 988 right away, any time.</p>"""),
),
# ---------------------------------------------------------------- 9
dict(
    num=9, slug="environmental-exposures", minutes=20,
    title="Environmental exposures",
    summary="Endocrine disruptors, a 5-minute exposure history, and practical, low-cost counseling.",
    objectives=[
        "Summarize the evidence on common exposures: air pollution, lead, radon, PFAS, and endocrine disruptors.",
        "Take a brief exposure history and order the few tests that are validated.",
        "Give practical, low-cost advice without causing fear.",
    ],
    lessons=[
        ("evidence", "What the evidence says", """""" + table(["Exposure", "Evidence", "What to do"], [
            ["Fine particle air pollution (PM2.5)", "Strong link to heart disease, stroke and lung disease", "Check AirNow on bad days; HEPA air purifiers indoors"],
            ["Radon", "Second leading cause of lung cancer in the U.S.", "Test homes; fix if 4 pCi/L or higher"],
            ["Lead", "No safe level; older homes (pre-1978 paint), some imported spices and cookware", "CDC blood lead reference value for children is 3.5 ug/dL"],
            ["PFAS (\"forever chemicals\")", "Linked to higher cholesterol, lower vaccine response, some cancers", "National Academies (2022): offer blood testing to people with likely high exposure; 20 ng/mL or higher calls for exposure reduction and added screening"],
            ["Endocrine disruptors (BPA, phthalates)", "Animal and observational human data; associations with metabolic and reproductive outcomes", "Reduce exposure through simple swaps"],
            ["Mercury in fish", "Concern in pregnancy and young children", "Follow FDA/EPA fish advice: choose lower-mercury fish"],
        ])),
        ("history", "Exposure history and counseling", """        <p>A 5-minute exposure history (based on the ATSDR CH2OP approach): <strong>C</strong>ommunity (nearby industry, air quality), <strong>H</strong>ome (age, water source, renovation, mold, radon test), <strong>H</strong>obbies (stained glass, firearms, ceramics), <strong>O</strong>ccupation, and <strong>P</strong>ersonal habits (smoking, vaping, diet).</p>
        <p><strong>Practical swaps to share with patients:</strong></p>
        <ul>
          <li>Don't heat food in plastic; use glass or stainless steel.</li>
          <li>Filter drinking water when there's a concern. Look for NSF/ANSI 53 (lead) or 58 (reverse osmosis) certifications that list PFAS. Test private wells.</li>
          <li>Ventilate when cooking, especially with gas stoves.</li>
          <li>Wet-dust and vacuum with a HEPA filter; take shoes off at the door.</li>
          <li>Choose low-mercury fish such as salmon, sardines, shrimp and canned light tuna; avoid shark, swordfish, king mackerel, tilefish and bigeye tuna.</li>
          <li>Choose fragrance-free products where practical.</li>
        </ul>
        <p><strong>Tests to avoid:</strong> provoked (chelation challenge) urine heavy metal tests are not valid and are discouraged by medical toxicologists. Urine mycotoxin panels aren't validated for diagnosing illness. Focus on lowering exposure, and test blood lead or PFAS only when there's a specific reason.</p>"""),
    ],
    pearls=[
        "Ask about home age, water source and hobbies. These questions uncover most significant exposures.",
        "Recommend a radon test to every homeowner. Kits are cheap.",
        "Give one or two swaps at a time so advice doesn't turn into fear.",
    ],
    redflags=[
        "Elevated blood lead in a child or pregnant patient: follow public health guidance and report as required.",
        "Symptoms that cluster at work or in one building, or in several household members.",
        "Suspected carbon monoxide exposure (headache and nausea in several people at home): emergency care.",
    ],
    case=("A couple trying to conceive asks how to \"detox.\" They live in a 1960s house with well water and are renovating the kitchen. One of them eats swordfish weekly.",
          "Skip detox products and provoked metal testing. Recommend testing the well water (including lead and, if local data suggest it, PFAS), a radon test, lead-safe renovation practices (pre-1978 paint), and switching to low-mercury fish. Consider a blood lead level for the partner planning pregnancy given the renovation. Suggest glass food containers and ventilation while cooking."),
    quiz=[
        ("Which test is discouraged by medical toxicologists?",
         ["Blood lead level", "Provoked (chelation challenge) urine heavy metal testing", "Home radon test"], 1,
         "Provoked urine testing has no valid reference ranges and leads to misdiagnosis."),
        ("At what radon level does EPA recommend fixing a home?",
         ["0.5 pCi/L", "4 pCi/L or higher", "Only above 50 pCi/L"], 1,
         "EPA recommends fixing homes at 4 pCi/L or higher and considering it between 2 and 4."),
    ],
    refs=[
        "National Academies of Sciences, Engineering, and Medicine. Guidance on PFAS Exposure, Testing, and Clinical Follow-Up. 2022.",
        "CDC. Blood Lead Reference Value. 2021.",
        "U.S. EPA. A Citizen's Guide to Radon.",
        "FDA/EPA. Advice About Eating Fish. Updated 2021.",
        "American College of Medical Toxicology. Position statement on post-chelator challenge urinary metal testing. J Med Toxicol. 2010.",
        "Rajagopalan S, et al. Air pollution and cardiovascular disease: JACC State-of-the-Art Review. J Am Coll Cardiol. 2018.",
        "ATSDR. Case Studies in Environmental Medicine: Taking an Exposure History.",
    ],
    handout=("Simple swaps at home", """        <p>You can't avoid every chemical, and you don't need to. A few simple steps lower the biggest exposures:</p>
        <ul>
          <li>Test your home for radon. Kits are inexpensive.</li>
          <li>Don't microwave food in plastic. Use glass or ceramic.</li>
          <li>If you have well water, test it. Use a certified filter if needed.</li>
          <li>Turn on the vent fan when you cook.</li>
          <li>Take shoes off at the door, and dust with a damp cloth.</li>
          <li>Pick lower-mercury fish like salmon, sardines and shrimp.</li>
        </ul>
        <p><strong>Living in a home built before 1978?</strong> Old paint may contain lead. Ask us before sanding or renovating, especially if you're pregnant or have young children.</p>"""),
),
# ---------------------------------------------------------------- 10
dict(
    num=10, slug="lab-interpretation", minutes=34,
    title="Lab selection and interpretation",
    summary="Ordering with purpose, reference vs. optimal ranges, and which specialty tests have real evidence.",
    objectives=[
        "Order tests that will change management, and anticipate false positives.",
        "Explain reference intervals and when \"optimal\" ranges are evidence-based.",
        "Judge specialty tests by their evidence before ordering.",
    ],
    lessons=[
        ("ordering", "Ordering with purpose", """        <p>Before ordering, ask: <strong>will this result change what I do?</strong> If not, it adds cost, worry and follow-up testing.</p>
        <ul>
          <li><strong>Panels multiply false positives.</strong> Reference intervals cover 95% of healthy people, so each test flags about 1 in 20 healthy patients. With 20 independent tests, the chance of at least one "abnormal" result is about 64%.</li>
          <li><strong>Pretest probability matters.</strong> A positive result in a low-risk patient is more likely to be a false positive.</li>
          <li><strong>Cost is part of the decision.</strong> Many specialty tests are self-pay. Tell patients the cost and what the result could change.</li>
        </ul>
        <p>Choosing Wisely examples that apply here: don't screen healthy adults for vitamin D deficiency, don't order reverse T3 routinely, and don't use IgG testing to diagnose food allergy or intolerance.</p>"""),
        ("ranges", "Reference vs. optimal ranges", """        <p>A reference interval is the middle 95% of results from a reference population. It describes what is common, not always what is healthy.</p>
        <ul>
          <li><strong>Some "optimal" targets are evidence-based:</strong> LDL goals by cardiovascular risk, A1c targets, ferritin of 75 ng/mL or higher for restless legs, and 25-hydroxyvitamin D of 20 ng/mL or higher for bone health (Institute of Medicine).</li>
          <li><strong>Many are not.</strong> Narrow "functional ranges" for TSH, fasting insulin or other markers often lack outcome data. Treating to them can cause harm, such as overtreating thyroid disease.</li>
          <li><strong>Results vary.</strong> Biological variation, lab methods, fasting, time of day (testosterone and cortisol), recent exercise, and biotin all change results. Repeat a surprising value before acting.</li>
          <li><strong>Trends beat single values.</strong> A rising A1c within the normal range tells you more than one result.</li>
        </ul>"""),
        ("specialty", "Specialty tests: what holds up", """        <p>Specialty labs (including those ordered through ordering platforms) range from well validated to unproven. A quick guide:</p>
""" + table(["Test", "Evidence", "Use it for"], [
            ["Fecal calprotectin", "Strong", "Separating IBS from inflammatory bowel disease"],
            ["ApoB and Lp(a)", "Strong", "Cardiovascular risk"],
            ["Coronary artery calcium", "Strong", "Statin decisions in borderline or intermediate risk"],
            ["hs-CRP", "Moderate", "Cardiovascular risk enhancer"],
            ["Glucose or lactulose breath test", "Moderate, with limits", "Suspected SIBO"],
            ["Fasting insulin and HOMA-IR", "Limited standardization", "Tracking insulin resistance over time"],
            ["Dried urine hormone panels", "Limited validation", "Not a substitute for serum testing; not needed to dose menopause hormone therapy"],
            ["Organic acids", "Limited", "Rare inherited metabolic disorders (specialist use)"],
            ["Comprehensive stool microbiome", "Not validated for treatment decisions", "Not recommended in routine care"],
            ["IgG food sensitivity", "Not valid", "Not recommended"],
            ["Salivary cortisol \"adrenal fatigue\" panel", "Not valid", "Not recommended (late-night salivary cortisol for Cushing's is valid)"],
            ["Urine mycotoxins, provoked urine metals", "Not valid", "Not recommended"],
            ["MTHFR genotype", "Not useful", "ACMG recommends against testing for thrombophilia or pregnancy loss"],
        ]) + """
        <p>When a patient brings outside results, thank them, explain what the test can and can't show, and refocus on findings that change care.</p>"""),
    ],
    pearls=[
        "Ask \"What will I do differently with this result?\" before ordering.",
        "Repeat a surprising result before you treat it.",
        "Most cardiometabolic risk can be estimated from a standard lipid panel, A1c, blood pressure, plus a one-time Lp(a).",
    ],
    redflags=[
        "Critical values (very high potassium, very low sodium, very high calcium, severe anemia): act the same day.",
        "A test result that doesn't fit the patient: consider lab error, interference (biotin) or specimen problems.",
        "Incidental findings: follow evidence-based guidance and avoid cascades of further testing.",
    ],
    case=("A patient brings a $400 panel showing \"high\" IgG to eggs, dairy and wheat, a \"low\" salivary cortisol pattern, and an MTHFR variant. They've cut out eggs, dairy and wheat and feel worse.",
          "Explain that IgG reflects exposure, not intolerance; the salivary panel isn't validated for adrenal fatigue; and MTHFR variants are common and don't change care. Help them reintroduce foods one at a time. If their symptoms suggest celiac disease, test once they are eating wheat again, since the test needs gluten exposure. Then run a focused evaluation of the symptoms that brought them in."),
    quiz=[
        ("If you order 20 independent tests on a healthy person, the chance of at least one abnormal result is about:",
         ["5%", "20%", "64%"], 2,
         "Each test flags about 5% of healthy people, so 1 minus 0.95 to the 20th power is about 64%."),
        ("Which specialty test is well validated?",
         ["IgG food sensitivity panel", "Fecal calprotectin", "Urine mycotoxin panel"], 1,
         "Fecal calprotectin reliably helps separate IBS from inflammatory bowel disease."),
    ],
    refs=[
        "Choosing Wisely (ABIM Foundation): recommendations from the Endocrine Society, AAAAI, and American Society for Clinical Pathology.",
        "Institute of Medicine. Dietary Reference Intakes for Calcium and Vitamin D. 2011.",
        "Hickey SE, et al. ACMG Practice Guideline: lack of evidence for MTHFR polymorphism testing. Genet Med. 2013; reaffirmed 2020.",
        "Grundy SM, et al. 2018 AHA/ACC Guideline on the Management of Blood Cholesterol. Circulation. 2019.",
        "Lacy BE, et al. ACG Clinical Guideline: Management of Irritable Bowel Syndrome. Am J Gastroenterol. 2021.",
        "American College of Medical Toxicology. Position statement on post-chelator challenge urinary metal testing. 2010.",
    ],
    handout=("Understanding your labs", """        <ul>
          <li><strong>"Normal" ranges</strong> cover most healthy people. A result slightly outside the range is often fine, and we may repeat it.</li>
          <li><strong>More tests aren't always better.</strong> Each extra test raises the chance of a false alarm.</li>
          <li><strong>Before blood work:</strong> ask if you need to fast, stop biotin for 2 days, and tell us about supplements.</li>
          <li><strong>Some tests sold online aren't reliable,</strong> such as IgG food sensitivity tests. Ask us before paying for one.</li>
        </ul>
        <p><strong>Good questions to ask about any test:</strong> What will this show? Will it change my treatment? What does it cost?</p>"""),
),
]
