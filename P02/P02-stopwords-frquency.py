import os
import pickle
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download NLTK stop words if not already installed
nltk.download('stopwords')

# Path to the folder containing the documents
DOCUMENT_FOLDER = r'C:\Users\Raja\OneDrive\Study material\SEM 7\SEM-7\NLP\NLP Practicals\P02\documents'
STORAGE_FILE = 'P02\corpus.pkl'  # File to store the serialized documents

# Function to read documents from a folder
def read_documents(folder_name):
    documents = []
    for filename in os.listdir(folder_name):
        if filename.endswith(".txt"):  
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

# Function to load documents from a serialized format using pickle
def load_documents(folder_name, storage_file):
    # Check if serialized documents exist
    if os.path.exists(storage_file):
        with open(storage_file, 'rb') as f:
            return pickle.load(f)
    else:
        # If not, read documents from the folder and serialize them
        documents = read_documents(folder_name)
        with open(storage_file, 'wb') as f:
            pickle.dump(documents, f)
        return documents

# Function to tokenize and count word frequency for a single document
def word_frequency(document):
    words = document.split()
    return Counter(words)

# Function to remove stop words and punctuation from a single document
def clean_document(document):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    
    words = document.split()
    filtered_words = [word.translate(translator).lower() for word in words if word.lower() not in stop_words]
    
    return " ".join(filtered_words), len(filtered_words)

# Function to print word frequencies and document sizes
def print_word_frequencies(documents):
    for i, doc in enumerate(documents, 1):
        word_freq = word_frequency(doc)
        total_words = len(doc.split())
        print(f"Document {i} Word Frequencies:")
        for word, freq in word_freq.items():
            print(f"{word} => {freq}")
        print(f"Total words: {total_words}")
        print()  # Print a newline between documents

# Function to print cleaned documents and their sizes
def print_cleaned_documents(documents):
    for i, doc in enumerate(documents, 1):
        cleaned_doc, cleaned_word_count = clean_document(doc)
        total_word_count = len(doc.split())
        print(f"Doc{i}")
        print(cleaned_doc)
        print(f"Original total words: {total_word_count}")
        print(f"Cleaned total words: {cleaned_word_count}")
        print()  # Print a newline between documents

# Main part of the program
def main():
    # Load documents from the specified folder
    documents = load_documents(DOCUMENT_FOLDER, STORAGE_FILE)

    # Provide options to the user
    print("Choose an option:")
    print("1) List words with their frequency")
    print("2) Print documents without stop words and punctuation")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print_word_frequencies(documents)
    elif choice == '2':
        print_cleaned_documents(documents)
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
