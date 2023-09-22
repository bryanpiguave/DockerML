import requests
from fastapi import FastAPI, Request

def main():
    url ="http://localhost:80"
    item_id = 1
    response = requests.get(f"{url}/items/{item_id}")

    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")

    return 0 

if __name__=="__main__":
    main()