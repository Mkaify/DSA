#include<iostream>
#include<windows.h>
#include<conio.h>
#include<stdio.h>

#define size 8

static float temp, data[size][size], x[10], x1[10];
short no_eq, itr;

using namespace std;

void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

int main() {
    short i, j, k = 8, l = 20, count = 1;

    gotoxy(24, 1);
    cout << "JACOBI METHOD";
    gotoxy(17, 2);
    cout << "****************************\n";
    
    cout << "\nHow Many Equations? ";
    cin >> no_eq;

    cout << "\nEnter data for equations";
    cout << "\n==========================";

    for (i = 0; i < no_eq; i++) {
        for (j = 0; j <= no_eq; j++) {
            gotoxy(l, k);
            cin >> data[i][j];
            l += 8;
            if (j == no_eq) {
                k++;
                l = 20;
            }
        }
    }

    cout << "How many iterations do you want to perform: ";
    cin >> itr;

    for (i = 0; i < no_eq; i++) {
        temp = data[i][no_eq];
        for (j = 0; j <= no_eq; j++) {
            data[i][j] /= temp;
        }
    }

    cout << "\n\nIterations                   Result\n\n";

    while (count <= itr) {
        for (i = 0; i < no_eq; i++) {
            x1[i] = data[i][no_eq];
            for (j = 0; j < no_eq; j++) {
                if (i != j)
                    x1[i] -= data[i][j] * x[j];
            }
        }

        cout << "                     " << count;
        for (k = 0; k < no_eq; k++) {
            x[k] = x1[k];
            printf("    %9.4f", x[k]);
        }
        cout << "\n";
        count++;
    }

    getch();

    return 0;
}
