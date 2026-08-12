---
corpus: agentic-memory
kind: paper-digest
slug: lewis-2020-rag-knowledge-nlp
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
authors:
  - "Patrick Lewis"
  - "Ethan Perez"
  - "Aleksandra Piktus"
  - "Fabio Petroni"
  - "Vladimir Karpukhin"
  - "Naman Goyal"
  - "Heinrich Küttler"
  - "Mike Lewis"
  - "Wen-tau Yih"
  - "Tim Rocktäschel"
  - "Sebastian Riedel"
  - "Douwe Kiela"
year: 2020
publication_date: "2020-05"
venue: "NeurIPS 2020"
source_url: "https://arxiv.org/abs/2005.11401"
doi: null
arxiv_id: "2005.11401"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "RAG demonstrates that you can decouple a model's parametric \"reasoning\" memory from a non-parametric \"facts\" memory and train them end-to-end without retrieval supervision — and the non-parametric half is hot-swappable, so updating the model's world knowledge becomes a file replacement instead of a retraining run."
topics:
  - retrieval-augmented-generation
  - rag
  - dense-passage-retrieval
  - non-parametric-memory
  - open-domain-qa
  - knowledge-intensive-nlp
  - seq2seq
  - end-to-end-retrieval
  - hot-swap-memory
  - hallucination-mitigation
tags:
  - paper
  - memory-architecture
  - foundational
  - rag-origin
  - engram-network
  - engram-retrieve
  - engram-ground
entities:
  - lewis-patrick
  - perez-ethan
  - kiela-douwe
  - riedel-sebastian
  - karpukhin-vladimir
  - facebook-ai-research
related_digests:
  - adler-2026-storage-not-memory
  - packer-2023-memgpt-os
  - chhikara-2025-mem0
  - latimer-2025-hindsight-memory
citations:
  - {title: "MS MARCO: A Human Generated MAchine Reading COmprehension Dataset", authors: ["Payal Bajaj", "Daniel Campos", "Nick Craswell", "et al."], year: 2016, venue: "arXiv preprint", doi: null, url: "http://arxiv.org/abs/1611.09268", arxiv_id: "1611.09268"}
  - {title: "Modeling of the question answering task in the yodaqa system", authors: ["Petr Baudiš", "Jan Šedivỳ"], year: 2015, venue: "CLEF (Springer)", doi: null, url: "https://link.springer.com/chapter/10.1007/978-3-319-24027-5_20", arxiv_id: null}
  - {title: "Semantic Parsing on Freebase from Question-Answer Pairs", authors: ["Jonathan Berant", "Andrew Chou", "Roy Frostig", "et al."], year: 2013, venue: "EMNLP 2013", doi: null, url: "http://www.aclweb.org/anthology/D13-1160", arxiv_id: null}
  - {title: "Palm: Pre-training an autoencoding & autoregressive language model for context-conditioned generation", authors: ["Bin Bi", "Chenliang Li", "Chen Wu", "et al."], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2004.07159", arxiv_id: "2004.07159"}
  - {title: "Reading Wikipedia to Answer Open-Domain Questions", authors: ["Danqi Chen", "Adam Fisch", "Jason Weston", "et al."], year: 2017, venue: "ACL 2017", doi: "10.18653/v1/P17-1171", url: "https://www.aclweb.org/anthology/P17-1171", arxiv_id: null}
  - {title: "Coarse-to-fine question answering for long documents", authors: ["Eunsol Choi", "Daniel Hewlett", "Jakob Uszkoreit", "et al."], year: 2017, venue: "ACL 2017", doi: "10.18653/v1/P17-1020", url: "https://www.aclweb.org/anthology/P17-1020", arxiv_id: null}
  - {title: "Simple and Effective Multi-Paragraph Reading Comprehension", authors: ["Christopher Clark", "Matt Gardner"], year: 2017, venue: "arXiv preprint", doi: null, url: "http://arxiv.org/abs/1710.10723", arxiv_id: "1710.10723"}
  - {title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", authors: ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "et al."], year: 2019, venue: "NAACL 2019", doi: "10.18653/v1/N19-1423", url: "https://www.aclweb.org/anthology/N19-1423", arxiv_id: null}
  - {title: "Wizard of wikipedia: Knowledge-powered conversational agents", authors: ["Emily Dinan", "Stephen Roller", "Kurt Shuster", "et al."], year: 2019, venue: "ICLR 2019", doi: null, url: "https://openreview.net/forum?id=r1l73iRqKm", arxiv_id: null}
  - {title: "SearchQA: A New Q&A Dataset Augmented with Context from a Search Engine", authors: ["Matthew Dunn", "Levent Sagun", "Mike Higgins", "et al."], year: 2017, venue: "arXiv preprint", doi: null, url: "http://arxiv.org/abs/1704.05179", arxiv_id: "1704.05179"}
  - {title: "Hierarchical neural story generation", authors: ["Angela Fan", "Mike Lewis", "Yann Dauphin"], year: 2018, venue: "ACL 2018", doi: "10.18653/v1/P18-1082", url: "https://www.aclweb.org/anthology/P18-1082", arxiv_id: null}
  - {title: "ELI5: Long form question answering", authors: ["Angela Fan", "Yacine Jernite", "Ethan Perez", "et al."], year: 2019, venue: "ACL 2019", doi: "10.18653/v1/P19-1346", url: "https://www.aclweb.org/anthology/P19-1346", arxiv_id: null}
  - {title: "Augmenting transformers with KNN-based composite memory", authors: ["Angela Fan", "Claire Gardent", "Chloe Braud", "et al."], year: 2020, venue: "OpenReview", doi: null, url: "https://openreview.net/forum?id=H1gx1CNKPH", arxiv_id: null}
  - {title: "Entities as experts: Sparse memory access with entity supervision", authors: ["Thibault Févry", "Livio Baldini Soares", "Nicholas FitzGerald", "et al."], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2004.07202", arxiv_id: "2004.07202"}
  - {title: "A knowledge-grounded neural conversation model", authors: ["Marjan Ghazvininejad", "Chris Brockett", "Ming-Wei Chang", "et al."], year: 2018, venue: "AAAI 2018", doi: null, url: "https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16710", arxiv_id: null}
  - {title: "When will AI exceed human performance? Evidence from AI experts", authors: ["Katja Grace", "John Salvatier", "Allan Dafoe", "et al."], year: 2017, venue: "arXiv preprint", doi: null, url: "http://arxiv.org/abs/1705.08807", arxiv_id: "1705.08807"}
  - {title: "Search engine guided neural machine translation", authors: ["Jiatao Gu", "Yong Wang", "Kyunghyun Cho", "et al."], year: 2018, venue: "AAAI 2018", doi: null, url: "https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17282", arxiv_id: null}
  - {title: "Generating sentences by editing prototypes", authors: ["Kelvin Guu", "Tatsunori B. Hashimoto", "Yonatan Oren", "et al."], year: 2018, venue: "TACL", doi: "10.1162/tacl_a_00030", url: "https://www.aclweb.org/anthology/Q18-1031", arxiv_id: null}
  - {title: "REALM: Retrieval-augmented language model pre-training", authors: ["Kelvin Guu", "Kenton Lee", "Zora Tung", "et al."], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2002.08909", arxiv_id: "2002.08909"}
  - {title: "A retrieve-and-edit framework for predicting structured outputs", authors: ["Tatsunori B Hashimoto", "Kelvin Guu", "Yonatan Oren", "et al."], year: 2018, venue: "NeurIPS 2018", doi: null, url: "http://papers.nips.cc/paper/8209-a-retrieve-and-edit-framework-for-predicting-structured-outputs.pdf", arxiv_id: null}
  - {title: "Simple and effective retrieve-edit-rerank text generation", authors: ["Nabil Hossain", "Marjan Ghazvininejad", "Luke Zettlemoyer"], year: 2020, venue: "ACL 2020", doi: "10.18653/v1/2020.acl-main.228", url: "https://www.aclweb.org/anthology/2020.acl-main.228", arxiv_id: null}
  - {title: "Billion-scale similarity search with GPUs", authors: ["Jeff Johnson", "Matthijs Douze", "Hervé Jégou"], year: 2017, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1702.08734", arxiv_id: "1702.08734"}
  - {title: "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension", authors: ["Mandar Joshi", "Eunsol Choi", "Daniel Weld", "et al."], year: 2017, venue: "ACL 2017", doi: "10.18653/v1/P17-1147", url: "https://www.aclweb.org/anthology/P17-1147", arxiv_id: null}
  - {title: "Inferring algorithmic patterns with stack-augmented recurrent nets", authors: ["Armand Joulin", "Tomas Mikolov"], year: 2015, venue: "NeurIPS 2015", doi: null, url: "https://papers.nips.cc/paper/5857-inferring-algorithmic-patterns-with-stack-augmented-recurrent-nets", arxiv_id: null}
  - {title: "Dense passage retrieval for open-domain question answering", authors: ["Vladimir Karpukhin", "Barlas Oguz", "Sewon Min", "et al."], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2004.04906", arxiv_id: "2004.04906"}
  - {title: "Generalization through memorization: Nearest neighbor language models", authors: ["Urvashi Khandelwal", "Omer Levy", "Dan Jurafsky", "et al."], year: 2020, venue: "ICLR 2020", doi: null, url: "https://openreview.net/forum?id=HklBjCEKvH", arxiv_id: null}
  - {title: "Adam: A method for stochastic optimization", authors: ["Diederik P. Kingma", "Jimmy Ba"], year: 2015, venue: "ICLR 2015", doi: null, url: "http://arxiv.org/abs/1412.6980", arxiv_id: "1412.6980"}
  - {title: "Natural Questions: a Benchmark for Question Answering Research", authors: ["Tom Kwiatkowski", "Jennimaria Palomaki", "Olivia Redfield", "et al."], year: 2019, venue: "TACL", doi: null, url: null, arxiv_id: null}
  - {title: "Large memory layers with product keys", authors: ["Guillaume Lample", "Alexandre Sablayrolles", "Marc'Aurelio Ranzato", "et al."], year: 2019, venue: "NeurIPS 2019", doi: null, url: "http://papers.nips.cc/paper/9061-large-memory-layers-with-product-keys.pdf", arxiv_id: null}
  - {title: "Latent retrieval for weakly supervised open domain question answering", authors: ["Kenton Lee", "Ming-Wei Chang", "Kristina Toutanova"], year: 2019, venue: "ACL 2019", doi: "10.18653/v1/P19-1612", url: "https://www.aclweb.org/anthology/P19-1612", arxiv_id: null}
  - {title: "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension", authors: ["Mike Lewis", "Yinhan Liu", "Naman Goyal", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1910.13461", arxiv_id: "1910.13461"}
  - {title: "A diversity-promoting objective function for neural conversation models", authors: ["Jiwei Li", "Michel Galley", "Chris Brockett", "et al."], year: 2016, venue: "NAACL 2016", doi: "10.18653/v1/N16-1014", url: "https://www.aclweb.org/anthology/N16-1014", arxiv_id: null}
  - {title: "Acute-eval: Improved dialogue evaluation with optimized questions and multi-turn comparisons", authors: ["Margaret Li", "Jason Weston", "Stephen Roller"], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1909.03087", arxiv_id: "1909.03087"}
  - {title: "Robust neural machine translation with joint textual and phonetic embedding", authors: ["Hairong Liu", "Mingbo Ma", "Liang Huang", "et al."], year: 2019, venue: "ACL 2019", doi: "10.18653/v1/P19-1291", url: "https://www.aclweb.org/anthology/P19-1291", arxiv_id: null}
  - {title: "Generating wikipedia by summarizing long sequences", authors: ["Peter J. Liu", "Mohammad Saleh", "Etienne Pot", "et al."], year: 2018, venue: "ICLR 2018", doi: null, url: "https://openreview.net/forum?id=Hyg0vbWC-", arxiv_id: null}
  - {title: "Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs", authors: ["Yury A. Malkov", "D. A. Yashunin"], year: 2016, venue: "IEEE TPAMI", doi: null, url: "https://arxiv.org/abs/1603.09320", arxiv_id: "1603.09320"}
  - {title: "The next decade in AI: four steps towards robust artificial intelligence", authors: ["Gary Marcus"], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2002.06177", arxiv_id: "2002.06177"}
  - {title: "How decoding strategies affect the verifiability of generated text", authors: ["Luca Massarelli", "Fabio Petroni", "Aleksandra Piktus", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1911.03587", arxiv_id: "1911.03587"}
  - {title: "Mixed precision training", authors: ["Paulius Micikevicius", "Sharan Narang", "Jonah Alben", "et al."], year: 2018, venue: "ICLR 2018", doi: null, url: "https://openreview.net/forum?id=r1gs9JgRZ", arxiv_id: null}
  - {title: "Towards exploiting background knowledge for building conversation systems", authors: ["Nikita Moghe", "Siddhartha Arora", "Suman Banerjee", "et al."], year: 2018, venue: "EMNLP 2018", doi: "10.18653/v1/D18-1255", url: "https://www.aclweb.org/anthology/D18-1255", arxiv_id: null}
  - {title: "Towards a better metric for evaluating question generation systems", authors: ["Preksha Nema", "Mitesh M. Khapra"], year: 2018, venue: "EMNLP 2018", doi: "10.18653/v1/D18-1429", url: "https://www.aclweb.org/anthology/D18-1429", arxiv_id: null}
  - {title: "MS MARCO: A human generated machine reading comprehension dataset", authors: ["Tri Nguyen", "Mir Rosenberg", "Xia Song", "et al."], year: 2016, venue: "CoCo@NIPS 2016", doi: null, url: "http://ceur-ws.org/Vol-1773/CoCoNIPS_2016_paper9.pdf", arxiv_id: null}
  - {title: "Passage re-ranking with BERT", authors: ["Rodrigo Nogueira", "Kyunghyun Cho"], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1901.04085", arxiv_id: "1901.04085"}
  - {title: "fairseq: A fast, extensible toolkit for sequence modeling", authors: ["Myle Ott", "Sergey Edunov", "Alexei Baevski", "et al."], year: 2019, venue: "NAACL 2019 (Demo)", doi: "10.18653/v1/N19-4009", url: "https://www.aclweb.org/anthology/N19-4009", arxiv_id: null}
  - {title: "Finding generalizable evidence by learning to convince q&a models", authors: ["Ethan Perez", "Siddharth Karamcheti", "Rob Fergus", "et al."], year: 2019, venue: "EMNLP-IJCNLP 2019", doi: "10.18653/v1/D19-1244", url: "https://www.aclweb.org/anthology/D19-1244", arxiv_id: null}
  - {title: "Language models as knowledge bases?", authors: ["Fabio Petroni", "Tim Rocktäschel", "Sebastian Riedel", "et al."], year: 2019, venue: "EMNLP-IJCNLP 2019", doi: "10.18653/v1/D19-1250", url: "https://www.aclweb.org/anthology/D19-1250", arxiv_id: null}
  - {title: "How context affects language models' factual predictions", authors: ["Fabio Petroni", "Patrick Lewis", "Aleksandra Piktus", "et al."], year: 2020, venue: "AKBC 2020", doi: null, url: "https://openreview.net/forum?id=025X0zPfn", arxiv_id: null}
  - {title: "Improving Language Understanding by Generative Pre-Training", authors: ["Alec Radford", "Karthik Narasimhan", "Tim Salimans", "et al."], year: 2018, venue: "OpenAI tech report", doi: null, url: "https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf", arxiv_id: null}
  - {title: "Language models are unsupervised multitask learners (GPT-2)", authors: ["Alec Radford", "Jeff Wu", "Rewon Child", "et al."], year: 2019, venue: "OpenAI tech report", doi: null, url: null, arxiv_id: null}
  - {title: "Exploring the limits of transfer learning with a unified text-to-text transformer (T5)", authors: ["Colin Raffel", "Noam Shazeer", "Adam Roberts", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1910.10683", arxiv_id: "1910.10683"}
  - {title: "How much knowledge can you pack into the parameters of a language model?", authors: ["Adam Roberts", "Colin Raffel", "Noam Shazeer"], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2002.08910", arxiv_id: "2002.08910"}
  - {title: "The probabilistic relevance framework: BM25 and beyond", authors: ["Stephen Robertson", "Hugo Zaragoza"], year: 2009, venue: "Found. Trends Inf. Retr.", doi: "10.1561/1500000019", url: "https://doi.org/10.1561/1500000019", arxiv_id: null}
  - {title: "Release strategies and the social impacts of language models", authors: ["Irene Solaiman", "Miles Brundage", "Jack Clark", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: null, arxiv_id: "1908.09203"}
  - {title: "End-to-end memory networks", authors: ["Sainbayar Sukhbaatar", "Arthur Szlam", "Jason Weston", "et al."], year: 2015, venue: "NeurIPS 2015", doi: null, url: "http://papers.nips.cc/paper/5846-end-to-end-memory-networks.pdf", arxiv_id: null}
  - {title: "FEVER: a large-scale dataset for fact extraction and VERification", authors: ["James Thorne", "Andreas Vlachos", "Christos Christodoulopoulos", "et al."], year: 2018, venue: "NAACL 2018", doi: "10.18653/v1/N18-1074", url: "https://www.aclweb.org/anthology/N18-1074", arxiv_id: null}
  - {title: "Avoiding catastrophic forgetting in mitigating model biases in sentence-pair classification with elastic weight consolidation", authors: ["James H. Thorne", "Andreas Vlachos"], year: 2020, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/2004.14366", arxiv_id: "2004.14366"}
  - {title: "Attention is all you need", authors: ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "et al."], year: 2017, venue: "NeurIPS 2017", doi: null, url: "http://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf", arxiv_id: null}
  - {title: "Diverse beam search for improved description of complex scenes", authors: ["Ashwin Vijayakumar", "Michael Cogswell", "Ramprasaath Selvaraju", "et al."], year: 2018, venue: "AAAI 2018", doi: null, url: "https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17329", arxiv_id: null}
  - {title: "GLUE: A multi-task benchmark and analysis platform for natural language understanding", authors: ["Alex Wang", "Amanpreet Singh", "Julian Michael", "et al."], year: 2018, venue: "EMNLP BlackboxNLP 2018", doi: "10.18653/v1/W18-5446", url: "https://www.aclweb.org/anthology/W18-5446", arxiv_id: null}
  - {title: "SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems", authors: ["Alex Wang", "Yada Pruksachatkun", "Nikita Nangia", "et al."], year: 2019, venue: "NeurIPS 2019", doi: null, url: "https://arxiv.org/abs/1905.00537", arxiv_id: "1905.00537"}
  - {title: "R3: Reinforced ranker-reader for open-domain question answering", authors: ["Shuohang Wang", "Mo Yu", "Xiaoxiao Guo", "et al."], year: 2018, venue: "AAAI 2018", doi: null, url: "https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16712", arxiv_id: null}
  - {title: "Evidence aggregation for answer re-ranking in open-domain question answering", authors: ["Shuohang Wang", "Mo Yu", "Jing Jiang", "et al."], year: 2018, venue: "ICLR 2018", doi: null, url: "https://openreview.net/forum?id=rJl3yM-Ab", arxiv_id: null}
  - {title: "Memory networks", authors: ["Jason Weston", "Sumit Chopra", "Antoine Bordes"], year: 2015, venue: "ICLR 2015", doi: null, url: "http://arxiv.org/abs/1410.3916", arxiv_id: "1410.3916"}
  - {title: "Retrieve and refine: Improved sequence generation models for dialogue", authors: ["Jason Weston", "Emily Dinan", "Alexander Miller"], year: 2018, venue: "EMNLP SCAI 2018", doi: "10.18653/v1/W18-5713", url: "https://www.aclweb.org/anthology/W18-5713", arxiv_id: null}
  - {title: "Huggingface's transformers: State-of-the-art natural language processing", authors: ["Thomas Wolf", "Lysandre Debut", "Victor Sanh", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: null, arxiv_id: "1910.03771"}
  - {title: "Addressing semantic drift in question generation for semi-supervised question answering", authors: ["Shiyue Zhang", "Mohit Bansal"], year: 2019, venue: "EMNLP-IJCNLP 2019", doi: "10.18653/v1/D19-1253", url: "https://www.aclweb.org/anthology/D19-1253", arxiv_id: null}
  - {title: "Reasoning over semantic-level graph for fact checking", authors: ["Wanjun Zhong", "Jingjing Xu", "Duyu Tang", "et al."], year: 2019, venue: "arXiv preprint", doi: null, url: "https://arxiv.org/abs/1909.03745", arxiv_id: "1909.03745"}
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Overview of our approach (RAG architecture: Query Encoder + Document Index + Generator with end-to-end backprop)"
  page: 2
  image_path: "figures/lewis-2020-rag-knowledge-nlp-fig.png"
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
**Published:** 2020-05 (NeurIPS 2020) · [Source](https://arxiv.org/abs/2005.11401)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Lewis et al. (FAIR / UCL / NYU) introduce RAG — a generic fine-tuning recipe that fuses a pre-trained BART-large seq2seq generator (~406M params, "parametric memory") with a pre-trained Dense Passage Retriever bi-encoder over a FAISS index of 21M 100-word Wikipedia chunks ("non-parametric memory"), and trains them end-to-end by marginalising the retrieved document as a latent variable — with no supervision on what should be retrieved. Two variants: **RAG-Sequence** picks one document for the whole output, **RAG-Token** can switch documents per token. With only 626M total trainable parameters they set SOTA on three open-domain QA benchmarks (Natural Questions 44.5 EM, WebQuestions 45.2, CuratedTREC 52.2) — beating the 11B-param T5+SSM closed-book baseline on NQ by 7.9 EM with ~18× fewer parameters, and beating extractive DPR-QA without needing a re-ranker or extractive reader. On generation tasks: RAG generates answers humans prefer over BART on factuality 42.7% to 7.1% of the time on Jeopardy question generation, hits 11.8% accuracy even when no retrieved doc contains the answer (where extractive scores 0%), and beats BART on MS-MARCO by ~2.6 BLEU/ROUGE-L. On FEVER fact verification, it lands within 4.3% of pipeline SOTA without using gold retrieval supervision. The killer demo: hot-swap the Wikipedia index from a 2016 dump to a 2018 dump and the model's answers about world leaders update from 70% correct on 2016 leaders to 68% on 2018 leaders, with no retraining — knowledge becomes a file you replace.

## Key Takeaway

RAG demonstrates that you can decouple a model's parametric "reasoning" memory from a non-parametric "facts" memory and train them end-to-end without retrieval supervision — and the non-parametric half is hot-swappable, so updating the model's world knowledge becomes a file replacement instead of a retraining run. The latent-variable framing is what makes this work: the retriever doesn't need labelled "correct documents" because the generator's likelihood gradient flows back through the marginalisation and teaches the retriever which passages help. This is the foundational architectural claim every later memory-system paper builds on, modifies, or pushes back against. **[ENGRAM: Network + Retrieve + Maintain]** — it codified non-parametric memory as the *shape* of choice, hybrid sparse/dense as the *retrieve* primitive, and index hot-swap as the *maintain* superpower that parametric-only systems structurally cannot match.

## Implications

- **The hot-swap test is the cleanest demonstration of "storage is not parameters" you can run** [ENGRAM: Maintain]: §4.5 swaps the Wikipedia index from December 2016 to December 2018 and answers about 82 changed world leaders flip accordingly (70% / 68% on matched indices, 4-12% on mismatched). For any memory system you're building, ask: can I edit a fact in 60 seconds without retraining? If not, you've baked storage into parameters.
- **End-to-end training without retrieval labels is the breakthrough, not the retriever itself** [ENGRAM: Retrieve + Aggregate]: REALM (2020) needed salient-span-masking pre-training; DPR needed gold-document supervision; RAG needs neither because it treats `z` as a latent and marginalises. Implication for memory architects: if you have a downstream signal (answer correctness, task reward, user thumbs-up), you can train your retriever from that signal alone — gold "this is the right memory" labels are a nice-to-have, not a requirement.
- **The "raw text as memory" choice is doing more work than people realise** [ENGRAM: Network + Ground]: §5 explicitly contrasts RAG against entity-embedding memories (Févry et al. 2020) and KNN-LM (Khandelwal et al. 2020), arguing raw text is *human-readable* (interpretable) and *human-writable* (editable). Every later "memory as markdown" architecture — including yours — inherits this design choice from §5 of this paper.
- **RAG-Token > RAG-Sequence when the output needs to fuse multiple sources; RAG-Sequence > RAG-Token when one document is enough** [ENGRAM: Retrieve + Aggregate]: Figure 2's posterior trace shows RAG-Token switches its document focus between "A Farewell to Arms" (doc 1) and "The Sun Also Rises" (doc 2) within a single Jeopardy clue, while RAG-Sequence is forced to commit. For your agent's memory layer, "one memory per turn" (Sequence) vs "many memories per token" (Token) is a real architectural fork — pick based on whether your tasks are mono-source or multi-source.
- **Parametric and non-parametric memory cooperate; they don't compete** [ENGRAM: Network]: Figure 2's "Sun" generation shows that after the retriever fires for the first token of a title, the posterior over documents *flattens* and BART's parametric memory completes the title from its own weights. Memory architectures should expect both layers to contribute; don't design a system that treats RAG as "the LLM but with a database" — design one that knows when to lean on each.
- **Retrieval can quietly collapse, and you may never notice** [ENGRAM: Maintain — failure mode]: Appendix H reports that on story generation [Fan et al. 2018], the retriever learned to retrieve the same documents regardless of input; once collapsed, the generator learned to ignore the retrieved documents entirely and RAG became BART. For any RAG system in production, instrument retrieval diversity as a first-class health metric — uniform retrieval-distribution = silent failure.
- **Frozen-document-index is a feature, not a limitation** [ENGRAM: Maintain]: §2.4 / §4.5 — the authors explicitly skip the REALM-style periodic re-encoding of the document index during training because "we do not find this step necessary for strong performance," and only fine-tune the *query* encoder + generator. This means your non-parametric memory can be pre-built offline, served from disk, and replaced atomically — three properties parametric memory cannot offer.
- **Generation > extraction even on tasks where extraction "should" win** [ENGRAM: Aggregate]: §4.1 — RAG sets SOTA on extractive open-domain QA without using an extractive reader. Even when the correct answer is *not* in any retrieved document, RAG scores 11.8% on Natural Questions (where an extractive model would score 0%). Implication: if your retrieval is even moderately good, a generative head is more robust than an extractive head — the parametric memory acts as a fallback when the retrieved evidence is incomplete.

## How to Apply It (method)

**Scenario:** You're an applied memory-architecture researcher building Flow OS's read path. Today your retriever is BM25-only over QMD's markdown vault, and you want to A/B-test whether end-to-end training a query encoder on real session outcomes (did the agent's response satisfy the user?) would beat both pure BM25 and a frozen off-the-shelf embedding model — without ever having to hand-label "this memory was relevant to this turn." Lewis 2020's recipe shows how.

**Steps:**

1. **Freeze your document index (E-side of ENGRAM stays cheap)**: Encode every memory file in your vault into dense vectors with a pre-trained bi-encoder (e.g., bge-small or whatever your DPR-equivalent is). Store the matrix on disk + a FAISS HNSW index. *Do not* fine-tune the document encoder — the paper explicitly skips this and reports no quality loss. This decouples encode cost from retriever quality.

2. **Initialise your retriever from a strong off-the-shelf checkpoint**: Use a pre-trained DPR-style query encoder (or any sentence-transformers model). Do NOT train from scratch — Lewis et al. only succeed because both retriever and generator come pre-trained on something reasonable.

3. **Build the joint forward pass with latent marginalisation**:

   ```
   For an input x (a Flow OS turn / question / agent prompt):
     1. q = QueryEncoder(x)                                # 768-d vector
     2. top_k_docs = FAISS.search(q, k=10)                 # 10 candidates
     3. p(z|x) ∝ exp(d(z)ᵀ q(x))                           # MIPS scores → distribution over the 10
     4. For each retrieved doc z_i:
          context = concat(x, z_i)
          p(y | x, z_i) = LLM(context)                     # your generator
     5. p(y|x) = Σ_i p(z_i|x) · p(y|x, z_i)                # marginalize (RAG-Sequence flavour)
   ```

4. **Pick a marginalisation flavour for your task**:
   - **RAG-Sequence** (one doc per response): simpler, better for "answer this question from one source." Use for fact lookups, single-topic queries.
   - **RAG-Token** (different doc per token): harder to decode (no clean beam search; the paper's "Thorough" vs "Fast" decoding is the workaround), better when one response fuses multiple memories. Use for multi-hop reasoning, synthesis tasks.

5. **Train end-to-end with task loss only — no retrieval supervision**: Collect (input, desired-output) pairs from past sessions where you have a reliable outcome signal — e.g., the user accepted the agent's answer, or a downstream eval passed. Backprop through the marginalised log-likelihood `−log p(y|x)` with Adam. Only the *query* encoder and the generator update; the document encoder stays frozen. Retrieval supervision is not required — the gradient teaches the query encoder which docs help generation.

6. **Instrument retrieval collapse as a health metric** (Appendix H lesson): every N training steps, measure (a) the entropy of `p(z|x)` averaged across a held-out batch and (b) the cosine similarity between retrieved-doc sets for very different inputs. If entropy plummets or similarity spikes, retrieval has collapsed — kill the run and revisit your task signal.

7. **Add a BM25 ablation as the floor**: Replace the learned retriever with BM25 over the same memory store, using BM25 scores as the `p(z|x)` logits. Per Table 6, BM25 *wins* on entity-centric tasks (FEVER) and *loses* badly on open-domain QA. This tells you which Flow OS tasks need the learned retriever vs which can stay cheap with lexical.

8. **Demonstrate the hot-swap property in your demo**: Add a new fact ("Nadia's birthday is …") as a markdown file. Re-embed only that file. Run the same query. Show the answer updates. This is the demo that sells the architecture to anyone who's tried to "edit" a fine-tuned model's facts.

**Expected outcome:** A retriever fine-tuned from real Flow OS outcomes (not gold labels), an empirical comparison against frozen-embedding and BM25 baselines that tells you which tasks justify the training cost, instrumentation that catches retrieval collapse before it ships, and a working hot-swap demo. You'll also have a clean datum for ENGRAM's *Retrieve × Aggregate* trade-off — the Token/Sequence variants are the cleanest mono-vs-multi-source operationalisation in the literature.

## Best Figure

![Figure 1 — Overview of the RAG approach (page 2)](figures/lewis-2020-rag-knowledge-nlp-fig.png)

**Image Candidates:**
- Figure 1 (p. 2): The architecture diagram showing Query Encoder → MIPS over Document Index → Generator → Marginalize, with three example task types (QA, fact verification, Jeopardy generation) feeding the same pipeline.
- Figure 2 (p. 7): The per-token posterior heatmap showing RAG-Token switching its document focus between "A Farewell to Arms" and "The Sun Also Rises" within a single Jeopardy clue — the cleanest visualization of multi-source generation.
- Figure 3 (p. 8): Three side-by-side plots showing how NQ exact match, retrieval recall, and MS-MARCO BLEU/ROUGE-L scale with the number of retrieved documents at test time.

**Best Image:**

**Figure Name:** Figure 1: "Overview of our approach. We combine a pre-trained retriever (Query Encoder + Document Index) with a pre-trained seq2seq model (Generator) and fine-tune end-to-end."

**Figure Page:** 2

**Slide Caption:** RAG fuses a frozen non-parametric document index, a learned query encoder, and a seq2seq generator into a single end-to-end-trainable system — the canonical reference architecture every later RAG paper modifies.

**Description:** Figure 1 is the architecture diagram that defined the field. On the left, three example inputs (a question, a fact-verification claim, a Jeopardy answer entity) feed a shared **Query Encoder** that produces `q(x)`. This goes into a Maximum Inner Product Search (MIPS) over the frozen **Document Index** `d(z)` (the "Non-Parametric" memory), returning top-K passages `z_1...z_K`. The retrieved passages plus the original input are fed to the **Generator** (BART-large, the "Parametric" memory), which produces an output distribution per document and *marginalizes* across them. The dashed arrow at the top — "End-to-End Backprop through `q` and `p_θ`" — is the load-bearing piece: the diagram makes visible that the document encoder is *frozen* (no gradient arrow into it) while the query encoder and generator update jointly from the task loss. This figure encodes three architectural commitments that propagate through every memory-system paper since: (1) memory lives as raw text in an external index, not as model weights; (2) retrieval is differentiable but not labelled — `z` is a latent variable, never a supervised target; (3) parametric and non-parametric memory cooperate at inference time rather than one replacing the other.

## What Experts Overlook

The detail most experts skim past is buried in §2.4 and Appendix H: **the document encoder is frozen during training, and the authors explicitly considered un-freezing it (as REALM does) and decided not to** because the gain didn't justify the engineering complexity. This is the unsexy operational decision that makes RAG actually deployable. REALM has to periodically re-encode all 21M Wikipedia chunks every few thousand training steps because BERTd is moving, which means a custom asynchronous index-refresh worker is part of the training loop. RAG just… doesn't have that worker. The document encoder is a static checkpoint, the FAISS index is built once, and only `BERT_q` (the query side) and BART update during fine-tuning. Appendix H then makes visible the failure mode this decision quietly enables: if the query encoder learns to send everything to the same handful of documents (retrieval collapse), the generator learns to ignore the docs and RAG silently degrades to plain BART — they observed this on story generation. So the architectural elegance is: **freeze the corpus side, accept that retrieval can collapse, and monitor for it** — rather than build the complex machinery REALM uses to keep both sides in sync.

**Why it matters:** This is the difference between an architecture you can ship and one you can publish but not deploy. Most memory-system designs implicitly assume you'll be able to re-encode your corpus on every model update. RAG's bet is that you won't, and that you shouldn't have to — the query-side updates pick up the slack. Crucially, this is what lets the index be *hot-swappable*: because the document encoder is a fixed function, you can encode a 2018 Wikipedia dump with the same checkpoint that encoded a 2016 dump, and the query encoder still knows how to talk to it. If both encoders were moving, hot-swap would be a retraining run, not a file copy.

**Example of good use:** When building Flow OS's read path, freeze the embedding model for the markdown vault. Run a daily job that embeds only new/changed files (not the full corpus). When you want to upgrade the embedding model, treat it as a planned migration with a full re-embed and a query-encoder fine-tune — but do it on a quarterly cadence, not per-training-step. Add a Grafana panel that tracks the entropy of `p(z|x)` over the last 1000 queries; if it drops below a threshold, page someone. This catches retrieval collapse before users notice answers getting blander.

**Example of misapplication:** A team copies RAG's training loop but un-freezes the document encoder "because BERT-base is small, why not." Now every gradient step invalidates the FAISS index, training becomes 10× slower, and the team builds (or vibe-codes) an async index-refresh worker that is buggy in subtle ways — sometimes serving stale embeddings, sometimes serving fresh ones, with no consistency contract. The model converges to higher dev-set scores but production retrieval is non-deterministic and the team can no longer hot-swap the index without re-training. They have RAG-the-paper without RAG-the-system. Worse: they never instrument retrieval entropy because the paper doesn't emphasise it as a metric (it's only in Appendix H), so when retrieval collapse hits on a deployment, their RAG is just BART with extra latency.

## Extracted Prompts

**Prompt explanation:** Hot-swap evaluation template — used in §4.5 to probe the model with a structured "world leader" question to test whether replacing the non-parametric index updates the model's knowledge.

```
Who is {position}?
```

(e.g., "Who is the President of Peru?" — used against both the December 2016 and December 2018 Wikipedia indices to measure how index swapping changes the model's answers about 82 world leaders who changed roles between the two dates.)

_(Note: this is the only natural-language prompt template explicitly stated in the paper. RAG is fine-tuned on input-output text pairs `(x, y)` for each downstream task — questions for QA, claims for FEVER, answer entities for Jeopardy — but those inputs are passed raw to the model without any task-specific prompt wrapper. There is no system prompt, persona, or instruction template — fine-tuning replaces what prompt engineering would do.)_

## Citations

- Karpukhin et al. 2020 — *Dense Passage Retrieval for Open-Domain Question Answering* — [arXiv:2004.04906](https://arxiv.org/abs/2004.04906) — the retriever (DPR) RAG initialises from.
- Lewis et al. 2019 — *BART: Denoising sequence-to-sequence pre-training* — [arXiv:1910.13461](https://arxiv.org/abs/1910.13461) — the parametric-memory generator.
- Guu et al. 2020 — *REALM: Retrieval-Augmented Language Model Pre-training* — [arXiv:2002.08909](https://arxiv.org/abs/2002.08909) — the contemporaneous retrieval+LM hybrid that RAG positions against.
- Khandelwal et al. 2020 — *Generalization through memorization: Nearest neighbor language models (kNN-LM)* — [OpenReview](https://openreview.net/forum?id=HklBjCEKvH) — alternative non-parametric memory design (kNN over hidden states rather than documents).
- Petroni et al. 2019 — *Language models as knowledge bases?* — [aclweb](https://www.aclweb.org/anthology/D19-1250) — the motivating "parametric memory has limits" paper from the same group.
- Févry et al. 2020 — *Entities as experts: Sparse memory access with entity supervision* — [arXiv:2004.07202](https://arxiv.org/abs/2004.07202) — the entity-embedding alternative RAG explicitly contrasts against.
- Lee et al. 2019 — *Latent retrieval for weakly supervised open domain question answering (ORQA)* — [ACL 2019](https://www.aclweb.org/anthology/P19-1612) — the latent-variable retrieval precursor RAG builds on.
- Roberts et al. 2020 — *How much knowledge can you pack into the parameters of a language model? (T5+SSM closed-book QA)* — [arXiv:2002.08910](https://arxiv.org/abs/2002.08910) — the 11B parametric-only baseline RAG beats with 18× fewer params.
- Weston et al. 2015 — *Memory networks* — [arXiv:1410.3916](https://arxiv.org/abs/1410.3916) — foundational external-memory neural architecture.
- Sukhbaatar et al. 2015 — *End-to-end memory networks* — [NeurIPS 2015](http://papers.nips.cc/paper/5846-end-to-end-memory-networks.pdf) — end-to-end-trainable memory precursor.

_(Full structured citation array of 68 references in frontmatter `citations:` field — used by `/citation-walk` to seed the next-hop crawl.)_

## Related Digests

- [[adler-2026-storage-not-memory]] — *Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall* — Adler et al. 2026's "write-time intelligence is anti-intelligence" thesis is essentially a critique-and-extension of RAG: yes, retrieve raw text (RAG's bet), but also push back on LLM-distillation pipelines that compress before query time.
- [[packer-2023-memgpt-os]] — *MemGPT: Towards LLMs as Operating Systems* — Packer 2023 generalises RAG's "external memory" idea into a paged-virtual-memory OS metaphor, with the LLM itself managing what to page in. RAG is the retrieve primitive; MemGPT adds the maintain layer.
- [[chhikara-2025-mem0]] — *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory* — Mem0 inherits RAG's flat-natural-language-store design choice (vs Zep's heavy graph) and validates that the simpler shape wins on cost-per-accuracy. Direct lineage from §5's "raw text as memory" commitment.
- [[latimer-2025-hindsight-memory]] — *Hindsight is 20/20: Building Agent Memory That Retains, Recalls, and Reflects* — Latimer 2025 keeps RAG's retrieval-centred core but splits memory into four epistemic networks (world / experience / opinion / observation). Architectural descendant; RAG is the "world" network's retrieval recipe.

## Reviewer Notes

**Overall severity:** Clean

No claims in the digest deviate materially from the paper. Cross-checks performed against the source:

- **44.5 EM on Natural Questions for RAG-Sequence** — confirmed in Table 1 (p. 6), bottom row, NQ column.
- **45.2 / 52.2 for WebQuestions / CuratedTREC** — confirmed in Table 1, RAG-Sequence row.
- **7.9 EM gap vs T5+SSM (36.6 → 44.5)** — confirmed in Table 1 row "T5-11B+SSM" (36.6) vs "RAG-Seq." (44.5).
- **18× parameter ratio (11B / 626M)** — confirmed in §G Parameters: "Our RAG models contain … a total of 626M trainable parameters" vs T5-11B's 11B. 11000/626 = 17.57, rounded to 18× — accurate.
- **Hot-swap: 70% / 68% / 12% / 4%** — confirmed in §4.5 "Index hot-swapping": "RAG answers 70% correctly using the 2016 index for 2016 world leaders and 68% using the 2018 index for 2018 world leaders. Accuracy with mismatched indices is low (12% with the 2018 index and 2016 leaders, 4% with the 2016 index and 2018 leaders)."
- **Jeopardy human eval: 42.7% RAG better, 7.1% BART better** — confirmed in §4.3 and Table 4.
- **MS-MARCO: +2.6 BLEU / +2.6 ROUGE-L** — confirmed in §4.2: "RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu points and 2.6 Rouge-L points." (Table 2 numbers: BART 41.6 B-1, RAG-Seq 44.2 B-1 → +2.6; BART 38.2 R-L, RAG-Seq 40.8 R-L → +2.6.)
- **11.8% accuracy when correct answer not in any retrieved doc** — confirmed in §4.1.
- **21M Wikipedia chunks, December 2018 dump, 100 words each** — confirmed in §3 Experiments.
- **FAISS + HNSW** — confirmed in §3.
- **626M total trainable params (110M BERTq + 406M BART; BERTd 110M is frozen)** — confirmed in §G. Note the digest's body wording "~406M params (parametric memory)" refers only to BART (the generator), which is correct framing — the full 626M includes the query encoder.
- **FEVER within 4.3% of SOTA (3-way), 2.7% (2-way), no retrieval supervision** — confirmed in §4.4.
- **Gold-article retrieval: 71% top-1, 90% top-10** — confirmed in §4.4.
- **Retrieval collapse on story generation** — confirmed in Appendix H.
- **Frozen document encoder decision** — confirmed in §2.4: "We do not find this step necessary for strong performance, and keep the document encoder (and index) fixed, only fine-tuning the query encoder BERTq and the BART generator."
- **Test-time k=15 for RAG-Token open QA, k=50 for RAG-Sequence** — confirmed in Appendix A.
- **8× 32GB V100 GPUs, mixed precision, FAISS on CPU (~100GB → 36GB after compression)** — confirmed in Appendix C.
- **Two RAG variants, equivalence for length-1 sequences (classification)** — confirmed in §2.1.

The only minor stylistic note: the digest characterises BART as the "parametric memory" (RAG's term) and treats the 406M figure as that component's parameter count. This matches the paper's framing in §2.3 and §G — no overextension.
