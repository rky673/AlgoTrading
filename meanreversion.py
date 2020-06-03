"""averageprice= E (price*volume)/ E volume """
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce
from time import time


def strategy(records, name):
    total_closing_price = 0
    record_count = 0
    sbal = 0
    tag = ''
    profit = 0
    bought = []
    sold = []
    avg = []
    ma = 0
    for index, record in enumerate(records['Prev Close']):
        record_count += 1
        total_closing_price += record

        # Moving avearge is calculated for every 20 ticks(records)
        if record_count >= 20:
            moving_average = total_closing_price / 20
            avg.append([records['Date'][index], moving_average])

            # If moving average is greater than last tick, place a buy order
            if (1.02 * record < moving_average < 1.05 * record or moving_average < 0.8 * record) and (
                    tag == 'sell' or tag == ''):
                while sbal < 0:
                    profit -= record
                    if profit < ma:
                        ma = profit
                    sbal += 1
                    bought.append([records['Date'][index], record])
                profit -= record
                sbal += 1
                if profit < ma:
                    ma = profit
                bought.append([records['Date'][index], record])
                tag = 'buy'

            elif (.95 * record > moving_average > .9 * record or moving_average > 1.05 * record) and (
                    tag == 'buy' or tag == ''):
                while sbal > 0:
                    sbal -= 1
                    profit += record
                    sold.append([records['Date'][index], record])
                profit += record
                sbal -= 1
                sold.append([records['Date'][index], record])
                tag = 'sell'

            total_closing_price -= records['Prev Close'][record_count - 20]

    sbal = len(bought) - len(sold)
    profit += (sbal * records['Prev Close'][len(records) - 1])
    print('% of returns are', profit / ma * (-100))
    df1 = pd.DataFrame(bought)
    df2 = pd.DataFrame(sold)
    df3 = pd.DataFrame(avg)
    plt.plot(records['Date'], records['Prev Close'])
    plt.plot(df3[0], df3[1])
    plt.scatter(df1[0], df1[1])
    plt.scatter(df2[0], df2[1])
    plt.title(name)
    plt.show()


def start(a):
    records = pd.read_csv(f'{a}.csv')
    strategy(records, a)


while True:
    an = input("enter the stock else e to exit").lower()
    tym = time()
    if an == 'e':
        print('ok bye')
        break
    try:
        print("time taken is ", time() - tym, "seconds")
        start(an)

    except Exception as e:
        print(e)
