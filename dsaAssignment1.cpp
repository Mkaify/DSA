#include <iostream>
#include <string>

using namespace std;

template <class T>
class DLLNode {
public:
    DLLNode() : next(nullptr), prev(nullptr) {}
    DLLNode(const T& el, DLLNode* n = nullptr, DLLNode* p = nullptr) : info(el), next(n), prev(p) {}
    T info;
    DLLNode* next;
    DLLNode* prev;
};

template <class T>
class DoublyLinkedList {
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}
    void addToDLLTail(const T&);
    T deleteFromDLLTail();
    void displayList();

    DLLNode<T>* head;
    DLLNode<T>* tail;
};

template <class T>
void DoublyLinkedList<T>::addToDLLTail(const T& el) {
    DLLNode<T>* newNode = new DLLNode<T>(el);
    if (!head) {
        head = tail = newNode;
    } else {
        newNode->prev = tail;
        tail->next = newNode;
        tail = newNode;
    }
}

template <class T>
T DoublyLinkedList<T>::deleteFromDLLTail() {
    if (!head) {
        cerr << "No passengers to remove." << endl;
        exit(1);
    }

    T passengerInfo = tail->info;
    if (head == tail) {
        delete tail;
        head = tail = nullptr;
    } else {
        DLLNode<T>* temp = tail;
        tail = tail->prev;
        tail->next = nullptr;
        delete temp;
    }

    return passengerInfo;
}

template <class T>
void DoublyLinkedList<T>::displayList() {
    DLLNode<T>* current = head;
    while (current) {
        cout << current->info << endl;
        current = current->next;
    }
}

class Passenger {
public:
    string name;
    Passenger* next;

    Passenger(const string& n) : name(n), next(nullptr) {}
};

class Flight {
public:
    string flightName;
    DoublyLinkedList<Passenger> passengers;
    Flight* next;

    Flight(const string& name) : flightName(name), next(nullptr) {}
};

class ReservationSystem {
private:
    DoublyLinkedList<Flight> flights;

public:
    ReservationSystem() {}

    void addFlight(const string& flightName) {
        Flight newFlight(flightName);
        flights.addToDLLTail(newFlight);
    }

    void reserveTicket(const string& flightName, const string& passengerName) {
        DLLNode<Flight>* currentFlightNode = flights.head;
        while (currentFlightNode) {
            if (currentFlightNode->info.flightName == flightName) {
                Passenger newPassenger(passengerName);
                currentFlightNode->info.passengers.addToDLLTail(newPassenger);
                cout << "Reservation for " << passengerName << " on " << flightName << " successful." << endl;
                return;
            }
            currentFlightNode = currentFlightNode->next;
        }
        cout << "Flight " << flightName << " not found." << endl;
    }

    void cancelReservation(const string& flightName, const string& passengerName) {
        DLLNode<Flight>* currentFlightNode = flights.head;
        while (currentFlightNode) {
            if (currentFlightNode->info.flightName == flightName) {
                DLLNode<Passenger>* currentPassengerNode = currentFlightNode->info.passengers.head;
                while (currentPassengerNode) {
                    if (currentPassengerNode->info.name == passengerName) {
                        currentFlightNode->info.passengers.deleteFromDLLTail();
                        cout << "Reservation for " << passengerName << " on " << flightName << " canceled." << endl;
                        return;
                    }
                    currentPassengerNode = currentPassengerNode->next;
                }
                cout << "No reservation found for " << passengerName << " on " << flightName << "." << endl;
                return;
            }
            currentFlightNode = currentFlightNode->next;
        }
        cout << "Flight " << flightName << " not found." << endl;
    }

    void checkReservation(const string& passengerName) {
        DLLNode<Flight>* currentFlightNode = flights.head;
        bool found = false;

        while (currentFlightNode) {
            DLLNode<Passenger>* currentPassengerNode = currentFlightNode->info.passengers.head;
            while (currentPassengerNode) {
                if (currentPassengerNode->info.name == passengerName) {
                    cout << passengerName << " has a reservation on " << currentFlightNode->info.flightName << "." << endl;
                    found = true;
                    break;
                }
                currentPassengerNode = currentPassengerNode->next;
            }
            currentFlightNode = currentFlightNode->next;
        }

        if (!found) {
            cout << "No reservation found for " << passengerName << " on any flight." << endl;
        }
    }

    void displayPassengers(const string& flightName) {
        DLLNode<Flight>* currentFlightNode = flights.head;
        while (currentFlightNode) {
            if (currentFlightNode->info.flightName == flightName) {
                currentFlightNode->info.passengers.displayList();
                return;
            }
            currentFlightNode = currentFlightNode->next;
        }
        cout << "Flight " << flightName << " not found." << endl;
    }
};

int main() {
    ReservationSystem reservationSystem;

    while (true) {
        cout << "\nAirline Ticket Reservation System" << endl;
        cout << "1. Add Flight" << endl;
        cout << "2. Reserve a Ticket" << endl;
        cout << "3. Cancel Reservation" << endl;
        cout << "4. Check Reservation" << endl;
        cout << "5. Display Passengers for a Flight" << endl;
        cout << "6. Quit" << endl;

        int choice;
        cin >> choice;
        cin.ignore(); // Clear the newline character from the input buffer

        switch (choice) {
            case 1: {
                string flightName;
                cout << "Enter the flight name: ";
                getline(cin, flightName);
                reservationSystem.addFlight(flightName);
                break;
            }
            case 2: {
                string flightName, passengerName;
                cout << "Enter the flight name: ";
                getline(cin, flightName);
                cout << "Enter the passenger's name: ";
                getline(cin, passengerName);
                reservationSystem.reserveTicket(flightName, passengerName);
                break;
            }
            case 3: {
                string flightName, passengerName;
                cout << "Enter the flight name: ";
                getline(cin, flightName);
                cout << "Enter the passenger's name: ";
                getline(cin, passengerName);
                reservationSystem.cancelReservation(flightName, passengerName);
                break;
            }
            case 4: {
                string passengerName;
                cout << "Enter the passenger's name: ";
                getline(cin, passengerName);
                reservationSystem.checkReservation(passengerName);
                break;
            }
            case 5: {
                string flightName;
                cout << "Enter the flight name: ";
                getline(cin, flightName);
                reservationSystem.displayPassengers(flightName);
                break;
            }
            case 6:
                cout << "Thank you for using the Airline Ticket Reservation System!" << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}

