// Certainly! Here's the algorithm for sorting an array in ascending order (commonly known as the "Bubble Sort" algorithm), followed by the corresponding C++ code:

// **Algorithm: Sorting an Array in Ascending Order (Bubble Sort)**

// **Input:**
// - An array A[] of size N.

// **Output:**
// - Array A[] sorted in ascending order.

// 1. Start with the first element (index 0) of the array.
// 2. Compare the current element (A[i]) with the next element (A[i+1]).
// 3. If A[i] > A[i+1], swap the two elements.
// 4. Repeat steps 2 and 3 for all elements in the array, starting from the first element.
// 5. After one pass through the array, the largest element will have "bubbled up" to the last position.
// 6. Repeat steps 1-5 for N-1 passes, each time reducing the number of elements to consider by 1.
// 7. The array is now sorted in ascending order.

// **C++ Code: Sorting an Array in Ascending Order (Bubble Sort)**


#include <iostream>

using namespace std;

int main() {
    int N;
    cout << "Enter the size of the array: ";
    cin >> N;

    int A[N];
    cout << "Enter " << N << " integer elements for the array:\n";
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    // Bubble Sort Algorithm
    for (int pass = 0; pass < N - 1; ++pass) {
        for (int i = 0; i < N - pass - 1; ++i) {
            if (A[i] > A[i + 1]) {
                // Swap A[i] and A[i+1]
                int temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
            }
        }
    }

    cout << "Sorted array in ascending order:\n";
    for (int i = 0; i < N; ++i) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}


// This code demonstrates the Bubble Sort algorithm to sort an array of integers in ascending order. It takes the array as input from the user and displays the sorted array.