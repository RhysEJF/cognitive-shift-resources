---
corpus: agentic-memory
kind: paper-digest
slug: santamargarita-2019-grid-tie-impedance
title: "Study of Applicability of Simple Closed Loop Input Impedance Model for Grid-Tie Inverters"
authors:
  - "Santamargarita, Daniel"
  - "Huerta, Francisco"
  - "Sanz, Marina"
  - "Lazaro, Antonio"
  - "D'Arco, Salvatore"
  - "Sanchez, Santiago"
  - "Tedeschi, Elisabetta"
  - "Roldan, Javier"
year: 2019
publication_date: "2019-10"
venue: "IECON 2019 — 45th Annual Conference of the IEEE Industrial Electronics Society"
source_url: "https://arxiv.org/abs/2401.17122"
doi: "10.1109/IECON.2019.8926942"
arxiv_id: "2401.17122"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "A reduced-order model is only safe inside the regime it was derived for: the CPL (constant-power-load) approximation of a grid-tie inverter's input impedance matches measurements when feedforward sensing is wideband, but starts to drift visibly once that sensing bandwidth is constrained — the model breaks exactly where the lossy assumption stops holding, not where the math stops working."
topics:
  - reduced-order-models
  - power-electronics
  - impedance-modeling
  - stability-analysis
  - off-topic-for-memory-architect-lens
tags:
  - paper
  - electrical-engineering
  - grid-tie-inverter
  - control-systems
  - off-topic
entities:
  - santamargarita-daniel
  - huerta-francisco
related_digests: []
citations:
  - title: "Topological Overview of Powertrains for Battery-Powered Vehicles With Range Extenders"
    authors: ["I. Aharon", "A. Kuperman"]
    year: 2011
    venue: "IEEE Trans. Power Electron., vol. 26, no. 3, pp. 868–876"
    doi: null
    url: null
    arxiv_id: null
  - title: "Electrical generation and distribution for the more electric aircraft"
    authors: ["C. R. Avery", "S. G. Burrow", "P. H. Mellor"]
    year: 2007
    venue: "42nd Int. Univ. Power Eng. Conf., pp. 1007–1012"
    doi: null
    url: null
    arxiv_id: null
  - title: "Predictive Energy Management for MVDC All-Electric Ships"
    authors: ["T. V. Vu", "et al."]
    year: 2017
    venue: "IEEE Electr. Sh. Technol. Symp., pp. 327–331"
    doi: null
    url: null
    arxiv_id: null
  - title: "Control and Design of DC Grids for Offshore Wind Farms"
    authors: ["C. Meyer", "M. Höing", "A. Peterson", "et al."]
    year: 2007
    venue: "IEEE Trans. Ind. Appl., vol. 43, no. 6, pp. 1475–1482"
    doi: null
    url: null
    arxiv_id: null
  - title: "Comprehensive review of stability criteria for DC power distribution systems"
    authors: ["A. Riccobono", "E. Santi"]
    year: 2014
    venue: "IEEE Trans. Ind. Appl., vol. 50, no. 5, pp. 3525–3535"
    doi: null
    url: null
    arxiv_id: null
  - title: "Research on Measurement of Dc Power Supply Impedance"
    authors: ["M. Liu", "H. Yuan", "Y. Sun"]
    year: 2009
    venue: "2009 9th Int. Conf. Electron. Meas. Instruments, pp. 2–706"
    doi: null
    url: null
    arxiv_id: null
  - title: "Practical issues of input/output impedance measurements in switching power supplies and application of measured data to stability analysis"
    authors: ["Y. Panov", "M. Jovanović"]
    year: 2005
    venue: "Conf. Proc. - IEEE Appl. Power Electron. Conf. Expo. - APEC, vol. 2, pp. 1339–1345"
    doi: null
    url: null
    arxiv_id: null
  - title: "Online grid impedance measurement using discrete-interval binary sequence injection"
    authors: ["T. Roinila", "M. Vilkko", "J. Sun"]
    year: 2014
    venue: "IEEE J. Emerg. Sel. Top. Power Electron., vol. 2, no. 4, pp. 985–993"
    doi: null
    url: null
    arxiv_id: null
  - title: "Online impedance measurement of cascaded DC/DC converters"
    authors: ["M. A. Granda", "C. Fernandez", "P. Zumel", "et al."]
    year: 2019
    venue: "Conf. Proc. - IEEE Appl. Power Electron. Conf. Expo. - APEC, vol. 2019–March, pp. 1351–1356"
    doi: null
    url: null
    arxiv_id: null
  - title: "Positive feedforward control of three-phase voltage source inverter for DC input bus stabilization with experimental validation"
    authors: ["A. Riccobono", "E. Santi"]
    year: 2013
    venue: "IEEE Trans. Ind. Appl., vol. 49, no. 1, pp. 168–177"
    doi: null
    url: null
    arxiv_id: null
  - title: "Low-cost input impedance estimator of Dc-to-Dc converters for designing the control loop in cascaded converters"
    authors: ["M. Sanz", "et al."]
    year: 2016
    venue: "Conf. Proc. - IEEE Appl. Power Electron. Conf. Expo. - APEC, vol. 2016–May, pp. 3090–3096"
    doi: null
    url: null
    arxiv_id: null
  - title: "Simple input impedance converter model to design regulators for dc-distributed system"
    authors: ["M. Sanz", "et al."]
    year: 2016
    venue: "2016 IEEE 17th Work. Control Model. Power Electron. COMPEL 2016"
    doi: null
    url: null
    arxiv_id: null
  - title: "VSC Current Control"
    authors: ["I. R. Yazdani Amirnaser"]
    year: 2010
    venue: "Voltage Sourced Converters in Power Systems"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 16
  title: "Experimental results of the input impedance for the same converter working at different powers"
  page: 6
  image_path: "figures/santamargarita-2019-grid-tie-impedance-fig.png"
---

# Study of Applicability of Simple Closed Loop Input Impedance Model for Grid-Tie Inverters

**Authors:** Daniel Santamargarita, Francisco Huerta, Marina Sanz, Antonio Lazaro, Salvatore D'Arco, Santiago Sanchez, Elisabetta Tedeschi, Javier Roldan
**Published:** 2019-10 · [Source](https://arxiv.org/abs/2401.17122)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

> **Lens-fit warning:** This is an electrical-engineering paper on power converters — it has **no AI, no language models, no memory systems, and no information-retrieval content**. It was almost certainly returned by a citation-graph walker that landed on a wrong-domain neighbour of the real seed. The digest below extracts the few cross-domain analogies that survive translation (reduced-order modelling, regime-of-validity, source/sink composition) but readers should not expect ENGRAM mapping or memory-architecture findings.

## TLDR

This 2019 IEEE conference paper (uploaded to arXiv 2024) tests when a deliberately-simplified ("reduced-order") model of a grid-tie inverter's input impedance is accurate enough to trust for DC-bus stability analysis, and when it isn't. The reduced model treats the inverter as a constant-power-load (CPL) — a negative resistance R_CPL = −V_in²/P in parallel with the input capacitor C_i — instead of solving the full DQ-frame controlled three-phase voltage-source-converter equations (set 3–8 in the paper). The team ran simulations across three rated powers (5 kW, 40 kW, 150 kW), two reference frames (DQ and αβ), and several controller bandwidths (160 Hz down to 15 Hz), and validated on a real 60-kW EGSTON-grid-emulator setup at 2.1 kW and 21 kW. Headline result: the CPL model fits the measured impedance very well across powers, reference frames and controller bandwidths — **as long as the input-voltage feedforward inside the controller is wideband**. The moment that feedforward is replaced by a constant or filtered to ≤1 kHz (which happens in real converters because of sensor noise), the model diverges noticeably from the measured impedance and may mis-predict stability. Practical recommendation: oversize the input capacitor; that swamps the controller dynamics and lets the cheap CPL model keep working in real designs.

## Key Takeaway

A reduced-order model is only safe inside the regime it was derived for: the CPL (constant-power-load) approximation of a grid-tie inverter's input impedance matches measurements when feedforward sensing is wideband, but starts to drift visibly once that sensing bandwidth is constrained — the model breaks exactly where the lossy assumption stops holding, not where the math stops working. The right defensive move is not "use the full model everywhere"; it's to identify the engineering knob (here, capacitor oversize) that pushes the system back into the model's valid regime.

## Implications

> _Note: this paper is outside the memory-architect lens. The bullets below are forced analogies — relate at your own risk._

- **A reduced-order model is a lossy summary, not a wrong summary**: The CPL approximation throws away the controller dynamics entirely and just says "the inverter draws P watts." That is the same compression bargain a memory system makes when it stores a Haiku-distilled summary instead of the raw transcript — useful so long as the part you discarded is dominated by something else (here: the capacitor; in memory: the still-retrievable source). When the dominant term changes (low feedforward bandwidth; or in memory, a query that needs the discarded nuance), the summary fails. **Encode-layer mapping (ENGRAM E):** know which detail your write-time distillation throws away, and which queries that decision will break.
- **Validate the assumption, not the output**: The paper doesn't just compare model vs. measurement on impedance magnitude — it identifies _the specific assumption that fails_ (constant or filtered feedforward) and traces the failure back through the model. For memory systems, this argues for **regression-on-assumption** tests, not just regression-on-answer: if your extractor assumes "one decision per turn", measure how often that assumption is wrong on real transcripts, not just whether final answers look right.
- **Oversize the buffer to keep the cheap model valid**: The paper's practical fix is "oversize the input capacitor so the controller dynamics don't matter." Memory-system analogue: keep enough raw context (recent turns un-distilled, or a high-resolution recency buffer) that the lossy long-term summaries don't have to carry edge-case load. **Maintenance-layer mapping (ENGRAM M):** an eviction policy that aggressively distills _everything_ is fragile; leave a buffer of un-compressed material near the working set.
- **Compose by impedance, not by interface**: Stability of a multi-converter DC bus depends on the **ratio Z_S/Z_L** (Eq. 1) of source and load impedances — i.e. the way two components interact, not their individual specs. Memory-system analogue: when you compose two retrieval stages or two write-time extractors, what matters is the _interaction_ between their failure modes (e.g. extractor produces low-recall outputs that the retriever then over-weights), not their isolated accuracy. **Network-layer mapping (ENGRAM N):** measure pair-wise compositional behaviour of memory modules, not just per-module accuracy.
- **The "real measurement" gap is the design constraint**: The paper's whole story turns on the fact that in a real converter the input-voltage sensor _cannot_ be infinite-bandwidth (noise floor forces a 1 kHz low-pass filter). The clean simulation assumed ideal sensing; production didn't. Memory-system analogue: a retrieval method that needs perfect semantic embeddings will fail the moment your embedding model is downgraded for cost — the right thing to do is design assuming a known-noisy retriever, not an ideal one. **Retrieve-layer mapping (ENGRAM R):** plan for the noisy production retriever, not the lab one.
- **No useful Ground/Aggregate/Trust signal here**: The paper has nothing to say about provenance, contradiction, write-time vs. query-time synthesis, drift, or the AI-as-maintainer question. Do not over-extract.

## How to Apply It (method)

**Scenario:** A memory-architecture team is shipping a write-time distillation layer (e.g., a Haiku-summarizer that compresses each session transcript into a 200-token "session memory" plus extracted entities). They believe the summarization is good enough on aggregate eval. They want to apply the spirit of this paper — _regime-of-validity testing_ — to find the queries where the lossy summary will silently fail in production, before users do.

**Steps:**

1. **State the lossy assumption explicitly**: Write down, in one sentence, what your reduced model _throws away_. (e.g. "The session summary preserves outcomes and named entities, and discards intermediate hypotheses that didn't pan out.") This is the analogue of "the inverter behaves as a constant-power load below the control bandwidth."

2. **Identify the engineering knob that keeps the assumption valid**: The paper's knob is input capacitor size. Yours might be: how many recent turns you keep un-summarized; or how aggressive your eviction policy is on the working set. Name the knob and its current setting.

3. **Build the "full model" reference**: Just as the paper computes the full analytical impedance (Eq. 3–8) to compare against the CPL model, build the equivalent for memory: a "no-summarization, RAG-over-full-transcript" baseline. It's slow and expensive — that's fine; it's the reference.

4. **Sweep the operating conditions**: Vary the analogue of power, reference frame, and controller bandwidth: session length (short / medium / long), question type (recall a fact / recall an intermediate / synthesize across turns), and recency (last hour / last week / last month). The paper does 3 powers × 2 frames × several bandwidths; do at least 3 × 3 × 2 = 18 buckets.

5. **Sweep the "feedforward bandwidth" analogue**: The single most important variable the paper finds is feedforward bandwidth. Yours might be: summarizer model size (Haiku-3 / Haiku-3.5 / Sonnet), or extraction-time temperature, or whether the summarizer sees the prior summary as context. Constrain it deliberately and see when the cheap layer breaks.

6. **Measure agreement on the answer AND on a structured intermediate**: The paper plots Bode magnitude and phase, not just stability/instability — i.e., it measures _how much_ the model deviates, not just _whether_ it deviates. For memory, log both end-task accuracy and an intermediate signal like "did the retriever return the source passage the gold answer cites." That intermediate signal will trip first.

7. **Find the failure regime, then engineer around it**: When you find the bucket where the lossy layer drifts (analogue: the constant/filtered feedforward case), don't rewrite the layer — change the engineering knob from step 2 (more un-summarized turns; larger working set) so the cheap layer is valid again. Treat the "rewrite the whole layer" option as last-resort.

   ```
   Audit prompt template (one per bucket, run on N=30 sessions per bucket):

   Given:
     - The full transcript of session <id> (assumed regime: <length>, <type>, <recency>)
     - The Haiku-distilled session memory for the same session
     - A test question Q drawn from <type>-bucket

   Compare:
     a) The answer produced by the agent using only the distilled memory
     b) The answer produced by the agent using the full transcript

   Output JSON:
     - agreement_on_final_answer: "match" | "partial" | "diverge"
     - agreement_on_cited_source: "match" | "diverge" | "no-citation"
     - failure_mode_if_diverge: one of [missing_intermediate, missing_entity,
                                         summary_overgeneralized, summary_hallucinated,
                                         other]
   ```

8. **Build the regression-on-assumption suite**: Pick the buckets where divergence > 5% and freeze them as a permanent eval set. The day any future change to the summarizer increases divergence in those buckets, the regression catches it — even if aggregate eval still looks fine.

**Expected outcome:** A documented "regime of validity" map for your write-time distillation layer — concretely, a table of (session-length × question-type × recency × summarizer-model) buckets each labelled "safe" or "drifts." Plus a named engineering knob (e.g. "keep last 12 turns un-summarized") with a calibrated setting that keeps the cheap layer valid for the buckets you care about. Plus a permanent eval set that catches future regressions on the failure buckets. This is the memory-systems analogue of the paper's "oversize the input capacitor" advice: don't replace the cheap layer, change the surrounding system so the cheap layer's assumption holds.

## Best Figure

![Figure 16 — Experimental results of the input impedance for the same converter working at different powers (page 6)](figures/santamargarita-2019-grid-tie-impedance-fig.png)

```
Image Candidates:
Figure 11 (p. 4): Shows where the simple CPL model first visibly diverges from the real impedance — DQ frame with constant feedforward.
Figure 13 (p. 5): The "real-world" case — DQ frame with 1 kHz feedforward bandwidth — and the practical consequence of finite sensor bandwidth.
Figure 16 (p. 6): The experimental money-shot — Bode plot of measured vs. modelled input impedance for a real 2L-VSC at 2.1 kW and 21 kW.

Best Image:
Figure Name: Figure 16: "Experimental results of the input impedance for the same converter working at different powers"
Figure Page: 6
Slide Caption: Measured vs. modelled input impedance of a real 2L-VSC at 2.1 kW and 21 kW — the headline experimental validation of the CPL model.
Description: Figure 16 is a Bode diagram (magnitude in dB on top, phase in degrees on bottom, both versus frequency 10⁻² – 10² Hz) overlaying four curves: the reduced-order CPL model and the experimental measurement at each of two operating powers (2.1 kW and 21 kW) for the same physical 60-kW 2L-VSC inverter. Both pairs of curves agree closely above ~1 Hz in magnitude and across the whole sweep in phase. The figure is the paper's primary validation that the CPL+capacitor reduced model — derived in 3 pages of analytical work — actually matches a real high-power converter once the input capacitor is appropriately sized. The same-converter / two-power design isolates the power-scaling behaviour of the model.
```

## What Experts Overlook

The overlooked detail is that **the paper's positive result is conditional on the input capacitor being oversized in the real converter** (C_in = 14.1 mF on the 60-kW EGSTON unit, where the simulation studies deliberately used the smallest commercial-grade capacitor for the rated power). The text says this explicitly in the conclusions ("the fact of having an oversized capacitor benefits the precision of the model") and in section IV ("a little oversized"). Most readers will see Fig. 16's clean agreement and conclude "the simple model works"; what's actually being shown is "the simple model works when the engineering knob the authors warned you about earlier in the paper has been set generously in the hardware under test." The simulation studies in Section III, by contrast, deliberately picked the worst case (minimum-spec capacitor) and that's where the model started to drift.

**Why it matters:** This is the paper's most useful design lesson, hiding inside its experimental setup rather than in its results section. The CPL model is not a universal good-enough approximation — it's a good-enough approximation _in a specific engineering regime_ that you have to set up deliberately. The "model works" finding is co-conditioned on a hardware decision, not just an analytical one. If you take the paper's bottom-line plot at face value without reading section IV's parameter table, you'll trust the model in the wrong regime.

**Example of good use:** A memory-systems engineer designing a Haiku-distilled session-memory layer notices that the analogue "oversized capacitor" knob is _the size of the un-summarized recency window_. They explicitly oversize it (keep the last 20 turns un-summarized rather than the spec-minimum 5), and the cheap summarization layer then works across the question types they care about. They document the recency-window size as a load-bearing parameter, not a free choice.

**Example of misapplication:** A team reads only the conclusions, ships the CPL model with the spec-minimum input capacitor (because BOM cost matters), and is surprised when their DC bus oscillates in field deployment. In memory-systems terms: a team distills everything aggressively to save tokens, sees aggregate eval still looks good (because the eval covers the regime where summaries are valid), and then ships into production where users ask exactly the queries that hit the discarded intermediate-hypothesis material — and the agent silently confabulates. The model was never wrong; the engineering regime was.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

The paper cites 13 references, all in electrical engineering (power electronics, control systems, grid integration). No AI, no NLP, no IR. The full list is in frontmatter `citations[]`. Highlights:

- [5] A. Riccobono and E. Santi (2014), _Comprehensive review of stability criteria for DC power distribution systems_, IEEE TIA — the stability-criteria reference this paper builds on (GMPM).
- [10] A. Riccobono and E. Santi (2013), _Positive feedforward control of three-phase VSI for DC input bus stabilization_ — the source of the feedforward control formulation whose bandwidth-sensitivity this paper exposes.
- [11], [12] M. Sanz et al. (2016) — the prior validations of the same CPL model for DC-DC converters, which this paper extends to DC-AC.
- [13] Yazdani & Amirnaser (2010), _Voltage Sourced Converters in Power Systems_ — the canonical DQ-frame VSC textbook the analytical derivation leans on.

None of these citations are relevant to memory architectures; the citation-walker should treat this node as a domain dead-end.

## Related Digests

_No related digests in the wiki — this paper is outside the memory-architecture topic cluster._

## Reviewer Notes

**Overall severity:** Clean

Every load-bearing claim in the digest was checked against the paper text:

- Rated powers (5 kW / 40 kW / 150 kW), reference frames (DQ / αβ), and controller bandwidths (160 Hz, 15 Hz) match Figs 5–9 and their captions.
- Real-converter parameters (60 kW commercial unit, C_in = 14.1 mF, test powers 2.1 kW and 21 kW, 1 kHz feedforward bandwidth) match Table I and Section IV text.
- CPL model formulation (R_CPL = -V_in²/P, total Z = parallel of R_CPL and input capacitor) matches Eqs (9)-(10).
- GMPM stability criterion, EGSTON grid emulator, FFT-based impedance reconstruction, and active damping with LCL filter all explicitly named in the paper.
- "13 references, all electrical-engineering / power-electronics" verified by counting the bibliography ([1]–[13]) and reading each entry's venue.
- The "oversized capacitor" caveat is in the paper's own Conclusions section, not a digest invention.

The digest's lens-fit warning, ENGRAM-mapping bullets, and worked memory-systems "method translation" are all clearly marked as analogies authored by the digester — they are not attributed to the paper, so they are not claims about the paper and do not need source-checking.
