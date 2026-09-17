## Given a sentence, write a Python program to print each word along with its reverse.
## by using built in function
def findreverse(word):
  return word[::-1]
s=input()
words=s.split(" ")
for word in words:
  reverse=findreverse(word)
  print(word,reverse)

def findreverse(word):
  output=""
  for ch in word:
    output=ch+output
  return output
s=input()
words=s.split()
count=0
for word in words:
  x=findreverse(word)
  if word==x:
    count+=1
print(count)
