# Convert decimal to hexadecimal
print('enter the number to be converted into its hexadecimal form')
num=int(input())
list_hexa=[]
i=num
list_num=[10,11,12,13,14,15]
#list_alp=['A','B','C','D','E','F']
while i>0:
    dig=i%16
    if dig in list_num:
        if dig==10:
            dig='A'
        elif dig==11:
            dig='B'
        elif dig==12:
            dig='C'
        elif dig==13:
            dig='D'
        elif dig==14:
            dig='E'
        else:
            dig='F'
    else:
        dig=str(i%16)
    list_hexa.append(dig)
    i=i//16
hexa_list=list_hexa[::-1]
hexa_num="".join(hexa_list)
print('hexadecimal form of decimal number',num,'is',hexa_num)
        