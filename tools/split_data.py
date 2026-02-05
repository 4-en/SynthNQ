# splits raw dataset into train, validation and test sets

import os
import json
import random

SOURCE_FILE = '../raw_data/synth_nq.jsonl'
OUTPUT_DIR = '../dataset/'

def split_data(source_file, train_file, val_file, test_file, train_ratio=0.8, val_ratio=0.1):
    with open(source_file, 'r') as f:
        lines = f.readlines()
    
    lines = [line for line in lines if line.strip()]  # Remove empty lines
    
    # shuffle lines
    random.seed(42)
    random.shuffle(lines)
    
    total_lines = len(lines)
    train_end = int(total_lines * train_ratio)
    val_end = train_end + int(total_lines * val_ratio)
    
    train_len = 0
    val_len = 0
    test_len = 0

    with open(train_file, 'w') as train_f, open(val_file, 'w') as val_f, open(test_file, 'w') as test_f:
        for i, line in enumerate(lines):
            if i < train_end:
                train_len += 1
                train_f.write(line)
            elif i < val_end:
                val_len += 1
                val_f.write(line)
            else:
                test_len += 1
                test_f.write(line)
                
    # write stats in table in md file
    with open(os.path.join(OUTPUT_DIR, 'README.md'), 'w') as f:
        
        f.write(f"# SynthNQ Dataset\n\n")
        f.write(f"This dataset is a synthetic version of the Natural Questions (NQ) dataset, generated using a large language model. It contains fictional question-answer pairs along with supporting passages and false answers to facilitate training and evaluation of question answering systems.\n\n")
        
        f.write(f"## Dataset Split\n\n")
        f.write(f"| Split | File | Number of Samples | Percentage |\n")
        f.write(f"|-------|------|-------------------|------------|\n")
        f.write(f"| Total | {source_file} | {total_lines} | 100% |\n")
        f.write(f"| Train | {train_file} | {train_len} | {train_len / total_lines:.2%} |\n")
        f.write(f"| Val   | {val_file} | {val_len} | {val_len / total_lines:.2%} |\n")
        f.write(f"| Test  | {test_file} | {test_len} | {test_len / total_lines:.2%} |\n\n")
        
        # schema of the dataset
        f.write(f"## Dataset Schema\n\n")
        f.write(f"Each entry in the dataset is a JSON object with the following fields:\n\n")
        f.write(f"| Field | Type | Description |\n")
        f.write(f"|-------|------|-------------|\n")
        f.write(f"| id | string | Unique identifier for the question |\n")
        f.write(f"| question | string | The question text |\n")
        f.write(f"| answer | string | The full answer text |\n")
        f.write(f"| short_answer | string | A concise short answer |\n")
        f.write(f"| passages | list of Passage objects | A list of passages supporting the answer |\n")
        f.write(f"| false_answers | list of strings | A list of plausible but incorrect short answers |\n\n")
        
        f.write(f"## Passage Schema\n\n")
        f.write(f"| Field | Type | Description |\n")
        f.write(f"|-------|------|-------------|\n")
        f.write(f"| summary | string | A short one-line summary or title of the passage |\n")
        f.write(f"| passage | string | The full passage text supporting the answer |\n\n")
        
        f.write(f"## Sample Entry\n\n")
        f.write(f"```json\n")
        sample = json.loads(lines[0])  # Load the first entry as a sample
        f.write(json.dumps(sample, indent=2))
        f.write(f"\n```\n")
        
                
if __name__ == "__main__":
    split_data(SOURCE_FILE, os.path.join(OUTPUT_DIR, 'synth_nq_train.jsonl'), os.path.join(OUTPUT_DIR, 'synth_nq_val.jsonl'), os.path.join(OUTPUT_DIR, 'synth_nq_test.jsonl'))