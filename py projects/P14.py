import time

while True:
    currencies = ['USD', 'EUR', 'GEL', 'JPY', 'GBP', 'RUB', 'CNY', 'INR', 'IQD', 'CHF', 
                'CAD', 'AUD', 'NZD', 'SEK', 'NOK', 'DKK', 'ZAR', 'BRL', 'MXN', 'KRW', 
                'TRY', 'PLN', 'SGD', 'THB', 'AED', 'SAR', 'HKD', 'IDR', 'MYR', 'PHP']
    print(currencies)
    A = (int(input("how many lari do you have : ")))
    B = (str(input("on what curency you want to change : ")))
    if B == "USD":
        print(A * 2.30)
    elif B == "EUR":
        print(A * 2.50)
    elif B == "GEL":
        print(A * 1.00)
    elif B == "JPY":
        print(A * 17.00)
    elif B == "GBP":
        print(A * 2.95)
    elif B == "RUB":
        print(A * 28.00)
    elif B == "CNY":
        print(A * 0.32)
    elif B == "INR":
        print(A * 27.00)
    elif B == "IQD":
        print(A * 790.00)
    elif B == "CHF":
        print(A * 2.60)
    elif B == "CAD":
        print(A * 1.70)
    elif B == "AUD":
        print(A * 1.50)
    elif B == "NZD":
        print(A * 1.40)
    elif B == "SEK":
        print(A * 0.22)
    elif B == "NOK":
        print(A * 0.21)
    elif B == "DKK":
        print(A * 0.34)
    elif B == "ZAR":
        print(A * 1.25)
    elif B == "BRL":
        print(A * 0.90)
    elif B == "MXN":
        print(A * 0.80)
    elif B == "KRW":
        print(A * 290.00)
    elif B == "TRY":
        print(A * 1.18)
    elif B == "PLN":
        print(A * 0.56)
    elif B == "SGD":
        print(A * 1.70)
    elif B == "THB":
        print(A * 1.30)
    elif B == "AED":
        print(A * 0.63)
    elif B == "SAR":
        print(A * 0.61)
    elif B == "HKD":
        print(A * 2.20)
    elif B == "IDR":
        print(A * 9400.00)
    elif B == "MYR":
        print(A * 0.50)
    elif B == "PHP":
        print(A * 12.50)
    else:
        print("Currency not found!")
    time.sleep(2)
