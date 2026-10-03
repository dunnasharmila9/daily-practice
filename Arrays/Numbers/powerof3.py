# LeetCode 326 - Power of Three
# Check whether a given integer is a power of three.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        elif n<=0 or n%3!=0:
            return False
        return self.isPowerOfThree(n//3)        
        