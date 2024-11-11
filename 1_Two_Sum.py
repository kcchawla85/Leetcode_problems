"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]"""
"""
Algorithm
1. Create two loops with indices i and j where i=nums[i] and j=nums[i+1]
2. If nums[i] = target - nums[i+1]
3. return [i,j]
"""
#CODE
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range((i+1), len(nums)):
          if nums[i]== target-nums[j]:
            return [i,j]
