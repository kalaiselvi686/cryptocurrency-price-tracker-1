import requests
import pandas as pd
from datetime import datetime

# CoinMarketCap API
url = "https://pro-api.coinmarketcap.com/public-api/v1/cryptocurrency/listings/latest"

params = {
    "start": 1,
    "limit": 10,
    "convert": "USD"
}

# Get data from CoinMarketCap
response = requests.get(url, params=params, timeout=15)

if response.status_code == 200:

    coins = response.json()["data"]

    data = []

    for coin in coins:
        usd = coin["quote"]["USD"]

        data.append({
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Coin": coin["name"],
            "Symbol": coin["symbol"],
            "Price": usd["price"],
            "24h Change": usd["percent_change_24h"],
            "Market Cap": usd["market_cap"]
        })

    # Create table
    df = pd.DataFrame(data)

    # Save data to CSV
    df.to_csv("crypto_data.csv", index=False)

    print("\nCryptocurrency data collected successfully!\n")
    print(df)

else:
    print("Failed to get data.")
    print("Status Code:", response.status_code)