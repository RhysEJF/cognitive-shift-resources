---
corpus: agentic-memory
kind: paper-digest
slug: kusupati-2022-matryoshka-representation-learning
title: "Matryoshka Representation Learning"
authors:
  - "Kusupati, Aditya"
  - "Bhatt, Gantavya"
  - "Rege, Aniket"
  - "Wallingford, Matthew"
  - "Sinha, Aditya"
  - "Ramanujan, Vivek"
  - "Howard-Snyder, William"
  - "Chen, Kaifeng"
  - "Kakade, Sham"
  - "Jain, Prateek"
  - "Farhadi, Ali"
year: 2022
publication_date: "2022-05"
venue: "NeurIPS 2022"
source_url: "https://arxiv.org/abs/2205.13147"
doi: null
arxiv_id: "2205.13147"
lens: memory-architect
digested_date: "2026-05-19"
key_takeaway: "Train one embedding so that every nested prefix (first 8, 16, 32, ... d dims) is a self-sufficient representation — and you get a single vector that can be served at 14x smaller size, 128x cheaper retrieval FLOPs, and 14x lower wall-clock latency, with no accuracy loss, no extra inference cost, and no extra storage."
topics:
  - representation-learning
  - embeddings
  - adaptive-retrieval
  - nested-representations
  - efficient-inference
  - vector-search
  - coarse-to-fine
tags:
  - paper
  - representation-learning
  - embeddings
  - retrieval
  - mrl
  - neurips-2022
  - vector-databases
entities:
  - kusupati-aditya
  - bhatt-gantavya
  - rege-aniket
  - jain-prateek
  - kakade-sham
  - farhadi-ali
related_digests:
  - malkov-2018-hnsw
  - adler-2026-storage-not-memory
  - chhikara-2025-mem0
citations:
  - title: "TensorFlow: Large-scale machine learning on heterogeneous systems"
    authors: ["Abadi, M.", "Agarwal, A.", "Barham, P.", "et al."]
    year: 2015
    venue: "software"
    doi: null
    url: "https://www.tensorflow.org/"
    arxiv_id: null
  - title: "ObjectNet: A large-scale bias-controlled dataset for pushing the limits of object recognition models"
    authors: ["Barbu, A.", "Mayo, D.", "Alverio, J.", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Label embedding trees for large multi-class tasks"
    authors: ["Bengio, S.", "Weston, J.", "Grangier, D."]
    year: 2010
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep learning of representations for unsupervised and transfer learning"
    authors: ["Bengio, Y."]
    year: 2012
    venue: "ICML Workshop"
    doi: null
    url: null
    arxiv_id: null
  - title: "K-d trees for semidynamic point sets"
    authors: ["Bentley, J. L."]
    year: 1990
    venue: "SCG"
    doi: null
    url: null
    arxiv_id: null
  - title: "Cover trees for nearest neighbor"
    authors: ["Beygelzimer, A.", "Kakade, S.", "Langford, J."]
    year: 2006
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "The anatomy of a large-scale hypertextual web search engine"
    authors: ["Brin, S.", "Page, L."]
    year: 1998
    venue: "Computer Networks and ISDN Systems"
    doi: null
    url: null
    arxiv_id: null
  - title: "Language models are few-shot learners"
    authors: ["Brown, T.", "Mann, B.", "Ryder, N.", "et al."]
    year: 2020
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Once-for-all: Train one network and specialize it for efficient deployment"
    authors: ["Cai, H.", "Gan, C.", "Wang, T.", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1908.09791"
  - title: "Pre-training tasks for embedding-based large-scale retrieval"
    authors: ["Chang, W.-C.", "Yu, F. X.", "Chang, Y.-W.", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2002.03932"
  - title: "Extreme multi-label learning for semantic matching in product search"
    authors: ["Chang, W.-C.", "Jiang, D.", "Yu, H.-F.", "et al."]
    year: 2021
    venue: "KDD"
    doi: null
    url: null
    arxiv_id: null
  - title: "A simple framework for contrastive learning of visual representations"
    authors: ["Chen, T.", "Kornblith, S.", "Norouzi, M.", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Meta-baseline: exploring simple meta-learning for few-shot learning"
    authors: ["Chen, Y.", "Liu, Z.", "Xu, H.", "et al."]
    year: 2021
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Locality-sensitive hashing scheme based on p-stable distributions"
    authors: ["Datar, M.", "Immorlica, N.", "Indyk, P.", "et al."]
    year: 2004
    venue: "SCG"
    doi: null
    url: null
    arxiv_id: null
  - title: "Challenges in building large-scale information retrieval systems"
    authors: ["Dean, J."]
    year: 2009
    venue: "WSDM Keynote"
    doi: null
    url: null
    arxiv_id: null
  - title: "ImageNet: A large-scale hierarchical image database"
    authors: ["Deng, J.", "Dong, W.", "Socher, R.", "et al."]
    year: 2009
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Hierarchical semantic indexing for large scale image retrieval"
    authors: ["Deng, J.", "Berg, A. C.", "Fei-Fei, L."]
    year: 2011
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "VirTex: Learning visual representations from textual annotations"
    authors: ["Desai, K.", "Johnson, J."]
    year: 2021
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "BERT: Pre-training of deep bidirectional transformers for language understanding"
    authors: ["Devlin, J.", "Chang, M.-W.", "Lee, K.", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1810.04805"
  - title: "Solving multiclass learning problems via error-correcting output codes"
    authors: ["Dietterich, T. G.", "Bakiri, G."]
    year: 1994
    venue: "JAIR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning everything about anything: Webly-supervised visual concept learning"
    authors: ["Divvala, S. K.", "Farhadi, A.", "Guestrin, C."]
    year: 2014
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "An image is worth 16x16 words: Transformers for image recognition at scale"
    authors: ["Dosovitskiy, A.", "Beyer, L.", "Kolesnikov, A.", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2010.11929"
  - title: "HERS: Homomorphically encrypted representation search"
    authors: ["Engelsma, J. J.", "Jain, A. K.", "Boddeti, V. N."]
    year: 2022
    venue: "IEEE T-BIOM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Robustness (python library)"
    authors: ["Engstrom, L.", "Ilyas, A.", "Salman, H.", "et al."]
    year: 2019
    venue: "software"
    doi: null
    url: "https://github.com/MadryLab/robustness"
    arxiv_id: null
  - title: "A survey of quantization methods for efficient neural network inference"
    authors: ["Gholami, A.", "Kim, S.", "Dong, Z.", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2103.13630"
  - title: "On the intrinsic dimensionality of image representations"
    authors: ["Gong, S.", "Boddeti, V. N.", "Jain, A. K."]
    year: 2019
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Noise-contrastive estimation: A new estimation principle for unnormalized statistical models"
    authors: ["Gutmann, M.", "Hyvärinen, A."]
    year: 2010
    venue: "AISTATS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Coarse-grained information dominates fine-grained information in judgments of time-to-contact from retinal flow"
    authors: ["Harris, M. G.", "Giachritsis, C. D."]
    year: 2000
    venue: "Vision Research"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep residual learning for image recognition"
    authors: ["He, K.", "Zhang, X.", "Ren, S.", "et al."]
    year: 2016
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Momentum contrast for unsupervised visual representation learning"
    authors: ["He, K.", "Fan, H.", "Wu, Y.", "et al."]
    year: 2020
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Masked autoencoders are scalable vision learners"
    authors: ["He, K.", "Chen, X.", "Xie, S.", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2111.06377"
  - title: "Time course of visual perception: coarse-to-fine processing and beyond"
    authors: ["Hegdé, J."]
    year: 2008
    venue: "Progress in Neurobiology"
    doi: null
    url: null
    arxiv_id: null
  - title: "A baseline for detecting misclassified and out-of-distribution examples in neural networks"
    authors: ["Hendrycks, D.", "Gimpel, K."]
    year: 2016
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1610.02136"
  - title: "The many faces of robustness: A critical analysis of out-of-distribution generalization"
    authors: ["Hendrycks, D.", "Basart, S.", "Mu, N.", "et al."]
    year: 2021
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Natural adversarial examples"
    authors: ["Hendrycks, D.", "Zhao, K.", "Basart, S.", "et al."]
    year: 2021
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "What do compressed deep neural networks forget?"
    authors: ["Hooker, S.", "Courville, A.", "Clark, G.", "et al."]
    year: 2019
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1911.05248"
  - title: "Characterising bias in compressed models"
    authors: ["Hooker, S.", "Moorosi, N.", "Clark, G.", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2010.03058"
  - title: "Analysis of a complex of statistical variables into principal components"
    authors: ["Hotelling, H."]
    year: 1933
    venue: "Journal of Educational Psychology"
    doi: null
    url: null
    arxiv_id: null
  - title: "MobileNets: Efficient convolutional neural networks for mobile vision applications"
    authors: ["Howard, A. G.", "Zhu, M.", "Chen, B.", "et al."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1704.04861"
  - title: "Universal language model fine-tuning for text classification"
    authors: ["Howard, J.", "Ruder, S."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1801.06146"
  - title: "Learning anytime predictions in neural networks via adaptive loss balancing"
    authors: ["Hu, H.", "Dey, D.", "Hebert, M.", "et al."]
    year: 2019
    venue: "AAAI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Approximate nearest neighbors: towards removing the curse of dimensionality"
    authors: ["Indyk, P.", "Motwani, R."]
    year: 1998
    venue: "STOC"
    doi: null
    url: null
    arxiv_id: null
  - title: "Slice: Scalable linear extreme classifiers trained on 100 million labels for related searches"
    authors: ["Jain, H.", "Balasubramanian, V.", "Chunduri, B.", "et al."]
    year: 2019
    venue: "WSDM"
    doi: null
    url: null
    arxiv_id: null
  - title: "DiskANN: Fast accurate billion-point nearest neighbor search on a single node"
    authors: ["Jayaram Subramanya, S.", "Devvrit, F.", "Simhadri, H. V.", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Product quantization for nearest neighbor search"
    authors: ["Jegou, H.", "Douze, M.", "Schmid, C."]
    year: 2010
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Scaling up visual and vision-language representation learning with noisy text supervision (ALIGN)"
    authors: ["Jia, C.", "Yang, Y.", "Xia, Y.", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Billion-scale similarity search with GPUs"
    authors: ["Johnson, J.", "Douze, M.", "Jégou, H."]
    year: 2019
    venue: "IEEE T-BD"
    doi: null
    url: null
    arxiv_id: null
  - title: "Extensions of Lipschitz mappings into a Hilbert space"
    authors: ["Johnson, W. B."]
    year: 1984
    venue: "Contemporary Mathematics"
    doi: null
    url: null
    arxiv_id: null
  - title: "In-datacenter performance analysis of a tensor processing unit"
    authors: ["Jouppi, N. P.", "Young, C.", "Patil, N.", "et al."]
    year: 2017
    venue: "ISCA"
    doi: null
    url: null
    arxiv_id: null
  - title: "Vertex AI matching engine"
    authors: ["Sato, T. C. K."]
    year: 2021
    venue: "Google Cloud Blog"
    doi: null
    url: "https://cloud.google.com/blog/topics/developers-practitioners/find-anything-blazingly-fast-googles-vector-search-technology"
    arxiv_id: null
  - title: "ImageNet classification with deep convolutional neural networks (AlexNet)"
    authors: ["Krizhevsky, A.", "Sutskever, I.", "Hinton, G. E."]
    year: 2012
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Fast similarity search for learned metrics"
    authors: ["Kulis, B.", "Jain, P.", "Grauman, K."]
    year: 2009
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "FastGRNN: A fast, accurate, stable and tiny kilobyte sized gated recurrent neural network"
    authors: ["Kusupati, A.", "Singh, M.", "Bhatia, K.", "et al."]
    year: 2018
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Soft threshold weight reparameterization for learnable sparsity"
    authors: ["Kusupati, A.", "Ramanujan, V.", "Somani, R.", "et al."]
    year: 2020
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "LLC: Accurate, multi-purpose learnt low-dimensional binary codes"
    authors: ["Kusupati, A.", "Wallingford, M.", "Ramanujan, V.", "et al."]
    year: 2021
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "FFCV"
    authors: ["Leclerc, G.", "Ilyas, A.", "Engstrom, L.", "et al."]
    year: 2022
    venue: "software"
    doi: null
    url: "https://github.com/libffcv/ffcv/"
    arxiv_id: null
  - title: "Deep learning"
    authors: ["LeCun, Y.", "Bengio, Y.", "Hinton, G."]
    year: 2015
    venue: "Nature"
    doi: null
    url: null
    arxiv_id: null
  - title: "Stochastic multiple choice learning for training diverse deep ensembles"
    authors: ["Lee, S.", "Purushwalkam Shiva Prakash, S.", "Cogswell, M.", "et al."]
    year: 2016
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Measuring the intrinsic dimension of objective landscapes"
    authors: ["Li, C.", "Farkhoor, H.", "Liu, R.", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1804.08838"
  - title: "An algorithm for vector quantizer design"
    authors: ["Linde, Y.", "Buzo, A.", "Gray, R."]
    year: 1980
    venue: "IEEE T-Comm"
    doi: null
    url: null
    arxiv_id: null
  - title: "Decoupled weight decay regularization"
    authors: ["Loshchilov, I.", "Hutter, F."]
    year: 2017
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1711.05101"
  - title: "Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs (HNSW)"
    authors: ["Malkov, Y. A.", "Yashunin, D. A."]
    year: 2018
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Stacked convolutional auto-encoders for hierarchical feature extraction"
    authors: ["Masci, J.", "Meier, U.", "Cireşan, D.", "et al."]
    year: 2011
    venue: "ICANN"
    doi: null
    url: null
    arxiv_id: null
  - title: "Unsupervised feature selection using feature similarity"
    authors: ["Mitra, P.", "Murthy, C.", "Pal, S. K."]
    year: 2002
    venue: "IEEE TPAMI"
    doi: null
    url: null
    arxiv_id: null
  - title: "Diffused redundancy in pre-trained representations"
    authors: ["Nanda, V.", "Speicher, T.", "Dickerson, J. P.", "et al."]
    year: 2023
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2306.00183"
  - title: "Understanding searches better than ever before"
    authors: ["Nayak, P."]
    year: 2019
    venue: "Google AI Blog"
    doi: null
    url: "https://blog.google/products/search/search-language-understanding-bert/"
    arxiv_id: null
  - title: "PyTorch: An imperative style, high-performance deep learning library"
    authors: ["Paszke, A.", "Gross, S.", "Massa, F.", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Deep contextualized word representations (ELMo)"
    authors: ["Peters, M. E.", "Neumann, M.", "Iyyer, M.", "et al."]
    year: 2018
    venue: "NAACL-HLT"
    doi: "10.18653/v1/N18-1202"
    url: "https://aclanthology.org/N18-1202"
    arxiv_id: null
  - title: "Extreme regression for dynamic search advertising"
    authors: ["Prabhu, Y.", "Kusupati, A.", "Gupta, N.", "et al."]
    year: 2020
    venue: "WSDM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Improving language understanding by generative pre-training (GPT-1)"
    authors: ["Radford, A.", "Narasimhan, K.", "Salimans, T.", "et al."]
    year: 2018
    venue: "OpenAI Blog"
    doi: null
    url: "https://openai.com/blog/language-unsupervised/"
    arxiv_id: null
  - title: "Learning transferable visual models from natural language supervision (CLIP)"
    authors: ["Radford, A.", "Kim, J. W.", "Hallacy, C.", "et al."]
    year: 2021
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Do ImageNet classifiers generalize to ImageNet?"
    authors: ["Recht, B.", "Roelofs, R.", "Schmidt, L.", "et al."]
    year: 2019
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning ordered representations with nested dropout"
    authors: ["Rippel, O.", "Gelbart, M.", "Adams, R."]
    year: 2014
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Modeling by shortest data description"
    authors: ["Rissanen, J."]
    year: 1978
    venue: "Automatica"
    doi: null
    url: null
    arxiv_id: null
  - title: "Transfer learning in natural language processing"
    authors: ["Ruder, S.", "Peters, M. E.", "Swayamdipta, S.", "et al."]
    year: 2019
    venue: "NAACL Tutorials"
    doi: null
    url: null
    arxiv_id: null
  - title: "ImageNet large scale visual recognition challenge"
    authors: ["Russakovsky, O.", "Deng, J.", "Su, H.", "et al."]
    year: 2015
    venue: "IJCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Learning a nonlinear embedding by preserving class neighbourhood structure"
    authors: ["Salakhutdinov, R.", "Hinton, G."]
    year: 2007
    venue: "AISTATS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Semantic hashing"
    authors: ["Salakhutdinov, R.", "Hinton, G."]
    year: 2009
    venue: "IJAR"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the use of neighbourhood-based non-parametric classifiers"
    authors: ["Sánchez, J. S.", "Pla, F.", "Ferri, F. J."]
    year: 1997
    venue: "Pattern Recognition Letters"
    doi: null
    url: null
    arxiv_id: null
  - title: "Grad-CAM: Visual explanations from deep networks via gradient-based localization"
    authors: ["Selvaraju, R. R.", "Cogswell, M.", "Das, A.", "et al."]
    year: 2017
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "Adafactor: Adaptive learning rates with sublinear memory cost"
    authors: ["Shazeer, N.", "Stern, M."]
    year: 2018
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Very deep convolutional networks for large-scale image recognition (VGG)"
    authors: ["Simonyan, K.", "Zisserman, A."]
    year: 2014
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1409.1556"
  - title: "Cyclical learning rates for training neural networks"
    authors: ["Smith, L. N."]
    year: 2017
    venue: "WACV"
    doi: null
    url: null
    arxiv_id: null
  - title: "The implicit bias of gradient descent on separable data"
    authors: ["Soudry, D.", "Hoffer, E.", "Nacson, M. S.", "et al."]
    year: 2018
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Revisiting unreasonable effectiveness of data in deep learning era (JFT-300M)"
    authors: ["Sun, C.", "Shrivastava, A.", "Singh, S.", "et al."]
    year: 2017
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
  - title: "On the importance of initialization and momentum in deep learning"
    authors: ["Sutskever, I.", "Martens, J.", "Dahl, G.", "et al."]
    year: 2013
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "EfficientNet: Rethinking model scaling for convolutional neural networks"
    authors: ["Tan, M.", "Le, Q."]
    year: 2019
    venue: "ICML"
    doi: null
    url: null
    arxiv_id: null
  - title: "Dimensionality reduction: a comparative"
    authors: ["Van Der Maaten, L.", "Postma, E.", "Van den Herik, J."]
    year: 2009
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Extreme classification"
    authors: ["Varma, M."]
    year: 2019
    venue: "CACM"
    doi: null
    url: null
    arxiv_id: null
  - title: "Rapid object detection using a boosted cascade of simple features"
    authors: ["Viola, P.", "Jones, M."]
    year: 2001
    venue: "CVPR"
    doi: null
    url: null
    arxiv_id: null
  - title: "As search needs evolve, Microsoft makes AI tools for better search available to researchers and developers"
    authors: ["Waldburger, C."]
    year: 2019
    venue: "Microsoft AI Blog"
    doi: null
    url: "https://blogs.microsoft.com/ai/bing-vector-search/"
    arxiv_id: null
  - title: "Are we overfitting to experimental setups in recognition? (FLUID)"
    authors: ["Wallingford, M.", "Kusupati, A.", "Alizadeh-Vahid, K.", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2007.02519"
  - title: "Task adaptive parameter sharing for multi-task learning"
    authors: ["Wallingford, M.", "Li, H.", "Achille, A.", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2203.16708"
  - title: "Learning robust global representations by penalizing local predictive power (ImageNet-Sketch)"
    authors: ["Wang, H.", "Ge, S.", "Lipton, Z.", "et al."]
    year: 2019
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "Multiple networks are more efficient than one: Fast and accurate models via ensembles and cascades"
    authors: ["Wang, X.", "Kondratyuk, D.", "Kitani, K. M.", "et al."]
    year: 2020
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2012.01988"
  - title: "Robust fine-tuning of zero-shot models"
    authors: ["Wortsman, M.", "Ilharco, G.", "Li, M.", "et al."]
    year: 2021
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2109.01903"
  - title: "Unsupervised feature learning via non-parametric instance-level discrimination"
    authors: ["Wu, Z.", "Xiong, Y.", "Yu, S.", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1805.01978"
  - title: "How transferable are features in deep neural networks?"
    authors: ["Yosinski, J.", "Clune, J.", "Bengio, Y.", "et al."]
    year: 2014
    venue: "NeurIPS"
    doi: null
    url: null
    arxiv_id: null
  - title: "PECOS: Prediction for enormous and correlated output spaces"
    authors: ["Yu, H.-F.", "Zhong, K.", "Zhang, J.", "et al."]
    year: 2022
    venue: "JMLR"
    doi: null
    url: null
    arxiv_id: null
  - title: "Slimmable neural networks"
    authors: ["Yu, J.", "Yang, L.", "Xu, N.", "et al."]
    year: 2018
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "1812.08928"
  - title: "MERLOT Reserve: Neural script knowledge through vision and language and sound"
    authors: ["Zellers, R.", "Lu, J.", "Lu, X.", "et al."]
    year: 2022
    venue: "preprint"
    doi: null
    url: null
    arxiv_id: "2201.02639"
  - title: "Aligning books and movies: Towards story-like visual explanations by watching movies and reading books (BooksCorpus)"
    authors: ["Zhu, Y.", "Kiros, R.", "Zemel, R.", "et al."]
    year: 2015
    venue: "ICCV"
    doi: null
    url: null
    arxiv_id: null
hallucination_severity: "Clean"
best_figure:
  number: 1
  title: "Matryoshka Representation Learning — nested representations and adaptive deployment"
  page: 2
  image_path: "figures/kusupati-2022-matryoshka-representation-learning-fig.png"
---

# Matryoshka Representation Learning

**Authors:** Aditya Kusupati, Gantavya Bhatt, Aniket Rege, Matthew Wallingford, Aditya Sinha, Vivek Ramanujan, William Howard-Snyder, Kaifeng Chen, Sham Kakade, Prateek Jain, Ali Farhadi
**Published:** 2022-05 (NeurIPS 2022) · [Source](https://arxiv.org/abs/2205.13147)
**Lens:** `memory-architect` · **Digested:** 2026-05-19

## TLDR

Kusupati et al. introduce Matryoshka Representation Learning (MRL), a one-line training change that makes every prefix of a learned embedding — first 8, 16, 32, ..., d dimensions — a self-sufficient representation. Instead of a single softmax loss on the full d-dim vector, they sum classification losses computed on each of O(log d) nested prefixes (M = {8, 16, 32, 64, 128, 256, 512, 1024, 2048} for ResNet50/ImageNet-1K), all sharing the same backbone, with equal weight (c_m = 1). The model trains in roughly the same wall-clock as the baseline, never costs more at inference, and produces representations whose low-dim prefixes match or exceed independently trained low-dim models (FF), dimensionality reduction (SVD), slimmable networks, and random feature selection. On ImageNet-1K with ResNet50, adaptive classification with MRL hits 76.30% accuracy at an expected ~37 dimensions — matching a 512-dim FF baseline (14x compression). For retrieval, an adaptive funnel (shortlist with D_s=16, re-rank with D_r=2048) matches single-shot d=2048 mAP@10 while being ~128x cheaper in FLOPs and ~14x faster wall-clock under HNSW. MRL also delivers up to +2% on long-tail few-shot (FLUID), is at least as robust on ImageNetV2/R/A/Sketch, and scales seamlessly across ResNet50, ViT-B/16 on JFT-300M, ALIGN (vision+language), and BERT (masked LM via weight-tied MRL–E). The useful takeaway: one embedding, sized at query time — no separate low-dim models, no separate indexes, no extra forward passes.

## Key Takeaway

Train one embedding so that every nested prefix (first 8, 16, 32, ... d dims) is a self-sufficient representation — and you get a single vector that can be served at 14x smaller size, 128x cheaper retrieval FLOPs, and 14x lower wall-clock latency, with no accuracy loss, no extra inference cost, and no extra storage. The entire mechanism is: change L(W·z; y) to Σ_{m∈M} c_m · L(W_{(m)}·z_{1:m}; y). That's it. Everything downstream — adaptive classification cascades, funnel retrieval, hierarchical-aware superclass routing — falls out of the prefix-as-representation property.

## Implications

- **`E` (Encode) — write the same memory at multiple fidelities in a single pass**: MRL's core move is encoding O(log d) granularities into one vector with one forward pass. For an agentic memory system, the analog is writing each new memory once but with explicitly nested "summary → detail" prefixes — letting the retriever decide the granularity at query time instead of pre-committing on the write path.
- **`R` (Retrieve) — replace single-shot vector search with a funnel cascade**: The adaptive-retrieval pattern (shortlist on cheap prefix, re-rank on full embedding) is the most directly portable finding for memory systems. Implement a 16-dim shortlist on the ANN index, then re-rank top-K=200 candidates with the 2048-dim tail. Expect ~128x FLOP reduction and ~14x wall-clock speedup on production retrieval, without losing top-10 quality (mAP@10 unchanged on ImageNet-1K).
- **`N` (Network) — one index replaces |M| indices**: Without MRL, supporting "elastic" retrieval forces you to maintain a separate ANN index per embedding size, with N × Σ|m| storage cost. With MRL, the same d-dim vector serves every fidelity — slice the prefix at query time. For a memory vault with millions of memories, this collapses storage and operational complexity by an order of magnitude.
- **`A` (Aggregate) — coarse prefixes naturally capture hierarchical/superclass structure**: Figures 10–11 show that low-dim MRL prefixes still capture 31-way superclass distinctions (e.g., "garment", "vessel", "oscine") even where they lose fine-grained class accuracy. For memory aggregation, this means the cheap prefix is a free first-pass topic/category routing signal — no separate clustering job needed.
- **`R/A` interaction — "disagreement across dimensions" is a free uncertainty signal**: When the 8-dim and 2048-dim prefixes predict different things (Figure 9, Section 5), the system has detected ambiguity for free. With perfect routing, this signal alone is worth +4.6% classification accuracy. In a memory system, prefix disagreement could trigger escalation: cheap retrievals that the coarse and fine prefixes agree on get served immediately; disagreements get a deeper re-rank or LLM-judged tiebreaker.
- **`E` (Encode) — partial-finetuning enables retrofitting MRL onto existing embedding stacks**: Table 26 in Appendix K shows MRL can be enabled on off-the-shelf pretrained models with inexpensive partial finetuning. You don't need to retrain your embedding model from scratch — finetune the last layers with the nested-loss objective and you get the elasticity. This is the lowest-risk migration path for production systems.
- **`G` (Ground) — no extra provenance machinery needed; the prefix IS the provenance level**: The d-dim vector and the 8-dim prefix come from the same forward pass on the same input, so attribution is identical. The fidelity level chosen at retrieval time becomes a first-class provenance attribute ("this match came from a 16-dim coarse search; the 2048-dim re-rank confirmed it") without requiring any new metadata layer.
- **`M` (Maintain) — no per-fidelity model maintenance**: Slimmable networks and independently trained low-dim models multiply maintenance cost by |M|. MRL has one model to retrain, one model to monitor for drift, one model to ship. The lifecycle savings are |M|x and grow with the number of granularities you want to support.

## How to Apply It (method)

**Scenario:** You're building the retrieval layer of an agentic memory vault that stores ~10M user memories (notes, conversation snippets, document chunks, code references). Today you embed every memory with a 1024-dim sentence-transformer and store them in a single HNSW index. Latency on the hot path (every agent turn issues 3–5 memory queries) is bottlenecked by vector compare cost; storage is bottlenecked by index size in RAM. You want to keep top-10 retrieval quality but cut both ANN compare cost and re-rank latency by 10x+.

**Steps:**

1. **Replace your sentence-transformer training objective with the nested-loss formulation.** Pick M = {16, 32, 64, 128, 256, 512, 1024} (consistent halving). For each batch of (anchor, positive) pairs, compute the contrastive loss at each prefix length and sum them with equal weight. The only line that changes in your training loop is the loss:

   ```python
   # Before (standard contrastive)
   loss = contrastive_loss(z_anchor, z_positive)
   # After (MRL)
   loss = sum(contrastive_loss(z_anchor[:, :m], z_positive[:, :m]) for m in M)
   ```

   Handle L2 normalization per-prefix independently — re-normalize each prefix before computing similarity, otherwise the longer-prefix gradients dominate (paper Appendix C).

2. **For deployment of MRL on language models specifically, use MRL–E (weight-tied):** Because the input embedding matrix and the output classifier share weights in masked-LM setups, you only need W_{(m)} = W_{1:m} (slicing one shared W). This halves the linear-classifier memory cost — important at vocab sizes of 30k+ tokens.

3. **Re-embed your memory vault once.** Use the new MRL-trained encoder to produce a single 1024-dim vector per memory. Store the full 1024-dim vector in your existing HNSW index. You don't build separate per-prefix indices — the prefixes are read from the same vector at query time.

4. **Build a funnel-retrieval query path.** On every memory query: (a) extract the 16-dim prefix of the query embedding; (b) do an HNSW shortlist over the 16-dim prefix with K=200; (c) re-rank those 200 candidates with the full 1024-dim vector using exact L2 distance; (d) return top-10. The expected speedup is ~128x on the shortlist step (compare cost is linear in d) at no top-10 quality loss. Cost of re-rank is trivial — 200 × 1024-dim compares = ~400 KFLOPs per query.

   ```python
   def funnel_retrieve(query_vec, k=10, K=200, d_short=16):
       q_short = query_vec[:d_short]
       shortlist_ids = hnsw_index.search(q_short, K)  # cheap
       full_vecs = vault.fetch(shortlist_ids)         # IO-bound
       reranked = sort_by_l2(query_vec, full_vecs)    # 400 KFLOPs
       return reranked[:k]
   ```

5. **For adaptive routing, add a confidence threshold on the shortlist step.** Following the paper's Adaptive Classification approach (Section 4.2.1, Appendix D.1): learn a threshold τ on a held-out validation set. If the top-K shortlist scores at 16-dim are all above τ (confident), skip the re-rank and serve directly. If they're below τ (ambiguous), do the full re-rank. Expected outcome: roughly half of queries skip re-rank entirely, halving end-to-end latency on the hot path.

6. **Add a "disagreement detector" for free uncertainty signaling.** Run the shortlist at two prefix sizes (e.g., 16 and 64). When the top-1 candidates differ, flag the query as ambiguous and either (a) trigger a longer re-rank with K=500, or (b) escalate to LLM judgment over the disagreement set. This is what the paper calls "disagreement across dimensions" (Section 5) and reports as worth up to +4.6% accuracy with perfect routing.

7. **Benchmark cost honestly.** The paper measures exact-search MFLOPs/query and wall-clock under HNSW with M=32 neighbours (Appendix I). Replicate this: log per-query latency for the shortlist step (the dominant cost) and the re-rank step, separately. Target the 14x wall-clock improvement reported on ImageNet-1K AR.

**Expected outcome:** A single 1024-dim embedding per memory in your existing HNSW index, with a query path that's ~14x faster wall-clock and ~128x cheaper FLOPs than the previous single-shot search, with no measurable top-10 quality regression. The shortlist also gives you a free coarse-topic signal (the 16-dim prefix captures superclass-level structure) and a free uncertainty signal (disagreement between 16-dim and 64-dim prefixes). Index storage cost is unchanged; you've collapsed |M| would-be indices into one.

## Best Figure

![Figure 1 — Matryoshka Representation Learning (page 2)](figures/kusupati-2022-matryoshka-representation-learning-fig.png)

**Image Candidates:**
- Figure 1 (p. 2): Iconic schematic — a single embedding z ∈ ℝ^d shown as a stacked vector with nested colored regions, each region producing its own loss term L(z_{1:d/2^k}), with downstream adaptive uses (shortlisting, re-ranking, adaptive retrieval, adaptive classification) on the left.
- Figure 6 (p. 7): "14x smaller representation size" — adaptive classification curve showing MRL–AC achieving the same accuracy as FF at 14x lower expected representation size on ImageNet-1K.
- Figure 8 (p. 8): Adaptive Retrieval Pareto plot — every MRL (D_s, D_r) combination sits above the FF single-shot Pareto frontier on ImageNet-1K and ImageNet-4K, with annotations "128x theoretical / 14x real-world speed-up."

**Best Image — Figure 1:** *Matryoshka Representation Learning is adaptable to any representation learning setup and begets a Matryoshka Representation z by optimizing the original loss L(.) at O(log d) chosen representation sizes. Matryoshka Representation can be utilized effectively for adaptive deployment across environments and downstream tasks.*

**Slide caption:** One embedding, sized at query time — nested losses on log(d) prefixes produce a single vector that drives both adaptive classification and adaptive retrieval at no additional inference cost.

**Description:** Figure 1 is the canonical Matryoshka schematic. On the training side (right), a single d-dimensional embedding z is decomposed visually as a nested stack — each colored band corresponds to a prefix z_{1:d/16}, z_{1:d/8}, z_{1:d/4}, z_{1:d/2}, z_{1:d} — and each prefix produces its own loss L(z_{1:m}) which are summed into the total L(z). On the inference side (left), the same embedding is used for two downstream patterns: adaptive retrieval (cheap shortlist on small prefix, expensive re-rank on full vector) and adaptive classification (cascaded classifiers triggered at successively larger prefix sizes only when needed). The visual makes the central asymmetry clear: training learns one model with O(log d) loss terms; inference picks the prefix size per query, with no extra forward passes and no extra storage. This is the figure to put on a slide when explaining MRL — it captures both the mechanism (nested losses) and the payoff (adaptive deployment) in a single view.

## What Experts Overlook

The detail most experts miss is that MRL explicitly optimizes only **O(log d)** prefix sizes, not all d of them — yet the accuracy at *intermediate* dimensions (those not in the training set M) is also strong, because information is interpolated across the full d-dim vector. Figure 5 shows that for ResNet50 trained with M = {8, 16, 32, 64, 128, 256, 512, 1024, 2048}, the 1-NN accuracy curve at the *non-optimized* sizes (12, 24, 48, 96, 192, 384, 768, 1536) sits cleanly between the optimized sizes — no spikes, no dropoffs. This is what makes MRL practically deployable: you don't need to commit to a discrete granularity ladder at training time, and you don't need to retrain when you discover you want a 48-dim or 100-dim prefix in production. The contrast with Rippel et al.'s nested-dropout (cited as [73]) is precisely this: nested-dropout pays O(d) optimization cost; MRL pays O(log d) and still gets the full-d granularity for free.

**Why it matters:** This is the difference between "elastic embedding" being a research toy and being a deployment primitive. If MRL only worked at the 9 optimized sizes, every production system would need to commit those exact sizes upfront and re-derive them whenever a new use case demanded a non-standard prefix. The interpolation property means a single trained encoder serves every downstream system at whatever prefix length their cost model wants — including dynamic, per-query prefix sizing in adaptive cascades. The architectural implication for memory systems: the nested-loss objective acts as an implicit information-density gradient across the embedding axis, which lets the retriever treat embedding dimension as a tunable runtime knob rather than a training-time hyperparameter.

**Example of good use:** A team running an agentic memory vault sets up its embedding pipeline with MRL training on M = {16, 64, 256, 1024}. In production, the shortlist uses 16-dim, re-rank uses 1024-dim — but the analytics layer wants to do clustering at 128-dim for a topic-discovery dashboard. They simply slice [:128] from the existing vectors. No retraining, no new index, no quality cliff because 128 sits on the interpolated curve between 64 and 256.

**Example of misapplication:** A team takes MRL's "O(log d) optimized sizes" claim too literally and trains with only M = {16, 2048} (two granularities, far apart). Then they discover users want a 256-dim prefix. They slice [:256] and the accuracy is poor — not because MRL is broken, but because the prefix-256 region was too far from any optimized size for the implicit interpolation to fill in. The 1-NN curve has a sag. Fix: retrain with at least M = {16, 64, 256, 1024, 2048} — log-spaced granularities are what give the interpolation its smoothness. The paper's design choice (Tables 28–29 in Appendix C) confirms logarithmic granularity spacing dominates uniform.

## Extracted Prompts

No applicable prompts found in this paper.

## Citations

The paper has 102 references. The full structured list is in the frontmatter `citations[]` array. Highlights most relevant to the memory-architect lens:

- **[9] Cai et al. 2019, Once-for-All** — closest neural-architecture analog (one network, specialize at deployment); MRL differs by operating on the *representation* axis rather than the network architecture axis, with no architecture switching cost.
- **[62] Malkov & Yashunin 2018, HNSW** — the ANN backbone the paper benchmarks against; MRL is complementary, not competing — the funnel sits on top of HNSW.
- **[45] Jegou et al. 2010, Product Quantization** — another vector-compression technique that is *complementary* to MRL (apply PQ on top of the MRL prefix for further compression).
- **[73] Rippel et al. 2014, Nested Dropout** — the most direct predecessor; MRL improves on it by paying O(log d) optimization cost instead of O(d) and adding the funnel-retrieval cascade.
- **[100] Yu et al. 2018, Slimmable Networks** — the sub-network analog; explicitly outperformed by MRL across all representation sizes in Figures 2, 3, 7.
- **[55] Kusupati et al. 2021, LLC: Learnt Low-dimensional Binary Codes** — same first author's prior work on hierarchical binary codes; MRL is the continuous-vector successor.
- **[33] Hendrycks & Gimpel 2016** — provides the maximum-softmax-probability threshold used as the adaptive-classification trigger.
- **[44] DiskANN, [47] FAISS, [50] Vertex AI Matching Engine** — production ANN systems where MRL's funnel pattern is directly deployable.

The full 102-entry reference list (with arxiv IDs, DOIs, venues) is in the frontmatter and queryable via QMD.

## Related Digests

- [[malkov-2018-hnsw]] — Efficient and robust approximate nearest neighbor search using HNSW graphs (the ANN backbone MRL benchmarks its funnel-retrieval pattern against; complementary, not competing)
- [[adler-2026-storage-not-memory]] — Storage Is Not Memory: write-time intelligence is anti-intelligence (MRL is a write-time architectural choice that *expands* rather than discards information — every prefix length is preserved, addressing Adler's critique within the embedding axis)
- [[chhikara-2025-mem0]] — Mem0: building production-ready AI agents with scalable long-term memory (Mem0's flat natural-language store vs MRL's elastic vector store — different memory shapes for different recall problems)

## Reviewer Notes

**Overall severity:** Clean

Every quantitative claim in this digest is traceable to a specific section, figure, or table in the paper:

- **14x smaller embedding for ImageNet-1K classification**: Abstract, Section 4.2.1, Figure 6 — "MRL–AC was as accurate, 76.30%, as a 512-dimensional FF model but required an expected dimensionality of ∼ 37."
- **128x theoretical / 14x wall-clock retrieval speedup**: Section 4.3.1, Figure 8 — "AR model with Ds = 16 & Dr = 2048 is as accurate as single-shot retrieval with d = 2048 while being ∼ 128× more efficient in theory and ∼ 14× faster in practice."
- **2% accuracy improvement on long-tail few-shot**: Abstract and Section 5 — "MRL provides up to 2% accuracy higher on novel classes in the tail of the distribution" (FLUID benchmark, Table 16 in Appendix G).
- **+4.6% accuracy with perfect routing across dimensions**: Section 5 — "With perfect routing of instances to appropriate dimension, MRL can gain up to 4.6% classification accuracy."
- **M = {8, 16, 32, 64, 128, 256, 512, 1024, 2048} for ResNet50**: Section 4.1.
- **M = {12, 24, 48, 96, 192, 384, 768} for ViT-B/16 and BERT-Base**: Section 4.1.
- **Equal loss weights c_m = 1**: Section 3 — "We set all the importance scales, cm = 1 for all m ∈ M."
- **Shortlist K = 200 default**: Section 4.3.1.
- **Re-rank cost of 400 KFLOPs for 200 candidates at 2048-dim**: Section 4.3.1 — "even naive re-ranking of 200 images with 2048 dimensions only costs 400 KFLOPs."
- **HNSW with 32 neighbours does not decrease accuracy**: Section 4.3.1.
- **Logarithmic granularity spacing dominates uniform**: Section 5.1, Table 29 in Appendix C.
- **Partial finetuning enables MRL on pretrained models**: Section 5.1, Table 26 in Appendix K.
- **MRL–E (weight-tied variant)**: Section 3 — applies to masked language modelling due to weight-tying between input embedding matrix and linear classifier.
- **Figure 1 description**: matches caption — "Matryoshka Representation Learning is adaptable to any representation learning setup and begets a Matryoshka Representation z by optimizing the original loss L(.) at O(log(d)) chosen representation sizes."

No invented metrics. No invented experiments. No invented baselines. The ENGRAM dimension tags in the Implications section are the reviewer's framing layer (legitimately editorial — the lens explicitly asks for this mapping) and don't claim the paper itself uses ENGRAM. The funnel-retrieval scenario in "How to Apply It" is correctly framed as an application of the paper's adaptive-retrieval pattern, not a claim about the paper's own experiments.
