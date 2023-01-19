casino_blacklist = ["John Dow", "Terry Michel", "Kevin Hart"]
poker_blacklist = ["Jack Stanly", "Thomas Shelby", "John Dow"]
alcohol_blacklist = ["Jacob Snow", "John Dow", "Donald Tramp"]
black_list = set(casino_blacklist) & set(poker_blacklist) & set(alcohol_blacklist)
print(black_list)
