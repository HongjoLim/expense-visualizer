from wsimple.api import Wsimple
import yfinance as yf

def get_otp():
    return input("Enter otpnumber: \n>>>")

def main():
    #email = str(input("Enter email: \n>>>"))
    #password = str(input("Enter password: \n>>>"))
    
    #ws = Wsimple(email, password, otp_callback=get_otp) 
    #print(ws.is_operational())
    #print(ws.get_exchange_rate())
    tickers_owned_us = ['MSFT', 'FB', 'GOOG', 'GOOGL', 'EPAM']
    tickers_owned_tsx = ['VFV.TO']
    positions_us_mk = [yf.Ticker(ticker) for ticker in tickers_owned_us]
    prices = [position.info['currentPrice'] for position in positions_us_mk]

    [print(price) for price in prices]

if __name__ == '__main__':
    main()