from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import subprocess
import threading
import re

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


def strip_quotes_inside_strings(code):
    string_pattern = re.compile(
        r"""
        (['"])               # Capture opening quote in group 1
        (                    # Start capture of string content in group 2
          (?:                # Non-capturing group for content
            \\.|             # Escaped char like \'
            [^\\\1]          # Any char except backslash or the quote char
          )*
        )
        \1                   # Match the same quote as opening
        """,
        re.VERBOSE
    )

    def replacer(match):
        quote = match.group(1)
        content = match.group(2)

        content = content.replace('\\\\', '__BACKSLASH__')

        content = content.replace("\\'", '__SINGLEQUOTE__')
        content = content.replace('\\"', '__DOUBLEQUOTE__')

        content = content.replace("'", "")
        content = content.replace('"', "")

        content = content.replace('__SINGLEQUOTE__', "\\'")
        content = content.replace('__DOUBLEQUOTE__', '\\"')
        content = content.replace('__BACKSLASH__', '\\\\')

        return quote + content + quote

    return string_pattern.sub(replacer, code)


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
        cmd = strip_quotes_inside_strings(cmd)
        print("Sanitized command:", cmd)
        thread = threading.Thread(target=run_subproc, args=(cmd,))
        thread.start()
