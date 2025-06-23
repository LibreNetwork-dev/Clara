import json

command = "notify-send Current_Time $(date +%T)"

base = ["time", "clock", "current time", "time now"]
actions = [
    "", "get", "show", "display", "print", "fetch", "return", "output", "tell", "give", "show me", "what is", "whats"
]
modifiers = ["", "now", "please", "current", "pls"]

variants = set()

for action in actions:
    for b in base:
        for mod in modifiers:
            parts = [action, b, mod]
            phrase = " ".join(p for p in parts if p).strip()
            variants.add(phrase.lower())
            variants.add(phrase.upper())
            variants.add(phrase.capitalize())

final = {v: command for v in sorted(variants)}

with open("../data/time.json", "w") as f:
    json.dump(final, f, indent=4)

print(f"✅ Saved {len(final)} command variants to 'time_commands.json'")
