import subprocess
import time

sites = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "reddit": "https://reddit.com",
    "github": "https://github.com",
    "twitter": "https://twitter.com",
    "wikipedia": "https://wikipedia.org",
    "duckduckgo": "https://duckduckgo.com",
    "stackoverflow": "https://stackoverflow.com",
    "paypal": "https://paypal.com",
    "imdb": "https://imdb.com",
    "linkedin": "https://linkedin.com",
    "pinterest": "https://pinterest.com",
    "netflix": "https://netflix.com",
    "spotify": "https://spotify.com",
    "amazon": "https://amazon.com",
    "ebay": "https://ebay.com",
    "bbc": "https://bbc.com",
    "cnn": "https://cnn.com",
    "nytimes": "https://nytimes.com",
    "quora": "https://quora.com",
    "medium": "https://medium.com",
    "tumblr": "https://tumblr.com",
    "twitch": "https://twitch.tv",
    "etsy": "https://etsy.com",
    "stackoverflow": "https://stackoverflow.com",
    "airbnb": "https://airbnb.com",
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
    "paypal": "https://paypal.com",
    "github": "https://github.com",
    "bitbucket": "https://bitbucket.org",
    "gitlab": "https://gitlab.com",
    "bbcnews": "https://bbc.co.uk/news",
    "theguardian": "https://theguardian.com",
    "washingtonpost": "https://washingtonpost.com",
    "aljazeera": "https://aljazeera.com",
    "forbes": "https://forbes.com",
    "techcrunch": "https://techcrunch.com",
    "wired": "https://wired.com",
    "buzzfeed": "https://buzzfeed.com",
    "reddit": "https://reddit.com",
    "9gag": "https://9gag.com",
    "imgur": "https://imgur.com",
    "soundcloud": "https://soundcloud.com",
    "bbciplayer": "https://bbc.co.uk/iplayer",
    "nasa": "https://nasa.gov",
    "nih": "https://nih.gov",
    "webmd": "https://webmd.com",
    "dictionary": "https://dictionary.com",
    "thesaurus": "https://thesaurus.com",
    "cnn": "https://cnn.com",
    "espn": "https://espn.com",
    "nba": "https://nba.com",
    "nhl": "https://nhl.com",
    "mlb": "https://mlb.com",
    "nfl": "https://nfl.com",
    "spotify": "https://spotify.com",
    "deezer": "https://deezer.com",
    "pandora": "https://pandora.com",
    "bbc": "https://bbc.com",
    "vox": "https://vox.com",
    "nationalgeographic": "https://nationalgeographic.com",
    "goodreads": "https://goodreads.com",
    "medium": "https://medium.com",
    "yelp": "https://yelp.com",
    "tripadvisor": "https://tripadvisor.com",
    "glassdoor": "https://glassdoor.com",
    "indeed": "https://indeed.com",
    "monster": "https://monster.com",
    "craigslist": "https://craigslist.org",
    "reddit": "https://reddit.com",
    "tumblr": "https://tumblr.com",
    "9gag": "https://9gag.com"
}

verbs = [
    "open", "please open", "launch", "go to", "visit", "bring up", "show me",
    "quickly open", "start", "access", "navigate to", "browse"
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
    "stackoverflow": ["stack overflow", "stackovrflow"],
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
    count = 0
    for site, url in sites.items():
        phrases = generate_site_phrases(site, url)
        for phrase, cmd in phrases.items():
            title = f"Instruction #{count+1}"
            message = f'"{phrase}" → {cmd}'
            print(title, message)
            count += 1
            time.sleep(0.1)  # adjust or remove delay as needed

    print(f"Sent {count} notifications.")

if __name__ == "__main__":
    main()
