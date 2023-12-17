import pandas as pd

class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        #print(self.dataframe)
        self.dataframe.columns = ['id', 'age', 'height', 'weight', 'city']
        self.city_avarages = self.dataframe.groupby('city')['height'].mean()
        print(self.city_avarages)

coty = CityAnalizer()