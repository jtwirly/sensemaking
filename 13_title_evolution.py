# -----------------------------------------------
#  13. Title Evolution:
# 
#  Conduct a word frequency analysis 
#  on course titles from 1996 and 2024 
#  to explore shifts in academic 
#  terminology and focus areas.
# -----------------------------------------------

import json
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string
import re

nltk.download('stopwords', quiet=True)

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def preprocess_title(title):
    # Convert to lowercase
    title = title.lower()
    # Remove course codes and numbers (including those with letters)
    title = re.sub(r'\b[a-z]+\d+[a-z]?\b|\b\d+\.\d+\b', '', title)
    # Remove punctuation
    title = ''.join([char for char in title if char not in string.punctuation])
    # Remove Roman numerals
    title = re.sub(r'\b(i{1,3}|iv|v|vi{1,3}|ix|x)\b', '', title)
    # Tokenize
    words = title.split()
    # Remove stopwords and short words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and len(word) > 2]
    return words

def get_word_frequencies(data, title_key):
    all_words = []
    for course in data:
        if title_key in course:
            all_words.extend(preprocess_title(course[title_key]))
    return Counter(all_words)

def plot_word_cloud(word_freq, year, output_file):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Most Common Words in Course Titles ({year})')
    plt.tight_layout(pad=0)
    plt.savefig(output_file)
    plt.close()

def plot_top_words(word_freq_1996, word_freq_2024, output_file):
    top_words_1996 = dict(word_freq_1996.most_common(15))
    top_words_2024 = dict(word_freq_2024.most_common(15))
    
    plt.figure(figsize=(12, 6))
    plt.bar(top_words_1996.keys(), top_words_1996.values(), alpha=0.5, label='1996')
    plt.bar(top_words_2024.keys(), top_words_2024.values(), alpha=0.5, label='2024')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 15 Words in Course Titles: 1996 vs 2024')
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def main():
    data_1996 = load_json_data('10_mit_1996.json')
    data_2024 = load_json_data('11_mit_2024.json')

    word_freq_1996 = get_word_frequencies(data_1996, 'course_title')
    word_freq_2024 = get_word_frequencies(data_2024, 'course_title')

    plot_word_cloud(word_freq_1996, '1996', 'wordcloud_1996.png')
    plot_word_cloud(word_freq_2024, '2024', 'wordcloud_2024.png')
    plot_top_words(word_freq_1996, word_freq_2024, 'top_words_comparison.png')

    print("Top 20 words in 1996:")
    print(word_freq_1996.most_common(20))
    print("\nTop 20 words in 2024:")
    print(word_freq_2024.most_common(20))

    # Analyze changes
    words_1996 = set(word_freq_1996.keys())
    words_2024 = set(word_freq_2024.keys())

    new_words = words_2024 - words_1996
    obsolete_words = words_1996 - words_2024

    print("\nNew words in 2024:")
    print(list(new_words)[:20])  # Print first 20 new words
    print("\nWords no longer used in 2024:")
    print(list(obsolete_words)[:20])  # Print first 20 obsolete words

if __name__ == "__main__":
    main()