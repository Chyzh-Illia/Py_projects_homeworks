my_list_1 = ["John Dow", "John Dow", "Marta Dow", "Marta Dow"]
my_list_2 = []
for i in my_list_1:
    if i in my_list_2:
        continue
    else:
        my_list_2.append(i)
print(my_list_2)
