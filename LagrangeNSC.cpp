#include<iostream>
#include<windows.h>
using namespace std;

void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

int main() {
    float table[10][2], xp, temp, ans = 0.0;
    int no, y = 0, a = 7;

    cout << "How Many Values Of X\n";
    cin >> no;
    cout << "Enter the values of x and f(x)\n";
    cout << "\n\t   x                      f(x)";
    cout << "\n\t------------------------------";

    for (int i = 0; i < no; i++) {
        gotoxy(11, a);
        cin >> table[i][y];
        gotoxy(21, a);
        cin >> table[i][y + 1];
        a++;
    }

    cout << "\nEnter the value of x  :    ";
    cin >> xp;

    for (int j = 0; j < no; j++) {
        temp = 1;
        for (int i = 0; i < no; i++) {
            if (i != j)
                temp *= ((xp - table[i][0]) / (table[j][0] - table[i][0]));
        }
        ans += temp * table[j][1];
    }

    cout << "\n ANSWER =      :  " << ans << endl;

    return 0;
}