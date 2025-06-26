import json

def generate_variations(songs):
    """
    songs: list of tuples (song_name, artist_name)
    returns: dict mapping input phrases to output commands
    """
    outputs = {}

    prefixes = [
        "play",
        "play the song",
        "play the track",
        "start playing",
        "start the song",
        "start the track",
        "can you play",
        "could you play",
        "please play",
    ]

    for song, artist in songs:
        song_lower = song.lower()
        artist_lower = artist.lower()

        for prefix in prefixes:
            # With just the song name
            inp1 = f"{prefix} {song_lower}"
            out1 = f"play('{song_lower}')"
            outputs[inp1] = out1

            # With song and artist
            inp2 = f"{prefix} {song_lower} by {artist_lower}"
            out2 = f"play('{song_lower} by {artist_lower}')"
            outputs[inp2] = out2

    return outputs

if __name__ == "__main__":
    
    songs = [
        ("Highway to Hell", "AC/DC"),
        ("Manchild", "Sabrina Carpenter"),
        ("Shape of You", "Ed Sheeran"),
        ("Blinding Lights", "The Weeknd"),
        ("Killing in the name", "rage against the machine"), 
        ("The battle of los angelas", "rage against the machine"),
        ("Snow on the beach", "taylor swift")
    ]

    variations = generate_variations(songs)

    with open("../data/music.json", "w") as f:
        json.dump(variations, f, indent=4)

    print(f"Generated {len(variations)} input-output pairs.")
