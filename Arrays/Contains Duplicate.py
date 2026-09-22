## # Problem: Contains Duplicate
# Topic: Arrays 
# LeetCode: 217
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key in freq:
            if freq[key]>=2:
                return True
        return False    