# LeetCode 1636 - Sort Array by Increasing Frequency
# Sort the array by increasing frequency.
# If two values have the same frequency, sort them in decreasing order.
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        dict={}
        ans=[]
        for num in nums:
            dict[num]=dict.get(num,0)+1
        items=sorted(dict.items(), key=lambda x:(x[1],-x[0]))
        for i in range(len(items)):
            b=items[i][1]
            for j in range(b):
                ans.append(items[i][0])
        return ans
