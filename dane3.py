class CityAnalizer:
    def __init__(self, filename = 'dane.csv'):
        self.citys = {}
        self.filename = filename
        self.load_data()

    def load_data(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            lines = file.readlines()

        data = [line.strip().split(',') for line in lines]

        for row in data:
            city = row[4]
            height = int(row[2])
            if city in self.citys:
                self.citys[city]['total'] += height
                self.citys[city]['number'] += 1
            else:
                self.citys[city] = {'total': height, 'number': 1}

    def show_height(self, x):
        for city, data in self.citys.items():
            avarage = data['total'] / data['number']
            print(f"Średni wzrost w mieście {city} wynosi: {avarage:.{x}f}")

city = CityAnalizer()
#city.load_data()
city.show_height(7)
city.show_height(3)
