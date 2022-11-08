# Import pandas
import pandas as pd

# reading csv file
df = pd.read_csv("E:\Suchi\GIT_Repos\pythonpractice\data_files\country_zones.csv")

# print(len(df['Country_Name']))
country_names=list(set(df['Country_Name']))
# print(country_names)


for i in country_names:
    if i[0]=='I':
        print(i)