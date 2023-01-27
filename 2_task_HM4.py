friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]
for i in range(len(friends_list)):
    print(friends_list[i].center(20, "*"))
    print(f"{friends_list[i] : >20}\n")
