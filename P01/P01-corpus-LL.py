import os
import pickle

# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def to_list(self):
        documents = []
        current_node = self.head
        while current_node:
            documents.append(current_node.data)
            current_node = current_node.next
        return documents

    def from_list(self, documents):
        for document in documents:
            self.append(document)

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Function to read documents
def read_documents(folder_name):
    documents = []
    for filename in os.listdir(folder_name):
        if filename.endswith(".txt"):  
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

# Function to store documents in a serialized format using pickle
def store_documents(linked_list, storage_file):
    documents = linked_list.to_list()
    with open(storage_file, 'wb') as f:
        pickle.dump(documents, f)

# Function to load documents from the serialized format
def load_documents(storage_file):
    linked_list = LinkedList()
    if os.path.exists(storage_file):
        with open(storage_file, 'rb') as f:
            documents = pickle.load(f)
            linked_list.from_list(documents)
    return linked_list

# Function to add new documents from a specified folder to the existing corpus
def add_documents_from_folder(folder_name, storage_file):
    linked_list = load_documents(storage_file)
    new_documents = read_documents(folder_name)

    # Only add documents that are not already in the corpus
    for new_doc in new_documents:
        if new_doc not in linked_list.to_list():
            linked_list.append(new_doc)

    store_documents(linked_list, storage_file)

# Function to add a new document directly from input
def add_document_from_input(storage_file):
    linked_list = load_documents(storage_file)
    new_document = input("Enter the content of the new document:\n")

    # Optionally check if the document already exists in the corpus
    if new_document not in linked_list.to_list():
        linked_list.append(new_document)
        store_documents(linked_list, storage_file)
        print("Document added!")
    else:
        print("Document already exists in the corpus.")

# Main part of the program
def main():
    # Replace this path with the path to your documents folder
    folder_name = r'P01\documents'
    storage_file = 'P01\corpus.pkl'  # File to store the serialized documents

    # Add documents from the specified folder to the corpus
    add_documents_from_folder(folder_name, storage_file)

    # Load existing documents and print the total count
    linked_list = load_documents(storage_file)
    print(f"Total {len(linked_list)} documents.")

    # Provide options to the user
    print("Choose an option:")
    print("1) Read documents")
    print("2) Add more documents")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        current_node = linked_list.head
        i = 1
        while current_node:
            print(f"Document {i}:\n{current_node.data}\n")
            current_node = current_node.next
            i += 1
    elif choice == '2':
        add_document_from_input(storage_file)
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
