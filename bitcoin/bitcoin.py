import sys
import requests

def main():
    # Ensure the user provided exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <amount>")

    # Try to convert the argument to a float representing the number of Bitcoins
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument must be a number")

    # Query the CoinDesk Bitcoin Price Index API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price data")

    # Extract the current price in USD from the JSON response
    try:
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
    except (KeyError, ValueError):
        sys.exit("Error parsing Bitcoin price data")

    # Calculate the total cost
    cost = amount * price

    # Output the cost formatted to four decimal places with a thousands separator
    print(f"${cost:,.4f}")

main()
