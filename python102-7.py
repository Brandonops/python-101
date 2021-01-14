list1 = [1,2,3,5,]
factor = 5
list2 = []
count = 0
while count < len(list1):
    list2.append(list1[count] * factor)
    count += 1
print(list2)