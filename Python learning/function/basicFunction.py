def vicyyy():
    print("hey my name is vicky")
vicyyy()

l = [1,2,3,41,23,'vicky sah',[34,53,32,78]]
def Printlist(a,b,c,d,e):
    for i in l:
        if type(i)==list:
            for j in i:
                print("this is element of list",j)
        else:
            print("this is not the element of the list",i)
    return a,b,c,d,e
gotValue = Printlist(10,3,2,4,45)
print(type(gotValue))

ans = map(lambda n: n * 2,[10,2,3,5])

print(tuple(ans))