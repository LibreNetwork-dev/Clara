import json

math_expressions = {
    "3*32": (3, "*", 32),
    "7+5": (7, "+", 5),
    "12-4": (12, "-", 4),
    "20/5": (20, "/", 5),
    "15*2": (15, "*", 2),
    "10*5": (10, "*", 5),
    "9-6": (9, "-", 6),
    "40123-1000001": (40123, "-", 1000001),
    "2^8": (2, "^", 8),
    "4^2": (4, "^", 2),
    "sqrt(16)": ("sqrt", 16, None),
    "sqrt(25)": ("sqrt", 25, None),
    "5^3": (5, "^", 3),
    "sqrt(49)": ("sqrt", 49, None)
}

templates = [
    "what is {}",
    "calculate {}",
    "how much is {}",
    "can you calculate {}",
    "{} please",
    "{}"
]

op_words = {
    "+": "plus",
    "-": "minus",
    "*": "times",
    "/": "divided by",
    "^": "to the power of",
    "sqrt": "square root of"
}

output = {}

for expr, parts in math_expressions.items():
    if parts[0] == "sqrt":
        spoken = f"{op_words['sqrt']} {parts[1]}"
    else:
        a, op, b = parts
        spoken = f"{a} {op_words[op]} {b}"

    for template in templates:
        phrase = template.format(spoken)
        output[phrase] = f"calc('{expr}')"

with open("../data/math.json", "w") as f:
    json.dump(output, f, indent=4)

print(f"Generated {len(output)} math query variations.")
