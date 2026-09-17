## Given a sentence, find the longest palindrome word. If multiple palindrome words have the same length, print the one with the greater number of vowels.

def equal(word1,word2):
  vowel_count1=0
  vowel_count2=0
  for ele in word1:
    if ele in 'aeiouAEIOU':
       vowel_count1+=1
  for ele in word2:
    if ele in 'aeiouAEIOU':
       vowel_count2+=1
  return vowel_count1,vowel_count2

def findreverse(word):
  output=""
  for ch in word:
    output=ch+output
  return output
s=input()
words=s.split()
l=0
palindrome_word=""
for word in words:
  x=findreverse(word)
  if x==word:
    a=len(word)
    if a>l:
      l=a
      palindrome_word=word
    elif a<l:
      palindrome_word=palindrome_word
    else:
       x,y=equal(word,palindrome_word)
       if x>y:
         palindrome_word=word
print(palindrome_word)

