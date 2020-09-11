#Given an array nums of integers, return how many of them contain an even number of digits.
 

#Example 1:

#Input: nums = [12,345,2,6,7896]
#Output: 2

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if  len(str(num)) % 2 == 0:
                count +=1
        return count
