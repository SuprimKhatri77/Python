import requests

def fetch_stock_data():
    url = 'https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata'
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stock_data = data["data"]
        market_cap = stock_data["data"][0]["MarketCap"]
        current_price = stock_data["data"][0]["CurrentPrice"]
        return market_cap, current_price
    else:
        raise Exception("Failed to fetch the stock data")
    
def main():
    try: 
        market_cap, current_price = fetch_stock_data()
        print(f"MarketCap: {market_cap} \nCurrentPrice: {current_price}")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()