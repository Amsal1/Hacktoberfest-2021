//Bubble Sort

#include <stdio.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x=*y;
    *y=temp;
}

void bubbleSort(int arr[],int n) {
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-i-1;j++)
            if(arr[j]>arr[j+1])
                swap(&arr[j],&arr[j+1]);
}

void printArr(int arr[],int n) {
    printf("[");
    for(int i=0;i<n;i++){
        if(i==n-1)
            printf("%d]",arr[i]);
        else
            printf("%d\t",arr[i]);
    }
    printf("\n");
}

void main() {
    int n;
    printf("Enter the size of the array: \n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the elements of the array: \n");
    for(int i=0;i<n;i++){
        printf("Enter element %d: \n",i);
        scanf("%d",&arr[i]);
    }
    printf("The array entered is: \n");
    printArr(arr,n);
    bubbleSort(arr,n);
    printf("The sorted array is: \n");
    printArr(arr,n);
}

