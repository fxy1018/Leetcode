import pandas as pd

a = [1,1,1,2,2,2,3,3,3]
b = [1,2,3,2,3,4,3,4,5]
c=[None,1,2,3,4,None,5,None,6]

df = pd.DataFrame({'A' : a,
              'B' : b,
              'C' : c})

table = pd.pivot_table(df, values = 'C', 
                        index = ['A'],
                        columns = ['B'])


print(len(table.columns))


         
