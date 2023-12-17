import pandas as pd
from matplotlib import pyplot as plt


class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        #print(self.dataframe)
        self.dataframe.columns = ['id', 'age', 'height', 'weight', 'city']
        self.city_avarages = self.dataframe.groupby('city')['height'].mean()
        #print(self.city_avarages)

    def plot(self):
        self.city_avarages.plot(kind='bar', figsize=(10, 6))
        plt.title('Średni wzrost w różnych miastach.')
        plt.xlabel('Miasto')
        plt.ylabel('Średni wzrost w miastach')
        plt.xticks(rotation=0)
        plt.show()


city = CityAnalizer()
city.plot()