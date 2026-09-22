# Problem: Number of Steps to Reduce a Number to Zero
# Topic: Math / Bit Manipulation
# LeetCode: 1342
# Idea: If the number is even, divide it by 2; if odd, subtract 1.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while(num!=0): 
            if num%2==0:
                num=num//2
                c+=1
            else:
                num=num-1
                c=c+1
        return c       