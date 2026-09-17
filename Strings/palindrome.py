## Given a string, write a Python program to check whether it is a palindrome or not. Print True if it is a palindrome, otherwise print False.
def palindrome(s):
  if len(s)==0:
    return False
  l=0
  f=0
  r=len(s)-1
  while(l<r):
    if s[l]!=s[r]:
      f=1
      break
    l=l+1
    r=r-1
  if f==0:
    return True
  else:
    return False
s=input()
a=palindrome(s)
print(a)
