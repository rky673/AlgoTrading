i = 1
while True:
    print(f"TRADE {i}")
    try:
        price = int(input('enter price'))
        principle = int(input('enter principle'))
        amount = int(principle * 20 / price)
        amountdelivered = int(principle / price)
        turnover = price * amount
        brok = .002 * turnover
        volatility = float(input('enter volatality'))
        profits = volatility * amount - brok
        deliveryprofits = amountdelivered * volatility - 20
        if amount == 0:
            print("cann't purchase shares please increse your funds")
        elif amountdelivered == 0:
            print("_____FOR TRADING_____")
            print(f'profitable aboue {.002 * price}')
            print(f'percentage profits {profits / principle * 100} %')
            print(f'actual profits {profits}')
            print("delivery can't be taken because of insufficient funds try in intraday")
        else:
            print("_____FOR TRADING_____")
            print(f'profitable aboue {.002 * price}')
            print(f'percentage profits {profits / principle * 100} %')
            print(f'actual profits {profits}')
            print("_____FOR DELIVERY_____")
            print(f'profitabe above {20 / amountdelivered}')
            print(f'percentage profits {deliveryprofits * 100 / principle} %')
            print(f'actual profits {deliveryprofits}')
    except Exception as e:
        print(e)
    print("\n\n\n")
    i += 1
