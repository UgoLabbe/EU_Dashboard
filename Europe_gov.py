import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load the geographic data for countries in Europe
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Keep only mainland Europe and Turkey
europe = world[(world['continent'] == 'Europe')]

# Remove Russia from the dataset
europe = europe[europe['name'] != 'Russia']

# Define the political orientation for each country
political_orientation = {
    'France': 'centre',
    'Germany': 'centre',
    'Spain': 'socialism',
    'Italy': 'far right',
    'Netherlands': 'right',
    'Belgium': 'centre',
    'Portugal': 'centre',
    'Sweden': 'centre',
    'Austria': 'right',
    'Greece': 'right',
    'Poland': 'far right',
    'Hungary': 'far right',
    'Czechia': 'right',
    'Slovakia': 'right',
    'Denmark': 'centre',
    'Finland': 'socialism',
    'Ireland': 'centre',
    'Bulgaria': 'right',
    'Romania': 'right',
    'Croatia': 'right',
    'Lithuania': 'centre',
    'Slovenia': 'centre',
    'Latvia': 'centre',
    'Estonia': 'centre',
    'Luxembourg': 'centre',
    'Cyprus': 'right',
    'Malta': 'centre',
    'Norway': 'socialism',
    'Switzerland': 'right',
    'Iceland': 'socialism',
    'Serbia': 'far right',
    'Bosnia and Herz.': 'right',
    'Montenegro': 'right',
    'North Macedonia': 'right',
    'Albania': 'right',
    'Kosovo': 'centre',
    'Ukraine': 'right',
    'Belarus': 'far right',
    'Moldova': 'right',
    'United Kingdom': 'right'
}

# Define the colors for each political orientation
colors = {
    'radical left': 'darkred',
    'ecology': 'green',
    'socialism': 'red',
    'centre': 'yellow',
    'right': 'lightblue',
    'far right': 'black'
}

# Assign colors to each country based on political orientation
europe['color'] = europe['name'].map(political_orientation).map(colors)

# Handle countries not in the political_orientation dictionary
europe['color'] = europe['color'].fillna('grey')  # Using grey for countries with undefined political orientation

# Create the map
minx, miny, maxx, maxy = europe.total_bounds
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
ax.set_xlim(-30, maxx)
ax.set_ylim(33, 72)
europe.boundary.plot(ax=ax)
europe.plot(ax=ax, color=europe['color'])

# Add a legend
patches = [mpatches.Patch(color=colors[key], label=key) for key in colors]
patches.append(mpatches.Patch(color='grey', label='other'))  # Adding the undefined color to the legend
plt.legend(handles=patches, loc='lower left')

# Add a title to the map
plt.title("Political Orientation of Governments in Europe")

# Show the map
plt.show()