import requests

def fetch_random_jokes_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1'


    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        userdata = data["data"]
        random_joke = userdata["data"][3]["content"]
        random_id = userdata["data"][3]["id"]
        return random_joke , random_id
    else:
        raise Exception("Failed to fetch the api data")
    
def main():
    try:
        random_joke,random_id = fetch_random_jokes_freeapi()
        print(f"Random Joke: {random_joke}  \nId: {random_id}")
    except Exception as e :
        print(str(e))

if __name__ == "__main__":
    main()