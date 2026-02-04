# SynthNQ: High-Fidelity Synthetic RAG Benchmark

**SynthNQ** is a robust framework and dataset for evaluating Retrieval-Augmented Generation (RAG) pipelines. It solves the **data leakage** problem by providing a purely fictionalized environment where models cannot rely on internal parametric memory, forcing total reliance on retrieved context.

## Key Features

* **Zero-Leakage Evaluation:** All entities, facts, and dates are synthetically generated and logically consistent.
* **Multi-Threaded Generation:** High-throughput synthesis engine with built-in cost tracking and token management.
* **Contradiction Filtering:** Automatically detects and skips generations that conflict with the intended fictional logic.
* **Synthetic Seeding:** Support for recursive dataset expansion by using previously generated entries as seeds for new data.
* **Granular Testing:** Maps questions to specific passages and includes "Hard Negatives" (False Answers) to stress-test generator precision.

## Dataset Schema

Each entry in the `.jsonl` output follows the `SynthNQEntry` structure:

| Field | Description |
| --- | --- |
| `id` | Unique 15-digit identifier. |
| `question` | The fictionalized query. |
| `answer` | Full-sentence grounded response. |
| `short_answer` | Concise target for Exact Match (EM) evaluation. |
| `passages` | Array of fictional contexts supporting the answer. |
| `false_answers` | Plausible but incorrect distractors for multiple-choice testing. |

## Quick Start

### Installation

```bash
pip install -r requirements.txt

```

### Generation

To generate your own custom fictional world using the synthesis engine:

```bash
python synth.py --api_key YOUR_API_KEY --target_size 1000 --num_threads 4

```

### Key Arguments

* `--num_threads`: Set parallel workers for faster synthesis.
* `--synth_seeding`: Enable to use synthetic entries as seeds for future sampling.

## Methodology

SynthNQ utilizes `PrimeQA/clapnq` as a linguistic skeleton. The `Synthesizer` pipeline replaces real-world entities using `faker` and `Gemini-3-Flash`, ensuring the resulting dataset maintains human-like query complexity while being factually "blank" to pre-trained models.

## Attribution

Derived from [ClapNQ](https://huggingface.co/datasets/PrimeQA/clapnq). Distributed under the **Apache 2.0 License**.
