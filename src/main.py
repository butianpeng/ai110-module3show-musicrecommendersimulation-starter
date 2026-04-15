"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.9},
        {"name": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.35},
        {"name": "Deep Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.95},
    ]

    for profile in profiles:
        print(f"\n=== Profile: {profile['name']} ===")
        recommendations = recommend_songs(profile, songs, k=3)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()
if __name__ == "__main__":
    main()