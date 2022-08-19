from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def index():
    df = yf.download('^TWII')
    df = df.reset_index()
    df['Date'] = df['Date'].dt.strftime("%Y/%m/%d")
    data = df[['Date','Open','Close','Low','High']].tail(100).values.tolist()
    return render_template('stock.html', data=data, title="台灣加權指數")

@app.route("/<symbol>")
def stock(symbol):
    df = yf.download(symbol)
    df = df.reset_index()
    df['Date'] = df['Date'].dt.strftime("%Y/%m/%d")
    data = df[['Date','Open','Close','Low','High']].tail(100).values.tolist()
    return render_template('stock.html', data=data, title=symbol)

if __name__ == "__main__":
    app.run(debug=True)