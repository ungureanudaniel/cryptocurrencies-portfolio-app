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
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=<YOUR_KEY_HERE>&start=1&limit=5000&convert=USD")
    api = json.loads(api_request.content)
    row_count = 0
    column_count = 0
    # ----------------------------------Header items start----------------------------------------
    header = ['Name', 'Current Price', 'Price Paid', 'Total Paid', 'P/L Per Coin', '1-Hour Change', '24-Hour Change', '7-Day Change', 'Current Value', 'P/L Total']

    for hd in header:
        label = Label(root, text=hd, bg='PaleGreen1', font="Verdana 12 bold")
        label.grid(row=row_count, column=column_count, sticky=N + S + E + W, padx=2, pady=2)
        column_count += 1

    row_count = 1



    # header_0 = tk.Label(root, text=header[0], bg='white', font="Verdana 8 bold")
    # header_0.grid(row=0, column=0, sticky=N + S + E + W)
    #
    # header_1 = tk.Label(root, text=header[1], bg='silver', font="Verdana 8 bold")
    # header_1.grid(row=0, column=1, sticky=N + S + E + W)
    #
    # header_2 = tk.Label(root, text=header[2], bg='white', font="Verdana 8 bold")
    # header_2.grid(row=0, column=2, sticky=N + S + E + W)
    #
    # header_3 = tk.Label(root, text=header[3], bg='silver', font="Verdana 8 bold")
    # header_3.grid(row=0, column=3, sticky=N + S + E + W)
    #
    # header_4 = tk.Label(root, text=header[4], bg='white', font="Verdana 8 bold")
    # header_4.grid(row=0, column=4, sticky=N + S + E + W)
    #
    # header_5 = tk.Label(root, text=header[5], bg='silver', font="Verdana 8 bold")
    # header_5.grid(row=0, column=5, sticky=N + S + E + W)
    #
    # header_6 = tk.Label(root, text=header[6], bg='white', font="Verdana 8 bold")
    # header_6.grid(row=0, column=6, sticky=N + S + E + W)
    #
    # header_7 = tk.Label(root, text=header[7], bg='silver', font="Verdana 8 bold")
    # header_7.grid(row=0, column=7, sticky=N + S + E + W)
    #
    # header_8 = tk.Label(root, text=header[8], bg='white', font="Verdana 8 bold")
    # header_8.grid(row=0, column=8, sticky=N + S + E + W)
    #
    # header_9 = tk.Label(root, text=header[9], bg='silver', font="Verdana 8 bold")
    # header_9.grid(row=0, column=9, sticky=N + S + E + W)
    # ----------------------------------Header items end----------------------------------------

    # ------------My portfolio start----------------
    my_portfolio = [
        {
            "sym": "BTC",
            "amount_owned": 0.449,
            "price_paid_per": 9350
        },
        {
            "sym": "ETH",
            "amount_owned": 5.3375,
            "price_paid_per": 127.72
        },
        {
            "sym": "XRP",
            "amount_owned": 4500,
            "price_paid_per": 0.3
        },
        {
            "sym": "LTC",
            "amount_owned": 11.394,
            "price_paid_per": 41.11
        },
        {
            "sym": "GNO",
            "amount_owned": 18,
            "price_paid_per": 13.37
        },
        {
            "sym": "XTZ",
            "amount_owned": 550,
            "price_paid_per": 2
        },
        {
            "sym": "NANO",
            "amount_owned": 100,
            "price_paid_per": 0.9347
        },
        {
            "sym": "BNB",
            "amount_owned": 8.04420898,
            "price_paid_per": 17
        },
        {
            "sym": "ATOM",
            "amount_owned": 100,
            "price_paid_per": 2.35101
        },
        {
            "sym": "ALGO",
            "amount_owned": 450.011,
            "price_paid_per": 0.29
        },
        {
            "sym": "GNO",
            "amount_owned": 18,
            "price_paid_per": 11.45
        },
        {
            "sym": "BAT",
            "amount_owned": 6617,
            "price_paid_per": 0.19
        }
    ]
    # ------------My portfolio end----------------

    portfolio_profit_loss = 0
    total_current_value = 0
    pie = []
    pie_size = []
    # ----------------------program loop-----------


    for x in api['data']:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:
                # Math
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x["quote"]["USD"]["price"])
                profit_loss = current_value - total_paid
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x["quote"]["USD"]["price"]) - float(coin["price_paid_per"])
                total_current_value += current_value
                pie.append(x["name"])
                pie_size.append(coin["amount_owned"])

                print(x["name"])
                print("Current price: ${0:.2f}".format(float(x["quote"]["USD"]["price"])))
                print("Total Paid: ${0:.2f}".format(float(total_paid)))
                print("Profit / Loss: ${0:.2f}".format(float(profit_loss)))
                print("Current Value: ${0:.2f}".format(float(current_value)))

                print("Profit / Loss per Coin: ${0:.2f}".format(float(profit_loss_per_coin)))
                print("Portfolio Profit / Loss: ${0:.2f}".format(float(portfolio_profit_loss)))

                name = Label(root, text=x["name"], bg="PaleTurquoise1")
                name.grid(row=row_count, column=0, sticky=N+S+E+W, padx=2, pady=2)

                current_price = Label(root, text=x["quote"]["USD"]["price"], bg="white")
                current_price.grid(row=row_count, column=1, sticky=N+S+E+W, padx=2, pady=2)

                price_paid_per = Label(root, text="${0:.2f}".format(float(coin["price_paid_per"])), bg="white")
                price_paid_per.grid(row=row_count, column=2, sticky=N + S + E + W, padx=2, pady=2)

                total_paid = Label(root, text="${0:.2f}".format(float(total_paid)), bg="white")
                total_paid.grid(row=row_count, column=3, sticky=N+S+E+W, padx=2, pady=2)

                profit_loss_per_coin = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="white", fg=red_green(float(profit_loss_per_coin)))
                profit_loss_per_coin.grid(row=row_count, column=4, sticky=N + S + E + W, padx=2, pady=2)

                _1_h_change = Label(root, text="{0:.2f}%".format(float(x["quote"]["USD"]["percent_change_1h"])), bg="white", fg=red_green(float(x["quote"]["USD"]["percent_change_1h"])))
                _1_h_change.grid(row=row_count, column=5, sticky=N+S+E+W, padx=2, pady=2)

                _24_h_change = Label(root, text="{0:.2f}%".format(float(x["quote"]["USD"]["percent_change_24h"])), bg="white", fg=red_green(float(x["quote"]["USD"]["percent_change_24h"])))
                _24_h_change.grid(row=row_count, column=6, sticky=N+S+E+W, padx=2, pady=2)

                _7_D_change = Label(root, text="{0:.2f}%".format(float(x["quote"]["USD"]["percent_change_7d"])), bg="white", fg=red_green(float(x["quote"]["USD"]["percent_change_7d"])))
                _7_D_change.grid(row=row_count, column=7, sticky=N+S+E+W, padx=2, pady=2)

                current_value = Label(root, text="${0:.2f}".format(float(current_value)), bg="white")
                current_value.grid(row=row_count, column=8, sticky=N + S + E + W, padx=2, pady=2)

                profit_loss = Label(root, text="${0:.2f}".format(float(profit_loss)), bg="white", fg=red_green(float(profit_loss)))
                profit_loss.grid(row=row_count, column=9, sticky=N + S + E + W, padx=2, pady=2)
                row_count += 1


        portfolio_profits = Label(root, text="P/L: ${0:.2f}".format(float(portfolio_profit_loss)), bg="white", font="Verdama 12 bold", fg=red_green(float(portfolio_profit_loss)))
        portfolio_profits.grid(row=row_count, column=0, sticky=N + S + E + W, padx=10, pady=10)

        root.title("Cryptocurrencies Portfolio - Total Value: ${0: .2f}".format(float(total_current_value)))

        api = ""

        update_button = Button(root, text="Update prices", command=lookup)
        update_button.grid(row=row_count, column="9", sticky=E + S, padx=10, pady=10)




        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        def chart(pie, pie_size):
            labels = pie
            sizes = pie_size
            number_of_colors = len(my_portfolio)
            colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = number_of_colors)
            patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
            plt.legend(patches, labels, loc="best")
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.tight_layout()
            plt.show()

        chart_button = Button(root, text="Pie Chart", command= lambda: chart(pie, pie_size))
        chart_button.grid(row=row_count, column="8", sticky=E + S, padx=10, pady=10)


lookup()
root.mainloop()
