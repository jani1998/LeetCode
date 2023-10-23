def addTwoNumbers(l1, l2):
    l1=l1[::-1]
    l2=l2[::-1]
    print(l1,l2)
    #for i in a:
     #   m=str(i)
    l1=''.join(map(str,l1))
    l2=''.join(map(str,l2))
    print(l1,l2)
    l1=int(l1)
    l2=int(l2)
    n=l1+l2
    print(n)
    m=str(n)
    print(type(m))
    list=[]
    for i in m:
        j=int(i)
        list.append(j)
    print(list[::-1)


l1 = [2,4,3]
l2 = [5,6,4]
addTwoNumbers(l1,l2)
