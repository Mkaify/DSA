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

    void insertAt(int data, int position) {
        if (position < 0)
            return;

        Node* newNode = new Node(data);

        if (position == 0 || head == NULL) {
            newNode->next = head;
            head = newNode;
            return;
        }

        Node* temp = head;
        int currentPos = 0;
        while (temp != NULL && currentPos < position - 1) {
            temp = temp->next;
            currentPos++;
        }

        if (temp == NULL)
            return;

        newNode->next = temp->next;
        temp->next = newNode;
    }

    void deleteAt(int position) {
        if (position < 0 || head == NULL)
            return;

        if (position == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        Node* temp = head;
        int currentPos = 0;
        while (temp != NULL && currentPos < position - 1) {
            temp = temp->next;
            currentPos++;
        }

        if (temp == NULL || temp->next == NULL)
            return;

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
        list.insertAt(data, i);
    }

    int choice;
    while (true) {
        cout << "Menu:" << endl;
        cout << "1. Insert Element at Position" << endl;
        cout << "2. Delete Element at Position" << endl;
        cout << "3. Print List" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            int insertValue, position;
            cout << "Enter a value to insert: ";
            cin >> insertValue;
            cout << "Enter the position to insert: ";
            cin >> position;
            list.insertAt(insertValue, position);
        } else if (choice == 2) {
            int position;
            cout << "Enter the position to delete: ";
            cin >> position;
            list.deleteAt(position);
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
