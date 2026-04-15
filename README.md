# 🎵 Music Recommender Simulation

## Project Summary

This recommender uses content-based filtering to suggest songs
based on a user's genre, mood, and energy preferences. It scores
each song and returns the top matches.

---

## How The System Works

This recommender uses content-based filtering. It compares each
song's genre, mood, energy, and tempo to the user's preferences.

**Song features used:** genre, mood, energy, tempo_bpm, valence, danceability

**UserProfile stores:** preferred_genre, preferred_mood, preferred_energy, preferred_tempo

**Scoring Rule (one song):**
- Genre match = +2.0 points
- Mood match = +1.0 point
- Energy closeness = up to +1.0 point

**Ranking Rule (all songs):** Sort all songs by score, recommend the top 3.

---

## Getting Started

### Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python3 -m src.main
```

### Running Tests

```bash
pytest
```

---

## Experiments You Tried

**Default profile: pop, happy, energy 0.8**

Results:
- Sunrise City — Score: 3.98 — Genre match + Mood match
- Gym Hero — Score: 2.87 — Genre match only
- Rooftop Lights — Score: 1.96 — Mood match only

Genre match had the biggest impact. Songs matching both genre
and mood scored highest.

---

## Limitations and Risks

- Only works on a tiny 10-song catalog
- Does not understand lyrics or context
- May over-favor one genre if catalog is unbalanced

---

## Reflection

Building this recommender showed me that real systems like Spotify
use the same basic idea: compare user preferences to item features,
score everything, and rank the results. The main risk of bias is
that if the catalog has more pop songs, pop users always win.
Human judgment is still needed to ensure diverse and fair results.