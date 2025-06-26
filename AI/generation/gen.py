import json

sites = {
    "google.com": "https://google.com",
    "facebook.com": "https://facebook.com",
    "wikipedia.org": "https://wikipedia.org",
    "youtube.com": "https://youtube.com",
    "reddit.com": "https://reddit.com",
    "torproject.org": "https://torproject.org",
    "soap2day.day": "https://soap2day.day",
    "yarrlist.com": "https://yarrlist.com/",
    "example.com": "https://example.com"
}

templates = [
    "open {}",
    "please open {}",
    "can you open {}",
    "open {} pls",
    "launch {}",
    "visit {}",
    "go to {}",
    "take me to {}",
    "open the {} site",
    "open the {} website"
]

output = {}
for name, url in sites.items():
    for template in templates:
        phrase = template.format(name)
        output[phrase] = f'os.execute("xdg-open {url}")'

with open("../data/browse.json", "w") as f:
    json.dump(output, f, indent=4)
