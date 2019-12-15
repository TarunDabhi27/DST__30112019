def oddeven(list1):
    odd = []
    even = []
    for i in list1:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return(even,odd)

if __name__ == "__main__":
    print(oddeven([1,2,3,4,5,6]))