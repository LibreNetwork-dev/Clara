# THIS IS WHAT YOU ARE SUPPOSED TO USE CHATGPT FOR, NOT MAIN PROJET CODE 
# THANK YOU FOR COMING TO MY TED TALK
import json

sites = {
    "google.com": "https://google.com",
    "youtube": "https://youtube.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "reddit": "https://reddit.com",
    "github": "https://github.com",
    "wikipedia.org": "https://wikipedia.org",
    "duckduckgo": "https://duckduckgo.com",
    "stackoverflow": "https://stackoverflow.com",
    "paypal": "https://paypal.com",
    "linkedin": "https://linkedin.com",
    "pinterest": "https://pinterest.com",
    "netflix": "https://netflix.com",
    "spotify": "https://spotify.com",
    "amazon": "https://amazon.com",
    "ebay": "https://ebay.com",
    "cnn": "https://cnn.com",
    "nytimes": "https://nytimes.com",
    "quora": "https://quora.com",
    "medium": "https://medium.com",
}

verbs = [
    "open", "please open", "launch", "go to",
    "start", "navigate to", "browse"
]

typos = {
    "google": ["gogle", "gooogle", "goo gle"],
    "youtube": ["youtub", "yutube"],
    "facebook": ["fb", "facebok", "face book"],
}

def generate_site_phrases(site, url):
    phrases = {}
    for verb in verbs:
        phrase = f"{verb} {site}"
        phrases[phrase] = f"xdg-open {url}"
        phrase_dotcom = f"{verb} {site}.com"
        phrases[phrase_dotcom] = f"xdg-open {url}"
    if site in typos:
        for typo in typos[site]:
            for verb in verbs:
                phrase_typo = f"{verb} {typo}"
                phrases[phrase_typo] = f"xdg-open {url}"
    phrases[site] = f"xdg-open {url}"
    if site in typos:
        for typo in typos[site]:
            phrases[typo] = f"xdg-open {url}"
    return phrases

def main():
    all_phrases = {}
    count = 0
    for site, url in sites.items():
        phrases = generate_site_phrases(site, url)
        for phrase, cmd in phrases.items():
            all_phrases[phrase] = cmd
            count += 1
    with open("../data/browse.json", "w", encoding="utf-8") as f:
        json.dump(all_phrases, f, indent=4, ensure_ascii=False)

    print(f"Saved {count} input-output pairs")

if __name__ == "__main__":
    main()
