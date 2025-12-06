#include <iostream>
#include <algorithm> 
using namespace std;

int main() {
    int m, n;

    
    cout << "Enter the number of elements in array A: ";
    cin >> m;

    cout << "Enter the number of elements in array B: ";
    cin >> n;

    int A[m];
    int B[n];

    
    cout << "Enter elements for array A (sorted): ";
    for (int i = 0; i < m; i++) {
        cin >> A[i];
    }

    cout << "Enter elements for array B (sorted): ";
    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    // Create a temporary array to store the merged elements
    int temp[m + n];

    // Merge both arrays into the temporary array
    for (int i = 0; i < m; i++) {
        temp[i] = A[i];
    }
    for (int i = 0; i < n; i++) {
        temp[m + i] = B[i];
    }

    // Sort the temporary array to get the merged result in sorted order
    sort(temp, temp + m + n);

    // Copy the smallest elements back to array A[]
    for (int i = 0; i < m; i++) {
        A[i] = temp[i];
    }

    // Copy the larger elements to array B[]
    for (int i = 0; i < n; i++) {
        B[i] = temp[m + i];
    }

    cout << "Merged A[] = {";
    for (int i = 0; i < m; i++) {
        cout << A[i];
        if (i < m - 1) {
            cout << ", ";
        }
    }
    cout << "}" << endl;

    cout << "Merged B[] = {";
    for (int i = 0; i < n; i++) {
        cout << B[i];
        if (i < n - 1) {
            cout << ", ";
        }
    }
    cout << "}" << endl;

    return 0;
}