import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

def summarize(text, num_sentences=5):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower()) # Convert to lowercase for consistency

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequencies
    freq = FreqDist(words)

    # Calculate sentence scores based on word frequencies
    scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                if sentence not in scores:
                    scores[sentence] = freq[word]
                else:
                    scores[sentence] += freq[word]

    # Get the top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, scores, key=scores.get)

    return ' '.join(summary_sentences)

# Another example text
text = """
    Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the
    interaction between computers and humans through natural language. It enables computers to
    understand, interpret, and generate human language in a way that is valuable and meaningful.
    NLP has many applications including sentiment analysis, machine translation, chatbots, and more.
    """

summary = summarize(text)
print(summary)
