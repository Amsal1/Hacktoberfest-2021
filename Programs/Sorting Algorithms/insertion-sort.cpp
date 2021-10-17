#include <iostream> 
using namespace std;

void insertion_sort(int arr[], int n) { 
	for(int i = 0; i < n; i++) {
		int crnt = arr[i]; 
		int j = i - 1; 
		while(arr[j] > crnt && j >= 0) { 
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = crnt;
	}

return;
}

int main(){ 
int n; 
cin >> n; 
int arr[n];		
for(int i = 0; i < n; i++) {
	cin >> arr[i];		//taking input 
}

cout << "Given array before sorting:" << endl;		//printing original array
for(int i = 0; i < n; i++) {
	cout << arr[i] << " ";
}
cout << endl;

insertion_sort(arr, n);


cout << "Given array after sorting:" << endl;		//printing sorted array 
for(int i = 0; i < n; i++) {
	cout << arr[i] << " ";
}
cout << endl; 
return 0;
}
