from matplotlib import pyplot as plt


class CityAnalizer:
    def __init__(self, filename = 'dane.csv'):
        self.cities = {}
        self.load_data(filename)

    def load_data(self, filename = 'dane.csv'):
        with open(filename, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            lines = file.readlines()

        data = [line.strip().split(',') for line in lines]

        for row in data:
            city = row[4]
            height = int(row[2])
            if city in self.cities:
                self.cities[city]['total'] += height
                self.cities[city]['number'] += 1
            else:
                self.cities[city] = {'total': height, 'number': 1}

    def show_height(self, city='', x=2):
        if city:
            if city in self.cities:
                data = self.cities[city]
                avarage = data['total'] / data['number']
                print(f"Średni wzrost w mieście {city:<8.8} wynosi: {avarage:.{x}f}")
            else:
                print(f"Nie mam takiego miasta jak {city} w bazie.")
        else:
            for city, data in self.cities.items():
                avarage = data['total'] / data['number']
                print(f"Średni wzrost w mieście {city:<8.8} wynosi: {avarage:.{x}f}")

    def avarages(self):
        avarages = {}
        for city, data in self.cities.items():
            avarage = data['total'] / data['number']
            avarages[city] = avarage
        return avarages



    def plot(self, what=''):
        avarages = self.avarages()
        cities = list(avarages.keys())
        values = list(avarages.values())

        plt.figure(figsize=(10, 6))
        plt.bar(cities, values, color="red")
        plt.title('Średni wzrost w różnych miastach.')
        plt.xlabel('Miasto')
        plt.ylabel('Średni wzrost w miastach')
        plt.show()




city = CityAnalizer()
city.plot()
#print(city.avarages())
#city.load_data()
#city.show_height()
#city.show_height("Wrocław")
#city.show_citys()

