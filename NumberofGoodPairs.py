#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.

#Return the number of good pairs.

#Example 1:

#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        j=1
        pairs=0
        while i < (len(nums) - 1):
            while j < len(nums):
                if nums[i] == nums[j]:
                    pairs += 1
                j += 1
                
            i += 1
            j = i + 1
        return pairs


