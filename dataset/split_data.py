# splits raw dataset into train, validation and test sets

import os

SOURCE_FILE = '../raw_data/synth_nq.jsonl'

def split_data(source_file, train_file, val_file, test_file, train_ratio=0.8, val_ratio=0.1):
    with open(source_file, 'r') as f:
        lines = f.readlines()
    
    lines = [line for line in lines if line.strip()]  # Remove empty lines
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
    with open('README.md', 'w') as f:
        f.write(f"# Dataset Split\n\n")
        f.write(f"| Split | File | Number of Samples | Percentage |\n")
        f.write(f"|-------|------|-------------------|------------|\n")
        f.write(f"| Total | {source_file} | {total_lines} | 100% |\n")
        f.write(f"| Train | {train_file} | {train_len} | {train_len / total_lines:.2%} |\n")
        f.write(f"| Val   | {val_file} | {val_len} | {val_len / total_lines:.2%} |\n")
        f.write(f"| Test  | {test_file} | {test_len} | {test_len / total_lines:.2%} |\n")
        
        
                
if __name__ == "__main__":
    split_data(SOURCE_FILE, 'synth_nq_train.jsonl', 'synth_nq_val.jsonl', 'synth_nq_test.jsonl')