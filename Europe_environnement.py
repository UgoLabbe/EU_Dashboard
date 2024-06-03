import pandas as pd
import csv

# Read the CSV file
df = pd.read_csv('data/API_Download_DS2_en_csv_v2_117194.csv', delimiter='"",""', quoting=csv.QUOTE_NONE, encoding='utf-8', on_bad_lines='skip')

# Remove the unnecessary trailing semicolon from column names
df.columns = df.columns.str.rstrip(';')
df.columns = df.columns.str.rstrip('"","')

df[['Country Name', 'Country Code']] = df['Country Name,"Country Code'].str.split(',""', expand=True)
df['Country Name'] = df['Country Name'].str.replace('"', '')

df['2023'] = df['2023'].str.replace('"",";', '')
df = df.drop(['Country Name,"Country Code', 'Indicator Code', 'Country Code'], axis=1)

# shift column 'Country Name' to first position 
first_column = df.pop('Country Name') 
df.insert(0, 'Country Name', first_column) 

# Transpose the DataFrame so that years become rows and countries become columns
df = df.transpose()

# Display the DataFrame
print(df)