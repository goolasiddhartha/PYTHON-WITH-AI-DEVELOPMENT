from collections import Counter
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Siddhartha studies computer science and he is learning NLP"
tokens = nltk.word_tokenize(text.lower())

word_counts = Counter(tokens)
print(word_counts)
