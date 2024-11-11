"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
"""
Algorithm
1. Convert x to str
2. Check is str(x) = reverse of str(x) if yes return True else False
"""
#CODE
class Solution:
    def isPalindrome(self, x: int) -> bool:
      if str(x)==str(x)[::-1]:
        return True
      return False
