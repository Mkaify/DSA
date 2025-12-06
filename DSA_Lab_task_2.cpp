#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"enter size of array";
    cin>>n;
    int arr[n];
    cout<<"enter array values";
    // int m;
    for (int i = 0; i <= n; i++)
    {
        cin>>arr[i];
    }
    cout<<"the summation of array is"<<endl;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    std::cout << "Sum of array elements: " << sum << std::endl;    
    return 0;
}
