# LeetCode 438 - Find All Anagrams in a String
# Find all starting indices of p's anagrams in string s.
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans=[]
        freq={}
        n1=len(s)
        n2=len(p)
        if n2>n1:
            return ans
        for ch in p:
            freq[ch]=freq.get(ch,0)+1
        window={}
        for i in range(n2):
            window[s[i]]=window.get(s[i],0)+1
        if freq==window:
            ans.append(0)
        for j in range(n2,n1):
            window[s[j]]=window.get(s[j],0)+1
            old=s[j-n2]
            window[old]-=1
            if window[old]==0:
                del window[old]
            if window==freq:
                ans.append(j-n2+1)
        return ans      
        