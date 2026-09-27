# LeetCode 242 - Valid Anagram
# Check whether two strings contain the same characters with the same frequencies.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1=[0]*26
        t1=[0]*26
        for ch in s:
            a=ord(ch)-97
            s1[a]+=1
        for ch in t:
            a=ord(ch)-97
            t1[a]+=1
        for i in range(26):
            if s1[i]!=t1[i]:
                return False
        return True            

                
        