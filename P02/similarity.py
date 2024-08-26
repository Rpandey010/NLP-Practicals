from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    """Read the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    """Calculate similarity percentage between two texts."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    similarity_percentage = similarity_matrix[0][0] * 100
    return similarity_percentage

def main():
    # Paths to your documents
    doc1_path = 'P02\document1.txt'
    doc2_path = 'P02\document2.txt'

    # Read documents
    text1 = read_file(doc1_path)
    text2 = read_file(doc2_path)

    # Calculate similarity
    similarity_percentage = calculate_similarity(text1, text2)
    
    # Print similarity percentage
    print(f"The similarity between the two documents is {similarity_percentage:.2f}%")

if __name__ == "__main__":
    main()
