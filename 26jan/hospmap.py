
import folium

# Create a map object centered on India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

# Read data from a CSV file containing the hospital locations
# Assume the file has columns "name", "latitude", and "longitude"
import pandas as pd
data = pd.read_csv(r"C:\Users\Asjad Seraj\OneDrive\Desktop\\26jan\\26jan\hospdata.csv")

#border Styling

borderStyle = {
    'color':'green',
    'weight':2,
    'fillOpacity':0
}

# Iterate through the hospital data and add markers to the map
for i, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(row["Hospital Name"], parse_html=True, max_width='100%', show=False, sticky=False, lazy=False),
        icon=folium.Icon(color='lightgray', icon_color='lightgreen', icon='info-sign', angle=0, prefix='glyphicon')
    ).add_to(m)

# Save the map to an HTML file
m.save("government_hospitals_map.html")
print(m)