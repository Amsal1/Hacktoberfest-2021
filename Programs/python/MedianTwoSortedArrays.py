/* 
Program description:

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.00000
  Explanation: merged array = [1,2,3] and median is 2.

Example 2:
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.50000
  Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

*/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2;
        print(nums3);
        nums3.sort();
        length =  len(nums3);
        length = math.ceil(length/2);             
        print(length);
        if(len(nums3) % 2 == 0):
            return (nums3[length-1]+nums3[length])/2;
        else:
            return nums3[length-1];
