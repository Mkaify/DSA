#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() {
        head = NULL;
    }

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

    void deleteNode(int data) {
        if (head == NULL) { // no element in the list
            return;
        }

        if (head->data == data) { // value to be deleted is at first index
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

    cout << "Enter the elements of the linked list in sorted order: ";
    for (int i = 0; i < size; i++) {
        int data;
        cin >> data;
        list.insert(data);
    }

    int choice;
    while (true) {
        cout << "Menu:" << endl;
        cout << "1. Insert Element" << endl;
        cout << "2. Delete Element" << endl;
        cout << "3. Print List" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            int insertValue;
            cout << "Enter a value to insert into the list: ";
            cin >> insertValue;
            list.insert(insertValue);
        } else if (choice == 2) {
            int deleteValue;
            cout << "Enter a value to delete from the list: ";
            cin >> deleteValue;
            list.deleteNode(deleteValue);
        } else if (choice == 3) {
            cout << "Linked List: ";
            list.printList();
        } else if (choice == 4) {
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
