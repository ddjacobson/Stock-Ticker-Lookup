import re
from flask import Flask, Blueprint, render_template, redirect, request
from flask.helpers import url_for
import yfinance as yf

pages = Blueprint('pages', __name__)

@pages.route('/discover', methods=['GET', 'POST'])
def discover():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("pages.stock_page", usr=user))
    else:
        return render_template("discover.html")             
 
@pages.route('/<usr>')  
def stock_page(usr):

    ticker = usr
    return render_template('stock_page.html', price=get_price(ticker), stockname=get_name(ticker), logo=get_logo(ticker), marketcap=get_market_cap(ticker), stocksummary=get_summary(ticker))

@pages.route('/learn')
def learn():
    return render_template('learn.html')


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

def get_price(name):
    stock = yf.Ticker(name)
    info = stock.info
    return info['regularMarketPrice']
