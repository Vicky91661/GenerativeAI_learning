import pandas as pd
data = pd.read_csv("data.csv")
print(data.head())
print("the type of the data is ", type(data))
print("the Column of the the data is ", list(data.columns))
print("the value in the coloumn of Period is ",data[['Period','Suppressed']])



url_data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")
print("type of the url data is ",type(url_data))
print("the data at the url at the 0th index is \n",url_data[0].head())

