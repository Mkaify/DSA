#include <iostream>
#include <climits>
using namespace std;

int main() {
    int N;
    cout << "Enter the number of elements in the array: ";
    cin >> N;

    int *arr = new int[N];

    cout << "Enter " << N << " integer values:\n";
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    int smallest = INT_MAX;
    int largest = INT_MIN;

    for (int i = 0; i < N; ++i) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    int difference = largest - smallest;

    cout << "Difference between largest and smallest values: " << difference << endl;

    delete[] arr;

    return 0;
}
