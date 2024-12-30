import requests

def fetch_random_product():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/30'
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        category = product_data["category"]
        brand = product_data["brand"]
        return category,brand
    else:
        raise Exception("Unable to fetch data")

def main():
    try:
        category , brand = fetch_random_product()
        print(f"Category: {category} \n Brand: {brand}")
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()