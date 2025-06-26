import json

# Units and their common spoken forms (for input phrasing)
units = {
    "m": ["meter"],
    "f": ["feets"],
    "i": ["inches"],
    "mi": ["mile", "miles"],
    "l": ["liters"],
    "ml": ["milliliters"],
    "gal": ["gallons"],
    "kg": ["kilograms"],
    "lb": ["pounds"],
}

# Conversion pairs you want to generate phrases for (from_unit, to_unit)
conversion_pairs = [
    ("lb", "kg"),
    ("kg", "lb"),
    ("m", "f"),
    ("f", "m"),
    ("i", "f"),
    ("f", "i"),
    ("mi", "f"),
    ("f", "mi"),
    ("l", "ml"),
    ("ml", "l"),
    ("l", "gal"),
    ("gal", "l"),
]

# Some example values to include in phrases
example_values = [1, 5, 10, "twelve"]

templates = [
    "what is {} {} to {}",
    "convert {} {} to {}",
    "how many {} in {} {}",
    "convert {} {} into {}",
]

output = {}

for from_unit, to_unit in conversion_pairs:
    from_names = units[from_unit]
    to_names = units[to_unit]

    for value in example_values:
        for from_name in from_names:
            for to_name in to_names:
                for template in templates:
                    if "how many" in template:
                        phrase = template.format(to_name, value, from_name)
                    else:
                        phrase = template.format(value, from_name, to_name)

                    phrase = phrase.lower()
                    key = phrase
                    val = f"convert('{value}', '{from_unit}', '{to_unit}')"
                    output[key] = val

with open("../data/conversion.json", "w") as f:
    json.dump(output, f, indent=4)

print(f"Generated {len(output)} i/o pairs.")
