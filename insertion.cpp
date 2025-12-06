#include <iostream>
using namespace std;

const int SIZE = 10; // Size of the array

// Function to find the location to insert ITEM in the sorted array A
int Find_Location_To_Insert(int A[], int N, int ITEM) {
    int LB = 0;
    int UB = N - 1;
    int K = 0;

    for (K = LB; K <= UB; ++K) {
        if (A[K] > ITEM) {
            return K; // Insertion at front or in the middle
        }
    }
    return K; // Insertion at the end of the array
}

// Function to insert ITEM in the array A at position K
void INSERT(int A[], int &N, int K, int ITEM) {
    int J = N - 1;

    while (J >= K) {
        A[J + 1] = A[J]; // Move elements downward
        J = J - 1;
    }

    A[K] = ITEM; // Insert element at position K
    N = N + 1;   // Reset N
}

int main() {
    int N = 0;
    int A[SIZE];

    // User input
    cout << "Enter the number of elements (N) in the array (up to " << SIZE << "): ";
    cin >> N;

    if (N == SIZE) {
        cout << "Overflow, Array is Full." << std::endl;
        return 1; // Exit with an error code
    }

    cout << "Enter " << N << " integer values for the array:\n";
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int ITEM;
    cout << "Enter the ITEM to be inserted: ";
    cin >> ITEM;

    int K = Find_Location_To_Insert(A, N, ITEM);
    INSERT(A, N, K, ITEM);

    cout << "Array after insertion:\n";
    for (int i = 0; i < N; ++i) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}
