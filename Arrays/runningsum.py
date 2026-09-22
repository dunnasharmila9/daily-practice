# Problem: Running Sum of 1d Array
# Topic: Arrays
# LeetCode: 1480
# Idea: Add each element to the sum of all previous elements.
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=0
        list=[]
        for num in nums:
            a=a+num
            list.append(a)
        return list    
