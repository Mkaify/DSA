
#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == target) {
            return i; // returns index
        }
    }
    return -1; 
}

int main() {
    const int size = 5; 
    int arr[size] = {10, 20, 30, 40, 50}; 

    cout << "Array elements: ";
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    int target;
    cout << "Enter the number you want to search for: ";
    cin >> target;

    int index = linearSearch(arr, size, target);

    if (index != -1) {
        cout << "Number found at index: " << index << std::endl;
    } else {
        cout << "Number does not exist in record." << std::endl;
    }

    return 0;
}
