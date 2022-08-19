from flask import Flask, render_template
import plotly.express as px

app = Flask(__name__)

@app.route("/")
def index():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    return render_template('chart.html', content=fig.to_html(full_html=False))

if __name__ == "__main__":
    app.run(debug=True)