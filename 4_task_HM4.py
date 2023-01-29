import re
CamelList = ["FirstItem", "FriendsList", "MyTuple"]
snake_list = []
for i in range(len(CamelList)):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_list.append(pattern.sub('_', CamelList[i]).lower())
print(snake_list)
