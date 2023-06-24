import requests
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')

    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        sys.exit('Invalid, please provide a valid float number.')

    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_data = response.json()
        current_price = bitcoin_data['bpi']['USD']['rate_float']

        cost = current_price * bitcoins_to_buy
        formatted_cost = "{:,.4f}".format(cost)  # Format the cost with the thousands separator
        print(F"${formatted_cost}", end="")
    except requests.RequestException:
        sys.exit("Error occurred while requesting data")


if __name__ == "__main__":
    main()
