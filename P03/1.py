import os
import math
from collections import Counter


folder_path = r'Lab 2'  


def load_documents(folder_path):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
                filenames.append(filename)
    return documents, filenames


def tokenize(document):
    words = document.lower().split()
    return Counter(words)


def dot_product(vector1, vector2):
    return sum(vector1[word] * vector2.get(word, 0) for word in vector1)


def magnitude(vector):
    return math.sqrt(sum(count ** 2 for count in vector.values()))


def cosine_similarity(vector1, vector2):
    if magnitude(vector1) == 0 or magnitude(vector2) == 0:
        return 0.0
    return dot_product(vector1, vector2) / (magnitude(vector1) * magnitude(vector2))

documents, filenames = load_documents(folder_path)

vectors = [tokenize(doc) for doc in documents]

num_docs = len(vectors)
cosine_sim_matrix = [[0] * num_docs for _ in range(num_docs)]

for i in range(num_docs):
    for j in range(num_docs):
        if i == j:
            cosine_sim_matrix[i][j] = 1.0  
        else:
            cosine_sim_matrix[i][j] = cosine_similarity(vectors[i], vectors[j])

all_words = sorted(set(word for vector in vectors for word in vector))

word_freq_dict = {word: [0] * num_docs for word in all_words}
for i, vector in enumerate(vectors):
    for word, freq in vector.items():
        word_freq_dict[word][i] = freq

word_col_width = max(len(word) for word in all_words) + 2
doc_col_width = max(len(filename) for filename in filenames) + 2

output_file = 'word_frequencies.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    
    header = "Word".ljust(word_col_width) + "".join(filename.ljust(doc_col_width) for filename in filenames) + "\n"
    file.write(header)
    file.write("-" * len(header) + "\n")
       
    for word in all_words:
        row = word.ljust(word_col_width) + "".join(str(freq).rjust(doc_col_width) for freq in word_freq_dict[word]) + "\n"
        file.write(row)

print("Cosine Similarity Matrix:")
for row in cosine_sim_matrix:
    print(row)

import pandas as pd
cosine_df = pd.DataFrame(cosine_sim_matrix, index=filenames, columns=filenames)
print("\nCosine Similarity DataFrame:")
print(cosine_df)

print(f"\nWord frequencies document-wise have been written to {output_file}")
