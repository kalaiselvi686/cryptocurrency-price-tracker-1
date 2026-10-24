# Cryptocurrency Price Tracker

This project uses Selenium to collect the leading cryptocurrencies from CoinMarketCap and append their name, symbol, price, 24-hour change, market cap, and UTC collection time to a CSV history file.

## Setup

From this directory, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Google Chrome must be installed. `webdriver-manager` downloads a compatible ChromeDriver on the first run.

## Usage

The default command collects 10 coins in headless Chrome and appends them to `crypto_prices.csv`:

```powershell
python crypto_price_tracker.py
```

Examples:

```powershell
python crypto_price_tracker.py --top 25 --csv data\prices.csv
python crypto_price_tracker.py --top 10 --no-headless
python crypto_price_tracker.py --max-price 100 --min-change 2.5
```

Use `python crypto_price_tracker.py --help` to see all options. Filters are applied after scraping, so a filtered run may save fewer rows than `--top` requests.