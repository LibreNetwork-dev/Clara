import json

tasks = [
    "do the thing",
    "walk the dog",
    "check the email",
    "make coffee",
    "start coding",
    "water the plants",
    "feed the cat",
    "take a break",
    "go for a run",
    "call mom"
]

output = {}

for task in tasks:
    for hour in range(1, 13):  # 1 to 12
        for minute in range(0, 60, 20):  # Every 20 minutes: 00, 20, 40
            for meridiem in ["AM", "PM"]:
                time_str = f"{hour}:{minute:02d} {meridiem}"
                instruction = f"At {time_str}, remind me to {task}"
                bash_cmd = (
                    f"bash -c \\\"echo 'notify-send \\\\\\\"Reminder\\\\\\\" \\\\\\\"{task}!\\\\\\\"' "
                    f"| at \\\\\\\"$(date -d '{time_str}' +%H:%M)\\\\\\\"\\\""
                )
                output[instruction] = bash_cmd

# Save to file
with open("../data/remind.json", "w") as f:
    json.dump(output, f, indent=4)

print(f"✅ Generated {len(output)} reminders (every 20 mins for each task).")
