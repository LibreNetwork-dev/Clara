
import json

base_command = "os.execute('pkill mpv')"

verbs = ["stop", "end", "kill", "cut", "shut", "turn"]
modifiers = ["", "please", "can you", "could you"]
fillers = [""]
music_terms = ["music", "the music", "the song"]

phrases = []

templates = [
    "{mod} {verb} {music}",
    "{mod} {verb} playing {music}",
    "{mod} {verb} {filler} {music}",
    "{mod} {verb} {music} off",
    "{mod} shut {music} off",
    "{mod} turn {music} off",
    "{mod} turn off {music}",
    "{mod} make {music} stop",
    "{mod} make {filler} {music} stop",
]

for mod in modifiers:
    for verb in verbs:
        for filler in fillers:
            for music in music_terms:
                for template in templates:
                    phrase = template.format(
                        mod=mod.strip(),
                        verb=verb,
                        filler=filler,
                        music=music
                    ).strip()
                    phrase = ' '.join(phrase.split())
                    phrases.append(phrase.lower())

unique_phrases = sorted(set(phrases))

output = {phrase: base_command for phrase in unique_phrases}

with open("../data/mcontrol.json", "w") as f:
    json.dump(output, f, indent=4)
olen = len(output)

print(f"generated {olen} io pairs")
