"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
"""
Algorithm
1. Sort the strings
2. Take the first and the last element
3. Check until which elemenet they are the same
4. Add the characters into a string ans
5. return ans
"""
#code
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =""
        strs=sorted(strs)
        first = strs[0]
        last= strs[-1]
        for i in range(min(len(first),len(last))):
            if (first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans
