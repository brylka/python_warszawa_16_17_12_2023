import pandas as pd
from matplotlib import pyplot as plt


class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        #print(self.dataframe)
        self.dataframe.columns = ['id', 'age', 'height', 'weight', 'city']
        self.city_avarages = self.dataframe.groupby('city')[['height','age', 'weight']].mean()
        #print(self.city_avarages)

    def plot(self):
        ax = self.city_avarages.plot(kind='bar', figsize=(10, 6))
        plt.title('Średni wzrost w różnych miastach.')
        plt.xlabel('Miasto')
        plt.ylabel('Średni wzrost w miastach')
        plt.xticks(rotation=0)
        for i in ax.patches:
            height = i.get_height()
            plt.annotate(f"{height:.2f}",
                         (i.get_x()+i.get_width() / 2, height),
                         textcoords="offset points",
                         xytext=(1,-40),
                         ha='center',
                         rotation = 90,
                         color="white")
        #for i, value in enumerate(self.city_avarages):
        #    plt.annotate(f"{value:.2f}", (i, value), textcoords="offset points", xytext=(0,5), ha='center')
        plt.show()


city = CityAnalizer()
city.plot()