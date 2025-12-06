#include <iostream>
using namespace std;

template<class T>
class DLLNode {
public:
    DLLNode() {
        next = prev = nullptr;
    }
    DLLNode(const T& el, DLLNode *n = nullptr, DLLNode *p = nullptr) {
        info = el;
        next = n;
        prev = p;
    }
    T info;
    DLLNode *next, *prev;
};

template<class T>
class DoublyLinkedList {
public:
    DoublyLinkedList() {
        head = tail = nullptr;
    }
    
    void addToDLLTail(const T& el) {
        if (!head) {
            head = tail = new DLLNode<T>(el);
        } else {
            tail->next = new DLLNode<T>(el);
            tail->next->prev = tail;
            tail = tail->next;
        }
    }

    void reverseList() {
        if (!head || head == tail) {
            return; // Nothing to reverse for empty list or list with one element
        }

        DLLNode<T>* current = head;
        while (current) {
            DLLNode<T>* temp = current->prev;
            current->prev = current->next;
            current->next = temp;
            current = current->prev; // Move to the next node
        }

        // Swap head and tail pointers
        DLLNode<T>* temp = head;
        head = tail;
        tail = temp;
    }

    void display() {
        DLLNode<T>* current = head;

        while (current) {
            cout << current->info;
            if (current->next) {
                cout << " <==> ";
            }
            current = current->next;
        }
        cout << endl;
    }

private:
    DLLNode<T> *head, *tail;
};

int main() {
    DoublyLinkedList<int> list;
    cout<<"Enter the size of Doublly LinkedList: ";
    int size;
    cin>>size;


    // Add elements to the list
    for (int i = 1; i <= size; i++) {
        int el;
        cin>>el;
        list.addToDLLTail(el);
    }

    cout << "Original doubly linked list:" << endl;
    list.display();

    // Reverse the list
    list.reverseList();

    cout << "Reverse doubly linked list:" << endl;
    list.display();

    return 0;
}
