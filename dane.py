with open('dane.csv', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    lines = file.readlines()

#print(first_line)
#print(lines)

data = [line.strip().split(',') for line in lines]

#print(data[1:])
print(data)

total_height_warszawa = 0
total_height_poznan = 0
i_warszawa = 0
i_poznan = 0
for row in data:
    if row[4] == 'Warszawa':
        total_height_warszawa += int(row[2])
        i_warszawa+=1
    elif row[4] == 'Poznań':
        total_height_poznan += int(row[2])
        i_poznan+=1

print(f"Średnia wzrostu dla Warszawy: {total_height_warszawa/i_warszawa}")
print(f"Średnia wzrostu dla Poznania: {total_height_poznan/i_poznan}")