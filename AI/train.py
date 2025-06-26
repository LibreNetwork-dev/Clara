import json
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments

from datasets import Dataset

file_paths = ["data/browse.json", "data/music.json", "data/math.json", "data/conversion.json", "data/mcontrol.json"]  

combined_data = {}

for path in file_paths:
    with open(path, 'r') as f:
        data_dict = json.load(f)
    combined_data.update(data_dict)  

data = [{"input": k, "output": v} for k, v in combined_data.items()]

dataset = Dataset.from_list(data)

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def preprocess(batch):
    inputs = tokenizer(batch["input"], padding="max_length", truncation=True, max_length=32)
    outputs = tokenizer(batch["output"], padding="max_length", truncation=True, max_length=64)
    labels = outputs["input_ids"]
    labels = [[(token if token != tokenizer.pad_token_id else -100) for token in label] for label in labels]
    inputs["labels"] = labels
    return inputs


dataset = dataset.map(preprocess, batched=True)

# inc epochs to ~5 for prod
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=2,
    per_device_train_batch_size=8,
    logging_dir="./logs",
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
)

trainer.train()

model.save_pretrained("./fine_tuned")
tokenizer.save_pretrained("./fine_tuned")
