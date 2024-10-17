import nltk
import editdistance
from collections import Counter
from nltk.corpus import stopwords
from nltk.util import ngrams
import string

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to read and preprocess text
def preprocess_text(file_path):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text = file.read().lower()
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return filtered_tokens

# Function to generate bigrams
def generate_bigrams(tokens):
    return list(ngrams(tokens, 2))

# Function to generate candidate words based on edit distance
def generate_candidates(word, dictionary, max_distance=2):
    candidates = [candidate for candidate in dictionary if editdistance.eval(word, candidate) <= max_distance]
    return candidates

# Function to spell-check the tokens using edit distance
def spell_check(tokens, dictionary):
    corrected_tokens = []
    for token in tokens:
        if token not in dictionary:
            # Generate candidate words based on edit distance
            candidates = generate_candidates(token, dictionary)
            if candidates:
                # Choose the most frequent candidate (this is basic, can be improved with a frequency model)
                corrected_token = max(candidates, key=dictionary.get)
                print(f"Correcting '{token}' to '{corrected_token}'")
                corrected_tokens.append(corrected_token)
            else:
                corrected_tokens.append(token)  # If no candidates, keep original token
        else:
            corrected_tokens.append(token)
    return corrected_tokens

# Function to build a dictionary from a corpus (for spell checking)
def build_dictionary(corpus):
    # Tokenize the corpus
    tokens = nltk.word_tokenize(corpus.lower())
    
    # Remove punctuation and stop words from the dictionary corpus
    tokens = [word for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Create a frequency dictionary
    return Counter(tokens)

# Example text for dictionary corpus
dictionary_corpus = """
Natural language processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret, and 
manipulate human language. NLP draws from many disciplines, including computer science and computational linguistics, in 
its pursuit to fill the gap between human communication and computer understanding.
"""

# Build a dictionary from the dictionary corpus
dictionary = build_dictionary(dictionary_corpus)

# File path to the 100-word text file (make sure to create 'sample_text.txt' with 100 words)
file_path = 'sample_text.txt'

# Step 1: Preprocess the text (remove stop words)
tokens = preprocess_text(file_path)
print("\nTokens after stopword removal:", tokens)

# Step 2: Perform spell checking
corrected_tokens = spell_check(tokens, dictionary)

# Step 3: Generate bigrams
bigrams = generate_bigrams(corrected_tokens)
print("\nBigrams:", bigrams)

# Save corrected tokens and bigrams to file (optional)
with open("corrected_output.txt", "w") as out_file:
    out_file.write("Corrected Tokens: " + ' '.join(corrected_tokens) + "\n")
    out_file.write("Bigrams: " + str(bigrams) + "\n")
