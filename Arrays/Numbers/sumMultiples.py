# LeetCode 2652 - Sum Multiples
# Return the sum of all integers from 1 to n that are divisible by 3, 5, or 7.
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum=sum+i
        return sum        
        