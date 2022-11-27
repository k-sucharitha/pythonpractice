# Import pandas
import pandas as pd

# # reading csv file
# df = pd.read_csv()

# # print(len(df['Country_Name']))
# country_names=list(set(df['Country_Name']))
# # print(country_names)


# for i in country_names:
#     if i[0]=='I':
#         print(i)

def parse_csv(file_path, char):
    df = pd.read_csv(file_path)

    country_names = df['Country_Name']

    res = []
    for i in country_names:
        if i[0]==char:
            res.append(i)

    return res

file_path = "E:\Suchi\GIT_Repos\pythonpractice\data_files\country_zones.csv"
print(parse_csv(file_path, "A"))
print(parse_csv(file_path, "I"))
print(parse_csv(file_path, "B"))
print(parse_csv(file_path, "D"))
 a=[1,2,'pk',0.9,87,91]
print(a)
for i in a:
    if isinstance(i,str):
        print(i)
    # else:
    #      isinstance(i,list):
        #  print(i)
a=[ i for i in a if isinstance(i,str)]         
print(a)
class Karvi:
    a=10
    def x(self,name,id):
        print('first class')
coml=Karvi()
coml.x('pk',123)
           


   
