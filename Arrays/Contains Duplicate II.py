# Problem: Contains Duplicate II
# Topic: Arrays / Hashing
# LeetCode: 219
# Idea: Check whether the same number appears within k positions.
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                 if i-dict[nums[i]]<=k:
                    return True
            dict[nums[i]]=i
        return False            
