# Find Anagram
print('enter the words to be checked')
anagram=False
t=input()
list1=t.split()
word_1=sorted(list1[0])
word_2=sorted(list1[1])
if word_1==word_2:
    anagram=True
print('given words are:',anagram)

