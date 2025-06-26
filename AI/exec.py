from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import subprocess
import threading


model_path = "./fine_tuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_command(instruction):
    inputs = tokenizer(instruction, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=120)
    command = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return command

def run_subproc(cmd):
    proc = subprocess.Popen(
        ["bin/lua", "scripts/main.lua", cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    out, err = proc.communicate()
    print(out)
    if err:
        print("lua script threw an error ", err)

if __name__ == "__main__":
    while True:
        instruction = input("Instruction: ")
        if instruction.lower() in ("exit", "quit", ""):
            break
        cmd = generate_command(instruction)
        print(cmd)
        thread = threading.Thread(target=run_subproc, args=(cmd,))
        thread.start()        
