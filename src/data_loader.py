#!/usr/bin/env python3
import json
import requests
import os

# URLs and filenames
urls = {
    "rs_train.jsonl": "https://inklab.usc.edu/RiddleSense/riddlesense_dataset/rs_train.jsonl",
    "rs_dev.jsonl": "https://inklab.usc.edu/RiddleSense/riddlesense_dataset/rs_dev.jsonl",
    "rs_test.jsonl": "https://inklab.usc.edu/RiddleSense/riddlesense_dataset/rs_test_hidden.jsonl"
}

# Create directory and download files
os.makedirs("riddle_data", exist_ok=True)

for filename, url in urls.items():
    filepath = f"riddle_data/{filename}"
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        with open(filepath, 'wb') as f:
            f.write(requests.get(url).content)

# Load and show data
for filename in urls.keys():
    with open(f"riddle_data/{filename}") as f:
        data = [json.loads(line) for line in f]
        print(f"{filename}: {len(data)} examples")

# Show first example
with open("riddle_data/rs_train.jsonl") as f:
    first = json.loads(f.readline())
    print(f"\nFirst example: {first['question']['stem']}")
    print(f"Answer: {first['answerKey']}")
