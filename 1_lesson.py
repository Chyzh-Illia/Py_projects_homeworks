# Challenge task
peter_salary = 3.000
anna_salary = 2.900
michel_salary = 1.500
shon_salary = 3.200

peter_age = 27
anna_age = 22
michel_age = 28
shon_age = 30

peter_name = "Peter Griffin"
anna_name = "Anna Bell"
michel_name = "Michel Bell"
shon_name = "Shon Steward"

peter_gender = False
anna_gender = True
michel_gender = True
shon_gender = False

peter_friends = ["Michel","Anna", "Shon"]
anna_friends = ["Peter", "Michel", "Shon"]
michel_friends = ["Peter", "Anna", "Shon"]
shon_friends = ["Michel", "Anna", "Peter"]

peter_coordinates = (50.29313687710791, 28.666789405132764)
anna_coordinates = (50.66935834257481, 26.293135154935054)
michel_coordinates = (50.05368499460403, 36.19640325374528)
shon_coordinates = (48.64643492460589, 39.32935530568801)

peter = {"Full_Name" : peter_name, "Age" : peter_age, "Salary" : peter_salary, "Gender" : peter_gender, "Friends" : peter_friends, "Coordinates" : peter_coordinates}
anna = {"Full_Name" : anna_name, "Age" : anna_age, "Salary" : anna_salary, "Gender" : anna_gender, "Friends" : anna_friends, "Coordinates" : anna_coordinates}
michel = {"Full_Name" : michel_name, "Age" : michel_age, "Salary" : michel_salary, "Gender" : michel_gender, "Friends" : michel_friends, "Coordinates" : michel_coordinates}
shon = {"Full_Name" : shon_name, "Age" : shon_age, "Salary" : shon_salary, "Gender" : shon_gender, "Friends" : shon_friends, "Coordinates" : shon_coordinates}

# 1 task
john_salary = 3.599
marta_salary = 4.999
print(john_salary, marta_salary)

# 2 task
john_age = 25
marta_age = 23
print(john_age, marta_age)

# 3 task
john_name = "John Snow"
marta_name = "Marta Snow"
print(john_name, marta_name)

# 4 task
john_gender = False
marta_gender = True
print(john_gender, marta_gender)

# 5 task
john_friends = [anna, shon]
marta_friends = [michel, peter]
print(john_friends, marta_friends)

# 6 task
list_names = ["Vadim", "Elena", "Tatiana", "Tatiana"]
set_names = set(list_names)
print(set_names)

# 7 task
john_coordinates = (46.48379559094589, 30.72957814700062)
marta_coordinates = (50.46133559383732, 30.503826099973974)
print(john_coordinates, marta_coordinates)

#8 task
john = {"Full_Name" : john_name, "Age" : john_age, "Salary" : john_salary, "Gender" : john_gender, "Friends" : john_friends, "Coordinates" : john_coordinates}
marta = {"Full_Name" : marta_name, "Age" : marta_age, "Salary" : marta_salary, "Gender" : marta_gender, "Friends" : marta_friends, "Coordinates" : marta_coordinates}
for key, value in john.items():
    print(key, "=>", value)
for key, value in marta.items():
    print(key, "=>", value)
