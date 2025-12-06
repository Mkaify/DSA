#include <iostream>

using namespace std;

// Function to find the location to delete ITEM in the array A
int Find_Location_To_Delete(int A[], int N, int ITEM) {
    int K = -1;

    for (int I = 0; I < N; ++I) {
        if (A[I] == ITEM) {
            K = I; // Found item to delete
            return K;
        }
    }

    return K; // Item not found in the array
}

// Function to delete ITEM from the array A at position K
void DELETE(int A[], int &N, int K, int ITEM) {
    ITEM = A[K];

    for (int J = K; J < N - 1; ++J) {
        A[J] = A[J + 1]; // Move elements upward
    }

    N = N - 1; // Reset N
}

int main() {
    int N;
    cout << "Enter the number of elements in the array: ";
    cin >> N;

    if (N == 0) {
        cout << "Underflow. Array is Empty." << endl;
        return 1; // Exit with an error code
    }

    int A[N];

    cout << "Enter " << N << " integer values for the array:\n";
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int ITEM;
    cout << "Enter the ITEM to be deleted: ";
    cin >> ITEM;

    int K = Find_Location_To_Delete(A, N, ITEM);

    if (K != -1) {
        DELETE(A, N, K, ITEM);
        cout << "Item deleted successfully." << endl;
    } else {
        cout << "Not Found in array." << endl;
    }

    cout << "Array after deletion:\n";
    for (int i = 0; i < N; ++i) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}
