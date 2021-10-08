#include <iostream>
using namespace std;
int main()
{
    int j, n;
    float arr[100];

    cout << "Enter total number of elements(1 to 100): ";
    cin >> n;
    cout << endl;
    for(j = 0; j < n; ++j)
    {
       cout << "Enter Number " << j + 1 << " : ";
       cin >> arr[j];
    }

    for(j = 1;j < n; ++j)
    {
       if(arr[0] < arr[j])
           arr[0] = arr[j];
    }
    cout << "Largest element = " << arr[0];

    return 0;
}
