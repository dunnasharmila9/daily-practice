# Problem: Find Pivot Index
# Topic: Arrays
# LeetCode: 724
# Idea: Find the index where the sum of elements on the left equals the sum on the right.
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1        
        