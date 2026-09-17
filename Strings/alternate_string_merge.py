## Given two strings, merge them by taking characters alternately from each string. If one string is longer, append its remaining characters at the end.
s1=input()
s2=input()
n1=len(s1)
n2=len(s2)
i=0
output=""
m=max(n1,n2)
while(i<m):
  if i<n1:
    output=output+s1[i]
  if i<n2:
    output=output+s2[i]
  i=i+1
print(output)

