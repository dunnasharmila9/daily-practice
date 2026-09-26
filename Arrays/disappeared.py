# Problem: Find All Numbers Disappeared in an Array
# Topic: Arrays
# LeetCode: 448
# Idea: Find the numbers from 1 to n that are missing from the array.
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[0]*(n+1)
        b=[]
        for num in nums:
            a[num]=-1
        for i in range(1,len(a)):
            if a[i]==0:
                b.append(i)
        return b        
