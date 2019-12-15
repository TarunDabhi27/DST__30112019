def multiplication(a,b=20):
    return a*b



print(multiplication(10,30))


def sum_no(*args):
    print(args)
    sum_args = 0
    for i in args:
        sum_args = sum_args+i
    return sum_args

print(sum_no(1,2,3,4,5,6,7,7,8))

def print_key_word(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(key,val)


print_key_word(id=1, name='Ramesh')