#include <iostream>
using namespace std;

// Define a class for a singly linked list node
class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

// Define a class for a sorted linked list
class LinkedList {
private:
    Node* head;

public:
    LinkedList() {
        head = NULL;
    }

    // Function to insert an element into the sorted linked list
    void insert(int data) {
        Node* newNode = new Node(data);

        if (head == NULL || data < head->data) {
            newNode->next = head;
            head = newNode;
            return;
        }

        Node* temp = head;
        while (temp->next != NULL && temp->next->data < data) {
            temp = temp->next;
        }

        newNode->next = temp->next;
        temp->next = newNode;
    }

    // Function to delete a node with a given data value
    void deleteNode(int data) {
        if (head == NULL) {
            return;
        }

        if (head->data == data) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        Node* temp = head;
        while (temp->next != NULL && temp->next->data != data) {
            temp = temp->next;
        }

        if (temp->next == NULL) {
            return;
        }

        Node* nodeToDelete = temp->next;
        temp->next = temp->next->next;
        delete nodeToDelete;
    }

    // Function to print the elements of the linked list
    void printList() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main() {
    LinkedList list;

    int size;
    cout << "Enter the size of the linked list: ";
    cin >> size;

    cout << "Enter the elements of the linked list : ";
    for (int i = 0; i < size; i++) {
        int data;
        cin >> data;
        list.insert(data);
    }
    cout << "Linked List: ";
            list.printList();

    int insertValue;
            cout << "Enter a value to insert into the list: ";
            cin >> insertValue;
            list.insert(insertValue);
    cout << "Linked List: ";
            list.printList();

            
    int deleteValue;
            cout << "Enter a value to delete from the list: ";
            cin >> deleteValue;
            list.deleteNode(deleteValue);
            
            
    cout << "Linked List: ";
            list.printList();



    return 0;
}

