class CityAnalizer:
    def __init__(self, filename = 'dane.csv'):
        self.citys = {}
        self.load_data(filename)

    def load_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
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

    def show_height(self, city='', x=2):
        if city:
            if city in self.citys:
                data = self.citys[city]
                avarage = data['total'] / data['number']
                print(f"Średni wzrost w mieście {city:<8.8} wynosi: {avarage:.{x}f}")
            else:
                print(f"Nie mam takiego miasta jak {city} w bazie.")
        else:
            for city, data in self.citys.items():
                avarage = data['total'] / data['number']
                print(f"Średni wzrost w mieście {city:<8.8} wynosi: {avarage:.{x}f}")

city = CityAnalizer()
#city.load_data()
#city.show_height()
city.show_height("Wrocław")
