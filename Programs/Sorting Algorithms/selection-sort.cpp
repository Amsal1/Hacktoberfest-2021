#include <iostream> 
using namespace std;

void selection_sort (int arr[], int n) { 
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) { 
			if (arr[j] < arr[i]) {
				int temp = arr[j]; 
				arr[j] = arr[i]; 
				arr[i] = temp;
			}
		}
	}

return;
}

int main() { 

	int n; 
	cin >> n; 
	int arr[n];		//taking input

	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}
	 
	cout << "Given array before sorting:" << endl;		//printing original array

	for (int i = 0; i < n; i++){
		cout << arr[i] << " ";
	}
	cout << endl;

	selection_sort(arr, n);

	cout << "Given array after sorting:" << endl;		//printing sorted array

	for (int i = 0; i < n; i++){
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}
