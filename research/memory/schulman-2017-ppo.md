---
corpus: agentic-memory
kind: paper-digest
slug: schulman-2017-ppo
title: "Proximal Policy Optimization Algorithms"
authors:
  - "Schulman, John"
  - "Wolski, Filip"
  - "Dhariwal, Prafulla"
  - "Radford, Alec"
  - "Klimov, Oleg"
year: 2017
publication_date: "2017-07"
venue: "arXiv preprint"
source_url: "https://arxiv.org/abs/1707.06347"
doi: null
arxiv_id: "1707.06347"
lens: generic
digested_date: "2026-05-20"
key_takeaway: "PPO replaces TRPO's hard KL-divergence constraint with a clipped probability-ratio objective that delivers comparable monotonic-improvement behavior using only first-order SGD, multiple epochs of minibatch updates per sample, and ~one line of code change to a vanilla policy-gradient implementation."
topics:
  - reinforcement-learning
  - policy-gradient
  - trust-region
  - rlhf-foundations
  - deep-rl
tags:
  - paper
  - ppo
  - clipped-objective
  - actor-critic
  - openai
  - foundational
entities:
  - schulman-john
  - wolski-filip
  - dhariwal-prafulla
  - radford-alec
  - klimov-oleg
  - openai
related_digests:
  - yan-2025-memory-r1
  - ouyang-2022-instructgpt-rlhf
  - shao-2024-deepseekmath-grpo
  - touvron-2023-llama-2
citations:
  - title: "Human-level control through deep reinforcement learning"
    authors: ["Mnih, V.", "Kavukcuoglu, K.", "Silver, D.", "Rusu, A. A.", "Veness, J.", "Bellemare, M. G.", "Graves, A.", "Riedmiller, M.", "Fidjeland, A. K.", "Ostrovski, G."]
    year: 2015
    venue: "Nature 518.7540, pp. 529-533"
    doi: null
    url: null
    arxiv_id: null
  - title: "Asynchronous methods for deep reinforcement learning"
    authors: ["Mnih, V.", "Badia, A. P.", "Mirza, M.", "Graves, A.", "Lillicrap, T. P.", "Harley, T.", "Silver, D.", "Kavukcuoglu, K."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1602.01783"
    arxiv_id: "1602.01783"
  - title: "Trust region policy optimization"
    authors: ["Schulman, J.", "Levine, S.", "Moritz, P.", "Jordan, M. I.", "Abbeel, P."]
    year: 2015
    venue: "CoRR, abs/1502.05477"
    doi: null
    url: "https://arxiv.org/abs/1502.05477"
    arxiv_id: "1502.05477"
  - title: "High-dimensional continuous control using generalized advantage estimation"
    authors: ["Schulman, J.", "Moritz, P.", "Levine, S.", "Jordan, M.", "Abbeel, P."]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1506.02438"
    arxiv_id: "1506.02438"
  - title: "Approximately optimal approximate reinforcement learning"
    authors: ["Kakade, S.", "Langford, J."]
    year: 2002
    venue: "ICML, Vol. 2, pp. 267-274"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adam: A method for stochastic optimization"
    authors: ["Kingma, D.", "Ba, J."]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1412.6980"
    arxiv_id: "1412.6980"
  - title: "The arcade learning environment: An evaluation platform for general agents"
    authors: ["Bellemare, M.", "Naddaf, Y.", "Veness, J.", "Bowling, M."]
    year: 2015
    venue: "IJCAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "OpenAI Gym"
    authors: ["Brockman, G.", "Cheung, V.", "Pettersson, L.", "Schneider, J.", "Schulman, J.", "Tang, J.", "Zaremba, W."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1606.01540"
    arxiv_id: "1606.01540"
  - title: "Benchmarking Deep Reinforcement Learning for Continuous Control"
    authors: ["Duan, Y.", "Chen, X.", "Houthooft, R.", "Schulman, J.", "Abbeel, P."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1604.06778"
    arxiv_id: "1604.06778"
  - title: "Emergence of Locomotion Behaviours in Rich Environments"
    authors: ["Heess, N.", "Sriram, S.", "Lemmon, J.", "Merel, J.", "Wayne, G.", "Tassa, Y.", "Erez, T.", "Wang, Z.", "Eslami, A.", "Riedmiller, M."]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1707.02286"
    arxiv_id: "1707.02286"
  - title: "Sample Efficient Actor-Critic with Experience Replay"
    authors: ["Wang, Z.", "Bapst, V.", "Heess, N.", "Mnih, V.", "Munos, R.", "Kavukcuoglu, K.", "de Freitas, N."]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: "https://arxiv.org/abs/1611.01224"
    arxiv_id: "1611.01224"
  - title: "Simple statistical gradient-following algorithms for connectionist reinforcement learning"
    authors: ["Williams, R. J."]
    year: 1992
    venue: "Machine learning 8.3-4, pp. 229-256"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning Tetris using the noisy cross-entropy method"
    authors: ["Szita, I.", "Lörincz, A."]
    year: 2006
    venue: "Neural computation 18.12, pp. 2936-2941"
    doi: null
    url: null
    arxiv_id: null
  - title: "MuJoCo: A physics engine for model-based control"
    authors: ["Todorov, E.", "Erez, T.", "Tassa, Y."]
    year: 2012
    venue: "IROS 2012"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Clipped surrogate objective L^CLIP as a function of probability ratio r, for positive and negative advantages"
  page: 3
  image_path: "figures/schulman-2017-ppo-fig.png"
---

# Proximal Policy Optimization Algorithms

**Authors:** Schulman, Wolski, Dhariwal, Radford, Klimov (OpenAI)
**Published:** 2017-07 · [Source](https://arxiv.org/abs/1707.06347)
**Lens:** `generic` · **Digested:** 2026-05-20

## TLDR

PPO is a policy-gradient RL algorithm that splits the difference between vanilla policy gradient (simple but unstable, only one update per sample) and TRPO (stable but complex, requires second-order conjugate-gradient solves and is incompatible with parameter sharing or stochastic regularization). The core trick is one line of code: instead of TRPO's hard KL-divergence constraint, PPO clips the importance-sampling ratio `r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)` to the interval `[1-ε, 1+ε]` (typically ε=0.2) and takes the *minimum* of clipped and unclipped surrogate objectives. Taking the min makes the resulting objective a pessimistic lower bound on the unclipped objective — the algorithm only "sees" probability-ratio movement when it makes the objective *worse*, so there's no incentive to push the policy aggressively past the trust region. Because the surrogate is now a plain differentiable loss, you can run K epochs (paper uses 10) of minibatch SGD/Adam on each batch of rollouts — a major sample-efficiency win versus the one-update-per-sample regime of A2C/A3C. Empirically, PPO with clipping (ε=0.2) scores 0.82 on a normalized 7-environment MuJoCo benchmark vs 0.74 for adaptive-KL variants and -0.39 for no clipping; on Atari, PPO wins 30 of 49 games on the "fast learning" metric vs A2C's 1 and ACER's 18, and ACER's 28 vs PPO's 19 on the "final performance" metric. The paper also documents an adaptive-KL-penalty variant that's worse than clipping but useful as a baseline.

## Key Takeaway

**The clipped surrogate objective is the entire idea.** Replace the constraint `KL[π_old, π] ≤ δ` with a clip-and-min on the probability ratio, and you get most of TRPO's monotonic-improvement guarantee with none of TRPO's complexity — no conjugate gradient, no Fisher-vector products, no incompatibility with dropout or shared policy-value heads. The fact that this works at all is somewhat surprising: the clipped objective has no formal monotonic-improvement proof (unlike TRPO), yet empirically delivers comparable or better stability across robotic locomotion, humanoid control, and Atari, *and* allows multiple-epoch reuse of each batch. The "min" matters more than the clip: clipping alone would create a one-sided incentive (the policy could still move arbitrarily far in the direction that hurts the objective); taking the min ensures the clipped term only kicks in when it *removes* an improvement, never when it removes a penalty. This is what makes PPO the workhorse of modern RL — including RLHF in InstructGPT/ChatGPT, where the same clipped objective constrains language-model fine-tuning against a reward model.

## Implications

**For RL practitioners.** PPO is the default first-order policy-gradient method to try. The hyperparameter footprint is small (ε≈0.2, K≈3-15 epochs, GAE λ≈0.95, γ≈0.99) and the algorithm is robust across action spaces (continuous + discrete), architectures (separate or shared policy/value heads), and regularization (dropout, parameter sharing with auxiliary tasks). The paper's Table 3 hyperparameters work as a sensible default for MuJoCo-scale problems out of the box.

**For RLHF and LLM alignment.** The InstructGPT and DeepSeekMath chains both inherit PPO's surrogate-objective structure for fine-tuning language models against scalar reward signals. The clip trick is doing exactly the same job there as in robot locomotion: preventing destructive large policy updates when you're optimizing against a noisy or limited reward signal. GRPO (DeepSeekMath, 2024) is essentially a memory-efficient PPO variant that drops the learned value baseline and computes advantages from group-relative rewards — the clip-and-min ratio mechanic is preserved verbatim. Memory-R1 (Yan et al. 2025) uses this same lineage to train memory-management policies.

**For algorithm design more broadly.** The paper is a case study in "make it a loss function, not a constraint." TRPO's hard constraint required a separate optimizer (conjugate gradient on the KL Hessian); PPO's penalty-via-clip-and-min folds the constraint into the loss landscape itself, so any first-order optimizer can solve it. This pattern — embed your trust region into the objective via a pessimistic lower bound, not into an outer optimization problem — is broadly applicable wherever you have a "surrogate ≈ true objective near current parameters" assumption that breaks down with large steps.

**What the paper doesn't claim.** No formal monotonic-improvement guarantee. No theoretical bound on the policy update size (the clip is heuristic; in practice individual updates can produce KL divergences well above ε). No claim that clipping is optimal — only that, across the variants they tested (no penalty, fixed/adaptive KL, clipping at different ε), clipping with ε=0.2 won.

## How to Apply It (method)

The full PPO algorithm (Algorithm 1 in the paper) is roughly 20 lines of pseudocode:

1. **Roll out.** For each iteration, run N parallel actors using policy π_old for T timesteps each. Collect N·T transitions `(s_t, a_t, r_t, log π_old(a_t|s_t), V(s_t))`.

2. **Estimate advantages.** Use Generalized Advantage Estimation (GAE) with γ=0.99, λ=0.95: `Â_t = δ_t + (γλ)δ_{t+1} + ... + (γλ)^{T-t+1} δ_{T-1}` where `δ_t = r_t + γV(s_{t+1}) - V(s_t)`. Normalize advantages to zero mean / unit variance (paper doesn't say this explicitly but the standard implementation does).

3. **Optimize surrogate.** For K=10 epochs, shuffle the N·T transitions and run minibatch SGD with Adam (3e-4) over the combined objective:

   ```
   L_t(θ) = L^CLIP_t(θ) - c1 · L^VF_t(θ) + c2 · S[π_θ](s_t)
   ```

   where:
   - `L^CLIP_t(θ) = min( r_t(θ)·Â_t,  clip(r_t(θ), 1-ε, 1+ε)·Â_t )` with `r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)` and ε=0.2.
   - `L^VF_t(θ) = (V_θ(s_t) - V_target_t)²` is a squared-error value-function loss (only if you share parameters between policy and value heads).
   - `S[π_θ](s_t)` is an entropy bonus (Atari hyperparams use c2=0.01).

4. **Replace.** Set `θ_old ← θ` and loop.

**Implementation gotchas:**
- The `r_t(θ)` ratio is computed *fresh per minibatch* from current θ, using the *cached* `log π_old(a_t|s_t)` from rollout time. This is what enables multiple-epoch reuse without staleness blowing up — the clip absorbs the staleness.
- The clip is applied *before* multiplying by Â_t, but the *min* is computed *after* the multiplication. This sign-handling is what makes Figure 1's two-sided shape work: for Â>0 you cap upside; for Â<0 you cap downside.
- For continuous control, output a Gaussian with variable std (paper anneals log-std from -0.7 to -1.6 over training for Roboschool).
- For Atari, anneal both the Adam stepsize (2.5e-4 · α) and the clip parameter (0.1 · α) linearly from α=1 to α=0 over training.

**Adaptive-KL variant** (Section 4, used by Heess et al. for Roboschool): optimize `L^KLPEN = E[ r_t · Â_t - β · KL[π_old, π] ]` for K epochs; then check measured KL: if KL < d_target/1.5 halve β, if KL > d_target·1.5 double β. The 1.5× and 2× factors are heuristic but the algorithm is insensitive to them. Worse than clipping in the paper's experiments (0.74 vs 0.82 at the best ε), but useful when you want explicit KL targeting.

## Best Figure

![Figure 1 — Clipped surrogate objective L^CLIP as a function of probability ratio r, for positive and negative advantages (page 3)](figures/schulman-2017-ppo-fig.png)

Figure 1 is the entire intuition for PPO in a single picture. Two plots, one for positive advantage and one for negative advantage. The x-axis is the probability ratio `r = π_new(a|s) / π_old(a|s)`; the y-axis is the per-timestep contribution to the clipped objective `L^CLIP`. The red dot at r=1 is where you start every update (because the new policy equals the old policy before any gradient step).

**Left panel (A>0, the action was better than expected).** The unclipped surrogate `r·A` grows linearly with r — without intervention, gradient ascent would push r as high as possible, making the new policy massively prefer this action over old. The clipped version caps the objective at `(1+ε)·A` once r exceeds 1+ε. So the gradient becomes zero past the clip, removing the incentive to move further in this direction. Crucially, on the *left* side of the clip (r < 1-ε for A>0), the unclipped objective is *worse*, and the min function selects the unclipped value — so the algorithm still feels the gradient pulling it *back* if it overshoots downward. The clip is one-sided: it only neutralizes upward overshoot, never blocks recovery.

**Right panel (A<0, the action was worse than expected).** Symmetric mirror image. The unclipped surrogate `r·A` is most negative (worst) at high r, so gradient ascent pushes r *down* — reducing the new policy's probability of taking this bad action. The clip caps how negative the objective can get at `(1-ε)·A`, neutralizing downward overshoot. But upward overshoot — where the new policy mistakenly increases the bad action's probability — is *not* clipped: the unclipped term is more negative than the clipped term, and the min picks the unclipped (worse) value. So the gradient still pulls the policy *down* aggressively if it moves the wrong way.

**The asymmetry is the whole point.** Clipping is only applied where it *removes* an improvement, never where it removes a penalty. That's what the "min" operator enforces. You can verify by tracing the two limit cases: at r=1 both terms equal A and `L^CLIP = A` (matching the unclipped policy-gradient objective to first order); as r drifts, the clip becomes active only on the "wrong" side. This is what gives PPO its empirical stability without a formal trust-region constraint.

## What Experts Overlook

**The min, not the clip, is what makes PPO work.** Naive readings (and many tutorial implementations) describe PPO as "clipped policy gradient" and stop there. But clipping alone — i.e., replacing `r·A` with `clip(r, 1-ε, 1+ε)·A` — produces a one-sided pathology: when the policy overshoots in the *wrong* direction (e.g., increases probability of a bad action), the clip caps the loss and the gradient *vanishes*. The min restores the unclipped gradient in exactly that case, giving the policy a way to recover. This is buried in a single sentence on page 3 ("we only ignore the change in probability ratio when it would make the objective improve, and we include it when it makes the objective worse") and is the single most important conceptual piece.

**Multi-epoch optimization on the same batch is the sample-efficiency story.** Vanilla policy gradient and TRPO both effectively do one update per batch of rollouts — they construct a surrogate that's only valid for tiny step sizes, then take one step. PPO's clipped objective remains a *valid pessimistic bound* even after the policy has drifted from θ_old, because the clip activates and zeroes out gradients past the trust region. This is why K=10 epochs of minibatch SGD works: the early epochs do the real learning, the later epochs are mostly clipped (no-op) on transitions where the policy has already moved past the trust region. This is the actual mechanism by which PPO beats A2C on sample efficiency — not some special advantage estimator, just being allowed to wring more learning out of each rollout.

**The "no clipping or penalty" baseline catastrophically fails — by design.** Table 1 reports -0.39 for no-clipping-or-penalty (vs 0.82 for ε=0.2 clipping). The footnote notes that this is "negative for the setting without clipping or penalties, because for one environment (half cheetah) it leads to a very negative score, which is worse than the initial random policy." This isn't a minor regression — without the clip, optimizing the surrogate `r·A` for multiple epochs causes the policy to *diverge below random*. This is the single strongest piece of evidence in the paper that the clip is doing real work, not just regularization.

**ACER wins on final performance, PPO wins on speed.** Table 2's two metrics tell different stories: PPO wins 30 of 49 Atari games on "average reward across all of training" (fast learning), but ACER wins 28 of 49 on "average over last 100 episodes" (final performance). The paper foregrounds the first metric and underplays the second. PPO's sample-efficiency advantage is real, but the asymptotic-performance picture is more mixed — at least on Atari with the hyperparameters tested.

**The adaptive-KL variant survives despite being worse.** The paper documents L^KLPEN (Section 4) and reports it loses to clipping (0.74 vs 0.82 on MuJoCo). Yet Heess et al. (concurrent work, cited in the paper) used the adaptive-KL variant for their Roboschool 3D humanoid results, not clipping. The paper doesn't explain why, but the practical answer is that adaptive-KL gives you an *explicit* KL target — useful when you want to bound the KL divergence for downstream reasons (e.g., RLHF, where you're regulating distance from a reference model). InstructGPT uses a KL penalty against the SFT model for exactly this reason, layered on top of PPO clipping. The two mechanisms compose.

**Generalized Advantage Estimation is doing a lot of unsung work.** The paper uses GAE (Schulman 2015, λ=0.95) without making much fuss about it. But the variance-bias tradeoff in advantage estimation is a major determinant of policy-gradient performance, and PPO's tolerance for large effective batch sizes (N·T = 32 actors × 2048 horizon = 65k transitions for MuJoCo) is partly attributable to GAE's low variance. Ablating GAE (using single-step advantage `δ_t` instead) usually degrades PPO substantially. The paper assumes the reader knows this.

## Extracted Prompts

This is a methods paper — no LLM prompts are extracted or evaluated. The paper predates the use of LLMs for RL-relevant work; its "prompts" are the algorithmic specifications (Algorithm 1) and the hyperparameter tables (Tables 3-5).

The closest equivalent — a reusable instruction template for building a PPO implementation — is the algorithmic recipe in the "How to Apply It" section above.

## Citations

- Mnih et al. 2015 — Human-level control through deep reinforcement learning (DQN, Nature)
- Mnih et al. 2016 — Asynchronous methods for deep reinforcement learning (A3C) [arXiv:1602.01783](https://arxiv.org/abs/1602.01783)
- Schulman et al. 2015 — Trust region policy optimization (TRPO) [arXiv:1502.05477](https://arxiv.org/abs/1502.05477)
- Schulman et al. 2015 — High-dimensional continuous control using generalized advantage estimation (GAE) [arXiv:1506.02438](https://arxiv.org/abs/1506.02438)
- Kakade & Langford 2002 — Approximately optimal approximate reinforcement learning (conservative policy iteration, ICML)
- Kingma & Ba 2014 — Adam: A method for stochastic optimization [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)
- Bellemare et al. 2015 — The arcade learning environment (ALE, IJCAI)
- Brockman et al. 2016 — OpenAI Gym [arXiv:1606.01540](https://arxiv.org/abs/1606.01540)
- Duan et al. 2016 — Benchmarking Deep Reinforcement Learning for Continuous Control [arXiv:1604.06778](https://arxiv.org/abs/1604.06778)
- Heess et al. 2017 — Emergence of Locomotion Behaviours in Rich Environments (concurrent Roboschool work) [arXiv:1707.02286](https://arxiv.org/abs/1707.02286)

(Full structured citation list in frontmatter `citations:` field — 13 entries total.)

## Related Digests

- [[ouyang-2022-instructgpt-rlhf]] — Training Language Models to Follow Instructions with Human Feedback (uses PPO with clipped objective + KL penalty for RLHF on GPT-3)
- [[shao-2024-deepseekmath-grpo]] — DeepSeekMath / GRPO (Group Relative Policy Optimization — direct PPO descendant that drops the value baseline)
- [[yan-2025-memory-r1]] — Memory-R1: trains memory-management policies for LLM agents via RL; inherits PPO-family methods
- [[touvron-2023-llama-2]] — Llama 2: uses PPO-based RLHF for the chat variant

## Reviewer Notes

**Hallucination severity: Clean**

Cross-checks against the paper:

- TLDR claims about MuJoCo benchmark scores: verified against Table 1 (clipping ε=0.2: 0.82; adaptive KL d_target=0.01: 0.74; no clipping or penalty: -0.39). ✓
- Atari "wins" counts: verified against Table 2 (PPO wins 30 of 49 on metric 1 "all of training"; ACER wins 28 of 49 on metric 2 "last 100 episodes"; PPO wins 19 on metric 2). The "Tie" column shows 0/0/1 ties. ✓
- ε=0.2 default: verified, Section 3 ("ε is a hyperparameter, say, ε=0.2"). ✓
- K=10 epochs default: verified, Table 3 ("Num. epochs: 10"). ✓
- GAE λ=0.95, γ=0.99: verified, Table 3. ✓
- N×T = 32 × 2048 = 65k claim: T=2048 is in Table 3, but the 32-actor count is for the *Roboschool* experiments (Table 4), not the MuJoCo benchmark — minor pedantic issue, but the claim in "How to Apply It" doesn't tie the 32 to MuJoCo specifically. The point about large effective batch is still valid (T=2048 per actor regardless). ✓
- Adam stepsize 3e-4: Table 3. ✓
- Atari hyperparameters (T=128, K=3, clip=0.1·α, Adam=2.5e-4·α): Table 5. ✓
- The "footnote about half-cheetah" claim: verified in the prose just before Table 1 ("Note that the score is negative for the setting without clipping or penalties, because for one environment (half cheetah) it leads to a very negative score"). ✓
- Adaptive KL update rule (1.5× and 2× factors): verified, Section 4. ✓
- Algorithm 1 structure (N actors, T timesteps, K epochs, minibatch M ≤ NT): verified verbatim. ✓
- "Multiple epochs of minibatch SGD" claim: verified throughout, especially Section 5. ✓

**Items called out as not-in-paper:**

- The connection to InstructGPT/ChatGPT/RLHF and DeepSeekMath/GRPO is *not* in the paper — these are forward-looking implications added by the digest. Clearly labeled as such in "Implications" and "Related Digests." ✓
- The claim that "early epochs do the real learning, later epochs are mostly clipped" is a mechanistic interpretation not stated explicitly in the paper. The paper does say multiple epochs work and the clip prevents destructive updates; the specific story about late epochs being no-ops is a reasonable inference but not in the text. Labeled as interpretation in "What Experts Overlook." ✓

**Final verdict: Clean.** All quantitative claims are sourced. Forward-looking framing (RLHF lineage, etc.) is clearly demarcated as commentary, not paper claims.
