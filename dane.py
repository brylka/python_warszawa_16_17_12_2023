with open('dane.csv', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    lines = file.readlines()

print(first_line)
print(lines)