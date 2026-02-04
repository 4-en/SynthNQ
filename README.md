# SynthNQ: High-Fidelity Synthetic RAG Benchmark

**SynthNQ** is a robust framework and dataset for evaluating Retrieval-Augmented Generation (RAG) pipelines. It solves the **data leakage** problem by providing a purely fictionalized environment where models cannot rely on internal parametric memory, forcing total reliance on retrieved context. The dataset includes questions, answers and contexts, making it suitable for both retrieval and generation evaluation.

## Key Features

* **Zero-Leakage Evaluation:** All entities, facts, and dates are synthetically generated and logically consistent.
* **Retrieval Evaluation:** Suitable for evaluating retrieval systems with provided passages and fictional answers.
* **Generation Evaluation:** Suitable for evaluating generator components with provided passages.
* **Contradiction Filtering:** Includes safeguard to minimize contradicting question, answers and passages.
* **Multiple-choice Evaluation:** Contains false but plausible answers that can be used for less expensive multiple-choice evaluation.

## Dataset Schema

Each entry in the `.jsonl` output follows the `SynthNQEntry` structure:

| Field | Description |
| --- | --- |
| `id` | Unique 15-digit identifier. |
| `question` | The fictionalized query. |
| `answer` | Multi-sentence grounded response. |
| `short_answer` | Concise target for Exact Match (EM) evaluation. |
| `passages` | Array of fictional contexts supporting the answer. |
| `false_answers` | Plausible but incorrect distractors for multiple-choice testing. |

## Quick Start

### Installation

```bash
pip install -r requirements.txt

```

### Generation

To generate new entries, use:

```bash
python synth.py --api_key YOUR_API_KEY --target_size 1000 --num_threads 4

```

### Key Arguments

* `--output_file`: Set output file for jsonl data.
* `--model_id`: Set the model id for generation (via google-genai).
* `--num_threads`: Set parallel workers for faster synthesis.
* `--synth_seeding`: Enable to use synthetic entries as seeds for future sampling.

## Methodology

SynthNQ utilizes `PrimeQA/clapnq` as a linguistic skeleton. The `Synthesizer` pipeline replaces real-world entities using `faker` and `Gemini-3-Flash`, ensuring the resulting dataset maintains human-like query complexity while being factually "blank" to pre-trained models.

## Attribution

Derived from [ClapNQ](https://github.com/primeqa/clapnq). Distributed under the **Apache 2.0 License**.
