list1 = [1,2,3,4,5]
'''square=[]
for i in list1:
    square.append(i**2)
print(square)'''

print([i**2 for i in list1])
print([i for i in list1 if i%2==0])

key_list = ['id','name','rollno']
val_list = [1,'Ramesh',10]

print({key:val for key,val in zip(key_list,val_list)})