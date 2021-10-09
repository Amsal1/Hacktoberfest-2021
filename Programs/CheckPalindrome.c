#include <stdio.h>

int main() {
    printf("Enter a Positive Integer:");
    int n,j=0,nnum=0;
    scanf("%d",&n);
    int k=n;
    while (k>0){
        j*=10;
        j+=k%10;


        k/=10;


    }
    if(j==n){
        printf("It is a palindrome\n");

    } else{
        printf("It is not a palindrome\n");
    }



    return 0;
}
