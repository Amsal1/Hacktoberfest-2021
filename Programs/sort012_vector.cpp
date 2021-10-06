// There are three types of colored balls in a bucket, ordered randomly. 
	// The colors are Red, blue and green.
	// You're provided with an array, that represents the bucket, and 0, 1, 2... 
	// ...represents the color Red, blue and green
	// You have to do some inplace operation by which the red ball comes first, 
	// blue comes second and green comes third
	// Note: you can't use sort function, and the operation should be in O(n) times





#include<bits/stdc++.h>
using namespace std;
int main(){
    int count=0,count1=0;
    int n;
     cout<<"enter the range : "<<endl;
     cin>>n;
     vector<int>num(n);
      for(int i=0;i<num.size();i++){
          cin>>num[i];
      }
     for(int i=0;i<num.size();i++){
         if(num[i]==2){
             num.erase(num.begin()+i);
             count1++;
             i--;
         }
           if(num[i]==1){
             num.erase(num.begin()+i);
             count++;
             i--;
         }
     }
     
    //       for(int i=0;i<num.size();i++){
       
    //  }
        int i=1;
     while(count+count1){
         if(count){
             num.push_back(1);
             count--;
         }
         else{
              num.push_back(2);
              count1--;
         }
         
     }
    //  for(int i=0;i<count+count1;i++){
    //      num.push_back(1);
         
    //  }
    // for(int i=0;i<count1;i++){
    //      num.push_back(2);
         
    //  }
          for(int i=0;i<n;i++){
         cout<<num[i]<<" ";
         
     }
     
}