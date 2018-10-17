import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

def markercolor(volcano_elevation):
    if volcano_elevation < 1000:
        return 'green'
    elif 1000 <= volcano_elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09],zoom_start=5,tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for la,lo,el,na in zip(latitude,longitude,elevation,name):
    iframe = folium.IFrame(html=html % (na,na,el), width=200, height=100)
    # fg.add_child(folium.Marker(location=[la,lo], popup=folium.Popup(iframe), icon=folium.Icon(color=markercolor(el)))) #regular markers
    fg.add_child(folium.CircleMarker(location=[la,lo], popup=folium.Popup(iframe), fill_color=markercolor(el), color=markercolor(el), radius=4, fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
