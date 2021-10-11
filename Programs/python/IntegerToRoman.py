/*
Problem Description:
  
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example1:
  Input: num = 3
  Output: "III"

Example2:
  Input: num = 58
  Output: "LVIII"
  Explanation: L = 50, V = 5, III = 3.
    
*/

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int2Rom = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        res = ""
        for e in range(len(str(num))):
            n = num % 10
            print(num)
            print(n)
            if n == 4 or n == 9:
                res = int2Rom[pow(10, e)] + int2Rom[(n + 1) * pow(10, e)] + res
            elif n >= 5:
                res = int2Rom[pow(10, e) * 5] + int2Rom[pow(10, e)]  * (n - 5) + res
            else:
                res = int2Rom[pow(10, e)] * n + res
            num //= 10
                
        return res
