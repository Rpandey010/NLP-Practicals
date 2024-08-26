import os
import pickle


def read_documents(folder_name):
    documents = []
    for filename in os.listdir(folder_name):
        if filename.endswith(".txt"):  
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents


def store_documents(documents, storage_file):
    with open(storage_file, 'wb') as f:
        pickle.dump(documents, f)


def load_documents(storage_file):
    if os.path.exists(storage_file):
        with open(storage_file, 'rb') as f:
            return pickle.load(f)
    return []


def add_documents_from_folder(folder_name, storage_file):
    existing_documents = load_documents(storage_file)
    new_documents = read_documents(folder_name)
    
    # Only add documents that are not already in the corpus
    for new_doc in new_documents:
        if new_doc not in existing_documents:
            existing_documents.append(new_doc)
    
    store_documents(existing_documents, storage_file)


def add_document_from_input(storage_file):
    existing_documents = load_documents(storage_file)
    new_document = input("Enter the content of the new document:\n")
    
    # Optionally check if the document already exists in the corpus
    if new_document not in existing_documents:
        existing_documents.append(new_document)
        store_documents(existing_documents, storage_file)
        print("Document added!")
    else:
        print("Document already exists in the corpus.")

# Main part of the program
def main():
    # Replace this path with the path to your documents folder
    folder_name = r'P01\documents'
    storage_file = 'corpus.pkl'  # File to store the serialized documents

    # Add documents from the specified folder to the corpus
    add_documents_from_folder(folder_name, storage_file)

    # Load existing documents and print the total count
    documents = load_documents(storage_file)
    print(f"Total {len(documents)} documents.")

    # Provide options to the user
    print("Choose an option:")
    print("1) Read documents")
    print("2) Add more documents")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        for i, doc in enumerate(documents, 1):
            print(f"Document {i}:\n{doc}\n")
    elif choice == '2':
        add_document_from_input(storage_file)
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
