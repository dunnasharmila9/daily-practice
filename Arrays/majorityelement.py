# Problem: Majority Element
# Topic: Arrays
# LeetCode: 169
# Idea: Find the element that appears more than n/2 times.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate                