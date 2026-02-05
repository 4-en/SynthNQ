# SynthNQ Dataset

This dataset is a synthetic version of the Natural Questions (NQ) dataset, generated using a large language model. It contains fictional question-answer pairs along with supporting passages and false answers to facilitate training and evaluation of question answering systems.

## Dataset Split

| Split | File | Number of Samples | Percentage |
|-------|------|-------------------|------------|
| Total | ../raw_data/synth_nq.jsonl | 3242 | 100% |
| Train | ../dataset/synth_nq_train.jsonl | 2593 | 79.98% |
| Val   | ../dataset/synth_nq_val.jsonl | 324 | 9.99% |
| Test  | ../dataset/synth_nq_test.jsonl | 325 | 10.02% |

## Dataset Schema

Each entry in the dataset is a JSON object with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier for the question |
| question | string | The question text |
| answer | string | The full answer text |
| short_answer | string | A concise short answer |
| passages | list of Passage objects | A list of passages supporting the answer |
| false_answers | list of strings | A list of plausible but incorrect short answers |

## Passage Schema

| Field | Type | Description |
|-------|------|-------------|
| summary | string | A short one-line summary or title of the passage |
| passage | string | The full passage text supporting the answer |

## Sample Entry

```json
{
  "id": "432872469478906",
  "question": "Is the South Margaret Institute developing a successor to their 2023 breakthrough study in synthetic tissue?",
  "answer": "In late 2023, Lead Biomedical Engineer Kyle Bell announced that the South Margaret Institute would be launching a second phase of their research titled 'Project Renaissance'. This new project is a direct follow-up to their successful 2023 pilot study on bio-compatible polymers and is scheduled to begin clinical implementation in August 2025. While the previous work focused on simple skin grafts, Kyle Bell confirmed that the new initiative will focus on complex vascular systems.",
  "short_answer": "Project Renaissance",
  "passages": [
    {
      "summary": "Introduction to the leadership and research focus at South Margaret.",
      "passage": "The South Margaret Institute of Technology has been at the forefront of medical advancements for over a decade. Under the guidance of Kyle Bell, the department of biomedical engineering has pioneered several techniques in cell scaffold construction. Their latest press release confirms that they are now looking to expand their research into fully synthetic organ prototypes via a new project."
    },
    {
      "summary": "The success of the initial biomedical study led by Kyle Bell.",
      "passage": "Kyle Bell, a renowned Biomedical Engineer, first gained international recognition for his work on bio-compatible polymers during the 2023 trials. His team at South Margaret published their findings in a prestigious journal, showing a 90 percent success rate in tissue integration. This accomplishment set the stage for a much larger, federally funded endeavor aimed at replacing damaged heart valves."
    },
    {
      "summary": "Official announcement and name of the follow-up project.",
      "passage": "In December 2023, the board of directors at the institute officially greenlit 'Project Renaissance', the highly anticipated successor to their initial trials. Lead researcher Kyle Bell stated that the project would shift focus from simple tissue to complex vascular systems and regenerative mapping. The announcement has sparked significant interest from both the medical community and venture capitalists interested in the future of biomedical engineering."
    },
    {
      "summary": "The scope and planned implementation timeline for the new study.",
      "passage": "While the original study was modest in scope, Project Renaissance aims to involve over five hundred patients across three continents. The South Margaret research wing is currently being upgraded to house the specialized 3D bioprinters required for this next phase of development. Kyle Bell expects the first human trials to commence by the third quarter of 2025 if all safety benchmarks are met."
    },
    {
      "summary": "Kyle Bell's long-term vision for Project Renaissance.",
      "passage": "The timeline for Project Renaissance has been meticulously planned to ensure patient safety and data integrity over the long term. Preliminary tests are scheduled for the end of next year, with the primary rollout occurring in 2025. Biomedical Engineer Kyle Bell has emphasized that this project represents the culmination of his life's work at the South Margaret facility."
    }
  ],
  "false_answers": [
    "Project Vitality",
    "The South Margaret Protocol",
    "Operation Bell-Curve"
  ]
}
```
