// Run with node milos5593-selectionSort.js

const array = [64, 25, 12, 22, 11]

/* 
    Time complexity: O(n^2)

    1. We start with a for loop that iterates over the array.
    2. We initialize a variable min to the current index.
    3. We then iterate over the array starting from the next index.
    4. If the value at the current index is less than the value at the min index, we update min to the current index.
    5. If min is not equal to the current index, we swap the values at the two indices.
    6. After the inner for loop finishes, we swap the values at the current index and min indices.
    7. We then return the array.
*/
let selectionSort = (arr) => {
    let len = arr.length
    for (let i = 0; i < len; i++) {
        let min = i
        for (let j = i + 1; j < len; j++) {
            if (arr[min] > arr[j]) {
                min = j
            }
        }
        if (min !== i) {
            let tmp = arr[i]
            arr[i] = arr[min]
            arr[min] = tmp
        }
    }
    return arr
}

console.log(selectionSort(array))
