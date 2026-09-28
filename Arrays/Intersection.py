# LeetCode 350 - Intersection of Two Arrays II
# Return the intersection of two arrays, including duplicate elements.
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        list=[]
        dict={}
        for nums in nums1:
            dict[nums]=dict.get(nums,0)+1
        for nums in nums2:
            if  nums in dict  and dict[nums]>0:
                dict[nums]-=1
                list.append(nums)
        return list            
