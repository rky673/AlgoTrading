import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce

df = pd.read_csv('option.csv')
# df.set_index('STRIKE PRICE',inplace=True)
# print(df.keys())
# print(df)
# print(df['LTP'])
x = df['STRIKE PRICE']
y = df['LTP']
ln = len(x)
profit = 0
buys = [0] * len(x)
sell = [0] * len(x)
most_profitable_trade = 0
most_profitable_range = []
most_profitable_index = []
for index, item in enumerate(x):
    diff = 1
    ind = index + 2 * diff
    while ind < ln:
        rao = []
        r1 = y[index]
        rao.append(index)
        ind = index + diff
        r2 = y[ind]
        rao.append(ind)
        ind += diff
        r3 = y[ind]
        rao.append(ind)
        if r1 + r3 < 2 * r2:
            temp = (2 * r2 - r1 - r3)
            profit += temp
            if temp > most_profitable_trade:
                most_profitable_trade = temp
                most_profitable_range = [x[rao[0]], x[rao[1]], x[rao[2]]]
                most_profitable_index = rao

            buys[rao[0]] += 1
            buys[rao[2]] += 1
            sell[rao[1]] += 2
        diff += 1
        ind = index + 2 * diff
# plt.plot(x, y)
# print(reduce(lambda a,b:a+b,buys))
# print(reduce(lambda a,b:a+b,sell))
plt.plot(x, buys)
plt.scatter(x, buys)
plt.plot(x, sell)
plt.scatter(x, sell)
plt.show()
k = [df['LTP'][most_profitable_index[0]], df['LTP'][most_profitable_index[1]], df['LTP'][most_profitable_index[2]]]
plt.plot(x, y)
plt.scatter(most_profitable_range, k)
plt.show()
# print(profit*75)
print("most profitable range of trade is", most_profitable_range)
print("premiums of most profitable range are", k)
print('profits made by a singe lot of most profitable trade is', most_profitable_trade * 75)
