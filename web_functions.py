import folium


# creates the map using folium and marks each location on the map
def create_map(data_frame):
    latitude = list(data_frame["Latitude"])  # store the latitudes of the locations into list
    longitude = list(data_frame["Longitude"])  # store the longitudes of the location into list
    loc_names = list(data_frame["Name"])  # store the names of said locations into list

    map1 = folium.Map(location=[32.96, -96.73], zoom_start=6, tiles="Stamen Terrain")  # create a blank map
    fg = folium.FeatureGroup(name="Map with locations")  # create a feature group

    # loop through lists and populate map with markers of locations
    for lat, long, names in zip(latitude, longitude, loc_names):
        temp = f"Longitude: {lat} \nLatitude: {long} \nName: {names}"
        popup = folium.Popup(temp, max_width=150)
        fg.add_child(folium.Marker(location=[lat, long], popup=popup, icon=folium.Icon(color='red')))

    map1.add_child(fg)
    map1.save("Map1.html")
