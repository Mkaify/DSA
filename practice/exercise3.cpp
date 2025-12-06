#include <iostream>
#include <algorithm>
using namespace std;

int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1; // Target not found
}

int main() {
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    int arr[size];
    cout << "Enter " << size << " numbers in ascending order:\n";
    for (int i = 0; i < size; ++i) {
        cin >> arr[i];
    }

    sort(arr, arr + size); // Sort the array -> function defined in algorithm

    int target;
    cout << "Enter the number you want to search for: ";
    cin >> target;

    int result = binarySearch(arr, size, target);

    if (result != -1) {
        cout << "Number found at index: " << result << endl;
    } else {
        cout << "Number not found in the array." << endl;
    }

    return 0;
}
