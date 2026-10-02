# LeetCode 2544 - Alternating Digit Sum
# Calculate the alternating sum of the digits of a positive integer.
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        import math
        r=math.floor(math.log10(n))+1
        sum=0
        a=-1
        while(n>0):
            d=n%10
            a=a+1
            if r%2==0:
                if a%2==0:
                    sum=sum-d
                else:
                    sum=sum+d
            else:
                if a%2==0:
                    sum=sum+d
                else:
                    sum=sum-d            
            n=n//10
        return sum           

        