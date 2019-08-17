import pandas as pd
import csv

df=pd.read_csv("cities.csv")
df.to_html('data1.html')


