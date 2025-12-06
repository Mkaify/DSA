#include<iostream>
using namespace std;

int main(){
    int R1;
    cout<<"Enter number of rows for Matrix1"<<endl;
    cin>>R1;
    int C1;
    cout<<"Enter number of columns for Matrix1"<<endl;
    cin>>C1;

    int Matrix1[R1][C1];
    cout<<"Enter elements of Matrix1"<<endl;

    for (int i = 0; i < R1; i++)
    {
        for (int j = 0; j < C1; j++)
        {
            cin>>Matrix1[i][j];
        }
        
    }
    int R2;
    cout<<"Enter number of rows for Matrix2"<<endl;
    cin>>R2;
    int C2;
    cout<<"Enter number of columns for Matrix2"<<endl;
    cin>>C2;
    cout<<"Enter elements of Matrix2"<<endl;
    int Matrix2[R2][C2];
    for (int i = 0; i < R2; i++)
    {
        for (int j = 0; j < C2; j++)
        {
            cin>>Matrix2[i][j];
        }
        
    }
    cout<<"Enter the operation you want to perform on the these Matrices: "<<endl;
    cout<<"1.Multiply"<<endl;
    cout<<"2.Add"<<endl;
    cout<<"3.Subtract"<<endl;
    
    int Result[R1][C2];
    int choice;
    cin>>choice;
    Main:
    switch (choice)
    {
    case 1:
        if (C1==R2)
        {
            for (int i = 0; i < R1; i++)
            {
                for (int j = 0; j < C2; j++)
                {
                    Result[i][j] = 0;
                    for (int k = 0; k < R2; k++)
                    {
                        Result[i][j] = Result[i][j] + Matrix1[i][k]*Matrix2[k][j];
                    }
                    
                }
                
            }
        
        cout<<"The Multiplied Matrix is: "<<endl;
        for (int i = 0; i < R1; i++)
        {
            for (int j = 0; j < C1; j++)
            {
                cout<<Result[i][j]<<" ";
            }
            cout<<endl;
            
        }
        
        }
        else{
        cout<<"invalid Dimensions"<<endl;
        }
        break;
    case 2:
        if (R1==R2 && C1==C2)
        {
            for (int i = 0; i < R1; i++)
            {
                for (int j = 0; j < C1; j++)
                {
                    Result[i][j] = Matrix1[i][j] + Matrix2[i][j];
                }
                
            }
            cout<<"The resultant Matrix is: "<<endl;
            for (int i = 0; i < R1; i++)
            {
                for (int j = 0; j < C1; j++)
                {
                    cout<<Result[i][j]<<" ";
                }
                cout<<endl;
                
            }
            
        }
        else
        cout<<"Invalid Dimensions."<<endl;
        break;
    case 3:
        if (R1==R2 && C1==C2)
        {
            for (int i = 0; i < R1; i++)
            {
                for (int j = 0; j < C1; j++)
                {
                    Result[i][j] = Matrix1[i][j] - Matrix2[i][j];
                }
                
            }
            cout<<"The resultant Matrix is: "<<endl;
            for (int i = 0; i < R1; i++)
            {
                for (int j = 0; j < C1; j++)
                {
                    cout<<Result[i][j]<<" ";
                }
                cout<<endl;
                
            }
        }
        else
        cout<<"Invalid Dimensions."<<endl;
        break;

    default:
        break;
    }

    return 0;
}