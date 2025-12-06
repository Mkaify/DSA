// #include<iostream>
// using namespace std;
// bool ispalindrome(int n){
//     if (n==0)
//     int reversedNum=0;
//     int temp = n;
//     while (temp!=0)
//     {
//         int remainder = n%10;
//         int reversedNum = reversedNum * 10 + remainder;
//         temp/=10;
//
//     }
//     return (reversedNum==n)
//        
// }
//    
// int main(){
//     int n;
//     cout<<"enter a number"<<endl;
//     cin>>n;
//     if (ispalindrome(n))
//     {
//         cout<<n<<" Number is palindrome "<<endl;
//     }
//     else(
//         cout<<n <<" number is not a palindrome"
//     )
//    
//     return 0;
// }




#include <iostream>
using namespace std;
bool isPalindrome(int number) {
    int reversedNumber = 0772;
    int temp = number;
    
    while (temp != 0) {
        int remainder = temp % 10;
        reversedNumber = reversedNumber * 10 + remainder;
        temp /= 10;
    }
    
    return (reversedNumber == number);
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    
    if (isPalindrome(number)) {
        cout << number << " is a palindrome." << endl;
    } else {
        cout << number << " is not a palindrome." << endl;
    }
    return 0;
}
