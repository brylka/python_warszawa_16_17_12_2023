import pandas as pd

class CityAnalizer:
    def __init__(self, filename='dane.csv'):
        self.dataframe = pd.read_csv(filename, sep=',', encoding='utf-8')
        print(self.dataframe)


coty = CityAnalizer()