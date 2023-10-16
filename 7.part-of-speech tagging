import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
text = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
