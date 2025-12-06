#include <iostream> 
using namespace std; 
class Node {    
public:
    int data;
    Node* next;
    Node(int value) {
        data = value;
        next = nullptr;
    }
};
class Stack {
private:
    Node* top;
public:
    Stack() {
        top = nullptr;
    }
    ~Stack() {
        while (!isEmpty()) {
            pop();
        }
    }
    bool isEmpty() {
        return top == nullptr;
    }
    void push(int value) {
        Node* newNode = new Node(value);
        newNode->next = top;
        top = newNode;
        cout << " Insertion is successfull !! " << endl;
    }
    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty. Cannot pop element." << endl;
            return -1;
        } else {
            Node* temp = top;
            int poppedValue = temp->data;
            top = top->next;
            delete temp;
            cout << "Popped " << poppedValue << " from the stack." << endl;
            return poppedValue;
        }
    }
    
    void traverse() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
        } else {
            cout << "Stack elements:" << endl;
            Node* current = top;
            while (current != nullptr) {
                cout << current->data << endl;
                current = current->next;
            }
        }
    }
};
int main() {
    Stack stack;
    while (true) {
        cout << ":: Stack using Linked list " << endl;
		cout << "***** Menu ***** " << endl;
        cout << "1. Push" << endl;
        cout << "2. Pop" << endl;
        cout << "3. Display" << endl;
        cout << "4. Exit" << endl;
		cout << "Enter your Choice :" << endl;
        int choice;
        cin >> choice;
        switch (choice) {
            case 1:
                int value;
                cout << "Enter the value to push: ";
                cin >> value;
                stack.push(value);
                break;
            case 2:
                stack.pop();
                break;
            case 3:
                stack.traverse();
                break;
            case 4:
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
    return 0;
}