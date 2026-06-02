# Text Sentiment Analysis With and Without NLTK

Text emotion detection and sentiment analysis using Python, with and without NLTK, with Matplotlib visualizations.

## Overview

This project contains two Python scripts that analyze the emotional tone of a text file and visualize the results as a bar chart.

| Feature | `main_no_nltk.py` | `main_nltk.py` |
|---|---|---|
| Tokenization | Built-in `.split()` | NLTK `word_tokenize` |
| Stop words | Manual list | NLTK built-in |
| Emotion detection | ✅ | ✅ |
| Sentiment analysis | ❌ | ✅ |
| Visualization | Bar chart | Bar chart + sentiment scores |

## Files

| File | Description |
|---|---|
| `main_no_nltk.py` | Emotion analysis without NLTK |
| `main_nltk.py` | Emotion analysis with NLTK + sentiment analysis |
| `read.txt` | The text used for analysis |
| `emotions.txt` | Word-to-emotion mapping (format: `word: emotion`) |

## Sample Text

The included `read.txt` contains Mark Zuckerberg's 2017 Harvard Commencement Address, where he speaks about purpose, equality, and building community. It serves as a good sample for testing the scripts, as the speech has a largely positive and motivational tone which makes the sentiment and emotion outputs easy to interpret.

## Requirements

Install the required libraries:

```bash
pip install matplotlib nltk
```

Then download the required NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
```

## Usage

Add the text you want to analyze to `read.txt`, then run either script:

```bash
# Without NLTK
python main_no_nltk.py

# With NLTK
python main_nltk.py
```

## Output

Both scripts display a bar chart showing emotion frequencies detected in the text. The NLTK version additionally shows a sentiment score box on the chart with positive, negative, and neutral scores.
