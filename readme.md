# 🚀 AI/ML/LLM Developer — Complete Learning Journey

> A hands-on journey from **Python fundamentals to Machine Learning, Deep Learning, Transformers, LLMs, Fine-Tuning, RAG, AI Agents, and Production AI systems.**

This repository documents my complete preparation and practical journey toward becoming an **AI/ML/LLM Model Developer**.

The goal is not just to learn concepts.

The goal is to:

* Understand the fundamentals
* Write the code myself
* Build projects
* Implement models
* Understand how LLMs work internally
* Fine-tune open-source models
* Build RAG systems
* Evaluate AI systems
* Deploy production-ready AI applications
* Prepare for real-world AI/ML/LLM engineering interviews

---

# 🎯 Learning Goal

The final goal of this repository is to progress through:

```text
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Mathematics
   ↓
Machine Learning
   ↓
PyTorch
   ↓
Deep Learning
   ↓
NLP
   ↓
Tokenization
   ↓
Embeddings
   ↓
Transformers
   ↓
LLM Architecture
   ↓
Pretraining
   ↓
Fine-Tuning
   ↓
LoRA / QLoRA
   ↓
RAG
   ↓
LLM Evaluation
   ↓
AI Agents
   ↓
Model Serving
   ↓
MLOps
   ↓
Production AI
```

---

# 📚 Complete Curriculum

## Part 1 — Python for AI/ML

### Chapter 1 — Python Fundamentals

Topics:

* Variables
* Data types
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* Loops
* List comprehensions
* Functions
* `*args`
* `**kwargs`
* Lambda functions
* Exceptions
* Modules
* Packages
* Decorators
* Generators
* Iterators
* Context managers

### Chapter 2 — Python for Data

Topics:

* NumPy
* Pandas
* Data cleaning
* Data transformation
* Vectorization
* Data preprocessing
* Feature engineering

---

# 🧮 Part 2 — Mathematics for Machine Learning

### Chapter 3 — Linear Algebra

* Scalars
* Vectors
* Matrices
* Tensors
* Dimensions
* Dot products
* Matrix multiplication
* Transpose
* Norms
* Cosine similarity
* Eigenvalues
* Eigenvectors

### Chapter 4 — Probability

* Probability
* Conditional probability
* Bayes theorem
* Random variables
* Distributions
* Expectation
* Variance
* Standard deviation
* Likelihood

### Chapter 5 — Calculus

* Derivatives
* Partial derivatives
* Gradients
* Chain rule
* Gradient descent

---

# 🤖 Part 3 — Machine Learning

### Chapter 6 — ML Fundamentals

* Supervised learning
* Unsupervised learning
* Reinforcement learning
* Training data
* Validation data
* Test data
* Features
* Labels
* Parameters
* Hyperparameters
* Training vs inference

### Chapter 7 — Regression

* Linear regression
* Polynomial regression
* Logistic regression

### Chapter 8 — Classification

* Binary classification
* Multiclass classification
* Multilabel classification
* Decision trees
* Random forests
* XGBoost
* SVM
* k-NN

### Chapter 9 — ML Evaluation

* Accuracy
* Precision
* Recall
* F1 score
* Confusion matrix
* ROC-AUC
* MAE
* MSE
* RMSE
* R²

### Chapter 10 — Overfitting

* Bias
* Variance
* Underfitting
* Overfitting
* L1 regularization
* L2 regularization
* Cross-validation
* Early stopping

---

# 🧠 Part 4 — Neural Networks

### Chapter 11 — Neural Network Fundamentals

* Neurons
* Weights
* Bias
* Forward propagation
* Backpropagation
* Loss
* Gradient descent

### Chapter 12 — Activation Functions

* ReLU
* Sigmoid
* Tanh
* Softmax

### Chapter 13 — Loss Functions

* MSE
* MAE
* Binary cross entropy
* Cross entropy
* Negative log likelihood

---

# 🔥 Part 5 — PyTorch

### Chapter 14 — PyTorch Basics

* Tensors
* Shapes
* Dtypes
* CPU
* GPU
* Indexing
* Broadcasting
* Autograd

### Chapter 15 — Neural Networks with PyTorch

* `nn.Module`
* `nn.Linear`
* `nn.ReLU`
* `nn.Dropout`
* `nn.Embedding`
* `nn.LayerNorm`

### Chapter 16 — Training

* Training loops
* Forward pass
* Loss calculation
* Backpropagation
* Optimizers
* Validation
* Checkpoints

### Chapter 17 — Optimizers

* SGD
* Momentum
* Adam
* AdamW
* Learning-rate scheduling

### Chapter 18 — Dataset & DataLoader

* Dataset
* DataLoader
* Batch size
* Shuffle
* `collate_fn`

---

# 📝 Part 6 — NLP

### Chapter 19 — Natural Language Processing

* Text classification
* Sentiment analysis
* Named Entity Recognition
* Translation
* Summarization
* Question answering
* Language modeling

### Chapter 20 — Text Preprocessing

* Normalization
* Vocabulary
* Tokens
* Special tokens
* Padding
* BOS
* EOS
* UNK

### Chapter 21 — Tokenization

* Word tokenization
* Character tokenization
* Subword tokenization
* BPE
* WordPiece
* Unigram

### Chapter 22 — Embeddings

* Word embeddings
* Token embeddings
* Positional embeddings
* Semantic similarity
* Cosine similarity

---

# 🏗️ Part 7 — Transformers

### Chapter 23 — Attention

* Query
* Key
* Value
* Attention scores
* Softmax
* Scaled dot-product attention

### Chapter 24 — Self-Attention

* Token relationships
* Context
* Attention weights
* Causal attention

### Chapter 25 — Multi-Head Attention

* Attention heads
* Parallel attention
* Concatenation
* Projection

### Chapter 26 — Transformer Architecture

```text
Tokens
   ↓
Token Embeddings
   ↓
Positional Information
   ↓
Self-Attention
   ↓
Add & Norm
   ↓
Feed Forward Network
   ↓
Add & Norm
   ↓
Transformer Blocks
   ↓
Output
```

### Chapter 27 — BERT vs GPT

Understand:

* Encoder
* Decoder
* Bidirectional attention
* Causal attention
* Masked language modeling
* Next-token prediction

### Chapter 28 — Causal Language Modeling

Understand:

```text
"The cat sat on the"
              ↓
            "mat"
```

and:

```text
P(xₜ | x₁, x₂, ..., xₜ₋₁)
```

---

# 🧪 Part 8 — LLM Training

### Chapter 29 — Pretraining

* Large-scale datasets
* Tokenization
* Batching
* Sequence length
* Next-token prediction
* Cross entropy
* Backpropagation
* Checkpoints
* Learning rate

### Chapter 30 — Build a Tiny GPT

Implement:

```text
Tokenizer
   ↓
Dataset
   ↓
Embedding
   ↓
Positional Encoding
   ↓
Self-Attention
   ↓
Multi-Head Attention
   ↓
Transformer Block
   ↓
Causal Mask
   ↓
LM Head
   ↓
Training
   ↓
Text Generation
```

---

# 🎯 Part 9 — LLM Fine-Tuning

### Chapter 31 — Pretraining vs Fine-Tuning

Understand the difference between:

```text
Pretraining
Large dataset
     ↓
General model
```

and:

```text
Fine-Tuning
Pretrained model
     ↓
Specialized dataset
     ↓
Specialized model
```

### Chapter 32 — Instruction Fine-Tuning

* Instruction datasets
* Chat templates
* Supervised fine-tuning
* Instruction following

### Chapter 33 — LoRA

Understand:

```text
Base Model
    +
LoRA Adapter
    ↓
Fine-Tuned Model
```

### Chapter 34 — QLoRA

* Quantization
* 4-bit models
* NF4
* PEFT
* Memory-efficient fine-tuning

### Chapter 35 — Hugging Face

Tools:

* Transformers
* Datasets
* Tokenizers
* Accelerate
* PEFT
* TRL
* Hugging Face Hub

---

# 📊 Part 10 — Dataset Preparation

### Chapter 36 — Data Pipeline

```text
Raw Data
   ↓
Cleaning
   ↓
Deduplication
   ↓
Filtering
   ↓
Normalization
   ↓
Tokenization
   ↓
Quality Checks
   ↓
Train / Validation / Test
```

### Chapter 37 — Dataset Quality

* Data quality
* Data diversity
* Data coverage
* Deduplication
* Data contamination
* Synthetic data
* Human annotation
* Noisy data
* PII

---

# 🔎 Part 11 — Retrieval-Augmented Generation

### Chapter 38 — RAG

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer
```

### Chapter 39 — Vector Search

* Embeddings
* Cosine similarity
* FAISS
* pgvector
* Pinecone
* Chroma
* Top-k retrieval

### Chapter 40 — RAG Quality

* Chunk size
* Chunk overlap
* Metadata filtering
* Hybrid search
* Reranking
* Retrieval precision
* Retrieval recall
* Hallucination reduction

---

# 📈 Part 12 — LLM Evaluation

### Chapter 41 — AI Evaluation

Measure:

* Accuracy
* Relevance
* Faithfulness
* Groundedness
* Hallucination
* Toxicity
* Latency
* Cost

### Chapter 42 — LLM Evaluation Systems

* Golden datasets
* Human evaluation
* LLM-as-a-Judge
* Pairwise evaluation
* Regression testing
* Benchmarking

---

# 🧑‍🏫 Part 13 — Alignment

### Chapter 43 — RLHF

Understand:

```text
Supervised Fine-Tuning
        ↓
Reward Model
        ↓
Reinforcement Learning
        ↓
Aligned Model
```

Topics:

* Preference data
* Reward models
* PPO
* RLHF

### Chapter 44 — DPO

* Preference datasets
* Chosen responses
* Rejected responses
* Direct Preference Optimization

---

# 🧠 Part 14 — Reasoning Models

### Chapter 45 — Reasoning

* Reasoning models
* Reasoning traces
* Test-time compute
* Reinforcement learning
* GRPO
* Reasoning evaluation

---

# 🛠️ Part 15 — LLM Application Engineering

### Chapter 46 — LLM APIs

* OpenAI-style APIs
* Anthropic
* Gemini
* AWS Bedrock
* Streaming
* Structured outputs
* JSON Schema
* Tool calling
* Retries
* Fallbacks

### Chapter 47 — Prompt Engineering

* Zero-shot prompting
* Few-shot prompting
* System prompts
* Prompt templates
* Structured outputs
* Tool calling
* Prompt decomposition
* Self-consistency
* Evaluation-driven prompting

### Chapter 48 — AI Agents

```text
User
 ↓
LLM
 ↓
Reason
 ↓
Select Tool
 ↓
Execute Tool
 ↓
Observe Result
 ↓
LLM
 ↓
Final Answer
```

Topics:

* Tool calling
* Planning
* Routing
* Memory
* Agent loops
* Multi-agent systems

---

# ⚙️ Part 16 — Production AI

### Chapter 49 — FastAPI

* REST APIs
* Async/await
* Pydantic
* Dependency injection
* Middleware
* Authentication
* Streaming
* Background tasks

### Chapter 50 — LLM Streaming

* StreamingResponse
* Server-Sent Events
* WebSockets
* Async generators

### Chapter 51 — Caching & Queues

* Redis
* Kafka
* RabbitMQ
* AWS SQS
* PostgreSQL
* Object storage
* Vector databases

---

# 🚀 Part 17 — Model Serving

### Chapter 52 — LLM Inference

* GPU inference
* Batching
* Continuous batching
* KV cache
* Throughput
* Latency
* GPU memory
* vLLM
* TGI

### Chapter 53 — Quantization

```text
FP32
 ↓
FP16 / BF16
 ↓
INT8
 ↓
INT4
```

Topics:

* Quantization
* GPTQ
* AWQ
* bitsandbytes
* Memory optimization

---

# 📦 Part 18 — MLOps

### Chapter 54 — Experiment Tracking

* Experiments
* Runs
* Metrics
* Artifacts
* Checkpoints
* Model versioning
* MLflow
* Weights & Biases

### Chapter 55 — Monitoring

Monitor:

* Latency
* Token usage
* Cost
* Errors
* Model quality
* Hallucinations
* GPU utilization

### Chapter 56 — Docker

* Dockerfiles
* Images
* Containers
* Environment variables
* Production deployment

---

# 💼 Part 19 — Interview Preparation

### Chapter 57 — Python Interview

Prepare:

* Lists vs tuples
* Dictionaries
* Shallow vs deep copy
* Decorators
* Generators
* Iterators
* GIL
* Threading
* Multiprocessing
* AsyncIO
* Context managers
* Memory management

### Chapter 58 — ML Interview

Prepare:

* Bias vs variance
* Overfitting
* Regularization
* Gradient descent
* Learning rate
* Normalization
* Precision vs recall
* Cross entropy

### Chapter 59 — Deep Learning Interview

Prepare:

* Forward propagation
* Backpropagation
* Activation functions
* Optimizers
* Batch normalization
* Layer normalization
* Dropout
* Vanishing gradients
* Exploding gradients

### Chapter 60 — Transformer Interview

Be able to explain:

```text
Tokenization
    ↓
Token IDs
    ↓
Embeddings
    ↓
Positional Information
    ↓
Q / K / V
    ↓
Self-Attention
    ↓
Multi-Head Attention
    ↓
Normalization
    ↓
Feed Forward
    ↓
Transformer Blocks
    ↓
LM Head
    ↓
Next Token
```

### Chapter 61 — LLM Interview

Questions to master:

* What is an LLM?
* How does GPT work?
* What is attention?
* What are Query, Key and Value?
* What is tokenization?
* What are embeddings?
* What is temperature?
* What are top-k and top-p?
* What is fine-tuning?
* What is LoRA?
* What is QLoRA?
* What is RAG?
* RAG vs fine-tuning?
* What causes hallucinations?
* How do you evaluate an LLM?
* How do you reduce inference latency?
* How would you fine-tune a 7B model?
* How would you prepare an LLM training dataset?

---

# 🏗️ Projects

The repository will contain practical projects throughout the learning journey.

## Project 1 — Machine Learning Pipeline

```text
CSV
 ↓
Pandas
 ↓
Data Cleaning
 ↓
Feature Engineering
 ↓
Train/Test Split
 ↓
ML Model
 ↓
Evaluation
 ↓
FastAPI
```

## Project 2 — Neural Network with PyTorch

Build:

* Dataset
* DataLoader
* Neural network
* Loss function
* Optimizer
* Training loop
* Validation
* Checkpointing

## Project 3 — Tiny GPT

Build a small GPT-style language model from scratch.

## Project 4 — LLM Fine-Tuning

Build:

```text
Dataset
 ↓
Cleaning
 ↓
Chat Template
 ↓
Tokenizer
 ↓
SFT
 ↓
LoRA
 ↓
Evaluation
 ↓
Model
```

## Project 5 — Production RAG

Build:

```text
PDF
 ↓
Document Processing
 ↓
Chunking
 ↓
Embeddings
 ↓
pgvector
 ↓
Retrieval
 ↓
Reranking
 ↓
LLM
 ↓
FastAPI
 ↓
Streaming
```

## Project 6 — LLM Evaluation Platform

Build an evaluation system that measures:

* Accuracy
* Relevance
* Groundedness
* Hallucination
* Latency
* Token usage
* Cost

---

# 🎥 YouTube Learning Series

This GitHub repository also accompanies my YouTube learning series.

Each major topic will be converted into practical videos.

### Video Progress

* [ ] Video 1 — Introduction + Python for AI
* [ ] Video 2 — NumPy for Machine Learning
* [ ] Video 3 — Pandas for Machine Learning
* [ ] Video 4 — Python Data Processing Practice
* [ ] Video 5 — Mathematics for ML
* [ ] Video 6 — Machine Learning Fundamentals
* [ ] Video 7 — Regression
* [ ] Video 8 — Classification
* [ ] Video 9 — ML Evaluation
* [ ] Video 10 — Overfitting & Regularization
* [ ] Video 11 — Neural Networks
* [ ] Video 12 — PyTorch Fundamentals
* [ ] Video 13 — PyTorch Training Loop
* [ ] Video 14 — NLP Fundamentals
* [ ] Video 15 — Tokenization
* [ ] Video 16 — Embeddings
* [ ] Video 17 — Attention
* [ ] Video 18 — Transformers
* [ ] Video 19 — GPT Architecture
* [ ] Video 20 — LLM Pretraining
* [ ] Video 21 — Fine-Tuning
* [ ] Video 22 — LoRA
* [ ] Video 23 — QLoRA
* [ ] Video 24 — Hugging Face
* [ ] Video 25 — Dataset Preparation
* [ ] Video 26 — RAG
* [ ] Video 27 — Vector Search
* [ ] Video 28 — RAG Evaluation
* [ ] Video 29 — LLM Evaluation
* [ ] Video 30 — AI Agents
* [ ] Video 31 — LLM Deployment
* [ ] Video 32 — LLM Interview Preparation

---

# 📅 Daily GitHub Practice

The repository follows a hands-on approach.

Every learning session should produce something:

```text
Concept
   ↓
Explanation
   ↓
Code
   ↓
Practice
   ↓
Mini Project
   ↓
GitHub Commit
```

The objective is to build a visible record of consistent progress rather than simply collecting tutorials.

---

# 🧠 Learning Philosophy

> **Learn → Code → Break → Debug → Explain → Build → Commit**

For every important concept:

1. Understand the theory.
2. Implement it yourself.
3. Test it with different inputs.
4. Break the implementation intentionally.
5. Debug the problem.
6. Explain the concept without notes.
7. Build something using it.
8. Commit the work to GitHub.

---

# 🎯 Final Target

By completing this repository, the goal is to be able to:

* Write production-quality Python.
* Work confidently with NumPy and Pandas.
* Understand ML fundamentals.
* Build and train neural networks with PyTorch.
* Explain NLP fundamentals.
* Implement attention and Transformers.
* Explain GPT-style LLM architecture.
* Prepare datasets for LLM training.
* Fine-tune open-source LLMs.
* Use LoRA and QLoRA.
* Build RAG systems.
* Evaluate LLM applications.
* Build AI agents.
* Serve models in production.
* Build FastAPI AI services.
* Optimize inference.
* Explain LLM architecture during interviews.
* Design real-world AI/ML systems.

---

# 🏆 Definition of Done

This journey is complete when I can take an AI problem and independently go from:

```text
Problem
   ↓
Data
   ↓
Data Preparation
   ↓
Model Selection
   ↓
Training / Fine-Tuning
   ↓
Evaluation
   ↓
Inference
   ↓
API
   ↓
Deployment
   ↓
Monitoring
```

and explain **why each decision was made**.

---

# 📌 Current Progress

### Foundations

* [x] Python fundamentals
* [ ] NumPy
* [ ] Pandas
* [ ] Mathematics

### Machine Learning

* [ ] ML fundamentals
* [ ] Regression
* [ ] Classification
* [ ] Evaluation
* [ ] Feature engineering

### Deep Learning

* [ ] Neural networks
* [ ] PyTorch
* [ ] Training
* [ ] Optimization

### NLP & LLMs

* [ ] NLP
* [ ] Tokenization
* [ ] Embeddings
* [ ] Attention
* [ ] Transformers
* [ ] GPT
* [ ] Pretraining
* [ ] Fine-tuning
* [ ] LoRA
* [ ] QLoRA

### Generative AI

* [ ] RAG
* [ ] Vector search
* [ ] Evaluation
* [ ] Agents
* [ ] Tool calling

### Production

* [ ] FastAPI
* [ ] Streaming
* [ ] Docker
* [ ] Model serving
* [ ] Quantization
* [ ] Monitoring
* [ ] MLOps

### Career

* [ ] ML interview preparation
* [ ] Deep Learning interview preparation
* [ ] LLM interview preparation
* [ ] System design
* [ ] End-to-end AI projects

---

# 🚀 Let's Build.

This repository is not intended to be a collection of copied tutorials.

It is a record of learning, implementation, experimentation, debugging and building.

**Python → ML → Deep Learning → Transformers → LLMs → Production AI**

One concept.

One implementation.

One commit at a time.
