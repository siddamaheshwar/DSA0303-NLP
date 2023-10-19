import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

def perform_ner(text):
    # Process the text using SpaCy NLP pipeline
    doc = nlp(text)
    
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

# Example usage
text = "Barack Obama was the 44th President of the United States. He was born in Hawaii."

# Perform Named Entity Recognition
entities = perform_ner(text)

# Print the extracted entities
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
