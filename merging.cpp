#include <iostream>

using namespace std;

int main() {
    int N, M;
    cout << "Enter the size of the first sorted array (N): ";
    cin >> N;

    int A[N];
    cout << "Enter " << N << " sorted elements for the first array:\n";
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    cout << "Enter the size of the second sorted array (M): ";
    cin >> M;

    int B[M];
    cout << "Enter " << M << " sorted elements for the second array:\n";
    for (int i = 0; i < M; ++i) {
        cin >> B[i];
    }

    int C[N + M]; // Initialize an array to hold the merged result
    int i = 0, j = 0, k = 0; // Pointers for A[], B[], and C[]

    // Merge the two sorted arrays into C[]
    while (i < N && j < M) {
        if (A[i] <= B[j]) {
            C[k] = A[i];
            ++i;
        } else {
            C[k] = B[j];
            ++j;
        }
        ++k;
    }

    // Copy remaining elements from A[] to C[]
    while (i < N) {
        C[k] = A[i];
        ++i;
        ++k;
    }

    // Copy remaining elements from B[] to C[]
    while (j < M) {
        C[k] = B[j];
        ++j;
        ++k;
    }

    cout << "Merged sorted array C[]:\n";
    for (int i = 0; i < N + M; ++i) {
        cout << C[i] << " ";
    }
    cout << endl;

    return 0;
}

// Certainly, I'll provide you with an algorithm first, followed by the C++ code for merging two sorted arrays taken from user input.

// **Algorithm: Merge Two Sorted Arrays**

// **Input:**
// - Two sorted arrays, A[] and B[].
// - Sizes of arrays: N and M.

// **Output:**
// - Merged sorted array C[].

// 1. Initialize an empty array C[] of size N + M to hold the merged result.
// 2. Initialize pointers `i`, `j`, and `k` to 0. (i for A[], j for B[], and k for C[])
// 3. Loop while `i` is less than `N` and `j` is less than `M`:
//    a. If A[i] is less than or equal to B[j]:
//       i. Set C[k] = A[i]
//       ii. Increment i and k by 1.
//    b. Otherwise, if B[j] is less than A[i]:
//       i. Set C[k] = B[j]
//       ii. Increment j and k by 1.
// 4. If there are remaining elements in A[], copy them to C[] starting from C[k] and increment k accordingly.
// 5. If there are remaining elements in B[], copy them to C[] starting from C[k] and increment k accordingly.
// 6. The merged array C[] now contains the sorted elements from A[] and B[].

// **C++ Code: Merge Two Sorted Arrays**
