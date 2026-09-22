# Problem: Richest Customer Wealth
# Topic: Arrays / Matrix
# LeetCode: 1672
# Idea: Calculate the total wealth of each customer and find the maximum.
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        max=0
        for i  in range(m):
            sum=0
            for j in range(n):
                sum=sum+accounts[i][j]
            if sum>max:
                max=sum