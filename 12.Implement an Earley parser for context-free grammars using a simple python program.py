import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = "the dog chased the cat".split()  # Split the sentence into a list of words
for tree in parser.parse(sentence):
    tree.pretty_print()
