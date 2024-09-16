test_list = [1,2,3,4,8,5,3]

print("Orignal List :"+str(test_list))

rest_list = []
for i in range(0,len(test_list)):
    if test_list[i]==3:
        rest_list.append(i)
print("new index list"+str(rest_list))

rest_list2 = [i for i in range(len(test_list)) if test_list[i]==3]

# Printing resultant list
print("new indices list: "+str(rest_list2))

rest_list3 = list(filter(lambda x:test_list[x]==3,range(len(test_list))))

print("new indices list: "+str(rest_list3))
