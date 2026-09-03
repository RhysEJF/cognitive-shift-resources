# Synthetic Personas and Simulated Users: a paper digest corpus

This folder holds structured digests of papers on **LLM-simulated personas, silicon sampling, and synthetic market research**: using AI personas to stand in for human respondents in surveys, concept tests, pricing studies, usability tests and interviews, and what the evidence says about when that works and when it does not.

It is built with the same AI research pipeline as the [memory corpus](../memory/) (`/digest-paper` inside a working second-brain system) and published here as part of [The Cognitive Shift](https://github.com/RhysEJF/cognitive-shift-resources)'s open research. This corpus starts with one paper; more digests will be added over time.

## How to read this corpus

- **[INDEX.md](INDEX.md)** is the full table: every paper with date digested, lens, and a one-sentence key takeaway. Start there.
- Each digest follows the same structure: **TLDR, Key Takeaway, Implications, How to Apply It, Best Figure, What Experts Overlook, Extracted Prompts, Citations, Related Papers, Reviewer Notes**. The Reviewer Notes section is a hallucination check of the digest against the source paper, with every flagged claim and the fix applied.
- Figures are cropped from the source paper and stored in `figures/`, credited to the paper's authors.

## The lens: why the digests read the way they do

Papers are digested through a **reading lens**, a persona prompt that defines who is reading and what kind of takeaways matter. This corpus uses a *synthetic-personas* lens: a team building virtual-audience simulators for market research (brand surveys, MaxDiff, Van Westendorp, conjoint, concept tests, customer interviews, A/B tests) who want actionable ways to make AI-persona results track real-world results more closely. Digests are written in plain language for a non-technical reader to share with a technical team, with numbers and findings rather than adjectives, and each section is meant to be copy-pasted into a briefing.

## Papers

| Paper | Why it is here |
|---|---|
| [MatrAIx: Simulating the World with 8.3 Billion Persona Agents](li-2026-matraix-persona-8b.md) (Li, Hao et al., 2026) | Population-scale persona infrastructure with an open 1M-persona dataset and playground. Its central result: the LLM playing the persona moves outcomes more than the persona does, so every synthetic study needs cross-model replication. |
