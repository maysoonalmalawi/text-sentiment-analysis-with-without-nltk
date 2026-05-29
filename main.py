# ============================================================
# Emotion Analysis from Text
# Reads a text file, filters meaningful words, matches them
# to emotions, and visualizes the results as a bar chart.
# ============================================================

import string
from collections import Counter
import matplotlib.pyplot as plt

# ── Step 1: Load and preprocess the text ──────────────────────

# Read the entire text file into a string
text = open("read.txt", encoding="utf-8").read()

# Convert all characters to lowercase for consistent comparison
lowercase_text = text.lower()

# Remove all punctuation so words like "happy!" and "happy" are treated the same
cleaned_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))

# Split the cleaned text into individual words (tokens)
tokenized_text = cleaned_text.split()

# ── Step 2: Remove stop words ─────────────────────────────────

# Common words that carry little meaning and should be excluded from analysis
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Keep only words that are NOT in the stop words list
final_words = []
for word in tokenized_text:
    if word not in stop_words:
        final_words.append(word)

# ── Step 3: Match words to emotions ───────────────────────────

# emotions.txt is expected to follow the format: word: emotion (one entry per line)
emotion_list = []  # Stores the emotion label for each matched word
word_list = []     # Stores the matched words found in the text

with open("emotions.txt", 'r') as file:
    for line in file:
        # Clean up each line by removing newlines, commas, and quotes
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()

        # Split each cleaned line into a word and its associated emotion
        word, emotion = clear_line.split(":")

        # If the emotion word appears in our filtered text, record the match
        if word in final_words:
            word_list.append(word)
            emotion_list.append(emotion)

# ── Step 4: Count and visualize emotion frequencies ───────────

# Count how many times each emotion appears
w = Counter(emotion_list)

# Plot the emotion counts as a bar chart
fig, ax = plt.subplots()
ax.bar(w.keys(), w.values())

# Add chart title and axis labels for clarity
ax.set_title("Emotion Frequency in Text")
ax.set_xlabel("Emotion")
ax.set_ylabel("Count")

# Rotate x-axis labels so emotion names don't overlap
fig.autofmt_xdate()

# Display the chart
plt.show()