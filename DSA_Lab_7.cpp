#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* prev;
    Node* next;

    Node(int value) : data(value), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
private:
    Node* head;
    Node* tail;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    // Insertion at the front
    void insertFront(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }

    // Insertion at the end
    void insertEnd(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    // Insertion before a node with given data
    void insertBefore(int targetData, int value) {
        Node* newNode = new Node(value);
        Node* current = head;
        while (current) {
            if (current->data == targetData) {
                if (current->prev) {
                    current->prev->next = newNode;
                    newNode->prev = current->prev;
                } else {
                    head = newNode;
                }
                newNode->next = current;
                current->prev = newNode;
                return;
            }
            current = current->next;
        }
        cout << "Node with data " << targetData << " not found. Insertion failed." << std::endl;
    }

    // Insertion after a node with given data
    void insertAfter(int targetData, int value) {
        Node* newNode = new Node(value);
        Node* current = head;
        while (current) {
            if (current->data == targetData) {
                if (current->next) {
                    current->next->prev = newNode;
                    newNode->next = current->next;
                } else {
                    tail = newNode;
                }
                newNode->prev = current;
                current->next = newNode;
                return;
            }
            current = current->next;
        }
        std::cout << "Node with data " << targetData << " not found. Insertion failed." << std::endl;
    }

    // Deletion of the first node
    void deleteFirst() {
        if (!head) {
            std::cout << "List is empty. Deletion failed." << std::endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        if (head) {
            head->prev = nullptr;
        } else {
            tail = nullptr;
        }
        delete temp;
    }

    // Deletion of the last node
    void deleteLast() {
        if (!tail) {
            std::cout << "List is empty. Deletion failed." << std::endl;
            return;
        }
        Node* temp = tail;
        tail = tail->prev;
        if (tail) {
            tail->next = nullptr;
        } else {
            head = nullptr;
        }
        delete temp;
    }

    // Deletion of a node with given data
    void deleteNode(int targetData) {
        Node* current = head;
        while (current) {
            if (current->data == targetData) {
                if (current->prev) {
                    current->prev->next = current->next;
                } else {
                    head = current->next;
                }
                if (current->next) {
                    current->next->prev = current->prev;
                } else {
                    tail = current->prev;
                }
                delete current;
                return;
            }
            current = current->next;
        }
        std::cout << "Node with data " << targetData << " not found. Deletion failed." << std::endl;
    }

    // Display the list
    void display() {
        Node* current = head;
        while (current) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
};

int main() {
    DoublyLinkedList myList;

    int choice, value, targetData;

    while (true) {
        std::cout << "\nDoubly Linked List Menu:" << std::endl;
        std::cout << "1. Insert at the front" << std::endl;
        std::cout << "2. Insert at the end" << std::endl;
        std::cout << "3. Insert before a node" << std::endl;
        std::cout << "4. Insert after a node" << std::endl;
        std::cout << "5. Delete the first node" << std::endl;
        std::cout << "6. Delete the last node" << std::endl;
        std::cout << "7. Delete a node by data" << std::endl;
        std::cout << "8. Display the list" << std::endl;
        std::cout << "9. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter the value to insert at the front: ";
                std::cin >> value;
                myList.insertFront(value);
                break;
            case 2:
                cout << "Enter the value to insert at the end: ";
                cin >> value;
                myList.insertEnd(value);
                break;
            case 3:
                cout << "Enter the target data (before which to insert): ";
                cin >> targetData;
                cout << "Enter the value to insert: ";
                cin >> value;
                myList.insertBefore(targetData, value);
                break;
            case 4:
                cout << "Enter the target data (after which to insert): ";
                cin >> targetData;
                cout << "Enter the value to insert: ";
                cin >> value;
                myList.insertAfter(targetData, value);
                break;
            case 5:
                myList.deleteFirst();
                break;
            case 6:
                myList.deleteLast();
                break;
            case 7:
                cout << "Enter the data to delete: ";
                cin >> value;
                myList.deleteNode(value);
                break;
            case 8:
                cout << "Current List: ";
                myList.display();
                break;
            case 9:
                cout << "Exiting the program." << std::endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << std::endl;
        }
    }

    return 0;
}
 