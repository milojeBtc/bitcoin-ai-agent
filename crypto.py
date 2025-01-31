import requests
import os
from dotenv import load_dotenv

def get_crypto_price(crypto="bitcoin",currency="INR"):
    print("Fetching...")
    load_dotenv()
    api_key = os.getenv("COIN_API")
    headers = {
    "X-API-KEY": api_key
    }
    url = f"https://openapiv1.coinstats.app/coins/{crypto}?currency={currency}"
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response.json()["price"]
    except requests.RequestException as e:
        return f"Error fetching cryptocurrency price: {e}"