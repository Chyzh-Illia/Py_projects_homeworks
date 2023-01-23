friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for man in friends:
    if man == "James":
        continue
    elif man in friends and man not in enemies:
        print(man + " we are the best friends")
    elif man in enemies:
        print(man + " we are not friends anymore")
