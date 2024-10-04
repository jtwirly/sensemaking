# -----------------------------------------------
#  6. Word Frequency Analysis:
# 
#  Objective: Perform a word frequency count 
#  on the course titles.
# 
#  Tools/Resources: You can use a “map reduce” 
#  style word counting approach.
# -----------------------------------------------

import re
from collections import Counter

# Read in the extracted titles
with open("extracted_titles.txt", "r") as file:
    titles = file.read().splitlines()

# Define a function to preprocess each title
def preprocess(title):
    # Convert to lowercase
    title = title.lower()
    # Remove punctuation and digits
    title = re.sub(r'[^a-zA-Z\s]', '', title)
    # Split into words
    words = title.split()
    return words

# Preprocess each title and flatten into a single list of words
words = [word for title in titles for word in preprocess(title)]

# Define stopwords
stopwords = ["and", "the", "for", "in", "of", "a", "an", "to", "at", "on", "with", "from", "by", "as", "cps"]

# Remove stopwords
words = [word for word in words if word not in stopwords]

# Count the frequency of each word
word_counts = Counter(words)

# Write the word frequencies to a file
with open("word_frequencies.txt", "w") as file:
    for word, count in word_counts.most_common():
        file.write(f"{word}: {count}\n")