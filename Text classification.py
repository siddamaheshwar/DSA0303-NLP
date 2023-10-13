import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Download the IMDB dataset from nltk
nltk.download('movie_reviews')

from nltk.corpus import movie_reviews

# Load the movie reviews dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
import random
random.shuffle(documents)

# Extract the text and labels from the dataset
texts = [" ".join(words) for words, label in documents]
labels = [label for words, label in documents]

# Create a TF-IDF vectorizer to convert text data to numerical features
vectorizer = TfidfVectorizer()

# Transform the text data into TF-IDF features
X = vectorizer.fit_transform(texts)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Initialize and train the Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predict labels for the test set
y_pred = classifier.predict(X_test)

# Print classification report
report = classification_report(y_test, y_pred)
print(report)
