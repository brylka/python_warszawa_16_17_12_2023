import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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

    def plot2(self):
        fig, ax1 = plt.subplots(figsize=(10,6))

        self.city_avarages['height'].plot(kind='bar', ax=ax1, color='blue', position=0, width=0.2)
        ax1.set_ylabel('Średni wzrost (cm)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        ax2 = ax1.twinx()
        self.city_avarages['weight'].plot(kind='bar', ax=ax2, color='red', position=1, width=0.2)
        ax2.set_ylabel('Średnia waga (kg)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')

        plt.title('Średni wzrost i waga w różnych miastach')
        plt.show()

    def plot_corr(self):
        corr_matrix = self.dataframe[['height','age', 'weight']].corr()
        sns.heatmap(corr_matrix, annot=True)
        plt.show()
        print(corr_matrix)

city = CityAnalizer()
city.plot_corr()