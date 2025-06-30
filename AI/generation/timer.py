# AI generated, good luck future me
# (its just a gen script)
import json
import os

hours = [0, 1, 2, 3, 4, 5, 6]
minutes = [0, 15, 30, 45, 50]
seconds = [0, 15, 30, 45]

results = {}

for hr in hours:
    for min_ in minutes:
        for sec in seconds:
            if hr == 0 and min_ == 0 and sec == 0:
                continue 

            parts = []

            if hr > 0:
                parts.append(f"{'an' if hr == 1 else hr} hour{'s' if hr > 1 else ''}")
            if min_ > 0:
                parts.append(f"{min_} minute{'s' if min_ != 1 else ''}")
            if sec > 0:
                parts.append(f"{sec} second{'s' if sec != 1 else ''}")

            phrase = "set a timer for " + (
                parts[0] if len(parts) == 1 else
                " and ".join([", ".join(parts[:-1]), parts[-1]]) if len(parts) > 2 else
                " and ".join(parts)
            )

            lua_call = f"setTimer({sec}, {min_}, {hr})"

            results[phrase] = lua_call
with open("../data/timer.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"{len(results)} io pairs written")
