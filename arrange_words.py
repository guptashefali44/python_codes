#sort a given string.Each word contains one single number which is position of word.

print('please enter the string to be sorted')
input_str=input()
sentence=input_str.split()
l=len(sentence)
num=[1,2,3,4,5,6,7,8,9]
word_index=[]
str_num=list(map(lambda x:str(x),num))
for word in sentence:
    for letter in word:
        if letter in str_num:
            ind=int(letter)-1
            word_list=list(word)
            word_list.remove(letter)
            new_word=''.join(word_list)
            pair=[new_word]
            pair.append(int(ind))
    word_index.append(pair)
#print(word_index)

output_str={}
for item in word_index:
    output_str[item[1]]=item[0]

output_list=[]
for i in range(0,l):
    new=output_str[i]
    output_list.append(new)

output_sentence=" ".join(output_list)
print(output_sentence)
    

    

            
    
    