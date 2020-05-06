# Given an array of integers, return the indices of the two numbers whose sum is equal to a given target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example: Given nums = [2, 7, 11, 15], target = 9
# The output should be [0, 1]. 
# Because nums[0] + nums[1] = 2 + 7 = 9.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if numMap.get(diff) != None: return [numMap.get(diff),i]
            else:
                numMap[nums[i]] = i
                i += 1
