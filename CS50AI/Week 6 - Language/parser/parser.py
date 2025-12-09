from nltk.tokenize import word_tokenize
import nltk
import sys
import re

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> CS | CS Conj CS | CS Conj VP | NP | VP
CS -> NP VP

NP -> Det Adj N | N PP | Det NP | Adj NP | N
VP -> V NP | Adv VP |Adv V | V Adv | V | V PP Adv | V PP
PP -> P NP | P

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    
    # Lowercase and tokenize the sentence
    tokens = word_tokenize(sentence.lower())

    words = []
    # Keep only tokens that contain letters
    for token in tokens:
        if re.search(r"[a-z]", token):
            words.append(token)

    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []
    
    for s in tree.subtrees():
        count = 0
        
        # Check if the subtree 's' is labeled as NP
        if s.label() == "NP": 
            for s2 in s.subtrees():
                
                # Count how many NP-labeled subtrees exist within 's'
                if s2.label() == "NP":
                    count += 1

            # Keep only the subtrees of `s` with exacly one 'NP' node
            if count == 1:
                chunks.append(s)

    return chunks


if __name__ == "__main__":
    main()
