import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors
from tkinter import *
import requests
import json
import os

os.system("clear")

root = Tk()
#----------------COLOR---------------------

def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"







#header_portfolio_profit_loss = Label(root, text="Portfolio Profit/Loss", bg="silver", font="Verdana 8 bold")
#header_portfolio_profit_loss.grid(row=10, column=9, sticky=N+S+E+W)

def lookup():
    api_request = requests.get("https://binanceapitest.github.io/Binance-Futures-API-doc/market_data//fapi/v1/depth")
    api = json.loads(api_request.content)
    print(api)

lookup()

