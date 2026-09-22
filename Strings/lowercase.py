## Given a string s, write a Python program to count the number of uppercase and lowercase letters in the string. Print the uppercase count and lowercase count.

s=input()
upper_count=0
lower_count=0
for ele in s:
  if ele.isupper():
    upper_count+=1
  else:
    lower_count+=1
print(upper_count,lower_count)
## second approach
s=input()
upper_count=0
lower_count=0
for ele in s:
  if ele>='A' and ele<='Z':
    upper_count+=1
  else:
    lower_count+=1
print(upper_count,lower_count)