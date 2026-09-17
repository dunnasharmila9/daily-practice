## Given a sentence, write a Python program to print each word along with its length, number of vowels, and number of consonants.
def vowelconst(word):
  vowelcount=0
  consonantcount=0
  for ele in word:
    if ele in 'aeiouAEIOU':
      vowelcount+=1
    else:
      consonantcount+=1
  return vowelcount ,consonantcount
def length(word):
  count=0
  for ele in word:
    count+=1
  return count
s=input()
i=1
words=s.split(" ")
for word in words:
  x,y=vowelconst(word)
  print(i,word,length(word),x,y)
  i+=1