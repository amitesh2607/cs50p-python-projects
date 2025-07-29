import sys
import json
import requests


try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=661e3f5ba1a7b928b157a70884ae826e44fc074ddf15591bd30bdd60d36ecc3c"
    )
except requests.RequestException:
    pass

# print(json.dumps(response.json(), indent=2))

o = response.json()
price = o["data"]["priceUsd"]
total_price = float(price) * n

print(f"${total_price:,.4f}")

# p = o["data"]
# print(p["priceUsd"])
