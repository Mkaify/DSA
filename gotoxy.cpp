#include<iostream>
#include<windows.h>
#include<conio.h>
#include<stdio.h>
#define size 8

static float temp,data[size][size],x[10],x1[size];
short no_eq,itr;

using namespace std;

void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

int main(){
    short i,j,k=8,l=20,count=1;
    gotoxy(24,1);cout<<"JACOBI METHOD";
    gotoxy(17,2);
    cout<<"****************************\n";
    cout<<"\nHow Many Equations? ";
    cin >> no_eq; // Initialize no_eq
    cout<<"\n Enter data for equations";
    cout<<"\n==========================";
    for (int i = 0; i < no_eq; i++) // Changed the loop condition
    {
        for (int j = 0; j <= no_eq; j++) // Changed the loop condition and the equality check
        {
            gotoxy(l,k);
            cin>>data[i][j];
            l+=8; // Corrected the increment
        }
        k++; // Moved this line outside the inner loop
        l=20; // Reset l for the next row
    }
    cout<<"How many iterations you want to do :";
    cin>>itr;
    for (i = 0; i < no_eq; i++) // Changed the loop condition
    {
        temp=data[i][i]; // Use correct index i
        for (j = 0; j <= no_eq; j++) // Changed the loop condition
        {
            data[i][j]/=temp;
        }
    }
    cout<<"\n\nIterations                   Result\n\n";
    while (count<=itr)
    {
        for (i = 0; i < no_eq; i++)
        {
            x1[i]-=data[i][no_eq];
            for (j = 0; j <= no_eq; j++) // Changed the loop condition
            {
                if(i==j)
                {
                    j++; // Increment j instead of decrementing it
                    continue;
                }
                x1[i]-=data[i][j]*x[j];
            }
        }
        cout<<"                     "<<count;
        for (k = 0; k < no_eq; k++) // Changed the loop condition
        {
            x[k]=x1[k];
            printf("    %9.4f",x[k]);
        }
     cout<<"\n"   ;
     count++;
    }
    
    getch();
    
    return 0;
}
