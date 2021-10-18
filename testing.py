import pandas as pd
data=pd.read_csv('C:\\Users\\HP Elitebook G6\\Desktop\\Python\covidproject\\state_wise.csv')
#print(data)
state=data['State']
#print(state)
state=tuple(state)
print(state)