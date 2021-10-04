#include <iostream>  
using namespace std;  
int main()  
{  
ineligible:    
         cout<<"You are not eligible to participate!\n";    
      cout<<"Enter your age:\n";    
      int age;  
      cin>>age;  
      if (age < 18){    
              goto ineligible;    
      }    
      else    
      {    
              cout<<"You are eligible to participate!";     
      }         
}  
