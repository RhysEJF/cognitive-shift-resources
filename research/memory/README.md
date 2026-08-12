# Memory for Agentic Systems — a 145-paper digest corpus

This folder is a research corpus on **memory architectures for AI agents**: 145 structured digests of papers spanning agent memory systems (Mem0, MemGPT-lineage, MIRIX, Hindsight, MemOS…), retrieval and RAG, long-context transformers, continual learning and catastrophic forgetting, mechanistic interpretability, and the cognitive-science foundations (complementary learning systems, sparse coding, episodic vs semantic memory).

It was built with an AI research pipeline (`/digest-paper` + citation-graph walking) inside a working second-brain system, then published here as part of [The Cognitive Shift](https://github.com/RhysEJF/cognitive-shift-resources)'s open research.

## How to read this corpus

- **[INDEX.md](INDEX.md)** — the full table: every paper with date digested, lens, and a one-sentence key takeaway. Start there.
- Each digest follows the same structure: **TLDR → Key Takeaway → Implications → How to Apply It → Best Figure → What Experts Overlook → Extracted Prompts → Citations → Reviewer Notes** (including a hallucination check against the source paper).
- Digests cross-link each other with `[[wiki-links]]` in their frontmatter (`related_digests`), so you can walk between related papers.

## The lens: why the digests read the way they do

Papers were digested through a **reading lens** — a persona prompt defining who is reading and what kind of takeaways matter. Most of this corpus (112 papers) used a *memory-architect* lens: a researcher building memory layers for agentic operating systems, focused on write-time vs query-time synthesis, shape-of-memory, drift/provenance/contradiction, and AI-as-maintainer. The remaining 33 used a generic lens.

The memory-architect digests tag findings with **ENGRAM**, a six-dimension framework for memory-architecture decisions following the lifecycle of a memory:

- **E — Encode**: what gets written, who triggers the write, whether an LLM distils on the write path
- **N — Network**: where memory lives — single file, markdown vault, vector store, polyglot stack, or graph
- **G — Ground**: provenance, attribution, verifiability, confidence
- **R — Retrieve**: query expression, ranking, hybrid vs semantic vs lexical
- **A — Aggregate**: turning experiences into patterns — or deliberately not
- **M — Maintain**: lifecycle management — decay, eviction, consolidation, contradiction repair

## A note on the worked examples

Many digests include "Scenario" / "How to Apply It" sections that ground the paper in a real agentic-OS build (a markdown-vault second brain with hybrid BM25+vector retrieval, session-based extraction, and slash-command workflows). That system is real; **the people in the examples are not** — names, contact details, and personal specifics in worked examples are fictional personas introduced at publication time.

## License & citation

Digests are AI-generated interpretations of the underlying papers — always check the digest's `source_url` and read the original before relying on a claim. Each digest's *Reviewer Notes* section includes a hallucination check, but errors survive. If you spot one, open an issue.
