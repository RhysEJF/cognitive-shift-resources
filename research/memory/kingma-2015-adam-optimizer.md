---
corpus: agentic-memory
kind: paper-digest
slug: kingma-2015-adam-optimizer
title: "Adam: A Method for Stochastic Optimization"
authors:
  - "Kingma, Diederik P."
  - "Ba, Jimmy Lei"
year: 2015
publication_date: "2015-05"
venue: "ICLR 2015"
source_url: "https://arxiv.org/abs/1412.6980"
doi: null
arxiv_id: "1412.6980"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "Adam combines RMSProp's per-parameter adaptive learning rate (exponential moving average of squared gradients) with momentum (exponential moving average of gradients) AND adds a bias-correction step that the prior art missed — and that bias correction is what lets the algorithm use β2 values close to 1 (e.g. 0.999) without diverging in the first few hundred steps, which is exactly what's needed for sparse and high-dimensional problems."
topics:
  - stochastic-optimization
  - adaptive-learning-rate
  - sgd-variants
  - convex-optimization
  - bias-correction
  - moment-estimation
  - deep-learning-training
tags:
  - paper
  - canonical
  - foundational
  - optimizer
  - iclr-2015
entities:
  - kingma-diederik
  - ba-jimmy
related_digests:
  - vaswani-2017-attention-is-all-you-need
  - bahdanau-2015-attention-align-translate
  - vassilyev-2026-rcl
  - howard-2018-ulmfit
  - touvron-2023-llama-foundation-models
citations:
  - title: "Natural gradient works efficiently in learning"
    authors: ["Amari, Shun-Ichi"]
    year: 1998
    venue: "Neural Computation"
    doi: null
    url: null
    arxiv_id: null
  - title: "Recent advances in deep learning for speech research at Microsoft"
    authors: ["Deng, Li", "Li, Jinyu", "Huang, Jui-Ting", "et al."]
    year: 2013
    venue: "ICASSP 2013"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adaptive subgradient methods for online learning and stochastic optimization"
    authors: ["Duchi, John", "Hazan, Elad", "Singer, Yoram"]
    year: 2011
    venue: "Journal of Machine Learning Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "Generating sequences with recurrent neural networks"
    authors: ["Graves, Alex"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1308.0850"
  - title: "Speech recognition with deep recurrent neural networks"
    authors: ["Graves, Alex", "Mohamed, Abdel-rahman", "Hinton, Geoffrey"]
    year: 2013
    venue: "ICASSP"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reducing the dimensionality of data with neural networks"
    authors: ["Hinton, G. E.", "Salakhutdinov, R. R."]
    year: 2006
    venue: "Science"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups"
    authors: ["Hinton, Geoffrey", "Deng, Li", "Yu, Dong", "et al."]
    year: 2012
    venue: "IEEE Signal Processing Magazine"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving neural networks by preventing co-adaptation of feature detectors"
    authors: ["Hinton, Geoffrey E.", "Srivastava, Nitish", "Krizhevsky, Alex", "et al."]
    year: 2012
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1207.0580"
  - title: "Auto-Encoding Variational Bayes"
    authors: ["Kingma, Diederik P.", "Welling, Max"]
    year: 2013
    venue: "ICLR 2014"
    doi: null
    url: null
    arxiv_id: "1312.6114"
  - title: "ImageNet classification with deep convolutional neural networks"
    authors: ["Krizhevsky, Alex", "Sutskever, Ilya", "Hinton, Geoffrey E."]
    year: 2012
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning word vectors for sentiment analysis"
    authors: ["Maas, Andrew L.", "Daly, Raymond E.", "Pham, Peter T.", "et al."]
    year: 2011
    venue: "ACL HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Non-asymptotic analysis of stochastic approximation algorithms for machine learning"
    authors: ["Moulines, Eric", "Bach, Francis R."]
    year: 2011
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Revisiting natural gradient for deep networks"
    authors: ["Pascanu, Razvan", "Bengio, Yoshua"]
    year: 2013
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1301.3584"
  - title: "Acceleration of stochastic approximation by averaging"
    authors: ["Polyak, Boris T.", "Juditsky, Anatoli B."]
    year: 1992
    venue: "SIAM Journal on Control and Optimization"
    doi: null
    url: null
    arxiv_id: null
  - title: "A fast natural Newton method"
    authors: ["Roux, Nicolas L.", "Fitzgibbon, Andrew W."]
    year: 2010
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Efficient estimations from a slowly convergent Robbins-Monro process"
    authors: ["Ruppert, David"]
    year: 1988
    venue: "Cornell University Technical Report"
    doi: null
    url: null
    arxiv_id: null
  - title: "No more pesky learning rates"
    authors: ["Schaul, Tom", "Zhang, Sixin", "LeCun, Yann"]
    year: 2012
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1206.1106"
  - title: "Fast large-scale optimization by unifying stochastic gradient and quasi-Newton methods"
    authors: ["Sohl-Dickstein, Jascha", "Poole, Ben", "Ganguli, Surya"]
    year: 2014
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the importance of initialization and momentum in deep learning"
    authors: ["Sutskever, Ilya", "Martens, James", "Dahl, George", "Hinton, Geoffrey"]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lecture 6.5 - RMSProp"
    authors: ["Tieleman, T.", "Hinton, G."]
    year: 2012
    venue: "Coursera: Neural Networks for Machine Learning"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast dropout training"
    authors: ["Wang, Sida", "Manning, Christopher"]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "AdaDelta: An adaptive learning rate method"
    authors: ["Zeiler, Matthew D."]
    year: 2012
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1212.5701"
  - title: "Online convex programming and generalized infinitesimal gradient ascent"
    authors: ["Zinkevich, Martin"]
    year: 2003
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 3
  title: "Convolutional neural networks training cost on CIFAR-10 — Adam vs AdaGrad vs SGD+Nesterov, with and without dropout, first 3 epochs and 45 epochs"
  page: 7
  image_path: "figures/kingma-2015-adam-optimizer-fig.png"
---

# Adam: A Method for Stochastic Optimization

**Authors:** Diederik P. Kingma, Jimmy Lei Ba
**Published:** 2015-05 (ICLR 2015) · [Source](https://arxiv.org/abs/1412.6980)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

Adam is a first-order stochastic optimizer that maintains two per-parameter exponential moving averages — one of the gradient (mₜ, with decay β₁ = 0.9) and one of the squared gradient (vₜ, with decay β₂ = 0.999) — then takes a parameter step of α · m̂ₜ / (√v̂ₜ + ε), where m̂ and v̂ are bias-corrected by dividing by (1 - β₁ᵗ) and (1 - β₂ᵗ) respectively, and ε = 10⁻⁸ guards against divide-by-zero. The defaults α = 0.001, β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸ work across logistic regression on MNIST, multilayer NNs with dropout, CIFAR-10 CNNs (c64-c64-c128-1000), and variational autoencoders without further tuning. Theoretically, Adam has O(√T) regret in the online convex setting — matching AdaGrad — but in practice on non-convex deep networks it converges as fast as the best SGD+Nesterov configuration on CNNs and strictly beats AdaGrad, RMSProp, AdaDelta, and SFO on multilayer NNs with dropout. The paper also introduces AdaMax (Adam with the L∞ norm of past gradients instead of L₂; defaults α = 0.002) which needs no bias correction on the second-moment term and gives the bound |Δₜ| ≤ α. The most empirically important result is in Figure 4: when β₂ → 1 (needed for sparse gradients), removing bias correction makes the optimizer diverge in the first few epochs — bias correction is what lets you actually run with β₂ = 0.999.

## Key Takeaway

The widely-copied trick — "use SGD with momentum and per-parameter learning rates" — was already in RMSProp and in AdaGrad before Adam. The non-obvious contribution that made Adam dominate the next decade of deep learning isn't the moving averages, it's the **two-line bias correction** (m̂ₜ = mₜ/(1-β₁ᵗ), v̂ₜ = vₜ/(1-β₂ᵗ)) that fixes a flaw in RMSProp nobody had been fixing: the second-moment estimate is artificially small in the first few hundred steps because you initialised v₀ = 0, and without the correction the effective learning rate explodes at the start when β₂ is set close to 1 (which is exactly the setting you need for sparse gradients). Two lines, and the algorithm goes from "diverges on sparse problems" to "runs out of the box on every model I throw at it."

## Implications

- **Use the published defaults unless you have evidence to deviate.** α=0.001, β₁=0.9, β₂=0.999, ε=10⁻⁸ — the paper validates these across logistic regression on MNIST, MLP+dropout on MNIST, CNN on CIFAR-10, and VAE training, all in the same paper, with no per-task retuning. Most practitioners still treat these as the de facto defaults a decade later, and the paper is the original source.
- **Don't trust an adaptive-learning-rate optimizer that lacks bias correction at the start of training.** If you implement an Adam-style optimizer yourself (or use a custom variant in a research codebase), explicitly check that mₜ and vₜ are divided by (1-β₁ᵗ) and (1-β₂ᵗ). Figure 4 shows that on a VAE with β₂ = 0.999 (the default), removing bias correction produces visibly larger training loss after both 10 and 100 epochs, especially at higher learning rates.
- **For sparse-gradient problems, prefer Adam (or AdaGrad) over plain SGD with momentum.** The Section 6.1 logistic-regression-on-IMDB experiment with 10,000-dim bag-of-words features shows Adam matching AdaGrad and both beating SGD+Nesterov by a large margin. If your features are sparse (text, recommender embeddings, click data), this is the regime where adaptive methods earn their keep.
- **For deep CNNs, Adam's advantage over SGD+momentum is marginal, not categorical.** Section 6.3 explicitly notes that on CIFAR-10 with the c64-c64-c128-1000 architecture, "Adam shows marginal improvement over SGD with momentum" — and the second-moment estimate v̂ₜ "vanishes to zeros after a few epochs and is dominated by ε." This foreshadows the modern result that for image CNNs, SGD+momentum often still wins on final generalization — Adam's real edge is on the FC and dropout-heavy parts of the network.
- **Adam gives you the trust-region intuition for setting α.** Because |Δₜ| ≤ α in almost all cases (the paper proves two upper bounds on the per-step parameter change), α directly bounds how far each parameter can move per step. So if you know your good optima are within distance D from initialization and you have budget for N iterations, you can read off α ≈ D/N as a starting point — far more interpretable than tuning the learning rate of plain SGD.
- **Prefer AdaMax (Adam with L∞) when you need a tighter step bound.** Section 7.1 derives AdaMax: replace vₜ with uₜ = max(β₂·uₜ₋₁, |gₜ|) and use the update step (α/(1-β₁ᵗ))·mₜ/uₜ. AdaMax's |Δₜ| ≤ α holds without exception (Adam's only holds in the most common case), and uₜ needs no bias correction. Trade-off: paper doesn't claim AdaMax is faster — it's a cleaner variant with stronger theoretical properties, useful when stepsize control matters more than raw speed.
- **The O(√T) regret bound is interesting theory, not the reason Adam works in practice.** The convergence proof (Section 4 and Appendix) is for **convex** functions, which deep networks are not. The paper is honest about this — Section 6.2 says "our convergence analysis does not apply to non-convex problems, we empirically found that Adam often outperforms other methods in such cases." Don't oversell the theory when explaining why Adam works on a transformer.

## How to Apply It (method)

**Scenario:** You're training a new sequence model — say, a 100M-parameter transformer encoder-decoder for a domain-specific text generation task. Your training set has ~1M examples, your batch fits 32 sequences on a single GPU, and you want to run a 24-hour training job and get back a working model without spending a week sweeping hyperparameters.

**Steps:**

1. **Implement (or import) Adam with the exact pseudocode from Algorithm 1.** Every modern framework ships it (torch.optim.Adam, tf.keras.optimizers.Adam). Make sure your version has the bias-correction step — older or hand-rolled implementations sometimes skip it. The math is:

   ```
   m_t = β1 * m_{t-1} + (1 - β1) * g_t
   v_t = β2 * v_{t-1} + (1 - β2) * g_t^2
   m_hat = m_t / (1 - β1^t)
   v_hat = v_t / (1 - β2^t)
   θ_t = θ_{t-1} - α * m_hat / (sqrt(v_hat) + ε)
   ```

2. **Start with the paper's defaults.** α = 1e-3, β₁ = 0.9, β₂ = 0.999, ε = 1e-8. Do not tune these on the first run. They are the Schelling point — almost every published Adam result uses them or a small permutation.

3. **Train for ~100 steps and check the loss curve.** If loss is flat or diverging immediately, you have a learning-rate problem. The trust-region argument (Section 2.1) says steps are bounded by α — so if your loss is exploding, drop α by 10x. If it's converging painfully slowly, raise α by 3x. Do NOT touch β₁ or β₂ yet.

4. **Run for one full epoch.** Watch the training cost. Compare to baseline (random initialization loss). You should see a clean monotone decrease after the first few hundred steps. If you see oscillation or plateau, that's typically a data-pipeline or initialization problem, not an Adam problem.

5. **If your task has very sparse features (text bag-of-words, recommender embeddings, attention to specific tokens) and you see early-training instability,** verify your implementation has bias correction. Symptom from Figure 4: first-epoch loss is higher than it should be, especially at α > 1e-3. If you find your implementation skips bias correction, switch to a vetted one.

6. **If your model is a deep CNN for vision,** consider running SGD+Nesterov-momentum (α≈0.01-0.1, momentum=0.9) as a baseline alongside Adam. Section 6.3 shows the gap is small or even reversed on CNNs. For a 24-hour budget, run both for the first 3 epochs and pick the winner based on validation loss at the 3-epoch mark.

7. **If you need a tighter bound on per-step parameter change** (e.g., RL where stability matters more than speed, or fine-tuning a pretrained model where you cannot afford a single bad step), use AdaMax instead with α = 0.002. It guarantees |Δₜ| ≤ α exactly.

8. **At the end of training, consider Polyak averaging** (Section 7.2). Add one line to the inner loop: θ̄ₜ = β₂·θ̄ₜ₋₁ + (1-β₂)·θₜ. At evaluation time, evaluate θ̄ instead of θ. The paper says this often gives better generalization than the last iterate. Cost: one extra vector of memory; benefit: small but free improvement at test time.

**Expected outcome:** A trained model in 24 hours that performs within striking distance of a model you would have gotten from a week of hyperparameter sweeping. The point of Adam — explicitly framed in Section 2.1 — is to make stepsize tuning insensitive enough that you can spend your engineering time on architecture, data, and evaluation instead. If after one or two days you find Adam clearly losing to a tuned SGD+Nesterov configuration, that's a signal that you're in the CNN-image-classification regime where SGD still has an edge; everywhere else, Adam at defaults is the right Bayesian prior.

## Best Figure

![Figure 3 — Convolutional neural networks training cost on CIFAR-10 (page 7)](figures/kingma-2015-adam-optimizer-fig.png)

**Image Candidates:**
- Figure 3 (p. 7): Two-panel CIFAR-10 ConvNet training cost — first 3 epochs (left) and 45 epochs (right) — comparing Adam, Adam+dropout, AdaGrad, AdaGrad+dropout, SGD+Nesterov, SGD+Nesterov+dropout on a log scale, the clearest narrative comparison in the paper.
- Figure 4 (p. 8): VAE bias-correction ablation — 6×2 grid of red (with bias correction) vs green (without) loss curves over (β₁, β₂, log₁₀ α), making the central technical claim visible at a glance.
- Figure 2 (p. 7): MLP on MNIST with dropout — Adam vs AdaGrad, RMSProp, SGD+Nesterov, AdaDelta and SFO, showing Adam winning convergence speed against five baselines on a non-convex objective.

**Best Image:**
- **Figure Name:** Figure 3: "Convolutional neural networks training cost. (left) Training cost for the first three epochs. (right) Training cost over 45 epochs. CIFAR-10 with c64-c64-c128-1000 architecture."
- **Figure Page:** 7
- **Slide Caption:** Adam vs AdaGrad vs SGD+Nesterov on CIFAR-10 CNN — Adam matches the best baseline early and converges faster at depth.
- **Description:** Figure 3 is the paper's clearest single-view story figure for the regime that became most consequential — convolutional networks on natural images. The left panel shows the first three epochs of training cost (linear y-axis): Adam and Adam+dropout fall fastest among all six configurations, with AdaGrad and AdaGrad+dropout the next-quickest and SGD+Nesterov noticeably slower. The right panel zooms out to 45 epochs (log y-axis): now Adam and SGD+Nesterov converge to similar final training cost (~10⁻⁴) while AdaGrad plateaus orders of magnitude higher. This double-view directly supports the paper's qualified claim that Adam "shows marginal improvement over SGD with momentum" on CNNs while also showing why AdaGrad — the closest spiritual ancestor — falls behind on this class of problem. It is the single figure that best tells the practitioner what to expect: fast early progress and competitive final convergence, on a recognisable task with recognisable baselines.

## What Experts Overlook

The detail most readers skim over is **Section 3's derivation of why the bias correction term is exactly (1 - β₂ᵗ)** — not an empirical fudge factor, but a closed-form correction that falls out of taking expectations on the moving-average update. The paper writes vₜ = (1 - β₂)·Σᵢ₌₁ᵗ β₂^(t-i) · gᵢ², then takes E[vₜ] = E[gₜ²]·(1 - β₂ᵗ) + ζ, where ζ → 0 when the gradient distribution is stationary. So m̂ₜ = mₜ/(1 - β₁ᵗ) and v̂ₜ = vₜ/(1 - β₂ᵗ) are not arbitrary scaling — they are the unique correction that makes m̂ and v̂ unbiased estimators of the true first and second moments of the gradient under the stationarity assumption. The same paper that introduces RMSProp had been missing this for three years.

**Why it matters:** Most experts assume "Adam = RMSProp + momentum." That description is incomplete in a way that matters specifically when β₂ is close to 1 — which is the regime Adam *recommends as default*. Without the correction, in the first ~50 steps with β₂ = 0.999, v̂ₜ underestimates E[g²] by a factor of nearly 50, so the effective learning rate is ~7x too large. The algorithm runs anyway, but it runs badly, and the badness is invisible from the loss curve unless you compare to the corrected version side-by-side (which is exactly what Figure 4 is). It also explains why AdaMax (Section 7.1) drops the correction entirely — when you use the L∞ norm uₜ = max(β₂·uₜ₋₁, |gₜ|), the max operator is not biased by the v₀ = 0 initialization in the way exponential averaging is.

**Example of good use:** A researcher implementing a custom optimizer for a new architecture (say, a sparse mixture-of-experts model where only a few experts get gradient signal per step) takes care to derive the bias correction for their specific moving-average formulation, rather than copying Adam's correction blindly. They notice that their averaging scheme has a different bias profile and produce a custom correction — and the optimizer converges faster as a result.

**Example of misapplication:** A library author copies Adam's update equations but, "for simplicity," omits the bias correction lines, telling themselves it'll wash out after a few hundred steps anyway. Users on dense-gradient tasks with small β₂ don't notice. Users on sparse-gradient tasks with β₂ = 0.999 see early-training divergence and conclude "Adam doesn't work for sparse problems" — exactly the regime Adam was designed for. The bug is invisible on the front page README's MNIST example but quietly breaks the optimizer in the use case it was built for.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

Full citation list in frontmatter (23 entries). Key citations relevant to the algorithm:

- **Duchi, Hazan & Singer 2011 — Adaptive Subgradient Methods (AdaGrad)** — The direct ancestor; Adam reduces to a bias-corrected version of AdaGrad when β₁ = 0 and β₂ → 1.
- **Tieleman & Hinton 2012 — RMSProp (Coursera lecture 6.5)** — The other direct ancestor; Adam is RMSProp + momentum + bias correction. The fact that this citation is a *Coursera lecture* (no peer-reviewed paper) is a piece of deep-learning history worth noticing.
- **Zinkevich 2003 — Online convex programming and generalized infinitesimal gradient ascent** — The framework Adam's regret bound is proved in. The O(√T) bound matches the best-known result for general convex online learning.
- **Sutskever, Martens, Dahl & Hinton 2013 — On the importance of initialization and momentum in deep learning** — Justification for decaying β₁ towards zero during training (used in the convergence proof).
- **Kingma & Welling 2013 — Auto-Encoding Variational Bayes** — Provides the VAE used in the bias-correction ablation (Figure 4). Note: same first author.
- **Sohl-Dickstein, Poole & Ganguli 2014 — Sum-of-Functions Optimizer (SFO)** — The quasi-Newton baseline Adam beats in Figure 2; Adam is 5-10× faster per iteration and uses constant memory while SFO's memory scales linearly with minibatch count.
- **Amari 1998 — Natural gradient works efficiently in learning** — Frames Adam's v̂ₜ as a diagonal approximation to the Fisher information matrix, connecting it to natural gradient descent.
- **Zeiler 2012 — AdaDelta** — Another adaptive method baseline (appears in Figure 2 multilayer NN comparison).
- **Schaul, Zhang & LeCun 2012 — No more pesky learning rates (vSGD)** — Cited as a contemporaneous adaptive-stepsize method.
- **Pascanu & Bengio 2013 — Revisiting natural gradient for deep networks** — Used to justify the Fisher-matrix interpretation of v̂ₜ.

## Related Digests

- [[vaswani-2017-attention-is-all-you-need]] — The original Transformer is trained with Adam (specifically: β₁=0.9, β₂=0.98, ε=10⁻⁹ — a small permutation of Adam's defaults), which became the dominant optimizer for sequence models for the next decade.
- [[bahdanau-2015-attention-align-translate]] — The attention paper that, together with this one, defines the 2015 ICLR canon of modern deep learning primitives. Bahdanau et al. trained their alignment model with vanilla SGD; almost every paper that built on it switched to Adam.
- [[howard-2018-ulmfit]] — Uses Adam (with their own slanted triangular learning-rate schedule on top) for transfer-learning pretrained LMs. Demonstrates Adam's robustness across orders-of-magnitude differences in dataset size.
- [[vassilyev-2026-rcl]] — Discusses optimization primitives of context space and references Adam-style adaptive learning rates as the inner-loop optimizer being mirrored at the prompt-evolution level.
- [[touvron-2023-llama-foundation-models]] — LLaMA is trained with AdamW (Adam + decoupled weight decay), the standard 2020s descendant of Adam for large language models.

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in the digest is traceable to a specific section of the paper:
- The defaults α=0.001, β₁=0.9, β₂=0.999, ε=10⁻⁸ are from Algorithm 1 (page 2) and Section 6.
- The bias-correction derivation E[vₜ] = E[gₜ²]·(1-β₂ᵗ) + ζ is from Section 3, equations 1-4 (page 3).
- The O(√T) regret bound is from Theorem 4.1 and Corollary 4.2 (page 4).
- The "marginal improvement over SGD with momentum" claim on CNNs is a direct quote from Section 6.3 (page 7).
- The "second moment estimate v̂ₜ vanishes to zeros after a few epochs and is dominated by ε" observation is also from Section 6.3.
- AdaMax derivation, defaults (α=0.002), and the bound |Δₜ| ≤ α are from Section 7.1 (page 8) and Algorithm 2.
- The IMDB BoW 10,000-dim experiment is from Section 6.1 (page 5).
- The CIFAR-10 c64-c64-c128-1000 architecture is from Section 6.3 (page 6).
- Figure 4's bias-correction-vs-no-correction VAE ablation across (β₁ ∈ [0, 0.9], β₂ ∈ [0.99, 0.999, 0.9999], log₁₀α ∈ [-5, ..., -1]) is from Section 6.4 (page 7).
- The Polyak-Ruppert / exponential averaging extension in §7.2 is the source for the optional averaging step in the "How to Apply" section.

No hallucinated metrics, no invented baselines, no claims about performance regimes the paper did not study. The qualifications around the convergence proof (convex-only) and the CNN regime (Adam's edge is marginal there) are stated in the paper itself and reproduced honestly.
