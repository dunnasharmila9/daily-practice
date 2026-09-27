# LeetCode 1748 - Sum of Unique Elements
# Given an integer array nums, return the sum of all elements that appear exactly once.
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        dict={}
        sum=0
        for num in nums:
            dict[num]=dict.get(num,0)+1
        for key in dict:
            if dict[key]==1:
                sum+=key
        return sum            
        