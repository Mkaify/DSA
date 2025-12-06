#include <iostream>

void mergeSortedArrays(int A[], int m, int B[], int n) {
    int i = m - 1; // Index of the last element in A
    int j = n - 1; // Index of the last element in B
    int k = m + n - 1; // Index of the last element in merged array (A)

    while (i >= 0 && j >= 0) {
        if (A[i] > B[j]) {
            A[k] = A[i];
            i--;
        } else {
            A[k] = B[j];
            j--;
        }
        k--;
    }

    // If there are remaining elements in B[], copy them to A[]
    while (j >= 0) {
        A[k] = B[j];
        j--;
        k--;
    }
}

int main() {
    int m, n;

    std::cout << "Enter the size of array A[]: ";
    std::cin >> m;
    int A[m];

    std::cout << "Enter " << m << " sorted elements for array A[]:\n";
    for (int i = 0; i < m; i++) {
        std::cin >> A[i];
    }

    std::cout << "Enter the size of array B[]: ";
    std::cin >> n;
    int B[n];

    std::cout << "Enter " << n << " sorted elements for array B[]:\n";
    for (int i = 0; i < n; i++) {
        std::cin >> B[i];
    }

    // Merge A[] and B[] while maintaining sorted order
    mergeSortedArrays(A, m, B, n);

    std::cout << "Merged A[] while maintaining sorted order:\n";
    for (int i = 0; i < m + n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << "\n";

    std::cout << "Remaining elements in B[]: ";
    for (int i = 0; i < n; i++) {
        std::cout << B[i] << " ";
    }
    std::cout << "\n";

    return 0;
}