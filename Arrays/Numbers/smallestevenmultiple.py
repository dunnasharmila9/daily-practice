# LeetCode 2413 - Smallest Even Multiple
# Return the smallest positive multiple of both n and 2.
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return 2*n    
        