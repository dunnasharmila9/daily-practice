# LeetCode 1207 - Unique Number of Occurrences
# Check whether the frequency of each value in the array is unique.
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        s=set()
        dict={}
        for num in arr:
            dict[num]=dict.get(num,0)+1
        for key in dict:
            a=dict[key]
            if a not in s:
                s.add(a)
            else:
                return False
        return True   