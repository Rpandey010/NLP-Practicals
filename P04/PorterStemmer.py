from nltk.stem import PorterStemmer
import re
import string
import os

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Define a rule-based approach for guessing root forms
def rule_based_root(word):
    rules = [
        (r'ies$', 'y'),    # plurals like "batteries" -> "battery"
        (r'ves$', 'f'),    # words ending in "ves" like "wolves" -> "wolf"
        (r'sses$', 'ss'),  # words like "processes" -> "process"
        (r'([aeiou])es$', r'\1'),  # words ending in vowel + es like "dishes" -> "dish"
        (r'([aeiou])ed$', r'\1'),  # past tense like "baked" -> "bake"
        (r'ing$', ''),     # words ending in "ing" like "running" -> "run"
        (r'ed$', ''),      # words ending in "ed" like "danced" -> "dance"
        (r's$', ''),       # remove plurals like "cats" -> "cat"
        (r'er$', ''),      # comparatives like "deeper" -> "deep"
        (r'est$', ''),     # superlatives like "deepest" -> "deep"
        (r'th$', ''),      # nouns/adjectives like "warmth" -> "warm"
        (r'ly$', ''),      # adverbs like "quickly" -> "quick"
        (r'ness$', ''),    # nouns like "happiness" -> "happy"
        (r'ful$', ''),     # adjectives like "beautiful" -> "beauty"
        (r'ous$', ''),     # adjectives like "dangerous" -> "danger"
        (r'able$', ''),    # adjectives like "comfortable" -> "comfort"
        (r'less$', ''),    # adjectives like "careless" -> "care"
        (r'ize$', ''),     # verbs like "realize" -> "real"
        (r'ify$', ''),     # verbs like "intensify" -> "intense"
        (r'ise$', ''),     # verbs like "realise" -> "real"
        (r'ate$', ''),     # verbs like "activate" -> "active"
        (r'ify$', ''),     # verbs like "intensify" -> "intense"
        (r'ize$', ''),     # verbs like "realize" -> "real"
        (r'ise$', ''),     # verbs like "realise" -> "real"
    
        
    ]
    
    for pattern, repl in rules:
        if re.search(pattern, word):
            return re.sub(pattern, repl, word)
    
    return word  # Return the original word if no rule matches

# Function to apply stemming and rule-based guessing
def stem_or_guess(word):
    # Use Porter Stemmer first
    stemmed_word = stemmer.stem(word)
    
    # If the stemmed word looks the same as the input word, apply rule-based approach
    if stemmed_word == word:
        return rule_based_root(word)
    return stemmed_word

# Read text from file and process
def process_corpus(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    # Read the corpus from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and split text into words
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    
    # Process each word
    for word in words:
        root_word = stem_or_guess(word.lower())
        print(f"Original: {word}, Root: {root_word}")

# Provide the path to your text file
file_path = 'P04/textCorpus.txt'
process_corpus(file_path)
