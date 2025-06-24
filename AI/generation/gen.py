import json
import time

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
    "twitch": "https://twitch.tv",
    "etsy": "https://etsy.com",
    "tripadvisor": "https://tripadvisor.com",
    "weather": "https://weather.com",
    "microsoft": "https://microsoft.com",
    "apple": "https://apple.com",
    "adobe": "https://adobe.com",
    "dropbox": "https://dropbox.com",
    "salesforce": "https://salesforce.com",
    "hulu": "https://hulu.com",
    "discord": "https://discord.com",
    "slack": "https://slack.com",
    "coursera": "https://coursera.org",
    "udemy": "https://udemy.com",
    "khanacademy": "https://khanacademy.org",
    "stackexchange": "https://stackexchange.com",
    "bitbucket": "https://bitbucket.org",
    "gitlab": "https://gitlab.com",
    "theguardian": "https://theguardian.com",
    "washingtonpost": "https://washingtonpost.com",
    "aljazeera": "https://aljazeera.com",
    "forbes": "https://forbes.com",
    "techcrunch": "https://techcrunch.com",
    "wired": "https://wired.com",
    "buzzfeed": "https://buzzfeed.com",
    "9gag": "https://9gag.com",
    "soundcloud": "https://soundcloud.com",
    "nasa": "https://nasa.gov",
    "nih": "https://nih.gov",
    "dictionary": "https://dictionary.com",
    "thesaurus": "https://thesaurus.com",
    "nationalgeographic": "https://nationalgeographic.com",
    "goodreads": "https://goodreads.com",
    "yelp": "https://yelp.com",
    "glassdoor": "https://glassdoor.com",
    "indeed": "https://indeed.com",
}

verbs = [
    "open", "please open", "launch", "go to",
    "start", "navigate to", "browse"
]

typos = {
    "google": ["gogle", "gooogle", "goo gle"],
    "youtube": ["youtub", "yutube"],
    "facebook": ["fb", "facebok", "face book"],
    "instagram": ["insta", "instgram", "instagrem"],
    "reddit": ["rddit", "reddt", "reditt"],
    "github": ["git hub", "githb", "gitub"],
    "twitter": ["twiter", "twittter"],
    "wikipedia": ["wikipediaa", "wikipedea"],
    "duckduckgo": ["duck duck go", "duckduckgo.com"],
    "stackoverflow": ["stack overflow"],
    "paypal": ["paypa", "paypel"],
    "imdb": ["imbd", "imdbb"],
    "linkedin": ["linkdin", "linkdln"],
    "pinterest": ["pintrest", "pinterst"],
    "netflix": ["netflx", "netflik"],
    "spotify": ["spotfy", "spotif"],
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

    print(f"Saved {count} input-output pairs to site_phrases.json")

if __name__ == "__main__":
    main()
