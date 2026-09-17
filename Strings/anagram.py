## Given two strings, write a Python program to check whether they are anagrams or not. Print True if they are anagrams, otherwise print False.

def anagram(s1,s2):
  n1=len(s1)
  n2=len(s2)
  f=0
  if n1!=n2:
    return False
  else:
    for i in range(n1):
      if s1.count(s1[i])!=s2.count(s1[i]):
        f=1
        break
  if f==0:
    return True
  else:
    return False
s1=input()
s2=input()
a=anagram(s1,s2)
print(a)
