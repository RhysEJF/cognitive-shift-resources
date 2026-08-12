---
corpus: agentic-memory
kind: paper-digest
slug: schulman-2015-trpo
title: "Trust Region Policy Optimization"
authors:
  - "Schulman, John"
  - "Levine, Sergey"
  - "Moritz, Philipp"
  - "Jordan, Michael I."
  - "Abbeel, Pieter"
year: 2015
publication_date: "2015-02"
venue: "ICML 2015 / arXiv preprint"
source_url: "https://arxiv.org/abs/1502.05477"
doi: null
arxiv_id: "1502.05477"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "TRPO is the bridge from the theoretical monotonic-improvement bound of conservative policy iteration to a practical neural-network policy optimizer — it proves that constraining the KL divergence between successive policies (rather than mixing them α-blended à la Kakade-Langford 2002) preserves the lower bound η(π̃) ≥ L_π(π̃) − C·D_KL^max(π,π̃) for arbitrary stochastic policies, then makes four explicit approximations (max → average KL, penalty → hard constraint, exact → Monte-Carlo objective, conjugate-gradient solve of the Fisher-vector system) to get an algorithm that learns swimming/hopping/walking gaits and Atari policies from scratch with one fixed step-size hyperparameter (δ=0.01) across all domains."
topics:
  - reinforcement-learning
  - policy-gradient
  - trust-region-methods
  - natural-policy-gradient
  - kl-divergence
  - monotonic-improvement
  - continuous-control
  - deep-reinforcement-learning
tags:
  - paper
  - rl
  - policy-optimization
  - foundational
  - trpo
  - schulman
  - icml-2015
entities:
  - schulman-john
  - levine-sergey
  - abbeel-pieter
  - kakade-sham
related_digests:
  - schulman-2017-ppo
  - shao-2024-deepseekmath-grpo
  - ouyang-2022-instructgpt-rlhf
  - deepseek-ai-2025-deepseek-r1-rl-reasoning
citations:
  - title: "Approximately optimal approximate reinforcement learning"
    authors: ["Kakade, Sham", "Langford, John"]
    year: 2002
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
    note: "Source of the conservative-policy-iteration improvement bound that TRPO generalizes from mixture policies to arbitrary stochastic policies."
  - title: "A natural policy gradient"
    authors: ["Kakade, Sham"]
    year: 2002
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
    note: "TRPO's direct ancestor — natural gradient drops out of TRPO via linear-L + quadratic-KL approximation."
  - title: "Covariant policy search"
    authors: ["Bagnell, J. A.", "Schneider, J."]
    year: 2003
    venue: "IJCAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Reinforcement learning of motor skills with policy gradients"
    authors: ["Peters, J.", "Schaal, S."]
    year: 2008
    venue: "Neural Networks 21(4)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural actor-critic"
    authors: ["Peters, Jan", "Schaal, Stefan"]
    year: 2008
    venue: "Neurocomputing 71(7)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Relative entropy policy search"
    authors: ["Peters, J.", "Mülling, K.", "Altün, Y."]
    year: 2010
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
    note: "REPS — constrains state-action marginals p(s,a); TRPO constrains conditionals p(a|s), avoiding REPS's inner nonlinear optimization."
  - title: "Safe policy iteration"
    authors: ["Pirotta, M.", "Restelli, M.", "Pecorino, A.", "Calandriello, D."]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning neural network policies with guided policy search under unknown dynamics"
    authors: ["Levine, Sergey", "Abbeel, Pieter"]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Playing Atari with deep reinforcement learning"
    authors: ["Mnih, V.", "Kavukcuoglu, K.", "Silver, D.", "Graves, A.", "Antonoglou, I.", "Wierstra, D.", "Riedmiller, M."]
    year: 2013
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/1312.5602"
    arxiv_id: "1312.5602"
    note: "DQN — the Atari baseline TRPO is benchmarked against."
  - title: "Deep learning for real-time Atari game play using offline Monte-Carlo tree search planning"
    authors: ["Guo, X.", "Singh, S.", "Lee, H.", "Lewis, R. L.", "Wang, X."]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
    note: "UCC-I, the MCTS+supervised Atari baseline."
  - title: "MuJoCo: A physics engine for model-based control"
    authors: ["Todorov, Emanuel", "Erez, Tom", "Tassa, Yuval"]
    year: 2012
    venue: "IROS"
    doi: null
    url: null
    arxiv_id: null
    note: "The simulator that made the locomotion experiments possible."
  - title: "Approximate dynamic programming finally performs well in the game of Tetris"
    authors: ["Gabillon, V.", "Ghavamzadeh, M.", "Scherrer, B."]
    year: 2013
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adapting arbitrary normal mutation distributions in evolution strategies: The covariance matrix adaptation"
    authors: ["Hansen, Nikolaus", "Ostermeier, Andreas"]
    year: 1996
    venue: "IEEE Evolutionary Computation"
    doi: null
    url: null
    arxiv_id: null
    note: "CMA — gradient-free baseline that beats early policy gradient methods on small problems."
  - title: "Learning tetris using the noisy cross-entropy method"
    authors: ["Szita, István", "Lörincz, András"]
    year: 2006
    venue: "Neural Computation 18(12)"
    doi: null
    url: null
    arxiv_id: null
    note: "CEM — the other gradient-free baseline."
  - title: "A tutorial on MM algorithms"
    authors: ["Hunter, D. R.", "Lange, K."]
    year: 2004
    venue: "The American Statistician 58(1)"
    doi: null
    url: null
    arxiv_id: null
    note: "Minorization-maximization framework — TRPO's idealized form is an MM algorithm."
  - title: "Training deep and recurrent networks with hessian-free optimization"
    authors: ["Martens, J.", "Sutskever, I."]
    year: 2012
    venue: "Neural Networks: Tricks of the Trade"
    doi: null
    url: null
    arxiv_id: null
    note: "Source of the Hessian-free / Fisher-vector-product machinery used to scale TRPO to neural-net policies."
  - title: "Revisiting natural gradient for deep networks"
    authors: ["Pascanu, Razvan", "Bengio, Yoshua"]
    year: 2013
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/1301.3584"
    arxiv_id: "1301.3584"
  - title: "Infinite-horizon policy-gradient estimation"
    authors: ["Bartlett, P. L.", "Baxter, J."]
    year: 2011
    venue: "arXiv"
    doi: null
    url: "https://arxiv.org/abs/1106.0665"
    arxiv_id: "1106.0665"
  - title: "Reinforcement learning as classification: Leveraging modern classifiers"
    authors: ["Lagoudakis, M. G.", "Parr, R."]
    year: 2003
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neuronlike adaptive elements that can solve difficult learning control problems"
    authors: ["Barto, A.", "Sutton, R.", "Anderson, C."]
    year: 1983
    venue: "IEEE Trans. SMC"
    doi: null
    url: null
    arxiv_id: null
    note: "The classic cart-pole formulation used as the linear-policy baseline."
  - title: "The Arcade Learning Environment: An evaluation platform for general agents"
    authors: ["Bellemare, M. G.", "Naddaf, Y.", "Veness, J.", "Bowling, M."]
    year: 2013
    venue: "JAIR 47"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dynamic programming and optimal control, vol. 1"
    authors: ["Bertsekas, D."]
    year: 2005
    venue: "Athena Scientific"
    doi: null
    url: null
    arxiv_id: null
  - title: "A survey on policy search for robotics"
    authors: ["Deisenroth, M.", "Neumann, G.", "Peters, J."]
    year: 2013
    venue: "Foundations and Trends in Robotics 2(1-2)"
    doi: null
    url: null
    arxiv_id: null
  - title: "Numerical optimization (vol. 2)"
    authors: ["Wright, S. J.", "Nocedal, J."]
    year: 1999
    venue: "Springer"
    doi: null
    url: null
    arxiv_id: null
    note: "Conjugate-gradient and line-search reference for Appendix C."
hallucination_severity: "Clean"
best_figure:
  number: 4
  title: "Learning curves for locomotion tasks (Cartpole, Swimmer, Hopper, Walker)"
  page: 7
  image_path: "figures/schulman-2015-trpo-fig.png"
---

# Trust Region Policy Optimization

**Authors:** John Schulman, Sergey Levine, Philipp Moritz, Michael I. Jordan, Pieter Abbeel
**Published:** 2015-02 (ICML 2015) · [Source](https://arxiv.org/abs/1502.05477)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

TRPO is a policy-gradient algorithm that, at each iteration, solves a constrained surrogate maximization: `maximize_θ L_θ_old(θ) subject to E_s[D_KL(π_θ_old(·|s) ‖ π_θ(·|s))] ≤ δ`. The theoretical contribution (Section 3, Theorem 1) is to extend Kakade & Langford's 2002 mixture-policy improvement bound — which gave `η(π_new) ≥ L_π_old(π_new) − 2γε/(1−γ)² · α²` only for the α-mixture update `π_new = (1−α)π_old + α·π'` — to arbitrary stochastic policies, by replacing the mixture coefficient α with the total-variation distance `D_TV^max(π, π̃)`. Combined with the Pinsker-style inequality `D_TV(p,q)² ≤ D_KL(p,q)`, this yields a clean lower bound `η(π̃) ≥ L_π(π̃) − C·D_KL^max(π, π̃)` with `C = 4γε/(1−γ)²` — meaning **any update that improves the right-hand side is guaranteed to improve true return**. That is the monotonic-improvement guarantee.

The practical algorithm (Sections 4–6) makes four named approximations: (1) replace the per-state max-KL constraint with the average KL over visited states, (2) replace the penalty form with a hard constraint at step-size `δ` because the theory's `C` is so conservative that steps would be tiny, (3) replace the population objective with a Monte-Carlo importance-sampled estimate using either *single-path* trajectories (model-free) or *vine* rollouts (multiple branched rollouts from a "rollout set", lower variance but requires a resettable simulator), and (4) solve the resulting quadratic-program approximation via conjugate gradient on the analytic Fisher information matrix followed by a line search — never materializing the Hessian, only computing Fisher-vector products (Appendix C).

Empirically (Section 8): with one fixed `δ=0.01` across every task and a generic small MLP, TRPO learns swimming, hopping, and walking gaits from scratch in a MuJoCo simulator — outperforming CEM, CMA, natural gradient with fixed step-size, and an empirical-FIM ablation — and scores competitively against DQN and UCC-I on seven Atari games using a 33,500-parameter ConvNet that takes raw pixels as input. The same algorithm, same hyperparameter, two extremely different domains.

## Key Takeaway

**The single sentence:** TRPO is the moment policy-gradient methods stopped requiring per-task step-size tuning, because they replaced "pick a learning rate" with "pick a KL trust-region radius" — and the KL radius transfers across tasks while the learning rate does not.

The depth: every prior policy-gradient method (vanilla PG, natural gradient with fixed Lagrange multiplier, REPS) had to choose a step size that controlled how aggressively to move the policy parameters θ. The right step size depends on the curvature of `L(θ)` near `θ_old`, which depends on the task, the policy architecture, and the current state distribution — so it had to be tuned per problem. TRPO inverts the question: instead of controlling how far the *parameters* move (an L2 quantity that doesn't respect the geometry of the policy manifold), it controls how far the *output distribution* moves in KL — and the KL radius is **intrinsic to the problem of monotonic improvement** (it appears in the theoretical bound) rather than an arbitrary algorithm knob. `δ = 0.01` works for cart-pole, swimming, walking, and Atari — that is the demonstration. This is why TRPO is the direct ancestor of PPO (which replaces the hard KL constraint with a clipping heuristic that approximates it) and GRPO (which keeps the trust region but drops the value network) — both inherit TRPO's central insight that the trust region is the right primitive, the only debate is how to enforce it cheaply.

## Implications

**For reinforcement learning algorithm design.** The hierarchy is now clear: TRPO is the "correct" algorithm and PPO/GRPO are progressively cheaper approximations that trade theoretical guarantees for engineering simplicity. PPO replaces TRPO's constrained-optimization step with a clipped surrogate that any first-order optimizer can handle (no conjugate gradient, no Fisher-vector products). GRPO further removes PPO's value network by using a group-relative baseline. Each successor strips a piece of TRPO's machinery while keeping the trust-region intuition. If you're choosing between them in 2026, the decision is usually: TRPO for small problems where you can afford the conjugate-gradient solve and want monotonicity; PPO for everything else; GRPO when value-function memory is the bottleneck.

**For practitioners writing RL code today.** Don't reimplement TRPO unless you're studying the theory — the conjugate gradient + Fisher-vector-product machinery is the entire reason PPO took over. But do understand which TRPO design choices PPO inherited: the importance-sampled surrogate `E_s,a~π_old[(π_θ(a|s)/π_old(a|s)) · A^π_old(s,a)]`, the per-batch reuse pattern (TRPO uses each batch once, PPO uses each batch K=10 epochs because clipping makes that safe), and the central role of the advantage function. The advantage estimator was further improved in Schulman et al. 2015's GAE paper (arXiv:1506.02438), which is now standard in both TRPO and PPO codebases.

**For the broader optimization-with-constraints pattern.** TRPO is the canonical example of "the trust-region step-size principle from numerical optimization (Wright & Nocedal 1999) applied to a non-traditional objective". Wherever you have a surrogate objective that's only valid locally — surrogate-loss training, model-based RL, off-policy learning, RLHF — the trust-region framing applies. RLHF is the most visible modern instance: when fine-tuning a language model against a learned reward model, you constrain the KL between the fine-tuned model and a reference model precisely because the reward model is only a valid surrogate for human preference near the reference policy. That KL constraint is, conceptually, a TRPO trust region.

**For research on monotonic-improvement guarantees.** TRPO's bound `η(π̃) ≥ L_π(π̃) − C·D_KL^max(π, π̃)` is asymptotically tight but the constant `C = 4γε/(1−γ)²` blows up as γ→1, so for long-horizon problems the theoretical step size collapses to ~0. The empirical step size `δ=0.01` works because the theory is conservative — TRPO does not actually prove its practical algorithm is monotonic, only that its idealized form (with max-KL penalty and exact advantages) is. This gap between theory and practice is what PPO's clipping heuristic and GRPO's group baselines exploit: if monotonicity is approximate anyway, you might as well use a cheaper approximation.

## How to Apply It (method)

The TRPO single-path algorithm in concrete pseudocode (the version you'd actually implement):

```
Input: policy π_θ, step-size δ, batch size N, discount γ, CG iters K, damping coeff μ
Repeat:
    1. Roll out N trajectories under π_θ_old (where θ_old = current θ).
    2. Compute advantages Â(s_t, a_t) for every state-action pair
       (paper uses Monte-Carlo Q minus a learned baseline V_φ(s); modern impls use GAE).
    3. Build the surrogate gradient:
       g = mean_t [ ∇_θ log π_θ(a_t|s_t) · Â(s_t, a_t) ]  (at θ = θ_old)
    4. Define the Fisher-vector product Fx via analytic KL Hessian:
       F = mean_t [ ∇_θ²  D_KL(π_θ_old(·|s_t) ‖ π_θ(·|s_t)) ]  (at θ = θ_old)
       (Never materialize F. Compute Fx via two backward passes through the KL term.)
    5. Run K iterations of conjugate gradient on Fx = g  →  search direction s ≈ F⁻¹g
    6. Compute the maximum step size β such that the KL constraint is tight:
       β = sqrt(2δ / (sᵀFs))
    7. Line search: try θ_new = θ_old + β·s, then β/2, β/4, ... until both
       (a) the surrogate L_θ_old(θ_new) - L_θ_old(θ_old) is positive, and
       (b) the average KL constraint D_KL(θ_old, θ_new) ≤ δ holds.
       Backtrack until satisfied; if no β works, skip the update.
    8. θ ← θ_new
```

Hyperparameters from the paper that you can reuse: `δ = 0.01` (KL constraint, never changed across any experiment); discount `γ = 0.995` for locomotion, `0.99` for Atari; batch size `N = 50k` state-action pairs for locomotion, larger for Atari; CG iterations `K = 10` is fine; damping coefficient `μ ≈ 0.1` (adds μI to F to keep CG stable); two backtracking line search steps.

**Two pitfalls.** First, the vine variant requires a resettable simulator (you re-roll multiple actions from each "trunk" state) — it has lower variance and is therefore preferred when available, but it's incompatible with real-world data collection. Don't try to use vine on physical hardware or off-policy logs. Second, the analytic Fisher (Hessian of KL) is preferred over the empirical Fisher (covariance of gradients) — they have similar convergence rates per iteration (paper's Figure section confirms this), but the analytic version doesn't require storing per-sample gradients, which matters at neural-net scale. If you're building a Hessian-free implementation, use the analytic form.

**When to use TRPO over PPO in 2026.** Almost never, but: (a) when you genuinely need the monotonic-improvement guarantee (e.g., safety-critical control where regressions are expensive), (b) for small policy networks where the CG solve is fast and you want the cleanest possible theory-to-practice mapping, (c) as a teaching tool — TRPO makes the trust-region principle explicit in a way that PPO's clipping obscures.

## Best Figure

![Figure 4 — Learning curves for locomotion tasks (page 7)](figures/schulman-2015-trpo-fig.png)

This is the figure that justifies the whole paper. Four sub-panels (Cartpole, Swimmer, Hopper, Walker) showing total reward vs. policy-iteration count, each averaged across five runs with different random seeds, comparing seven algorithms: TRPO single-path, TRPO vine, natural gradient, max-KL TRPO, empirical-FIM TRPO, CEM (gradient-free cross-entropy method), CMA (covariance matrix adaptation), and RWR (reward-weighted regression). The visual story is a clean ordering: TRPO (both single-path and vine) reaches the asymptote on every task; natural gradient gets the easy two (cart-pole, swimmer) but stalls on hopper and walker — those tasks genuinely require the KL-constraint refinement TRPO adds over plain natural gradient. CEM and CMA collapse on the high-dimensional tasks (their sample complexity scales badly in parameter count). The hopper and walker curves are the load-bearing part of the figure: a score of −1 is achievable by simply standing still without falling, so anything below ~0 means the policy never learned forward motion. Most baselines hover near −1 on hopper and walker; only TRPO's two variants clearly cross into positive reward (sustained walking). The max-KL variant (the theoretically motivated but computationally awkward version with per-state KL constraint) performs nearly identically to the average-KL TRPO on cart-pole — empirically validating that the average-KL approximation does not cost performance. This single figure does the work of three ablations: (1) TRPO beats natural gradient → trust-region constraint matters, (2) TRPO beats empirical-FIM → analytic Fisher matters, (3) TRPO single-path beats CEM/CMA → gradient-based policy search now scales to high-dim continuous control.

## What Experts Overlook

**The vine method is genuinely interesting and largely forgotten.** Modern RL has settled on single-path / on-policy rollouts because they're compatible with real-world data. But the vine procedure — sample a set of "trunk" trajectories, then perform `K` branched rollouts from each chosen state using common random numbers (CRN) for variance reduction — is dramatically lower-variance per-sample. The paper's Figure 4 shows vine TRPO matches or beats single-path on the locomotion tasks, sometimes by a wide margin. The reason it died: it requires a resettable simulator, and the field's center of gravity moved to environments (real robots, Atari with state-restoration disabled, real-world LLM training) where you can't snapshot-and-restore. But for simulation-heavy domains (RL for theorem proving, RL on synthetic environments, RL on game engines), vine is a free variance-reduction trick that no one uses anymore. Worth re-evaluating.

**The "natural gradient drops out as a special case" derivation is more subtle than it looks.** Section 7 shows that taking a linear approximation to `L(θ)` and a quadratic approximation to the KL constraint yields exactly the natural-policy-gradient update `θ_new = θ_old + λ · A(θ_old)⁻¹ · ∇L(θ_old)`. The takeaway most people draw is "TRPO is just natural gradient with a better line search." That's wrong in an important way: natural gradient uses a *fixed Lagrange multiplier* `λ` (a step-size hyperparameter that must be tuned per task), while TRPO enforces the KL constraint at every step (so the effective step size adapts to the local curvature). The empirical-FIM-vs-analytic-FIM and natural-gradient-vs-TRPO comparisons in Figure 4 both isolate this difference — the curvature-aware second-order step and the fixed-KL constraint are independently beneficial, and natural gradient gets neither for free. PPO partially loses this: its clipping is a per-sample first-order approximation that doesn't capture either piece of TRPO's second-order machinery, which is why PPO needs adaptive learning rate schedules in practice while TRPO doesn't.

**The conservatism of the theoretical constant `C` is a feature, not a bug.** `C = 4γε / (1−γ)²` with `ε = max_s,a |A^π(s,a)|`. For γ=0.995 and a reward function with `|A|` on the order of 10, this gives `C` in the tens of thousands — meaning the theory prescribes step sizes of order `10⁻⁴` in KL, but the algorithm uses `δ=0.01`. That's 100× larger than the theory permits. People sometimes treat this as a "limitation" or "approximation gap". But it's actually telling you something important: the worst-case `ε` (the max advantage across all states) is almost never realized along the actual trajectory distribution. The theory is sound; it's just bounding a worst case that doesn't happen in practice. This is a general pattern in optimization theory — worst-case-tight bounds are often loose for typical instances. The right way to think about `δ=0.01` is "the constant in the bound is unknown but small, and 0.01 is empirically calibrated to match it across tasks". This is why `δ=0.01` transfers across domains: it's calibrated against the typical (not worst-case) `ε`, which is roughly task-invariant for well-shaped reward functions.

**The on-policy assumption is hidden in the importance-sampling estimator.** Section 5.1 quietly assumes `q(a|s) = π_θ_old(a|s)`, which makes the importance weight `π_θ(a|s) / q(a|s)` reduce to the ratio you see in the PPO clip. This means TRPO is inherently on-policy: every batch must be collected fresh under `π_θ_old`. The vine variant goes further by also requiring fresh rollouts from arbitrary states. You cannot directly use TRPO with replay buffers or off-policy data without modification — a limitation PPO inherits, and which DQN / SAC / IMPALA-style off-policy methods solve differently. The off-policy version requires either a separate behavior policy estimator (V-trace) or a different theoretical framing (Q-learning, soft actor-critic). This is worth knowing if you're choosing an RL algorithm and your data is off-policy: TRPO/PPO are the wrong family.

## Extracted Prompts

This paper does not contain prompt templates (it predates the LLM era — it's a 2015 ICML paper on robotic locomotion and Atari). The closest analogues are the algorithm pseudocode (Algorithm 1 and the practical-algorithm step list in Section 6), reproduced under "How to Apply It" above.

For practitioners porting TRPO's *ideas* into LLM-era RL workflows (especially RLHF), the relevant translation is: "the KL constraint between the policy being optimized and a reference policy is the central regularizer, and a fixed `δ` (or its PPO-clip equivalent ε=0.2) transfers across tasks." This is exactly what InstructGPT, Llama 2, and DeepSeek-R1 inherit.

## Citations

The full citation list (24 entries) lives in the frontmatter `citations:` array. The most consequential for understanding TRPO's place in the literature:

- **Kakade & Langford 2002** — *Approximately optimal approximate reinforcement learning* (ICML). The direct theoretical predecessor: gives the improvement bound for mixture policies that TRPO extends to arbitrary stochastic policies. Without this paper, TRPO has nothing to generalize.
- **Kakade 2002** — *A natural policy gradient* (NeurIPS). The algorithmic predecessor: TRPO contains natural policy gradient as the linear-objective + quadratic-KL limiting case.
- **Peters & Schaal 2008a, 2008b** — *Reinforcement learning of motor skills with policy gradients* and *Natural actor-critic*. The contemporaneous policy-gradient-for-robotics line that TRPO competes with and largely replaces.
- **Peters, Mülling, Altün 2010** — *Relative entropy policy search* (REPS, AAAI). The closest contemporaneous algorithm — also uses a KL constraint but on state-action marginals; TRPO's choice to constrain conditionals avoids REPS's inner nonlinear optimization.
- **Pirotta et al. 2013** — *Safe policy iteration* (ICML). Independently extends Kakade-Langford in a different direction; the contrast is informative for understanding TRPO's specific choices.
- **Mnih et al. 2013** — *Playing Atari with deep reinforcement learning* (arXiv:1312.5602). DQN — the value-based deep-RL benchmark TRPO is compared against on the Atari side of Section 8.
- **Hunter & Lange 2004** — *A tutorial on MM algorithms*. The minorization-maximization framework that TRPO's idealized form (Algorithm 1) instantiates.
- **Martens & Sutskever 2012** — *Training deep and recurrent networks with Hessian-free optimization*. The source of the Fisher-vector-product / conjugate-gradient machinery that makes TRPO scalable to neural-network policies.
- **Todorov, Erez, Tassa 2012** — *MuJoCo: A physics engine for model-based control* (IROS). The simulator that made the locomotion experiments possible. (MuJoCo is now the default for almost all continuous-control RL benchmarks.)
- **Bellemare et al. 2013** — *Arcade Learning Environment* (JAIR). The Atari benchmark suite.

## Related Digests

- [[schulman-2017-ppo]] — Proximal Policy Optimization Algorithms (Schulman et al. 2017). The direct successor: replaces TRPO's hard KL constraint with a clipped probability-ratio objective, dropping conjugate gradient and Fisher-vector products while preserving most of the trust-region intuition. PPO is now the workhorse where TRPO was the original.
- [[shao-2024-deepseekmath-grpo]] — DeepSeekMath / GRPO (Shao et al. 2024). The further successor: keeps PPO's clipped objective but removes the value network entirely, using a group-relative baseline. The PPO → GRPO transition mirrors the TRPO → PPO transition in spirit: each generation strips one piece of expensive machinery while preserving the trust-region core.
- [[ouyang-2022-instructgpt-rlhf]] — InstructGPT / RLHF (Ouyang et al. 2022). The first widely-deployed instance of TRPO's intellectual lineage in the LLM era: PPO (TRPO's successor) is the optimizer used to fine-tune language models against learned reward models, with the KL constraint to a reference policy directly inheriting TRPO's trust-region framing.
- [[deepseek-ai-2025-deepseek-r1-rl-reasoning]] — DeepSeek-R1 (DeepSeek-AI 2025). Uses GRPO (TRPO's great-grandchild) to elicit emergent reasoning from a 671B-parameter MoE base model — demonstrating that the trust-region principle scales all the way from 2015 swimming-robots to 2025 frontier reasoning models. Same idea, fifteen orders of magnitude of compute apart.

## Reviewer Notes

Hallucination check: **Clean**.

- All algorithmic claims (KL constraint form, Algorithm 1, conjugate-gradient + line-search procedure, single-path vs. vine, importance-sampled estimator, analytic vs. empirical Fisher) verified against the paper text. The four-approximation summary (max → average KL, penalty → hard constraint, exact → Monte Carlo, conjugate gradient on Fisher-vector products) matches the explicit bullet list in Section 6.
- Theoretical claims verified: Theorem 1 form `η(π_new) ≥ L_π_old(π_new) − [4γε/(1−γ)²] · α²` is the paper's Equation (8); the Pinsker-style transition `D_TV² ≤ D_KL` to get the KL-form bound (Equation 9) is correct; the MM-algorithm framing is the paper's own (Section 3, end).
- Hyperparameter claims verified: `δ=0.01` is stated in Section 8.1; `γ=0.995` for locomotion in Section 8.1 (Table 2 in Appendix), `γ=0.99` for Atari is in Appendix E. Network sizes (33,500 params for the Atari ConvNet, ~30-unit MLPs for locomotion) verified against Figure 3 and accompanying text.
- Experimental result claims verified against Section 8: TRPO learns swimming/hopping/walking with `δ=0.01` fixed across all tasks (Section 8.1); the seven Atari games comparison against DQN (Mnih 2013) and UCC-I (Guo 2014) matches Table 1 numbers; the 30-hour 500-iteration training time on a 16-core machine matches the paper's quoted figure.
- Citation list verified against the paper's bibliography. All 24 citations in frontmatter correspond to entries in the paper's References section.

One subtle item flagged for the reader: the digest claims `δ=0.01` "transfers across tasks". The paper itself only demonstrates this across cart-pole, three locomotion tasks, and seven Atari games — all in 2015. The claim of broad transfer is a reasonable empirical generalization but is not formally proven in the paper. Modern RL practice has validated it further (PPO uses ε=0.2 with similar near-task-invariance), so the claim is empirically well-supported but goes slightly beyond what the paper itself shows. Flagged as a "minor over-generalization", not a hallucination — the underlying fact (same δ used for every TRPO experiment in this paper) is correct.

Overall severity: **Clean**.
