from flask import Flask
import folium
import geocoder

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/map")
def show():
    m = folium.Map()
    return m.get_root().render()

@app.route("/map/<city>")
def show_map(city):
    if city:
        gps = geocoder.osm(city).latlng
        m = folium.Map(gps, zoom_start=16)
        folium.Marker(gps, popup=city).add_to(m)
    return m.get_root().render()

if __name__ == "__main__":
    app.run(debug=True)