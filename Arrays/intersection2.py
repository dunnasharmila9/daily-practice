# LeetCode 349 - Intersection of Two Arrays
# Return the unique elements that are present in both arrays.
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l=[]
        freq={}
        for nums in nums1:
            freq[nums]=freq.get(nums,0)+1
        for nums in nums2:
            if nums in freq and freq[nums]>0:
                freq[nums]-=1
                if nums not in l:
                    l.append(nums)
        return l                
        