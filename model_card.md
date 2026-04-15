# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

## 2. Goal / Task
Suggest the top 3 songs from a small catalog that best match a
user's preferred genre, mood, and energy level.

## 3. Data Used
10 songs in data/songs.csv. Features include genre, mood, energy,
tempo, valence, and danceability. Only mainstream Western genres
are represented. No songs were added or removed.

## 4. Algorithm Summary
Each song gets a score. Genre match adds 2.0 points. Mood match
adds 1.0 point. Energy closeness adds up to 1.0 point. Songs are
ranked from highest to lowest score and the top 3 are returned.

## 5. Observed Behavior / Biases
Genre match dominates the score. A rock user sometimes gets pop
songs because mood match outweighs genre mismatch. Users who
prefer ambient or jazz get poor results since the catalog has
very few of those songs.

## 6. Evaluation Process
Tested 3 profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock.
Lofi and Rock results felt accurate. Pop occasionally surfaced
non-pop songs due to strong mood matches.

## 7. Intended Use and Non-Intended Use
Designed for classroom exploration only. Not for real users or
production music apps.

## 8. Ideas for Improvement
- Add more songs across more genres
- Add tempo range matching
- Balance diversity so top results aren't all the same genre

## 9. Personal Reflection
My biggest learning was that even simple math can feel smart.
AI tools helped me write code faster, but I had to double-check
the scoring logic myself. What surprised me most was how much
one weight (genre) could control all the results.