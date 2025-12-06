#include <iostream>
using namespace std;

int main() {
    const int startYear = 1960;
    const int endYear = 2023;
    const int arraySize = endYear - startYear + 1;

    int year[arraySize] = {0}; // Initialize the array with all zeros

    // Populate the array with the number of workers born in each year
    // For example, you can input the data manually or read it from a file.

    // Task A: Find the number of years in which no worker was born
    int yearsWithNoWorkers = 0;
    for (int i = 0; i < arraySize; ++i) {
        if (year[i] == 0) {
            yearsWithNoWorkers++;
        }
    }

    std::cout << "Number of years in which no worker was born: " << yearsWithNoWorkers << std::endl;

    // Task B: Find the number N50 of workers who will be at least 50 years old at the end of the year
    int N50 = 0;
    for (int i = arraySize - 1; i >= 0; --i) {
        N50 += year[i];
        if ((endYear - startYear) - i >= 50) {
            break; // Stop counting once we reach 50 years and beyond
        }
    }

    std::cout << "Number of workers who will be at least 50 years old at the end of the year: " << N50 << std::endl;

    return 0;
}
