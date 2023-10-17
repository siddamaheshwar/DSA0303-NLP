import nltk
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased'
""")
parser = nltk.ChartParser(grammar)
sentence = "the cat chased the dog".split()
for tree in parser.parse(sentence):
    tree.pretty_print()
