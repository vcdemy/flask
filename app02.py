from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/map")
def show_map():
    m = folium.Map()
    return m.get_root().render()

if __name__ == "__main__":
    app.run(debug=True)