import requests

def fetch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_location = user_data["location"]["country"]
        return user_name, user_location
    else:
        raise Exception("Failed to  fetch user data")
    

def main():
        try:
            user_name,user_location = fetch_random_user_freeapi()
            print(f"Username: {user_name} \nLocation: {user_location}")
        except Exception as e:
            print(str(e))
if __name__ == "__main__":
        main()