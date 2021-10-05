#include<iostream>
using namespace std;
int SmallestElement(int arr[], int l){

   int temp = arr[0];
   for(int i=0; i<l; i++) {
      if(temp>arr[i]) {
         temp=arr[i];
      }
   }
   return temp;
}
int main() {
   int l;
   cout<<"Enter the size of array: ";
   cin>>l; 
   int arr[n-1];
   cout<<"Enter array elements: ";
   for(int i=0; i<l; i++){
      cin>>arr[i];
   }
   int Smallest = SmallestElement(arr, l);
   cout<<"Smallest Element is: "<<Smallest;
   return 0;
}
