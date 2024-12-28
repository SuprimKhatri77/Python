import requests

def fetch_random_user_id():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/13'
    resp = requests.get(url)
    data = resp.json()

    if data["success"] and "data" in data:
        var = data["data"]
        user_gender = var["gender"]
        last_name = var["name"]["last"]
        message = data["message"]
        return user_gender, last_name, message
    else:
        raise Exception("Failed to fetch data ")
    
def main():
    try:
        user_gender, last_name, message = fetch_random_user_id()
        print(f"Gender: {user_gender} \nLast: {last_name} \nMessage: {message}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()