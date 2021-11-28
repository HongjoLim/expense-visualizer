from wsimple.api import Wsimple
import json

CREDENTIALS_JSON_FILE_NAME = 'ws_credentials.json'

def read_file(file_name):

    with open(file_name, 'r') as f:
        lines = f.read()
        
    return lines

def get_credentials_from_json(content):
    return json.loads(content)

def get_otp():
    return input("Enter otpnumber: \n>>>")

def main():
    json_content =  read_file(CREDENTIALS_JSON_FILE_NAME)
    credentials = get_credentials_from_json(json_content)
    email = credentials['email']
    password = credentials['password']

    ws = Wsimple(email, password, otp_callback=get_otp) 
    accounts = [account for account in ws.get_accounts()['results'] if account['status'] != 'closed']

    [print(account['position_quantities']) for account in accounts]

    #print(ws.is_operational())
    #print(ws.get_exchange_rate())
    tickers_owned_us = ['MSFT', 'FB', 'GOOG', 'GOOGL', 'EPAM']

if __name__ == '__main__':
    main()