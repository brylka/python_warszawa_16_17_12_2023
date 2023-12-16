with open('dane.csv', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    lines = file.readlines()

#print(first_line)
#print(lines)

data = [line.strip().split(',') for line in lines]

#print(data[1:])
#print(data)

citys = {}

for row in data:
    city = row[4]
    height = int(row[2])
    if city in citys:
        citys[city]['total'] += height
        citys[city]['number'] += 1
    else:
        citys[city] = {'total': height, 'number': 1}

#print(citys)

for city, data in citys.items():
    avarage = data['total'] / data['number']
    print(f"Średni wzrost w mieście {city} wynosi: {avarage}")