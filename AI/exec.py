from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import subprocess
import threading
import re
from evdev import InputDevice, categorize, ecodes, list_devices
import pygame
import os
import time

model_path = "./fine_tuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def listen_bind():
    keyboard = None
    for path in list_devices():
        dev = InputDevice(path)
        if "keyboard" in dev.name.lower():
            keyboard = InputDevice(path)
            break

    if not keyboard:
        print("Keyboard not found.")
        exit(1)

    print(f"Listening on: {keyboard.path}")

    mod_super = False

    for event in keyboard.read_loop():
        if event.type == ecodes.EV_KEY:
            key = categorize(event)
            code = key.keycode if isinstance(key.keycode, str) else key.keycode[0]

            if key.keystate == key.key_down:
                if code in ("KEY_LEFTMETA", "KEY_RIGHTMETA"):
                    mod_super = True
                elif code == "KEY_GRAVE" and mod_super:
                    inst = get_instruction()
                    cmd = strip_quotes_inside_strings(generate_command(inst))
                    thread = threading.Thread(target=run_subproc, args=(cmd,))
                    thread.start()

                    

            elif key.keystate == key.key_up:
                if code in ("KEY_LEFTMETA", "KEY_RIGHTMETA"):
                    mod_super = False

def get_instruction():
    # no taskbar (X11 only)
    os.environ["SDL_VIDEO_X11_WMCLASS"] = "invisible"
    os.environ["SDL_VIDEO_X11_NET_WM_STATE"] = "_NET_WM_STATE_SKIP_TASKBAR,_NET_WM_STATE_ABOVE"

    pygame.init()
    screen = pygame.display.set_mode((600, 100), pygame.NOFRAME)
    pygame.display.set_caption("Assistant")
    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()

    input_text = ""
    key_hold = {}
    repeat_interval = 0.2

    cursor_visible = True
    last_cursor_toggle = time.time()
    cursor_interval = 0.5

    while True:
        now = time.time()
        screen.fill((20, 20, 20))

        # Blink cursor
        if now - last_cursor_toggle >= cursor_interval:
            cursor_visible = not cursor_visible
            last_cursor_toggle = now

        display_text = input_text + ('|' if cursor_visible else '')
        text_surface = font.render(display_text, True, (255, 255, 255))
        screen.blit(text_surface, (20, 25))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()

        for key, (last_time, char) in list(key_hold.items()):
            if not keys[key]:
                del key_hold[key]
                continue
            if now - last_time > repeat_interval:
                if key == pygame.K_BACKSPACE:
                    if mods & pygame.KMOD_CTRL:
                        input_text = input_text.rstrip()
                        input_text = input_text[:input_text.rstrip().rfind(" ") + 1] if " " in input_text else ""
                    else:
                        input_text = input_text[:-1]
                elif char:
                    input_text += char
                key_hold[key] = (now, char)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    pygame.quit()
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    if mods & pygame.KMOD_CTRL:
                        input_text = input_text.rstrip()
                        input_text = input_text[:input_text.rstrip().rfind(" ") + 1] if " " in input_text else ""
                    else:
                        input_text = input_text[:-1]
                    key_hold[event.key] = (now, '')
                else:
                    input_text += event.unicode
                    key_hold[event.key] = (now, event.unicode)

            elif event.type == pygame.KEYUP:
                key_hold.pop(event.key, None)

        clock.tick(60)



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
    listen_bind()