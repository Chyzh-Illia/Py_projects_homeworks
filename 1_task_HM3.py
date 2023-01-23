my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = []
my_list_3 = []
for element in range(len(my_list)):
    if my_list[element] % 2 == 0:
        my_list_3.append((element, my_list[element]))
    else:
        my_list_2.append((element, my_list[element]))
print(my_list_2, my_list_3)
