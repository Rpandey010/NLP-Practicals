import nltk
import editdistance
from collections import defaultdict, Counter
import itertools

# Download required NLTK data
nltk.download('punkt')

# Sample corpus (you can use a larger text corpus in practice)
corpus = """I love NLP. Natural language processing is amazing. I love learning about artificial intelligence. 
NLP is a branch of AI. I love solving NLP problems."""
tokens = nltk.word_tokenize(corpus.lower())

# Function to generate n-grams (unigram, bigram, trigram)
def generate_ngrams(tokens, n=1):
    return list(nltk.ngrams(tokens, n))

# Create unigram, bigram, and trigram models
unigrams = Counter(generate_ngrams(tokens, n=1))
bigrams = Counter(generate_ngrams(tokens, n=2))
trigrams = Counter(generate_ngrams(tokens, n=3))

# Function to generate candidate words based on edit distance
def generate_candidates(word, dictionary, max_distance=2):
    candidates = [candidate for candidate in dictionary if editdistance.eval(word, candidate) <= max_distance]
    return candidates

# Function to score candidates using unigram model
def unigram_score(candidate, unigram_model):
    return unigram_model[(candidate,)]

# Function to score candidates using bigram context
def bigram_score(prev_word, candidate, bigram_model):
    return bigram_model[(prev_word, candidate)]

# Function to score candidates using trigram context
def trigram_score(prev_word, candidate, next_word, trigram_model):
    return trigram_model[(prev_word, candidate, next_word)]

# Example usage
word_to_correct = "loev"
dictionary = set(tokens)  # Simulate dictionary from tokens

# Step 1: Generate candidate words based on edit distance
candidates = generate_candidates(word_to_correct, dictionary)
print(f"Candidates for '{word_to_correct}': {candidates}")

# Step 2: Rank candidates using unigram, bigram, and trigram models

# Assume previous and next words are available for contextual correction
previous_word = "i"
next_word = "nlp"

# Unigram ranking
unigram_scores = {candidate: unigram_score(candidate, unigrams) for candidate in candidates}
print("Unigram scores:", unigram_scores)

# Bigram ranking (using previous word context)
bigram_scores = {candidate: bigram_score(previous_word, candidate, bigrams) for candidate in candidates}
print("Bigram scores:", bigram_scores)

# Trigram ranking (using both previous and next word context)
trigram_scores = {candidate: trigram_score(previous_word, candidate, next_word, trigrams) for candidate in candidates}
print("Trigram scores:", trigram_scores)

# Final correction based on highest trigram score (or fallback to bigram/unigram)
best_correction = max(trigram_scores, key=trigram_scores.get)
print(f"Best correction for '{word_to_correct}': {best_correction}")
