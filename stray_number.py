# Find Stray Numbers
print('enter numbers to be checked(space separated)')
num=input()
stray=[]
list1=num.split()
list2=list(map(lambda x:int(x),list1))
d={}
for item in list2:
    if item in d:
        d[item]+=1
    else:
        d[item]=1
for i in d:
    count=d[i]%2
    if count==0:
        pass
    else:
        stray.append(i)
print(d)
print(stray)