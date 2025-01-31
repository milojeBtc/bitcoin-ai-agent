from crypto import get_crypto_price
import os
from dotenv import load_dotenv
from together import Together
import time

load_dotenv()
os.getenv("TOGETHER_API_KEY")

client = Together()

LAST_REQUEST_TIME = 0
RATE_LIMIT_SECONDS = 300

cache = {}
def rate_limit():
    global LAST_REQUEST_TIME
    curr_time = time.time()
    if curr_time-LAST_REQUEST_TIME<RATE_LIMIT_SECONDS:
        return False
    LAST_REQUEST_TIME = curr_time
    return True

crypto_price_tool = [
        {
            "type": "function",
            "function": {
            "name": "get_crypto_price",
            "description": "Get current price of bitcoin in INR",
            }
        }
    ]
prompt = f"""
    You are a helpful and knowledgeable assistant designed to provide users with the current Bitcoin price in INR. 
    Follow these guidelines:
    1. Use the provided tool to fetch Bitcoin prices whenever necessary. The tool's output is accurate and up-to-date.
    2. If the user asks in a language other than English, summarize or translate their query into English and respond in English.
    3. Maintain a conversational tone and context for multi-turn conversations, ensuring users feel understood.
"""
messages = [
        {"role": "system", "content": prompt},
]

def process_user_input(user_input):
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.5,
        tools=crypto_price_tool
    )
    if response.choices[0].message.tool_calls:
      try:
        print("Searching...")
        if(not rate_limit()):
           price = cache["price"]
        else:
           price = get_crypto_price()
           cache["price"]=price
        price = str(price)
        messages.append({
                    "tool_call_id": response.choices[0].message.tool_calls[0].id,
                    "role": "tool",
                    "name": response.choices[0].message.tool_calls[0].function.name,
                    "content": f"This is the price obtained from the function call in INR: {price}"
        })
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=messages,
            max_tokens=100,
            temperature=0.5
         )
        response = response.choices[0].message.content
      except Exception as e:
        return f"Error: {e}"
    else:
        response = response.choices[0].message.content
    return response

if __name__ == '__main__':
    print("Enter your prompt. Type exit to quit")
    while True:
        user_input = input("User:")
        if user_input=="exit":
            break
        print("AGENT:",process_user_input(user_input))