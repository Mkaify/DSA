#include <iostream>
using namespace std;
int main()
{
    int M, N, X, Y;
    MainMenu:
    cout << "Enter the number of rows for 1st Matrix: " << endl;
    cin >> M;
    cout << "Enter the number of columns for 1st Matrix: " << endl;
    cin >> N;
    cout << "Enter the number of rows for 2nd Matrix: " << endl;
    cin >> X;
    cout << "Enter the number of columns for 2nd Matrix: " << endl;
    cin >> Y;
    if(X!=M || Y!=N){
	
    cout<<"The order of matrix is invalid"<<endl;
    goto MainMenu;}
    int matrix1[M][N];
    cout << "Enter the elements of the first matrix:" << endl;
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> matrix1[i][j];
        }
    }
    int matrix2[X][Y];
    cout << "Enter the elements of the second matrix:" << endl;
    for (int i = 0; i < X; i++)
    {
        for (int j = 0; j < Y; j++)
        {
            cin >> matrix2[i][j];
        }
    }
    int result[M][N];
    cout << "Select operation:" << endl;
    cout << "1. Multiply matrices" << endl;
    cout << "2. Add matrices" << endl;
    cout << "3. Subtract matrices" << endl;
    int choice;
    cin >> choice;
    switch (choice)
    {
    case 1:
        if (N == X)
        { 
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < Y; j++)
                {
                    result[i][j] = 0;
                    for (int k = 0; k < X; k++)
                    {
                        result[i][j] += matrix1[i][k] * matrix2[k][j];
                    }
                }
            }
            cout << "Multiplied matrix:" << endl;
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    cout << result[i][j] << " ";
                }
                cout << endl;
            }
        }
        else
        {
            cout << "Unexpected Dimension\n";
        }
        break;
    case 2: 
        if (M == X && N == Y)
        {
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    result[i][j] = matrix1[i][j] + matrix2[i][j];
                }
            }
            cout << "Added matrix:" << endl;
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    cout << result[i][j] << " ";
                }
                cout << endl;
            }
        }
        else
        {
            cout << "Unexpected Dimension\n";
        }
        break;
    case 3: 
        if (M == X && N == Y)
        {
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    result[i][j] = matrix1[i][j] - matrix2[i][j];
                }
            }
            cout << "Subtracted matrix:" << endl;
            for (int i = 0; i < M; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    cout << result[i][j] << " ";
                }
                cout << endl;
            }
        }
        else
        {
            cout << "Unexpected Dimension\n";
        }
        break;
    default:
        cout << "Invalid choice." << endl;
        return 1;
    }
    char ch;
    cout << "Do you want to do more Calculations:(y/n)\n";
    cin >> ch;
    if (ch == 'y' || ch == 'Y')
    {
        goto MainMenu;
    }
    return 0;
}