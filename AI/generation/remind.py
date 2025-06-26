import json

tasks = [
    "do the thing",
    "walk my dog",
    "make coffee",
    "water the plants",
    "feed the cat",
    "take a break",
    "go for a run",
    "call mom"
]

output = {}

for task in tasks:
    for hour in range(1, 13):  
        for minute in range(0, 60, 20):
            for meridiem in ["AM", "PM"]:
                time_str = f"{hour}:{minute:02d} {meridiem}"
                instruction = f"At {time_str}, remind me to {task}"
                bash_cmd = (
                    f"bash -c \\\"echo 'notify-send \\\\\\\"Reminder\\\\\\\" \\\\\\\"{task}!\\\\\\\"' "
                    f"| at \\\\\\\"$(date -d '{time_str}' +%H:%M)\\\\\\\"\\\""
                )
                output[instruction] = bash_cmd

with open("../data/remind.json", "w") as f:
    json.dump(output, f, indent=4)

print(f"✅ Generated {len(output)} i/o pairs")
