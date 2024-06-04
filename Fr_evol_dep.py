import pandas as pd
import re
import matplotlib.pyplot as plt

# President mandates
president = {
    'Jacques Chirac': [1995, 2007],
    'Nicolas Sarkozy': [2007, 2012],
    'François Hollande': [2012, 2017],
    'Emmanuel Macron': [2017, 2022],}

# Add president mandates to graphs
def add_pres(president):
    # Add vertical lines for each presidential term
    for president, years in president.items():
        plt.axvline(x=years[0], color='k', linestyle='--', linewidth=1)
        plt.text(
            years[0] + 0.5, 
            plt.ylim()[1] - 5, 
            president, 
            rotation=90, 
            verticalalignment='top')

# Read the Excel file into a DataFrame
df = pd.read_excel("data/T_3301.xlsx", sheet_name="Data")
GDP = pd.read_excel("data/FRA_GDP.xlsx")

# Remove all starting whitespace
df.rename(columns=lambda x: x.strip(), inplace=True)

###FOCUS ON WHOLE EXPENSES

# Dataframe with all "global" budget
global_df = [col for col in df.columns if re.match(r'^\d{2} ', col)]
global_df = pd.concat([df.iloc[:,0],df[global_df]], axis=1)

# Add GDP
global_df = global_df.merge(GDP, on='Annuel')

# Do expenses as a proportion of the GDP
global_df.iloc[:,1:11,] = global_df.iloc[:,1:11,].div(global_df.PIB, axis=0)*100

df_column = global_df[global_df.columns.drop(['Annuel', 'PIB'])].columns

# Plot 
fig, ax = plt.subplots()
ax.stackplot(df['Annuel'], global_df[global_df.columns.drop(['Annuel', 'PIB'])].transpose(), labels=df_column)

# Add vertical lines for each presidential term
add_pres(president)

plt.xlabel('Years')
plt.ylabel("in % of GDP")
plt.title('Evolution of the National Expense in France')
plt.legend(loc='lower left')
plt.show()

###FOCUS ON SOCIAL SECURITY EXPENSES

# Dataframe with all "global" budget
Secu_df = [col for col in df.columns if re.match(r'^10.\d{1}', col)]
Secu_df = pd.concat([df.iloc[:,0],df[Secu_df]], axis=1)

# Add GDP
Secu_df = Secu_df.merge(GDP, on='Annuel')

# Do expenses as a proportion of the GDP
Secu_df.iloc[:,1:10,] = Secu_df.iloc[:,1:10,].div(Secu_df.PIB, axis=0)*100

df_column = Secu_df[Secu_df.columns.drop(['Annuel', 'PIB'])].columns

# Plot 
fig, ax = plt.subplots()
ax.stackplot(df['Annuel'], Secu_df[Secu_df.columns.drop(['Annuel', 'PIB'])].transpose(), labels=df_column)

add_pres(president)
plt.xlabel('Years')
plt.ylabel("in % of GDP")
plt.title('Evolution of the Social Security Expense in France')
plt.legend(loc='lower left')
plt.grid(True, axis='y')
plt.show()

# Since François Hollande
president_FH = {
    'François Hollande': [2012, 2017],
    'Emmanuel Macron': [2017, 2022],}
fig, ax = plt.subplots()
ax.plot(df['Annuel'][17:28], Secu_df[Secu_df.columns.drop(['Annuel', 'PIB'])][17:28], label=df_column)

add_pres(president_FH)
plt.xlabel('Years')
plt.ylabel("in % of GDP")
plt.title('Evolution of the Social Security Expense in France')
plt.legend(loc='lower left')
plt.grid(True, axis='y')
plt.show()
