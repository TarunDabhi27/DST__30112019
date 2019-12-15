'''func1 = lambda x:x**2
print(func1(5))

func2 = lambda a: a**2 if(a>10 & a<20) else a

print(func2(11))'''
list1=['abc ',' cde ']
print(list(map(lambda a:a.strip(),list1)))

list2=range(10)

print(list(filter(lambda a: a%2==0 ,list2)))