import os
import nltk
from nltk.util import ngrams

# Download NLTK data if not already downloaded
nltk.download('punkt')

# Step 1: Read the text file
def read_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert to lowercase
    return text

# Step 2: Tokenize the text and extract unique words
def unique_words(text):
    tokens = nltk.word_tokenize(text)
    unique_tokens = list(set([word for word in tokens if word.isalpha()]))  # Only alphabetic words
    return unique_tokens

# Step 3: Create character bigrams for each word
def word_bigrams(word):
    return list(ngrams(word, 2))

# Step 4: Get bigrams for a target word
def target_bigrams(target_word):
    return list(ngrams(target_word, 2))

# Step 5: Compare bigrams of the target word with bigrams of unique words and form a candidate list
def compare_bigrams(target_word, unique_words_list):
    target_word_bigrams = target_bigrams(target_word)
    candidate_list = []

    for word in unique_words_list:
        word_bigrams_list = word_bigrams(word)
        # Compare bigrams
        common_bigrams = set(target_word_bigrams).intersection(set(word_bigrams_list))
        if common_bigrams:
            candidate_list.append((word, len(common_bigrams)))  # Append word and count of matching bigrams
    
    return candidate_list

# Function to write bigrams to a file
def write_bigrams_to_file(file_path, bigrams):
    with open(file_path, 'w') as file:
        for bigram in bigrams:
            file.write(f"{bigram}\n")

# Step 6: Run the program
def main():
    # File path to the text document
    file_path = 'P05\Bi-Gram Friendly.txt'
    
    # Read text
    text = read_text(file_path)
    
    # Extract unique words from the text
    unique_words_list = unique_words(text)
    
    # Write bigrams for unique words to file
    unique_word_bigrams = []
    for word in unique_words_list:
        unique_word_bigrams.extend(word_bigrams(word))
    write_bigrams_to_file('Unique_words_bigram.txt', unique_word_bigrams)
    
    # Display the unique words
    print("Unique Words in the Document:")
    print(unique_words_list)
    
    # Write unique words to file
    with open('Unique_Words.txt', 'w') as file:
        for word in unique_words_list:
            file.write(f"{word}\n")
    
    # Take input for the target word
    target_word = input("Enter the target word: ").lower()
    
    # Get the list of candidate words based on bigram comparison
    candidate_list = compare_bigrams(target_word, unique_words_list)
    
    # Write bigrams for the target word to file
    target_word_bigrams = target_bigrams(target_word)
    write_bigrams_to_file('target_words_bigrams.txt', target_word_bigrams)
    
    # Sort the candidate list based on the number of matching bigrams (higher first)
    candidate_list.sort(key=lambda x: x[1], reverse=True)
    
    # Display the candidate list
    print("\nCandidate List (word, matching bigrams count):")
    for word, match_count in candidate_list:
        print(f"{word}: {match_count}")
    
    # Write candidate list to file
    with open('Candidate_List.txt', 'w') as file:
        for word, match_count in candidate_list:
            file.write(f"{word}: {match_count}\n")

if __name__ == '__main__':
    main()

