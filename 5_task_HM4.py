import re

with open("text", "r") as file:
    file_data = file.read()
    print(file_data)
    print(re.split("\. | \.\.\.\. | \.\.\.\.\.\.", file_data))
