import nltk

# Define a context-free grammar for subject-verb agreement
grammar = nltk.CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> Det_SG N_SG
    NP_PL -> Det_PL N_PL
    VP_SG -> V_SG
    VP_PL -> V_PL
    Det_SG -> 'the'
    Det_PL -> 'the'
    N_SG -> 'cat'
    N_PL -> 'cats'
    V_SG -> 'chases'
    V_PL -> 'chase'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

def check_agreement(sentence):
    # Tokenize the sentence
    tokens = sentence.split()

    # Parse the sentence
    for tree in parser.parse(tokens):
        tree.pretty_print()
        return True

    return False

# Example usage
sentence1 = "the cat chases the cat"  # Correct agreement
sentence2 = "the cat chases the cats"  # Incorrect agreement

# Check agreement for sentence 1
result1 = check_agreement(sentence1)
print(f"Sentence 1 Agreement: {'Yes' if result1 else 'No'}")

# Check agreement for sentence 2
result2 = check_agreement(sentence2)
print(f"Sentence 2 Agreement: {'Yes' if result2 else 'No'}")
