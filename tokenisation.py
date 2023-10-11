import nltk

# Download the necessary resources (if not already downloaded)
nltk.download('punkt')

# Define a sentence for tokenization
sentence = "Tokenization is an important step in NLP."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Print the tokens
print(tokens)
