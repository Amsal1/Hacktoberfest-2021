#include <iostream>
using namespace std;

void primeNos(int n){
    bool check[n+1];
    for(int i=0;i<n+1;i++){
        check[i]=false;
    }
    for(int i=2;i<n+1;i++){
        int t=2;
        while(i*t < n+1){
            check[i*t]= true;
            t+=1;
        }
    }
    for(int i=2; i<n+1;i++ ){
        if(!check[i])
            cout<<i<<endl;
    }
}

int main() {
    int x;
    cout << "Prime numbers less than or equal to ";
    cin>>x;
    primeNos(x);
    return 0;
}
