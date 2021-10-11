/*
Problem Description

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
  Input: n = 19
  Output: true
  Explanation:
  12 + 92 = 82
  82 + 22 = 68
  62 + 82 = 100
  12 + 02 + 02 = 1
 
*/

class Solution:
    def isHappy(self, n: int) -> bool:
        array = []
        
        def squareRoot(n):
            if n == 1:
                return True
            
            # string = str(n)
            sumVal = 0
            
#             for s in string:
#                 sumVal = sumVal + pow(int(s),2)
            
        
            while n > 0:
                x = n % 10
                n = n // 10
                sumVal += x*x
                
            
            if sumVal not in array:
                print(array)
                array.append(sumVal)
            else:
                return False
                
            return squareRoot(sumVal)
        
        result = squareRoot(n)
        return result
    
