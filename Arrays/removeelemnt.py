# LeetCode 27 - Remove Element
# Remove all occurrences of val from nums in-place and return the number of remaining elements.
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            while left<=right:
                if nums[left]==val:
                    nums[left]=nums[right]
                    right-=1
                else:
                    left+=1
        return right+1            
