list1 = [2, 4, 5]
list2 = [2, 3, 6]
result_list = []



count = 0
for i in list1:
    result_list.append(i * list2[count])
    count += 1
print(result_list)


