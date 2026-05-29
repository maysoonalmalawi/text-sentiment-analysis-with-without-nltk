# ============================================================
# Sentiment Analysis from Text (NLTK Version)
# Reads a text file, filters meaningful words using NLTK,
# detects emotions, analyzes sentiment, and visualizes results.
# ============================================================

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# ── Step 1: Load and preprocess the text ──────────────────────

# Read the entire text file into a string
text = open("read.txt", encoding="utf-8").read()

# Convert all characters to lowercase
lowercase_text = text.lower()

# Remove all punctuation
cleaned_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))

# Tokenize the cleaned text using NLTK's word tokenizer
tokenized_text = word_tokenize(cleaned_text, language='english')

# ── Step 2: Remove stop words ─────────────────────────────────

# Use NLTK's built-in English stop words to filter out meaningless words
final_words = []
for word in tokenized_text:
    if word not in stopwords.words('english'):
        final_words.append(word)

# ── Step 3: Sentiment Analysis ────────────────────────────────

# Use NLTK's SentimentIntensityAnalyzer to get sentiment scores
score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
neg = score['neg']
pos = score['pos']

# Compare scores to determine and print the overall sentiment
if neg > pos:
    print("Negative Sentiment")
elif pos > neg:
    print("Positive Sentiment")
else:
    print("Neutral Sentiment")

# ── Step 4: Match words to emotions ───────────────────────────

# emotions.txt is expected to follow the format: word: emotion (one entry per line)
emotion_list = []  # Stores the emotion label for each matched word

with open("emotions.txt", 'r') as file:
    for line in file:
        # Clean up each line by removing newlines, commas, and quotes
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()

        # Split each cleaned line into a word and its associated emotion
        word, emotion = clear_line.split(":")

        # If the emotion word appears in our filtered text, record the match
        if word in final_words:
            emotion_list.append(emotion)

# ── Step 5: Count and visualize emotion frequencies ───────────

# Count how many times each emotion appears
w = Counter(emotion_list)

# Plot the emotion counts as a bar chart
fig, ax = plt.subplots()
ax.bar(w.keys(), w.values())

# Add chart title and axis labels for clarity
ax.set_title("Emotion Frequency & Sentiment Analysis")
ax.set_xlabel("Emotion")
ax.set_ylabel("Count")

# Rotate x-axis labels so emotion names don't overlap
fig.autofmt_xdate()

# Display the full sentiment scores as a text box on the chart
sentiment_text = (f"Positive: {score['pos']:.2f}\n"
                  f"Negative: {score['neg']:.2f}\n"
                  f"Neutral:  {score['neu']:.2f}")

ax.text(0.02, 0.95, sentiment_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

# Render and display the final chart
plt.show()