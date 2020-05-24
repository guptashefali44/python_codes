# Binary to Decimal
print('enter the binary number')
num=input()
#print(num)
num_list=list(num)
#print(num_list)
num_inlist=list(map(lambda x:int(x),num_list))
#print(num_inlist)
l=len(num_inlist)
count=l
dec_num=0
for item in num_inlist[::-1]:
    dec_num=item*(2**(l-count))+dec_num
    count=count-1
    
print('decimal form of given binary number is',dec_num)