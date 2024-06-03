import pandas as pd
import re
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel("data/T_3301.xlsx", sheet_name="Data")

# Remove all starting whitespace
df.rename(columns=lambda x: x.strip(), inplace=True)

# Dataframe with all "global" budget

global_df = [col for col in df.columns if re.match(r'^\d{2} ', col)]
global_df = pd.concat([df.iloc[:,0],df[global_df]], axis=1)
df_column = global_df[global_df.columns.drop('Annuel')].columns

# President mandates
president = {
    'Jacques Chirac': [1995, 2007],
    'Nicolas Sarkozy': [2007, 2012],
    'François Hollande': [2012, 2017],
    'Emmanuel Macron': [2017, 2022],}

#Plot 

fig, ax = plt.subplots()
ax.stackplot(df['Annuel'], global_df[global_df.columns.drop('Annuel')].transpose(), labels=df_column)

# Add vertical lines for each presidential term
for president, years in president.items():
    plt.axvline(x=years[0], color='k', linestyle='--', linewidth=1)
    plt.text(
        years[0] + 0.5, 
        plt.ylim()[1] - 5, 
        president, 
        rotation=90, 
        verticalalignment='top'
    )

plt.xlabel('Years')
plt.ylabel("in Billion of €")
plt.title('Evolution of the National Expense in France')
plt.legend(loc='lower left')
plt.grid(True)
plt.show()
