#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;         //no of elements in array
  cin>>n;
  vector<int>v(n);
  for(int i=0;i<n;i++){
    cin>>v[i];
  }
  cout<<"The elements before sorting:";
  for(int i=0;i<n;i++){
    cout<<v[i]<<" ";
  }
  cout<<"\n";
  int key, j;
  for (int i = 1; i < n; i++){
     key = v[i];
     j = i - 1;
     while (j >= 0 && v[j] > key)
     {
            v[j + 1] = v[j];
            j = j - 1;
     }
     v[j + 1] = key;
  }
  cout<<"The elements after sorting:";
  for(int i=0;i<n;i++){
    cout<<v[i]<<" ";
  }
  cout<<"\n";
  return 0;
}
