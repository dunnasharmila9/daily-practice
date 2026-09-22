# Problem: Kids With the Greatest Number of Candies
# Topic: Arrays
# LeetCode: 1431
# Idea: Check whether each kid can have the greatest number of candies after getting extra candies.
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        list=[]
        for num in candies:
            max=num+extraCandies
            a=max
            for i in range(len(candies)):
                if candies[i]>max:
                    max=candies[i]
            if max==a:
                list.append(True)
            else:
                list.append(False)
        return list                    
                    
             
        