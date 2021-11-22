import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation >= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    folium.Marker(  # to return to normal remove circle
        radius=6,
        location=[lt, ln],
        popup=str(el) + " meters",
        # fill_color=color_producer(el),  # remove
        # color='grey',  # remove
        # fill_opacity=0.7  # remove
        icon=folium.Icon(color=color_producer(el))
    ).add_to(fgv)

fgp = folium.FeatureGroup(name='Population')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

fgv.add_to(map)
fgp.add_to(map)
map.add_child(folium.LayerControl())
map.save("map1.html")