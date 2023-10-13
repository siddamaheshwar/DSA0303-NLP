import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Define the text
text = "Apple is headquartered in Cupertino, California. Steve Jobs was one of the co-founders."

# Process the text using the NLP pipeline
doc = nlp(text)

# Iterate over the entities and print them
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
