import re

values_list = []
keys_list = []
amanda_data = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
amanda_data = amanda_data.strip()
amanda_data = amanda_data.replace('sssss', '')
new_list = re.split(r"[=,&]", amanda_data)
new_list = list(filter(None, new_list))
for i in range(len(new_list)):
    if i == 0 or i % 2 == 0:
        keys_list.append(new_list[i])
    else:
        values_list.append(new_list[i])
new_dict = dict(zip(keys_list, values_list))
print(new_dict)
