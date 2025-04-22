import requests
from sys import exit, argv

def coin_price(n):
    try:
        r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        price = float(r.json()['data']['priceUsd']) * n
    except requests.RequestException:
        exit(r.status_code)
    except ValueError:
        exit("Type casting error")
    else:
        return price
    
def main():
    try:
        coin_num = float(argv[1])
    except IndexError:
        exit("Missing command-line argument")
    except ValueError:
        exit("Command-line argument is not a number")

    amount = coin_price(coin_num)

    print(f"${amount:,.4f}")
    
    

main()