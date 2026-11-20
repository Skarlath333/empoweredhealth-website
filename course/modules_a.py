"""Course content, modules 1 to 5. Original writing; sources are listed in each module's refs."""


def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'        <div class="table-scroll"><table class="lab-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


MODULES = [
# ---------------------------------------------------------------- 1
dict(
    num=1, slug="foundations", minutes=30,
    title="Foundations of root-cause care",
    summary="Systems thinking, the extended intake and timeline, and fitting functional medicine alongside conventional care.",
    objectives=[
        "Describe how upstream factors (sleep, diet, stress, exposures) drive common chronic presentations.",
        "Take an extended history and timeline that links life events to symptom onset.",
        "Explain where root-cause care adds to, and doesn't replace, guideline-based treatment.",
    ],
    lessons=[
        ("systems", "Systems thinking in practice", """        <p>A diagnosis tells you <em>what</em> is happening. Root-cause care adds a second question: <em>why in this patient, and why now?</em> Two patients with stage 1 hypertension may share a label but not a cause. One has untreated sleep apnea, the other a high-sodium diet and heavy alcohol use. Treating the blood pressure is necessary for both. Finding the driver changes the rest of the plan.</p>
        <p>Rather than reviewing organ systems in isolation, map how they interact. A useful working set of upstream domains:</p>
""" + table(["Domain", "Ask about", "Commonly linked to"], [
            ["Sleep", "Duration, snoring, witnessed apneas, shift work", "Insulin resistance, hypertension, mood, weight"],
            ["Nutrition", "Ultra-processed food, protein, fiber, alcohol", "Dyslipidemia, fatty liver, GI symptoms"],
            ["Movement", "Steps, strength training, sitting time", "Glycemic control, sarcopenia, mood"],
            ["Stress", "Load, supports, trauma history", "Sleep, GI function, blood pressure"],
            ["Exposures", "Smoking, occupation, water source, home age", "Respiratory, endocrine and cancer risk"],
            ["History", "Family history, medications, antibiotic and PPI use", "Nutrient depletion, microbiome changes"],
        ]) + """
        <p>The goal is a problem list where each diagnosis sits next to its likely contributors. That list becomes the plan: treat the diagnosis, and work on the two or three contributors most likely to move it.</p>"""),
        ("intake", "The extended intake and timeline", """        <p>The extended intake has three parts, and it can be spread across two visits.</p>
        <ol>
          <li><strong>The story.</strong> Start open-ended: "When did you last feel well?" Then ask what changed around that time. Patients often know the turning point (a move, a pregnancy, an infection, a new medication) even when they haven't connected it to their symptoms.</li>
          <li><strong>The timeline.</strong> Lay out life events in order next to symptom onset: birth and early life, major infections and antibiotic courses, surgeries, pregnancies, medication starts and stops, losses and other stressors. Look for clusters.</li>
          <li><strong>Validated screens.</strong> Use short, scored tools instead of open-ended review of systems where you can.</li>
        </ol>
""" + table(["Screen", "What it covers", "Notes"], [
            ["PHQ-9", "Depression", "Item 9 asks about self-harm; have a plan for positive answers"],
            ["GAD-7", "Anxiety", "Score of 10 or more warrants further evaluation"],
            ["STOP-BANG", "Obstructive sleep apnea", "Score of 3 or more suggests intermediate to high risk"],
            ["Epworth Sleepiness Scale", "Daytime sleepiness", "Over 10 suggests excessive sleepiness"],
            ["Perceived Stress Scale (PSS-10)", "Stress load", "Useful to track change over time"],
            ["3-day food and symptom log", "Diet, timing, triggers", "Cheap, and patients learn from doing it"],
        ]) + """
        <p>Close the intake by agreeing on priorities. A patient with eight concerns does better with two or three changes they choose than with a twelve-item plan. Write those down together and set a follow-up date.</p>"""),
        ("alongside", "Working alongside conventional care", """        <p>Root-cause care is an addition to standard medicine, not a replacement for it. In practice that means:</p>
        <ul>
          <li><strong>Guidelines first.</strong> Screenings, vaccines, and evidence-based medications stay in the plan. Lifestyle work runs alongside treatment, not instead of it, unless the risk is low and the patient chooses a time-limited trial with a set recheck.</li>
          <li><strong>Shared decision-making.</strong> Present options with honest effect sizes. "Lifestyle change can lower blood pressure about as much as one medication" is more useful than "diet can fix this."</li>
          <li><strong>Supplements are medicines.</strong> Under U.S. law they are not reviewed by the FDA for safety or benefit before sale. Prefer products with third-party testing (USP Verified or NSF Certified), check interactions (St. John's wort induces CYP3A4; vitamin K affects warfarin), and record them on the medication list.</li>
          <li><strong>Coordinate.</strong> Send visit notes to the primary care clinician and specialists. A patient seeing several clinicians needs one shared plan.</li>
          <li><strong>Know your scope.</strong> Follow your state's scope-of-practice and collaboration rules, and current DEA rules for prescribing controlled substances (such as testosterone) by telehealth, which have been changing.</li>
        </ul>
        <p>Evidence quality varies widely in this field. This course says when an idea is well supported, when it is promising, and when it is not supported. Patients deserve the same honesty.</p>"""),
    ],
    pearls=[
        "Review the medication list as a possible cause. Long-term metformin can lower B12, PPIs can lower magnesium and B12, and statins are associated with muscle symptoms.",
        "Ask \"When did you last feel well?\" early. The answer often points to the trigger.",
        "Limit the plan to two or three changes per visit, chosen with the patient.",
    ],
    redflags=[
        "Unintentional weight loss, GI bleeding, new neurologic deficits, chest pain, or fevers and night sweats.",
        "Overdue age-appropriate cancer screening. Get it done before attributing symptoms to lifestyle.",
        "A positive answer on PHQ-9 item 9: assess suicide risk the same day; the 988 Suicide &amp; Crisis Lifeline is available by call or text.",
    ],
    case=("A 48-year-old with fatigue, an A1c of 6.0% and blood pressure of 138/88 sleeps 5.5 hours a night and snores loudly. Before adding medications, what would you screen for first?",
          "Screen for obstructive sleep apnea (STOP-BANG, then a home sleep test or polysomnography if positive). Untreated sleep apnea worsens blood pressure, insulin resistance and fatigue, so treating it can improve all three. Address sleep duration at the same time, and treat blood pressure per guidelines if it stays elevated."),
    quiz=[
        ("A patient has new stage 1 hypertension. The best root-cause approach is to:",
         ["Delay all treatment until lifestyle changes are tried for a year",
          "Treat per guidelines and also look for drivers such as sleep apnea, alcohol and sodium",
          "Order a broad specialty lab panel before deciding anything"], 1,
         "Root-cause care adds a search for drivers alongside guideline-based treatment. It does not replace it."),
        ("Which statement about dietary supplements in the U.S. is true?",
         ["The FDA approves them for safety and benefit before sale",
          "They are not reviewed by the FDA before sale, so third-party testing and interaction checks matter",
          "They cannot interact with prescription drugs"], 1,
         "Supplements are not reviewed for safety or benefit before sale. Look for USP or NSF marks and check interactions."),
    ],
    refs=[
        "National Center for Complementary and Integrative Health (NIH). Complementary, Alternative, or Integrative Health: What's In a Name?",
        "Whelton PK, et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Hypertension. 2018.",
        "Chung F, et al. STOP-Bang Questionnaire: a practical approach to screen for obstructive sleep apnea. Chest. 2016.",
        "Kroenke K, et al. The PHQ-9. J Gen Intern Med. 2001. Spitzer RL, et al. GAD-7. Arch Intern Med. 2006.",
        "U.S. FDA. Drug Safety Communication: Low magnesium levels can be associated with long-term use of proton pump inhibitors. 2011.",
        "American Diabetes Association. Standards of Care in Diabetes (current edition): B12 monitoring with long-term metformin.",
        "FDA. Dietary Supplements: Information for Consumers on Using Dietary Supplements.",
    ],
    handout=("What is functional medicine?", """        <p>Functional medicine asks <strong>why</strong> a health problem is happening. Your body's systems are connected. Poor sleep raises stress hormones, which affect blood sugar, which affects energy and mood. So we look at your food, sleep, movement, stress, environment and history, and work on those along with your symptoms.</p>
        <p>It works alongside your regular medical care, not instead of it. You may still need medicines, screenings and specialists.</p>
        <p><strong>Try this week:</strong> For 3 days, write down what you ate, how you slept, and your energy from 1 to 10 each afternoon. Bring it to your next visit.</p>
        <p><strong>Tell us about every supplement you take.</strong> Some supplements change how medicines work.</p>"""),
),
# ---------------------------------------------------------------- 2
dict(
    num=2, slug="nutrition", minutes=40,
    title="Nutrition as therapy",
    summary="Dietary patterns with real evidence, elimination diets done safely, and counseling that sticks.",
    objectives=[
        "Recommend dietary patterns with outcome evidence, with realistic effect sizes.",
        "Run an elimination diet safely, and know when testing must come first.",
        "Use brief motivational interviewing to set nutrition goals patients keep.",
    ],
    lessons=[
        ("patterns", "Dietary patterns with evidence", """        <p>Patterns beat single nutrients. The strongest outcome data support a few overlapping patterns built on vegetables, fruit, legumes, whole grains, nuts, olive oil and fish, with little ultra-processed food.</p>
""" + table(["Pattern", "Key evidence", "Best fit"], [
            ["Mediterranean", "PREDIMED: about 30% fewer major cardiovascular events with added olive oil or nuts", "Cardiovascular risk, metabolic syndrome"],
            ["DASH", "Lowered systolic pressure about 11 mmHg in people with hypertension; more with sodium reduction", "Hypertension"],
            ["Higher fiber", "Target about 14 g per 1,000 kcal (roughly 25 to 38 g a day); linked to lower mortality and diabetes risk", "Almost everyone"],
            ["Less ultra-processed food", "NIH inpatient trial: people ate about 500 kcal a day more on an ultra-processed diet", "Weight, appetite"],
        ]) + """
        <p><strong>Protein</strong> deserves attention in older adults and during weight loss. Expert groups suggest about 1.0 to 1.2 g/kg/day for healthy older adults, spread across meals, to help preserve muscle.</p>"""),
        ("elimination", "Elimination diets done safely", """        <p>Elimination diets are useful tools with real risks: nutrient gaps, social burden, and disordered eating. Use them with a clear question and an end date.</p>
        <ul>
          <li><strong>Test for celiac disease first.</strong> Order tissue transglutaminase IgA (tTG-IgA) with total IgA <em>while the patient is still eating gluten</em>. Going gluten-free first can make the tests falsely negative.</li>
          <li><strong>Low-FODMAP has the best evidence for IBS.</strong> It runs in three phases: restriction for 2 to 6 weeks, structured reintroduction, then a personalized long-term diet. A dietitian improves results.</li>
          <li><strong>Skip IgG food sensitivity panels.</strong> IgG to foods reflects exposure, not intolerance. Allergy societies advise against using them, and they lead to needless restriction.</li>
          <li><strong>Be careful in children, pregnancy, and anyone with a history of eating disorders.</strong> Screen before you restrict.</li>
        </ul>
        <p>A good elimination trial removes one or a few suspected foods for 2 to 4 weeks, tracks symptoms, then reintroduces one food at a time over 2 to 3 days each.</p>"""),
        ("anti-inflammatory", "Anti-inflammatory eating and weight", """        <p>"Anti-inflammatory" is a loose label, but the foods behind it are well studied: fish twice a week, olive oil as the main fat, plenty of colorful plants, nuts and legumes, and fewer refined starches, sugary drinks and processed meats. These patterns lower CRP modestly and improve cardiometabolic markers.</p>
        <p><strong>Alcohol</strong> raises blood pressure, triglycerides and liver fat and worsens sleep. There is no level that is good for health; less is better.</p>
        <p><strong>Patients on GLP-1 medications</strong> eat much less, so food quality matters more. Prioritize protein at each meal, fiber and fluids for constipation, and resistance training at least twice a week to limit muscle loss.</p>"""),
        ("counseling", "Counseling that sticks", """        <p>Advice alone rarely changes behavior. Brief motivational interviewing helps. Use OARS:</p>
        <ul>
          <li><strong>Open questions:</strong> "What would you like to change about how you eat?"</li>
          <li><strong>Affirmations:</strong> notice effort, not just results.</li>
          <li><strong>Reflections:</strong> say back what you heard, including mixed feelings.</li>
          <li><strong>Summaries:</strong> end with the plan in the patient's words.</li>
        </ul>
        <p>Turn the plan into one or two specific goals ("vegetables at lunch and dinner on weekdays") rather than rules ("eat clean"). Make it affordable: frozen vegetables, canned beans and fish, oats and eggs all count. Refer to a registered dietitian when you can; Medicare covers medical nutrition therapy for diabetes and kidney disease.</p>"""),
    ],
    pearls=[
        "Order celiac serology before anyone goes gluten-free.",
        "Ask what the patient ate yesterday. It gives a more honest picture than \"How is your diet?\"",
        "Every elimination diet needs a reintroduction phase and an end date.",
    ],
    redflags=[
        "Unintentional weight loss, trouble swallowing, or persistent vomiting.",
        "Signs of an eating disorder (restriction, bingeing, purging, fear of foods). Refer before prescribing any restrictive diet.",
        "Iron deficiency anemia or chronic diarrhea that hasn't been worked up.",
    ],
    case=("A 34-year-old with bloating and loose stools stopped eating gluten two months ago and feels somewhat better. She asks if she has celiac disease.",
          "Her current tTG-IgA may be falsely negative because she isn't eating gluten. Options are a gluten challenge (eating gluten daily for several weeks, following current guidance) before serology, or HLA-DQ2/DQ8 genetic testing, which can rule celiac disease out if negative. If celiac is excluded, consider IBS and a dietitian-guided low-FODMAP trial."),
    quiz=[
        ("Which test best screens for celiac disease?",
         ["IgG food sensitivity panel", "tTG-IgA with total IgA while eating gluten", "Stool microbiome test"], 1,
         "tTG-IgA with total IgA is the recommended first test, and the patient must be eating gluten."),
        ("The low-FODMAP diet should be:",
         ["Followed strictly for life", "Used in phases: short restriction, reintroduction, then personalization", "Started without any assessment"], 1,
         "Long-term strict restriction isn't needed. Reintroduction finds the patient's own triggers."),
    ],
    refs=[
        "Estruch R, et al. Primary prevention of cardiovascular disease with a Mediterranean diet supplemented with extra-virgin olive oil or nuts (PREDIMED). N Engl J Med. 2018.",
        "Appel LJ, et al. A clinical trial of the effects of dietary patterns on blood pressure (DASH). N Engl J Med. 1997.",
        "Hall KD, et al. Ultra-processed diets cause excess calorie intake and weight gain. Cell Metab. 2019.",
        "U.S. Dietary Guidelines for Americans, 2020 to 2025: fiber recommendations.",
        "Bauer J, et al. Evidence-based recommendations for optimal dietary protein intake in older people (PROT-AGE). J Am Med Dir Assoc. 2013.",
        "Rubio-Tapia A, et al. ACG Clinical Guidelines: Diagnosis and Management of Celiac Disease. Am J Gastroenterol. 2023.",
        "Lacy BE, et al. ACG Clinical Guideline: Management of Irritable Bowel Syndrome. Am J Gastroenterol. 2021.",
        "Choosing Wisely, American Academy of Allergy, Asthma &amp; Immunology: don't perform unproven diagnostic tests such as IgG testing for food allergy.",
    ],
    handout=("Eating to feel better", """        <p>You don't need a perfect diet. Small steps add up:</p>
        <ul>
          <li>Fill half your plate with vegetables or fruit. Frozen and canned count.</li>
          <li>Add beans, lentils, nuts or whole grains for fiber.</li>
          <li>Use olive oil as your main fat, and eat fish twice a week if you can.</li>
          <li>Include protein (eggs, fish, chicken, beans, Greek yogurt) at each meal.</li>
          <li>Cut back on sugary drinks, chips, and packaged snacks.</li>
        </ul>
        <p><strong>Thinking about cutting out gluten or other foods?</strong> Talk with us first. Some tests only work while you're still eating those foods.</p>
        <p><strong>Try this week:</strong> Pick one meal a day and add a vegetable to it.</p>"""),
),
# ---------------------------------------------------------------- 3
dict(
    num=3, slug="gut-health", minutes=32,
    title="GI health and the microbiome",
    summary="Assessing bloating and IBS, SIBO, fiber and probiotics, and what stool testing can and can't tell you.",
    objectives=[
        "Apply Rome IV criteria and recognize alarm features that need endoscopy or referral.",
        "Use breath testing and treatment for SIBO with an understanding of their limits.",
        "Recommend fiber, peppermint oil and probiotics where the evidence supports them.",
    ],
    lessons=[
        ("assessing", "Assessing GI symptoms", """        <p><strong>IBS (Rome IV):</strong> recurrent abdominal pain at least 1 day a week over the last 3 months, with 2 or more of: related to defecation, a change in stool frequency, or a change in stool form. Symptoms should have started at least 6 months before diagnosis. Subtype by stool form: IBS-C, IBS-D, or mixed.</p>
        <p>IBS is a positive diagnosis, not just a diagnosis of exclusion. A limited workup is enough for most patients without alarm features:</p>
""" + table(["Test", "When", "Why"], [
            ["CBC", "Most patients", "Anemia suggests another cause"],
            ["Celiac serology (tTG-IgA, total IgA)", "IBS-D or mixed", "Celiac disease mimics IBS"],
            ["Fecal calprotectin or CRP", "Diarrhea", "Screens for inflammatory bowel disease"],
            ["Giardia stool test", "Diarrhea with exposure risk", "Treatable infection"],
            ["Colonoscopy", "Alarm features, or due for age-based screening (45+)", "Rule out cancer and IBD"],
        ])),
        ("sibo", "SIBO and the microbiome", """        <p>Small intestinal bacterial overgrowth (SIBO) is more likely with PPIs, opioids, diabetes or other motility disorders, prior abdominal surgery, and scleroderma.</p>
        <ul>
          <li><strong>Breath testing</strong> (glucose or lactulose) is the usual test. North American consensus: a hydrogen rise of 20 ppm or more within 90 minutes is positive; methane of 10 ppm or more suggests intestinal methanogen overgrowth, often with constipation. False positives and negatives are common, so interpret in context.</li>
          <li><strong>Treatment:</strong> rifaximin is FDA-approved for IBS-D (550 mg three times a day for 14 days) and is commonly used for SIBO. Fix the cause where you can: deprescribe PPIs that aren't needed, review opioids, and manage diabetes.</li>
          <li><strong>Commercial stool microbiome panels</strong> describe which bacteria are present, but there are no validated cutoffs that guide treatment. They are not part of guideline-based care.</li>
        </ul>
        <p>Long-term PPI use deserves review at every visit. Many patients can taper (halve the dose for 2 to 4 weeks, then stop, using on-demand antacids or H2 blockers for rebound symptoms). Keep PPIs for Barrett's esophagus, severe esophagitis, and high bleeding risk.</p>"""),
        ("fiber-probiotics", "Fiber, probiotics and food", """""" + table(["Intervention", "Evidence", "How to use"], [
            ["Soluble fiber (psyllium)", "Recommended for IBS symptoms (ACG)", "Start 3 to 4 g a day and increase slowly; insoluble bran can worsen bloating"],
            ["Peppermint oil", "Conditional recommendation for global IBS symptoms (ACG)", "Enteric-coated capsules; may worsen reflux"],
            ["Low-FODMAP diet", "Limited trial recommended for IBS (ACG)", "Phased, ideally with a dietitian"],
            ["Probiotics", "AGA advises against for most GI conditions outside trials", "Possible exception: specific strains to prevent C. difficile with antibiotics"],
            ["Fermented foods", "Raised microbiome diversity and lowered inflammatory markers in a small trial", "Yogurt, kefir, kimchi, sauerkraut as tolerated"],
            ["Gut-directed CBT or hypnotherapy", "Recommended for IBS (ACG)", "Works well alongside diet changes"],
        ])),
    ],
    pearls=[
        "Check celiac serology before labeling IBS-D.",
        "Fecal calprotectin helps separate IBS from inflammatory bowel disease in patients with diarrhea.",
        "Before treating \"SIBO,\" ask why it might be there: PPIs, opioids, motility problems or surgery.",
    ],
    redflags=[
        "Rectal bleeding, iron deficiency anemia, unintentional weight loss, or nocturnal diarrhea.",
        "New symptoms at 45 or older, or a family history of colorectal cancer, IBD or celiac disease.",
        "Difficulty swallowing, persistent vomiting, or fever with abdominal pain.",
    ],
    case=("A 29-year-old has had cramping and loose stools for a year, better after bowel movements. CBC is normal. She has no alarm features. She asks for a comprehensive stool microbiome test.",
          "She likely meets Rome IV criteria for IBS-D. Check celiac serology and fecal calprotectin. A stool microbiome panel won't change management. Start with soluble fiber, a trial of peppermint oil or a dietitian-guided low-FODMAP diet, and consider gut-directed CBT. Rifaximin is an option if symptoms persist."),
    quiz=[
        ("Which finding is an alarm feature that warrants further workup in suspected IBS?",
         ["Bloating after meals", "Pain relieved by defecation", "Iron deficiency anemia"], 2,
         "Anemia, bleeding, weight loss, nocturnal symptoms and older age at onset need further evaluation."),
        ("What does current AGA guidance say about probiotics?",
         ["Recommended for all patients with IBS", "Not recommended for most GI conditions outside clinical trials", "Should replace antibiotics"], 1,
         "AGA advises against probiotics for most GI conditions except in clinical trials, with a few specific exceptions."),
    ],
    refs=[
        "Lacy BE, et al. ACG Clinical Guideline: Management of Irritable Bowel Syndrome. Am J Gastroenterol. 2021.",
        "Mearin F, Lacy BE, et al. Bowel Disorders (Rome IV). Gastroenterology. 2016.",
        "Rezaie A, et al. Hydrogen and Methane-Based Breath Testing in Gastrointestinal Disorders: The North American Consensus. Am J Gastroenterol. 2017.",
        "Pimentel M, et al. ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth. Am J Gastroenterol. 2020.",
        "Su GL, et al. AGA Clinical Practice Guidelines on the Role of Probiotics in the Management of Gastrointestinal Disorders. Gastroenterology. 2020.",
        "Targownik LE, et al. AGA Clinical Practice Update on De-Prescribing of Proton Pump Inhibitors. Gastroenterology. 2022.",
        "Wastyk HC, et al. Gut-microbiota-targeted diets modulate human immune status. Cell. 2021.",
    ],
    handout=("Caring for your gut", """        <ul>
          <li>Add fiber slowly. A spoonful of psyllium (like Metamucil) in water each day is a good start.</li>
          <li>Drink plenty of water, especially as you add fiber.</li>
          <li>Try fermented foods you enjoy, such as yogurt or kefir.</li>
          <li>Eat slowly, and move your body every day. Walking helps digestion.</li>
          <li>Stress affects the gut. Calming practices can ease symptoms.</li>
        </ul>
        <p><strong>Call us or get care soon</strong> if you see blood in your stool, lose weight without trying, wake up at night with diarrhea, or have trouble swallowing.</p>
        <p><strong>Taking acid reducers (like omeprazole) every day?</strong> Ask us whether you still need them. Don't stop suddenly on your own.</p>"""),
),
# ---------------------------------------------------------------- 4
dict(
    num=4, slug="metabolic-health", minutes=42,
    title="Insulin resistance and cardiometabolic risk",
    summary="Fasting insulin, HOMA-IR, A1c, ApoB and Lp(a), plus lifestyle and medication options.",
    objectives=[
        "Recognize insulin resistance and metabolic syndrome before diabetes develops.",
        "Use ApoB, Lp(a) and coronary calcium to refine cardiovascular risk.",
        "Combine lifestyle change and medication using outcome data.",
    ],
    lessons=[
        ("early", "Spotting insulin resistance early", """        <p>Insulin resistance can precede diabetes by a decade. Look for central weight gain, acanthosis nigricans, skin tags, PCOS, fatty liver, high triglycerides with low HDL, and a history of gestational diabetes.</p>
""" + table(["Measure", "Threshold", "Notes"], [
            ["A1c", "5.7 to 6.4% prediabetes; 6.5% or more diabetes", "Less reliable with anemia, recent transfusion, or some hemoglobin variants"],
            ["Fasting glucose", "100 to 125 mg/dL prediabetes; 126 or more diabetes", "Confirm abnormal results"],
            ["Metabolic syndrome", "3 of 5: waist over 40 in (men) or 35 in (women); TG 150+; HDL under 40 (men) or 50 (women); BP 130/85+; glucose 100+", "Raises cardiovascular and diabetes risk"],
            ["Triglyceride to HDL ratio", "Higher ratios track with insulin resistance", "Cheap surrogate from a standard lipid panel"],
            ["Fasting insulin and HOMA-IR", "HOMA-IR = glucose (mg/dL) x insulin (uIU/mL) / 405", "No standardized cutoff and assays vary; best for trends"],
        ]) + """
        <p><strong>Screen early.</strong> The ADA recommends testing all adults starting at age 35, and earlier in adults with overweight or obesity and a risk factor. Check liver health too: metabolic dysfunction-associated steatotic liver disease (MASLD) is common, and a FIB-4 score helps decide who needs elastography.</p>"""),
        ("lipids", "Lipids beyond LDL", """""" + table(["Test", "What it adds", "Use"], [
            ["ApoB", "Counts atherogenic particles (one ApoB per particle)", "Helpful when triglycerides are high or LDL seems falsely reassuring"],
            ["Lp(a)", "Genetic, mostly fixed risk factor", "Measure once in adulthood; 50 mg/dL (about 125 nmol/L) or higher is a risk enhancer"],
            ["Non-HDL cholesterol", "All atherogenic cholesterol", "Free from a standard panel; no fasting needed"],
            ["hs-CRP", "Inflammation", "2 mg/L or higher is a risk enhancer"],
            ["Coronary artery calcium (CAC)", "Shows plaque directly", "For borderline or intermediate risk when the statin decision is unclear; a score of 0 lowers near-term risk"],
        ]) + """
        <p>Estimate 10-year risk with the AHA PREVENT calculator, then use risk enhancers (family history, Lp(a), CRP, metabolic syndrome, chronic kidney disease, inflammatory disease, early menopause, preeclampsia) to guide shared decisions about statins.</p>"""),
        ("lifestyle", "Lifestyle that moves the numbers", """        <p>The Diabetes Prevention Program is the benchmark: about 7% weight loss plus 150 minutes a week of activity cut progression to diabetes by 58% (71% in adults 60 and older). Metformin cut it by 31%.</p>
        <ul>
          <li><strong>Resistance training</strong> two or more days a week improves insulin sensitivity independent of weight loss.</li>
          <li><strong>Walking after meals</strong>, even 10 to 15 minutes, lowers post-meal glucose.</li>
          <li><strong>Sleep</strong> under 6 hours worsens insulin sensitivity. Screen for sleep apnea.</li>
          <li><strong>Diet:</strong> fewer refined carbohydrates and sugary drinks, more fiber and protein. Lower-carbohydrate and Mediterranean patterns both work; adherence matters more than the label.</li>
          <li><strong>Continuous glucose monitors</strong> in people without diabetes can motivate change, but evidence for health outcomes is limited.</li>
        </ul>"""),
        ("medications", "Medications and when to use them", """""" + table(["Drug", "Key evidence or role", "Cautions"], [
            ["Metformin", "Consider for prediabetes, especially BMI 35+, under 60, or prior gestational diabetes", "GI upset; check B12 over time"],
            ["GLP-1 receptor agonists (semaglutide) and GIP/GLP-1 (tirzepatide)", "Weight loss of roughly 15 to 20%; semaglutide cut major cardiovascular events 20% in people with CVD and obesity (SELECT)", "Not for personal or family history of medullary thyroid cancer or MEN2; GI effects; muscle loss; use FDA-approved products"],
            ["SGLT2 inhibitors", "Heart failure and kidney protection", "Genital infections; rare euglycemic ketoacidosis"],
            ["Statins", "First-line for elevated risk per guidelines", "Muscle symptoms are often not caused by the statin; consider rechallenge or another statin"],
        ]) + """
        <p>Medication and lifestyle work together. GLP-1 users who keep up protein intake and strength training preserve more muscle, and those who stop the drug usually regain weight unless habits have changed.</p>"""),
    ],
    pearls=[
        "Triglycerides over 150 with a low HDL are an insulin resistance clue on a routine panel.",
        "Order Lp(a) once. It is largely genetic, and a high result changes how aggressive you should be with other risk factors.",
        "Use HOMA-IR to track a patient over time, not to diagnose.",
    ],
    redflags=[
        "Glucose over 250 mg/dL with symptoms, weight loss, or ketones: evaluate the same day for diabetes needing insulin or DKA.",
        "LDL 190 mg/dL or higher: consider familial hypercholesterolemia and screen relatives.",
        "Chest pain, exertional shortness of breath or claudication: evaluate for vascular disease before starting an exercise plan.",
    ],
    case=("A 52-year-old woman has an A1c of 6.1%, triglycerides of 210, HDL of 38, a waist of 39 inches, and LDL of 118. Her father had a heart attack at 50.",
          "She has prediabetes and metabolic syndrome. Plan DPP-style lifestyle change (about 7% weight loss, 150 minutes of activity, strength training), check Lp(a) and ApoB, and estimate risk with PREVENT. With the family history and metabolic syndrome as risk enhancers, discuss a statin or a CAC score to guide that decision. Consider metformin or GLP-1 therapy if weight or glucose don't improve."),
    quiz=[
        ("In the Diabetes Prevention Program, lifestyle change reduced progression to diabetes by about:",
         ["10%", "31%", "58%"], 2,
         "Lifestyle change reduced diabetes incidence by 58%; metformin reduced it by 31%."),
        ("How often should most adults have Lp(a) measured?",
         ["Every year", "Once in adulthood", "Only after a heart attack"], 1,
         "Lp(a) is mostly genetic and stable, so one measurement is usually enough."),
    ],
    refs=[
        "Diabetes Prevention Program Research Group. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med. 2002.",
        "American Diabetes Association. Standards of Care in Diabetes (current edition), sections 2 and 3.",
        "Grundy SM, et al. Diagnosis and management of the metabolic syndrome: AHA/NHLBI Scientific Statement. Circulation. 2005.",
        "Grundy SM, et al. 2018 AHA/ACC Guideline on the Management of Blood Cholesterol. Circulation. 2019.",
        "Khan SS, et al. Development and validation of the American Heart Association's PREVENT equations. Circulation. 2024.",
        "Lincoff AM, et al. Semaglutide and cardiovascular outcomes in obesity without diabetes (SELECT). N Engl J Med. 2023.",
        "Rinella ME, et al. AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver disease. Hepatology. 2023.",
    ],
    handout=("Blood sugar and your heart", """        <p>Insulin resistance means your body has to work harder to keep blood sugar normal. It often comes before diabetes and raises heart risk. The good news: it responds well to change.</p>
        <ul>
          <li>Walk for 10 to 15 minutes after meals.</li>
          <li>Do strength exercises (like squats, wall push-ups or bands) twice a week.</li>
          <li>Swap sugary drinks for water, and add protein and fiber to meals.</li>
          <li>Aim for 7 or more hours of sleep. Loud snoring is worth mentioning to us.</li>
          <li>Losing even 5 to 7% of your weight can lower your risk a lot.</li>
        </ul>
        <p><strong>Numbers to know:</strong> your A1c, blood pressure, and cholesterol. Ask us what yours are.</p>"""),
),
# ---------------------------------------------------------------- 5
dict(
    num=5, slug="thyroid-fatigue", minutes=30,
    title="Thyroid and the fatigue workup",
    summary="TSH, free T4 and antibodies, plus the iron, B12, vitamin D, sleep and mood causes of tiredness.",
    objectives=[
        "Run a focused, cost-conscious workup for persistent fatigue.",
        "Interpret thyroid tests, including subclinical hypothyroidism.",
        "Dose and monitor levothyroxine, and discuss combination therapy honestly.",
    ],
    lessons=[
        ("fatigue", "The fatigue workup", """        <p>Most fatigue has more than one cause. Start with sleep, mood, medications, alcohol, menstrual blood loss, diet, and activity. A focused first round of labs:</p>
""" + table(["Test", "Look for", "Notes"], [
            ["CBC", "Anemia", "Microcytosis suggests iron deficiency"],
            ["Ferritin", "Iron deficiency", "Under 30 ng/mL indicates deficiency; ferritin rises with inflammation, so a normal value doesn't always rule it out"],
            ["TSH", "Thyroid dysfunction", "Add free T4 if abnormal"],
            ["CMP and A1c", "Kidney, liver, glucose", "Hyperglycemia causes fatigue"],
            ["B12", "Deficiency", "Check with metformin, PPIs, vegan diet, or older age; add methylmalonic acid if 200 to 400 pg/mL"],
            ["Pregnancy test", "Pregnancy", "When applicable"],
        ]) + """
        <p><strong>Iron deficiency without anemia</strong> can cause fatigue: in one trial, oral iron improved fatigue in non-anemic women with ferritin under 50 ng/mL. Always ask why iron is low. Men and postmenopausal women with iron deficiency need a GI evaluation.</p>
        <p><strong>Vitamin D</strong>: the Endocrine Society (2024) advises against routine 25-hydroxyvitamin D testing in healthy adults. Test when there is a clinical reason, such as malabsorption, osteoporosis, or kidney disease.</p>"""),
        ("thyroid-labs", "Reading thyroid labs", """""" + table(["Pattern", "Likely meaning", "Next step"], [
            ["High TSH, low free T4", "Overt hypothyroidism", "Treat; check TPO antibodies for Hashimoto's"],
            ["High TSH, normal free T4", "Subclinical hypothyroidism", "Repeat in 6 to 12 weeks; treat if TSH 10 or more, pregnancy or trying to conceive, or consider with symptoms"],
            ["Low TSH, high free T4 or T3", "Hyperthyroidism", "TRAb or uptake scan; refer as needed"],
            ["Low TSH, low free T4", "Possible central hypothyroidism or acute illness", "Evaluate the pituitary"],
        ]) + """
        <ul>
          <li><strong>Biotin</strong> supplements can distort thyroid results. Have patients stop biotin at least 2 days before testing.</li>
          <li><strong>Older adults:</strong> TSH rises with age. In the TRUST trial, levothyroxine did not improve symptoms in adults 65 and older with subclinical hypothyroidism.</li>
          <li><strong>Reverse T3</strong> is not recommended for routine use and doesn't guide treatment.</li>
        </ul>"""),
        ("treating", "Treating hypothyroidism well", """        <ul>
          <li><strong>Dose:</strong> full replacement is about 1.6 mcg/kg/day for younger healthy adults. Start 25 to 50 mcg a day in older adults or anyone with heart disease.</li>
          <li><strong>Absorption:</strong> take on an empty stomach, 30 to 60 minutes before breakfast (or at bedtime, consistently), and 4 hours apart from calcium, iron and some other medications. PPIs and celiac disease reduce absorption.</li>
          <li><strong>Monitoring:</strong> recheck TSH 6 to 8 weeks after any dose change, then yearly when stable.</li>
          <li><strong>Avoid overtreatment.</strong> A suppressed TSH raises the risk of atrial fibrillation and bone loss, especially in older and postmenopausal patients.</li>
          <li><strong>Combination T4/T3:</strong> guidelines don't recommend it routinely. A 2021 international consensus allows a trial in patients who still have symptoms on levothyroxine with a normal TSH, after other causes are addressed, with monitoring. Desiccated thyroid has a fixed, high T3 ratio and is not first-line.</li>
        </ul>
        <p>If a patient with a normal TSH still feels exhausted, revisit the fatigue workup: sleep apnea, depression, iron, and life load are more often the answer than thyroid dosing.</p>"""),
    ],
    pearls=[
        "Ask about biotin before every thyroid test.",
        "Ferritin is an acute phase reactant. A \"normal\" ferritin with inflammation can hide iron deficiency; check transferrin saturation too.",
        "Persistent fatigue with a normal TSH is rarely a thyroid problem. Screen sleep and mood.",
    ],
    redflags=[
        "Fatigue with weight loss, fevers, night sweats, or swollen lymph nodes.",
        "Iron deficiency in men or postmenopausal women: refer for GI evaluation.",
        "A thyroid nodule, rapid neck swelling, or hoarseness: ultrasound and referral.",
        "Suspected myxedema or thyroid storm: emergency care.",
    ],
    case=("A 38-year-old woman with heavy periods reports exhaustion. Hemoglobin is 12.4 g/dL, ferritin 14 ng/mL, and TSH 2.1. She asks for a full thyroid panel with reverse T3.",
          "She has iron deficiency without anemia, a likely cause of her fatigue. Her TSH is normal, and reverse T3 won't change management. Treat with oral iron (alternate-day dosing can improve absorption and tolerance), evaluate the heavy menstrual bleeding, and recheck ferritin in about 8 to 12 weeks. Screen sleep and mood as well."),
    quiz=[
        ("A 72-year-old has a TSH of 6.8 and a normal free T4 with mild fatigue. The best next step is:",
         ["Start full-dose levothyroxine", "Repeat the TSH and look for other causes of fatigue; treatment rarely helps symptoms in this group", "Order reverse T3"], 1,
         "TSH rises with age, and the TRUST trial found no symptom benefit from treatment in adults 65 and older with subclinical hypothyroidism."),
        ("Which supplement can interfere with thyroid lab results?",
         ["Magnesium", "Biotin", "Fish oil"], 1,
         "High-dose biotin interferes with many immunoassays, including TSH and free T4."),
    ],
    refs=[
        "Jonklaas J, et al. Guidelines for the Treatment of Hypothyroidism (American Thyroid Association). Thyroid. 2014.",
        "Jonklaas J, et al. Evidence-Based Use of Levothyroxine/Liothyronine Combinations in Treating Hypothyroidism: A Consensus Document. Thyroid. 2021.",
        "Stott DJ, et al. Thyroid Hormone Therapy for Older Adults with Subclinical Hypothyroidism (TRUST). N Engl J Med. 2017.",
        "Vaucher P, et al. Effect of iron supplementation on fatigue in nonanemic menstruating women with low ferritin. CMAJ. 2012.",
        "Ko CW, et al. AGA Clinical Practice Guidelines on the Gastrointestinal Evaluation of Iron Deficiency Anemia. Gastroenterology. 2020.",
        "Demay MB, et al. Vitamin D for the Prevention of Disease: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2024.",
        "U.S. FDA. Biotin (Vitamin B7): Safety Communication - May Interfere with Lab Tests. 2017, updated 2019.",
    ],
    handout=("Why am I so tired?", """        <p>Feeling tired all the time is common, and it usually has more than one cause. We'll look at:</p>
        <ul>
          <li><strong>Sleep:</strong> how long, how well, and whether you snore</li>
          <li><strong>Blood work:</strong> iron, thyroid, blood sugar, and B12</li>
          <li><strong>Mood and stress:</strong> these affect energy a lot</li>
          <li><strong>Medicines and alcohol</strong></li>
        </ul>
        <p><strong>Before your blood test:</strong> stop biotin (often in hair, skin and nail vitamins) for at least 2 days. It can make thyroid results wrong.</p>
        <p><strong>If you take thyroid medicine:</strong> take it on an empty stomach with water, and wait 4 hours before taking calcium or iron.</p>
        <p><strong>Try this week:</strong> Go to bed and wake up at the same time every day, even on weekends.</p>"""),
),
]
