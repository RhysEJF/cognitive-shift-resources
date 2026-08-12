---
corpus: agentic-memory
kind: paper-digest
slug: elhage-2022-toy-models-superposition
title: "Toy Models of Superposition"
authors:
  - "Elhage, Nelson"
  - "Hume, Tristan"
  - "Olsson, Catherine"
  - "Schiefer, Nicholas"
  - "Henighan, Tom"
  - "Kravec, Shauna"
  - "Hatfield-Dodds, Zac"
  - "Lasenby, Robert"
  - "Drain, Dawn"
  - "Chen, Carol"
  - "Grosse, Roger"
  - "McCandlish, Sam"
  - "Kaplan, Jared"
  - "Amodei, Dario"
  - "Wattenberg, Martin"
  - "Olah, Christopher"
year: 2022
publication_date: "2022-09"
venue: "Transformer Circuits Thread"
source_url: "https://arxiv.org/abs/2209.10652"
doi: null
arxiv_id: "2209.10652"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Polysemanticity isn't a flaw — it's neural networks compressing far more features than they have neurons by storing them as almost-orthogonal directions in superposition, controlled by a sharp phase change as feature sparsity rises, and any memory architecture that retrieves on neurons (or single embedding axes) will sometimes return mixtures of unrelated concepts unless it explicitly unfolds the superposition."
topics:
  - superposition
  - mechanistic-interpretability
  - polysemanticity
  - feature-representation
  - compressed-sensing
  - memory-architecture
  - sparse-features
  - phase-changes
  - feature-dictionaries
  - adversarial-examples
tags:
  - paper
  - mech-interp
  - anthropic
  - foundational
  - interpretability
  - representation-learning
  - toy-models
entities:
  - elhage-nelson
  - olah-christopher
  - wattenberg-martin
  - olsson-catherine
  - hume-tristan
  - schiefer-nicholas
  - henighan-tom
  - kaplan-jared
  - amodei-dario
  - anthropic
related_digests:
  - cunningham-2023-sparse-autoencoders-features
  - marks-2024-sparse-feature-circuits
  - mao-2026-agent-memory-circuits
citations:
  - title: "Zoom In: An Introduction to Circuits"
    authors: ["Chris Olah", "Nick Cammarata", "Ludwig Schubert", "et al."]
    year: 2020
    venue: "Distill"
    doi: "10.23915/distill.00024.001"
    url: null
    arxiv_id: null
  - title: "Softmax Linear Units"
    authors: ["Nelson Elhage", "Tristan Hume", "Catherine Olsson", "et al."]
    year: 2022
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressed sensing"
    authors: ["David L. Donoho"]
    year: 2006
    venue: "IEEE Transactions on Information Theory"
    doi: null
    url: null
    arxiv_id: null
  - title: "Local vs. Distributed Coding"
    authors: ["Simon J. Thorpe"]
    year: 1989
    venue: "Intellectica"
    doi: null
    url: null
    arxiv_id: null
  - title: "Representation learning: A review and new perspectives"
    authors: ["Yoshua Bengio", "Aaron Courville", "Pascal Vincent"]
    year: 2013
    venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
    doi: null
    url: null
    arxiv_id: null
  - title: "Curve Detectors"
    authors: ["Nick Cammarata", "Gabriel Goh", "Shan Carter", "et al."]
    year: 2020
    venue: "Distill"
    doi: null
    url: null
    arxiv_id: null
  - title: "Superposition of many models into one"
    authors: ["Brian Cheung", "Alex Terekhov", "Yubei Chen", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Linguistic regularities in continuous space word representations"
    authors: ["Tomas Mikolov", "Wen-tau Yih", "Geoffrey Zweig"]
    year: 2013
    venue: "NAACL-HLT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Linguistic regularities in sparse and explicit word representations"
    authors: ["Omer Levy", "Yoav Goldberg"]
    year: 2014
    venue: "CoNLL"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised representation learning with deep convolutional generative adversarial networks"
    authors: ["Alec Radford", "Luke Metz", "Soumith Chintala"]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1511.06434"
  - title: "Visualizing and understanding recurrent networks"
    authors: ["Andrej Karpathy", "Justin Johnson", "Li Fei-Fei"]
    year: 2015
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1506.02078"
  - title: "Learning to generate reviews and discovering sentiment"
    authors: ["Alec Radford", "Rafal Jozefowicz", "Ilya Sutskever"]
    year: 2017
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1704.01444"
  - title: "Object detectors emerge in deep scene CNNs"
    authors: ["Bolei Zhou", "Aditya Khosla", "Agata Lapedriza", "et al."]
    year: 2014
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1412.6856"
  - title: "Network Dissection: Quantifying Interpretability of Deep Visual Representations"
    authors: ["David Bau", "Bolei Zhou", "Aditya Khosla", "et al."]
    year: 2017
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Understanding the role of individual units in a deep neural network"
    authors: ["David Bau", "Jun-Yan Zhu", "Hendrik Strobelt", "et al."]
    year: 2020
    venue: "PNAS"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the importance of single directions for generalization"
    authors: ["Ari S. Morcos", "David G. Barrett", "Neil C. Rabinowitz", "Matthew Botvinick"]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1803.06959"
  - title: "On Interpretability and Feature Representations: An Analysis of the Sentiment Neuron"
    authors: ["Jonathan Donnelly", "Adam Roegiest"]
    year: 2019
    venue: "ECIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "High-Low Frequency Detectors"
    authors: ["Ludwig Schubert", "Chelsea Voss", "Nick Cammarata", "et al."]
    year: 2021
    venue: "Distill"
    doi: "10.23915/distill.00024.005"
    url: null
    arxiv_id: null
  - title: "Multimodal Neurons in Artificial Neural Networks"
    authors: ["Gabriel Goh", "Nick Cammarata", "Chelsea Voss", "et al."]
    year: 2021
    venue: "Distill"
    doi: "10.23915/distill.00030"
    url: null
    arxiv_id: null
  - title: "Convergent learning: Do different neural networks learn the same representations?"
    authors: ["Yixuan Li", "Jason Yosinski", "Jeff Clune", "et al."]
    year: 2015
    venue: "FE@NIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Feature Visualization"
    authors: ["Chris Olah", "Alexander Mordvintsev", "Ludwig Schubert"]
    year: 2017
    venue: "Distill"
    doi: "10.23915/distill.00007"
    url: null
    arxiv_id: null
  - title: "Adversarial examples are not bugs, they are features"
    authors: ["Andrew Ilyas", "Shibani Santurkar", "Dimitris Tsipras", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Proofs and refutations"
    authors: ["Imre Lakatos"]
    year: 1963
    venue: "Nelson London"
    doi: null
    url: null
    arxiv_id: null
  - title: "Sparse coding with an overcomplete basis set: A strategy employed by V1?"
    authors: ["Bruno A. Olshausen", "David J. Field"]
    year: 1997
    venue: "Vision Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "Decoding by linear programming"
    authors: ["Emmanuel J. Candes", "Terence Tao"]
    year: 2005
    venue: "IEEE Transactions on Information Theory"
    doi: null
    url: null
    arxiv_id: null
  - title: "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks"
    authors: ["Andrew M. Saxe", "James L. McClelland", "Surya Ganguli"]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-context Learning and Induction Heads"
    authors: ["Catherine Olsson", "Nelson Elhage", "Neel Nanda", "et al."]
    year: 2022
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "A Mechanistic Interpretability Analysis of Grokking"
    authors: ["Neel Nanda", "Tom Lieberum"]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Grokking: Generalization beyond overfitting on small algorithmic datasets"
    authors: ["Alethea Power", "Yuri Burda", "Harri Edwards", "et al."]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2201.02177"
  - title: "The surprising simplicity of the early-time learning dynamics of neural networks"
    authors: ["Wei Hu", "Lechao Xiao", "Ben Adlam", "Jeffrey Pennington"]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "A mathematical theory of semantic development in deep neural networks"
    authors: ["Andrew M. Saxe", "James L. McClelland", "Surya Ganguli"]
    year: 2019
    venue: "PNAS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Towards the science of security and privacy in machine learning"
    authors: ["Nicolas Papernot", "Patrick McDaniel", "Arunesh Sinha", "Michael Wellman"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1611.03814"
  - title: "Adversarial spheres"
    authors: ["Justin Gilmer", "Luke Metz", "Fartash Faghri", "et al."]
    year: 2018
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1801.02774"
  - title: "Adversarial robustness as a prior for learned representations"
    authors: ["Logan Engstrom", "Andrew Ilyas", "Shibani Santurkar", "et al."]
    year: 2019
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1906.00945"
  - title: "Delving into transferable adversarial examples and black-box attacks"
    authors: ["Yanpei Liu", "Xinyun Chen", "Chang Liu", "Dawn Song"]
    year: 2016
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "1611.02770"
  - title: "An introduction to systems biology: design principles of biological circuits"
    authors: ["Uri Alon"]
    year: 2019
    venue: "CRC Press"
    doi: "10.1201/9781420011432"
    url: null
    arxiv_id: null
  - title: "The Building Blocks of Interpretability"
    authors: ["Chris Olah", "Arvind Satyanarayan", "Ian Johnson", "et al."]
    year: 2018
    venue: "Distill"
    doi: "10.23915/distill.00010"
    url: null
    arxiv_id: null
  - title: "Visualizing Weights"
    authors: ["Chelsea Voss", "Nick Cammarata", "Gabriel Goh", "et al."]
    year: 2021
    venue: "Distill"
    doi: "10.23915/distill.00024.007"
    url: null
    arxiv_id: null
  - title: "A Review of Sparse Expert Models in Deep Learning"
    authors: ["William Fedus", "Jeff Dean", "Barret Zoph"]
    year: 2022
    venue: "arXiv preprint"
    doi: null
    url: null
    arxiv_id: "2209.01667"
  - title: "A Mathematical Framework for Transformer Circuits"
    authors: ["Nelson Elhage", "Neel Nanda", "Catherine Olsson", "et al."]
    year: 2021
    venue: "Transformer Circuits Thread"
    doi: null
    url: null
    arxiv_id: null
  - title: "An Overview of Early Vision in InceptionV1"
    authors: ["Chris Olah", "Nick Cammarata", "Ludwig Schubert", "et al."]
    year: 2020
    venue: "Distill"
    doi: "10.23915/distill.00024.002"
    url: null
    arxiv_id: null
  - title: "beta-VAE: Learning basic visual concepts with a constrained variational framework"
    authors: ["Irina Higgins", "Loic Matthey", "Arka Pal", "et al."]
    year: 2016
    venue: "ICLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "InfoGAN: Interpretable representation learning by information maximizing GANs"
    authors: ["Xi Chen", "Yan Duan", "Rein Houthooft", "et al."]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Disentangling by factorising"
    authors: ["Hyunjik Kim", "Andriy Mnih"]
    year: 2018
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Uncertainty principles and ideal atomic decomposition"
    authors: ["David L. Donoho", "Xiaoming Huo"]
    year: 2001
    venue: "IEEE Transactions on Information Theory"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressed sensing and best k-term approximation"
    authors: ["Albert Cohen", "Wolfgang Dahmen", "Ronald DeVore"]
    year: 2009
    venue: "Journal of the American Mathematical Society"
    doi: null
    url: null
    arxiv_id: null
  - title: "A remark on compressed sensing"
    authors: ["B. S. Kashin", "V. N. Temlyakov"]
    year: 2007
    venue: "Mathematical Notes"
    doi: null
    url: null
    arxiv_id: null
  - title: "Information-theoretic bounds on sparsity recovery in the high-dimensional and noisy setting"
    authors: ["Martin Wainwright"]
    year: 2007
    venue: "IEEE ISIT"
    doi: null
    url: null
    arxiv_id: null
  - title: "Lower bounds for sparse recovery"
    authors: ["Khanh Do Ba", "Piotr Indyk", "Eric Price", "David P. Woodruff"]
    year: 2010
    venue: "ACM-SIAM SODA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Neighborly polytopes and sparse solution of underdetermined linear equations"
    authors: ["David L. Donoho"]
    year: 2005
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressed sensing: How sharp is the RIP"
    authors: ["Jeffrey D. Blanchard", "Coralia Cartis", "Jared Tanner"]
    year: 2009
    venue: "SIAM Review"
    doi: null
    url: null
    arxiv_id: null
  - title: "A deep learning approach to structured signal recovery"
    authors: ["Ali Mousavi", "Ankit B. Patel", "Richard G. Baraniuk"]
    year: 2015
    venue: "Allerton"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learned D-AMP: Principled neural network based compressive image recovery"
    authors: ["Chris Metzler", "Ali Mousavi", "Richard Baraniuk"]
    year: 2017
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressed Sensing using Generative Models"
    authors: ["Ashish Bora", "Ajil Jalal", "Eric Price", "Alexandros G. Dimakis"]
    year: 2017
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Average firing rate rather than temporal pattern determines metabolic cost of activity in thalamocortical relay neurons"
    authors: ["G. Yi", "W. Grill"]
    year: 2019
    venue: "Scientific Reports"
    doi: "10.1038/s41598-019-43460-8"
    url: null
    arxiv_id: null
  - title: "Distributed representations"
    authors: ["Tony Plate"]
    year: 2003
    venue: "Cognitive Science"
    doi: null
    url: null
    arxiv_id: null
  - title: "Compressed Sensing, Sparsity, and Dimensionality in Neuronal Information Processing and Data Analysis"
    authors: ["Surya Ganguli", "Haim Sompolinsky"]
    year: 2012
    venue: "Annual Review of Neuroscience"
    doi: "10.1146/annurev-neuro-062111-150410"
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "As Sparsity Increases, Models Use 'Superposition' To Represent More Features Than Dimensions"
  page: 2
  image_path: "figures/elhage-2022-toy-models-superposition-fig.png"
---

# Toy Models of Superposition

**Authors:** Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, Christopher Olah
**Published:** 2022-09 · [Source](https://arxiv.org/abs/2209.10652)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

This Anthropic paper trains small ReLU autoencoders (typically n=20–400 input features into m=2–40 hidden dimensions) on synthetic data where each "feature" fires with probability 1-S (S from 0 to 0.999), and shows the network learns to pack more features than it has dimensions whenever features are sparse — the same model that behaves like PCA at 0% sparsity arranges 5 features as a pentagon in 2D at 90% sparsity. The transition isn't gradual: a first-order phase change separates "feature ignored" from "feature in superposition" from "feature with dedicated dimension," and the resulting feature dimensionalities cluster at specific fractions (1/2 for antipodal pairs, 2/3 for triangles, 3/4 for tetrahedra, 2/5 for pentagons, 3/8 for square antiprisms) — the same geometries that solve the Thomson problem of packing points on a sphere. With a ReLU on the hidden layer, the network can perform computation in superposition (it learns abs(x) for 100 features in 40 neurons), producing the same monosemantic-vs-polysemantic neuron mix observed in real vision and language models. Adversarial vulnerability rises >3× as superposition forms, and tracks features-per-dimension almost exactly. The strategic upshot: "solving superposition" — gaining the ability to enumerate features — is the prerequisite for safety-relevant interpretability claims, and the paper's three candidate routes are (1) train models without it (likely costly, MoE is suggestive), (2) post-hoc find an overcomplete basis (sparse coding at million × billion scale), or (3) hybrid methods.

## Key Takeaway

The intuitive picture — that a neuron either represents a clean concept or it's broken — is wrong in the most useful direction: polysemantic neurons aren't a bug, they're a network compressing more features than it has neurons because the math actually works, but only if those features are sparse. The corollary is that any system that treats neurons (or single embedding axes) as the atomic unit of meaning will sometimes return mixtures of unrelated concepts, and the only way out is to either pay a performance cost to suppress superposition or to do extra work after the fact to unfold it.

## Implications

**(ENGRAM dimensions are tagged in bold at the end of each bullet.)**

- **Treat your single-vector embedding store as fundamentally polysemantic** — by analogy with these toy models, when you cosine-search a flat vector index, "unrelated features start to be embedded with positive dot products to each other" (verbatim from the Strategic Picture section), so a nearest-neighbour hit can be a contamination from a superposed feature you didn't intend to retrieve. Build a contamination check into your eval, not just a recall@k. **(R — Retrieve; G — Ground)**
- **Sparsity is the lever, not model size** — the paper shows superposition strength is governed by the feature importance and sparsity curves of the data, not by raw parameter count. For a memory layer, this means the right knob to tune isn't "bigger embedder" but "what fraction of write events should actually create a new memory" — making writes rarer (more sparse) increases the model's incentive to pack, while making them denser pushes toward clean orthogonal storage. **(E — Encode; N — Network)**
- **Phase changes mean you can't gradient-descend out of polysemanticity** — because the transitions between "not learned / superposed / dedicated" are first-order discontinuous, you can't make a memory system incrementally cleaner by nudging hyperparameters; you have to cross a regime boundary (e.g. add L1 to activations or restructure the network) to flip a feature out of superposition. Plan for step-change reconfigurations rather than continuous tuning. **(M — Maintain; A — Aggregate)**
- **Build a "local non-superposition" assumption only at the sub-distribution level** — the paper finds correlated features form orthogonal local bases inside larger superposed models, which justifies running clean PCA / cosine analyses on narrow topical sub-distributions even when the full vault is superposed. Concretely: per-topic mini-indexes or per-conversation working memory can use simpler retrieval than the global memory layer. **(N — Network; R — Retrieve)**
- **Anticipate adversarial / accidental contamination scales with packing density** — adversarial vulnerability rose >3× as superposition formed and closely tracked features-per-dimension. The same mechanism makes a memory layer vulnerable to confounded queries: as you pack more concepts into a fixed embedding budget, a single misplaced token in the query can collapse retrieval onto the wrong superposed feature. Measure brittleness, not just accuracy. **(G — Ground; R — Retrieve)**
- **Co-occurrence structure determines what gets confused for what** — correlated features cluster in the same tegum factor with positive interference; anticorrelated ones get put antipodally with negative interference. For a memory layer, this means concepts that frequently co-occur in your source material (e.g. "Flow" and "the user's name", or "AskRally" and "personas") will end up in the same retrieval neighbourhood whether you want them to or not — and the cost of breaking them apart is paid in lost compression. **(E — Encode; A — Aggregate)**
- **Compressed sensing gives you an upper bound on how many features your layer can hold** — m = Ω(k log(n/k)) (Theorem 1 in the appendix) is the inner-dimension lower bound; equivalently, your m-dimensional embedding can hold at most O(m / log(n/k)) actively-firing features per query. Use this to size your embedding dimension against the *active* feature count, not the total feature count. **(N — Network)**
- **"AI as maintainer" maps onto Approach 3 (hybrid)** — the paper's third strategic route is to change models so superposition is *easier to decode after the fact* rather than eliminated. For an agentic memory OS, the analogue is to have the writing agent produce slight architectural redundancy (e.g. double-write important features to dedicated topic indexes) so the reading agent has an easier sparse-coding problem at query time. **(M — Maintain; A — Aggregate)**

## How to Apply It (method)

**Scenario:** You run a Flow OS-style memory layer where session transcripts are auto-extracted into atomic memory cards and embedded into a single hybrid index. You're seeing weird retrieval misses: queries about one client are pulling memories about an unrelated client whose conversations co-occurred in time, and you suspect your embeddings are in superposition. You want to (a) measure how much superposition is in your layer, (b) decide which approach from the paper to apply, and (c) implement Approach 3 (hybrid) as the cheapest first move.

**Steps:**

1. **Build a synthetic feature ground-truth set.** Define ~50 "concepts" you care about retrieving cleanly (client names, projects, mental models). For each, write 5–10 short paraphrases that should all retrieve under the same intent. This is your stand-in for the paper's known feature vector x.

2. **Measure feature dimensionality empirically.** Embed all paraphrases and project the per-concept centroid onto every other concept centroid:

   ```
   D_i = ||c_i||^2  /  sum_j (c_hat_i · c_j)^2
   ```

   This is the paper's exact dimensionality metric applied to your retrieval layer. Concepts with D close to 1 have a dedicated direction; D ≈ 0.5 means they're sharing a direction with one other concept (antipodal pair); D close to 0 means your layer can't represent them at all. Plot the histogram — sticky peaks at 1/2, 2/3, 3/4 are an exact reproduction of the paper's geometric phase signature.

3. **Estimate your sparsity regime.** For a 7-day window, count what fraction of memory writes mention each concept. If most concepts are <1% of writes (highly sparse), you're in the regime where superposition is mathematically optimal — fighting it costs you a lot. If a few dominant concepts (e.g. "Flow") are >10% of writes, you're closer to the dense regime and superposition is buying you less.

4. **Decide which of the paper's three strategies fits.**
   - **Approach 1 (remove superposition):** add L1 regularization to your embedder's activations and accept a hit on packing density. Worth it only if you have spare embedding dimensions to absorb the cost.
   - **Approach 2 (overcomplete basis after the fact):** train a sparse autoencoder on a sample of your stored embeddings, find an overcomplete dictionary, query through the dictionary rather than the raw vectors. Heavy engineering lift.
   - **Approach 3 (hybrid):** the lightest first move — explored below.

5. **Implement Approach 3: redundant write paths for high-importance concepts.** For each concept you measured as severely superposed in step 2, have the writing agent maintain a small per-concept inverted index in parallel with the main embedding store. The prompt template:

   ```
   You are the memory writer. The following memory card is being saved.
   First, embed it as normal. Then, scan it for any of these high-importance
   concepts: <list of concepts with D < 0.4 from step 2>. For each one found,
   also write a pointer to this memory card into memory/indexes/<concept>.md
   as a one-line bullet. Do NOT include concepts not in the list.

   Memory card:
   <text>
   ```

6. **Query through both paths and merge.** On retrieval, do the normal hybrid query AND scan the per-concept indexes for any concept-name match in the user's query. Union the results and dedupe. The per-concept index is your "unfolded" path; the embedding store is your "superposed" path.

7. **Re-measure after a week.** Re-run step 2 on a fresh sample. If D values for your tracked concepts moved closer to 1, the hybrid is working. If they didn't move (because the embedder is still doing the same thing), the win is in the redundant index — log retrieval source attribution per query to confirm where the wins are coming from.

8. **(Optional) Adversarial robustness probe.** Pick 5 concepts and construct minimal-edit query perturbations (add or remove one token) and measure retrieval flip rate. Per the paper, flip rate should scale with features-per-dimension. If your flip rate is >20% you have a brittle layer; reducing superposition (Approach 1 or 3) should drop it.

**Expected outcome:** You'll know with numbers — not vibes — whether your memory layer is in superposition for the concepts you care about, you'll have a per-concept dimensionality chart that flags which concepts are at risk of cross-contamination, and you'll have a hybrid write/read path that gives the most important concepts a "dedicated dimension" outside the embedding store, traded off against extra write cost. Crucially, you'll have stopped guessing about retrieval failures: they're now reproducible and measurable.

## Best Figure

![Figure 1 — As Sparsity Increases, Models Use "Superposition" To Represent More Features Than Dimensions (page 2)](figures/elhage-2022-toy-models-superposition-fig.png)

**Image Candidates:**
- Hero figure on page 2 ("As Sparsity Increases…"): three 2D scatter panels at 0%, 80%, 90% sparsity showing five features collapsing from "two dedicated axes + three ignored" → "two antipodal pairs + one ignored" → "pentagon, all five embedded with positive interference." Tells the entire paper in one view.
- The "dimensions per feature" plot in the Geometry section (D* = m/||W||²_F vs sparsity): shows the "sticky" 1, 1/2, 2/5, 3/8 plateaus and is the paper's most original quantitative result.
- The privileged-basis comparison in "Visualizing Superposition in Terms of Neurons": neuron stack plots transitioning from monosemantic to polysemantic as sparsity rises.

**Best Image:**
Figure Name: "As Sparsity Increases, Models Use 'Superposition' To Represent More Features Than Dimensions"
Figure Page: 2
Slide Caption: Same five features, same network — at 0% sparsity the model uses PCA (two features dedicated, three ignored); at 80% it forms antipodal pairs; at 90% it packs all five into a pentagon with positive interference.
Description: Three side-by-side 2D scatter plots show how a ReLU autoencoder embeds five features of varying importance (yellow = most, dark green = least) into a 2-dimensional hidden space at three sparsity levels (0%, 80%, 90% probability a feature is zero). At 0% sparsity the model behaves like PCA — only the two most important features get dedicated orthogonal directions; the three less important features are mapped to zero (the caption literally reads "Less important features map to zero"). At 80% sparsity the model arranges the four most important features as antipodal pairs (each feature's vector is the exact negative of its partner's), still discarding the least important. At 90% sparsity all five features are embedded as the vertices of a regular pentagon, with a labelled diagonal showing the "positive interference" cost. The figure makes the paper's central claim visible in a single image — that the same network architecture can be in three qualitatively different representational regimes depending only on input sparsity, and that the regimes correspond to precise geometric configurations (orthogonal basis → antipodal pairs → polytope).

## What Experts Overlook

The paper's strategic section says superposition can only be "solved" if you can enumerate features, and most readers take this as a technical interpretability point — train a sparse autoencoder, find a dictionary, done. The detail that gets overlooked is the asymmetric-superposition motif buried in the Computation section: when a model is forced to do real work on top of superposed features (computing abs(x) on 100 features in 40 neurons), it does **not** stop at the elegant antipodal-pair geometry. Instead, it learns asymmetric weight pairs like W=[2, −½] paired with output weights W=[½, 2], and then a *second* dedicated inhibitory neuron whose only job is to suppress one feature whenever the other could cause positive interference. The model is essentially building its own contradiction-handling circuit inside the superposition itself, converting unavoidable positive interference (which costs a lot at the output ReLU) into negative interference (which is cheap). This isn't elegant geometry — it's a hack the network learns when geometry alone isn't enough.

**Why it matters:** It tells you that a memory layer running on top of a superposed embedding store will, given enough optimization pressure, evolve **circuits**, not just representations, to handle the interference. The relevant unit of analysis isn't "is this embedding monosemantic?" — it's "which other parts of the system are quietly cancelling out the interference this embedding creates?" That cancellation logic is itself part of the memory architecture, and if you don't recognize it, you'll think your retriever is clean when actually a downstream re-ranker has learned to silently down-weight a specific co-confounded concept.

**Example of good use:** A Flow OS memory layer that detects, say, retrievals for "AskRally" frequently come back paired with "personas" but the user's query only mentioned AskRally. The "memory architect" recognizes this as positive interference between two superposed concepts and deliberately trains a tiny inhibitory re-ranker — a 1-layer model whose only job is to down-weight "persona"-tagged memories when the query is AskRally-without-personas. This is the asymmetric-superposition motif applied to a memory layer: do the hard work in a small specialised circuit rather than trying to clean up the upstream embedder.

**Example of misapplication:** A team notices the same AskRally/personas confusion and tries to "fix" it by retraining the embedder to push the two concepts orthogonal. This works for those two but pushes some other co-occurring pair into the slot that just opened up — they get whack-a-mole. Worse, they fail to notice that their downstream re-ranker had already learned a (silent, opaque) inhibition rule for the original pair, and now the re-ranker's logic is wrong for the new representation. The memory layer's behaviour worsens *because* they touched the geometry without realizing a circuit was already compensating.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

The paper has 57 references. Top 10:

- Olah et al., 2020 — *Zoom In: An Introduction to Circuits* (Distill)
- Elhage et al., 2022 — *Softmax Linear Units* (Transformer Circuits Thread)
- Donoho, 2006 — *Compressed sensing* (IEEE Trans. Info. Theory)
- Thorpe, 1989 — *Local vs. Distributed Coding* (Intellectica)
- Bengio, Courville, Vincent, 2013 — *Representation learning: A review and new perspectives*
- Cammarata et al., 2020 — *Curve Detectors* (Distill)
- Cheung et al., 2019 — *Superposition of many models into one* (NeurIPS)
- Mikolov, Yih, Zweig, 2013 — *Linguistic regularities in continuous space word representations*
- Olshausen & Field, 1997 — *Sparse coding with an overcomplete basis set: A strategy employed by V1?*
- Candes & Tao, 2005 — *Decoding by linear programming*

Full structured list (57 entries) lives in the `citations:` block in this file's frontmatter.

## Related Digests

- [[cunningham-2023-sparse-autoencoders-features]] — Sparse Autoencoders Find Highly Interpretable Features in Language Models (the direct empirical follow-up that operationalizes Approach 2 from this paper)
- [[marks-2024-sparse-feature-circuits]] — Sparse Feature Circuits (next-hop work that builds circuits out of the SAE features)
- [[mao-2026-agent-memory-circuits]] — Agent Memory Circuits (applies the SAE-circuit lens to agent memory architectures, completing the chain)

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in the digest (m=2–40, n=20–400 hidden / feature counts, S range, >3× adversarial vulnerability, the 1/2, 2/3, 3/4, 2/5, 3/8 dimensionality plateaus, the Thomson connection, the m = Ω(k log(n/k)) compressed sensing bound, the asymmetric-superposition W=[2, −½] / W=[½, 2] pattern, the abs(x) absolute-value task with n=100 features and m=40 neurons) is verbatim in the paper. The geometric configurations are explicitly named in the "Why These Geometric Structures?" subsection. The asymmetric-superposition motif is reproduced precisely as the paper states. The three strategic approaches and the L1-regularization-on-activations route are stated verbatim in the Strategic Picture section. The pentagon / antipodal pair / orthogonal-basis transitions across 0%, 80%, 90% sparsity are exactly the labelling in the page-2 hero figure.

No fabricated content beyond well-labelled reader-lens extrapolation (the Flow OS / memory-layer applied use case in the Method section is explicitly framed as "scenario," not as a claim about the paper).
