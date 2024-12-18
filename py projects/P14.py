#curency changer

import time

while True:
    currencies = ['USD', 'EUR', 'GEL', 'JPY', 'GBP', 'RUB', 'CNY', 'INR', 'IQD', 'CHF', 
                'CAD', 'AUD', 'NZD', 'SEK', 'NOK', 'DKK', 'ZAR', 'BRL', 'MXN', 'KRW', 
                'TRY', 'PLN', 'SGD', 'THB', 'AED', 'SAR', 'HKD', 'IDR', 'MYR', 'PHP']
    print(currencies)
    A = (int(input("how many lari do you have : ")))
    B = (str(input("on what curency you want to change : ")))
    if B == "NZD":
        print(A * 0.55)
    elif B == "SEK":
        print(A * 3.60)
    elif B == "NOK":
        print(A * 3.70)
    elif B == "DKK":
        print(A * 2.40)
    elif B == "ZAR":
        print(A * 6.80)
    elif B == "BRL":
        print(A * 1.75)
    elif B == "MXN":
        print(A * 6.00)
    elif B == "KRW":
        print(A * 450.00)
    elif B == "TRY":
        print(A * 9.20)
    elif B == "PLN":
        print(A * 1.40)
    elif B == "SGD":
        print(A * 0.48)
    elif B == "THB":
        print(A * 11.20)
    elif B == "AED":
        print(A * 1.28)
    elif B == "SAR":
        print(A * 1.30)
    elif B == "HKD":
        print(A * 2.70)
    elif B == "IDR":
        print(A * 5300.00)
    elif B == "MYR":
        print(A * 1.50)
    elif B == "PHP":
        print(A * 19.80)
    elif B == "EGP":
        print(A * 10.50)
    elif B == "ARS":
        print(A * 70.00)
    elif B == "VND":
        print(A * 8100.00)
    elif B == "COP":
        print(A * 1600.00)
    elif B == "UAH":
        print(A * 9.50)
    elif B == "RON":
        print(A * 1.75)
    elif B == "BGN":
        print(A * 1.80)
    elif B == "HUF":
        print(A * 110.00)
    elif B == "CZK":
        print(A * 7.50)
    elif B == "ISK":
        print(A * 45.00)
    elif B == "LKR":
        print(A * 130.00)
    elif B == "PKR":
        print(A * 60.00)
    elif B == "KWD":
        print(A * 0.11)
    elif B == "BHD":
        print(A * 0.13)
    elif B == "OMR":
        print(A * 0.13)
    elif B == "QAR":
        print(A * 1.30)
    elif B == "JOD":
        print(A * 0.25)
    elif B == "CLP":
        print(A * 280.00)
    elif B == "DZD":
        print(A * 46.00)
    elif B == "NGN":
        print(A * 500.00)
    else:
        print("Error: Currency not found")
    time.sleep(2)