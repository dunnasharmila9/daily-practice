## Given a string containing lowercase letters followed by digits, shift the previous letter forward by the value of each digit and print the resulting string. If the shift goes beyond z, wrap around to a.
s=input()
n=len(s)
output=""
for i in range(0,len(s)):
  if s[i].isdigit():
    a=s[i-1]
    x=ord(a)+int(s[i])
    if x<=122:
       output=output+chr(x)
    else:
     k=x-26
     output=output+chr(k)
  else:
    output=output+s[i]
print(output)


