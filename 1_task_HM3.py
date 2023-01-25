my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = []
my_list_3 = []
for index, value in enumerate(my_list):
    my_tuple = index, value
    if value % 2 == 0:
        my_list_3.append(tuple(my_tuple))
    else:
        my_list_2.append(tuple(my_tuple))
print(my_list_2, my_list_3)
