#include <iostream>
using namespace std;

int main() {
    int n, ReversedNumber = 0, Remainder;

    cout << "Enter any Number in Integer: ";
    cin >> n;

    while(n != 0) {
        Remainder = n%10;
        ReversedNumber = ReversedNumber*10 + Remainder;
        n /= 10;
    }

    cout << "Reversed Number = " << ReversedNumber;

}
