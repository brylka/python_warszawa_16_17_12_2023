with open('dane.csv', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    lines = file.readlines()

#print(first_line)
#print(lines)

data = [line.strip().split(',') for line in lines]

#print(data[1:])
#print(data)

total_height = 0

for row in data:
    total_height += int(row[2])

print(total_height/len(data))