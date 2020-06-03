import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def get_ans(a):
    df = pd.read_csv(f'{a}.csv')
    df['20d'] = np.round(df['Average Price'].rolling(window=20).mean())
    df['5d'] = np.round(df['Average Price'].rolling(window=5).mean())
    df['diff'] = df['5d'] - df['20d']
    # for i in range(269, 290):
    #     print(df['Date'][i], "  ", df['diff'][i])
    plt.plot(df['Date'], df['5d'], 'g-')
    plt.plot(df['Date'], df['20d'], 'y-')
    plt.plot(df['Date'], df['Prev Close'], 'r-')
    i = 21
    bal = 0
    sbal = 0
    bought = []
    sold = []
    ma = 0
    while i < len(df):
        if (df['5d'][i] - df['20d'][i]) * (df['5d'][i - 1] - df['20d'][i - 1]) < 0:
            if df['5d'][i] - df['20d'][i] > 0:
                while sbal < 0:
                    bal -= df['5d'][i]
                    if bal < ma:
                        ma = bal
                    sbal += 1
                    bought.append([df['Date'][i], df['5d'][i]])
                bal -= df['5d'][i]
                if bal < ma:
                    ma = bal
                sbal += 1
                bought.append([df['Date'][i], df['5d'][i]])
            elif df['5d'][i] - df['20d'][i] < 0:  # and sbal > 0:
                while sbal > 0:
                    bal += df['5d'][i]
                    sbal -= 1
                    sold.append([df['Date'][i], df['5d'][i]])
                bal += df['5d'][i]
                sbal -= 1
                sold.append([df['Date'][i], df['5d'][i]])
        i += 1

    # print(bal," ",sbal)
    # print(bought)
    # print(sold)
    bal += sbal * df['5d'][len(df) - 1]
    df1 = pd.DataFrame(bought)
    df2 = pd.DataFrame(sold)
    plt.scatter(df1[0], df1[1])
    plt.scatter(df2[0], df2[1])
    if ma == 0:
        print(f'balance is {bal} for 0 investment')
    else:
        print(f'% returns are {bal / ma * (-100)}')
        print(f'investment required : {-ma}')
    plt.title(a)
    plt.show()


while True:
    an = input("enter the stock else e to exit").lower()
    if an == 'e':
        print('ok bye')
        break
    try:
        get_ans(an)
    except Exception as e:
        print(e)
# get_ans('baj')


# -------------------------------------------------INTRODUCTION----------------------------------------------------
