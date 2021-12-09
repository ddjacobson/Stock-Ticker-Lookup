from flask import Flask, redirect, url_for, render_template
import yfinance as yf

app = Flask(__name__)

def get_name(name):
    stock = yf.Ticker(name)
    info = stock.info
    return info["longName"]

def get_logo(name):
    stock = yf.Ticker(name)
    info = stock.info
    return info['logo_url']

def get_summary(name):
    stock = yf.Ticker(name)
    info = stock.info
    return info["longBusinessSummary"]

def get_market_cap(name):
    stock = yf.Ticker(name)
    info = stock.info
    num = info["marketCap"]
    if len(str(num)) in range(1, 10):
        new_num = float(num / 1000000)
        rounded = round(new_num, 2)
        final = str(rounded) + "M"
    elif len(str(num)) in range(10, 13):
        new_num = float(num / 1000000000)
        rounded = round(new_num, 2)
        final = str(rounded) + "B"
    elif len(str(num)) >= 13:
        new_num = float(num / 1000000000000)
        rounded = round(new_num, 2)
        final = str(rounded) + "T"
    return final

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def stock_page(name):
    return render_template("index.html", stockname=get_name(name), logo=get_logo(name), marketcap=get_market_cap(name),
                           stocksummary=get_summary(name))


if __name__ == '__main__':
    app.run(debug=True)
