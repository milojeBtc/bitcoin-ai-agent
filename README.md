# AI AGENT FOR BITCOIN PRICES WITH SUPPORT FOR ALL LANGUAGES
- It fetches bitcoin prices with caching and rate-limiting
- It responds to any language-but the response is always in English
- Uses LLaMA 3.1 8B from TogetherAI

## Setup
1. Clone the repository
2. Install the dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and store the environment variables. Refer to the `example.env` file

## Prompt Engineering
1. Defining context and role:
   ```
   "You are a helpful and knowledgeable assistant designed to provide users with the current Bitcoin price in INR. ."
   ```
2. Integration of tool: We define some guidelines for the way it is supposed to work
   ```
   Use the provided tool to fetch Bitcoin prices whenever necessary. The tool's output is accurate and up-to-date.
   ```
3. Handling translation:
   ```
   If the user asks in a language other than English, summarize or translate their query into English and respond in English.
   ```
4. Ensuring a conversational guideline:
   ```
   Maintain a conversational tone and context for multi-turn conversations, ensuring users feel understood.
   ```
5. Description of crypto tool: We define the purpose of the crypto tool
   ```
   "description": "Get current price of bitcoin in INR",
   ```
6. Storing context
   We store the user responses and responses from the assistant and provide them back for context
7. Getting a response for the result from the function to get response from the assistant
   ```
   messages.append({
                    "tool_call_id": response.choices[0].message.tool_calls[0].id,
                    "role": "tool",
                    "name": response.choices[0].message.tool_calls[0].function.name,
                    "content": f"This is the price obtained from the function call in INR: {price}"
        })
   ```
## Sample response
```
Enter your prompt. Type exit to quit
User:Hi
AGENT: It's nice to talk to you. Is there something specific you'd like to know or discuss? You can ask me anything, and I'll do my best to help. By the way, would you like to know the current price of Bitcoin in INR?
User:Yes, please
Searching...
Fetching...
AGENT: It seems like you're asking for the current Bitcoin price in INR, but I'm not sure what specifically you're looking for. Could you please clarify or ask a question, like "What's the current Bitcoin price in INR"?

I'll use the provided tool to fetch the latest price for you.
User:Yes, I want the current price of BTC?
Searching...
AGENT: The current price of Bitcoin in INR is approximately ₹8,19,67,071. However, please note that the price may fluctuate rapidly and might be different at the time of your actual inquiry. I've fetched the price for you as of my knowledge cutoff.
User:Namaste!
AGENT: Namaste! How can I assist you with the current price of Bitcoin in INR?
User:Bye
AGENT: Have a good day!
User:exit
```

## Assumptions & Limitations:
1. The agent responds only in English, even if the user's input is in another language.
2. The agent uses time-based cryptocurrency price caching and rate-limiting(up to 5 mins) to avoid redundant API calls. So, the rates can be
   5 mins old.
3. The translation capability is basic and relies on the LLaMA model's multilingual understanding.
4. No streaming has been included in the code, which means the user will have to wait for the entire response
5. The responses are kept short with the assumption that 100 tokens would be enough for the responses. The number of tokens per word is
   assumed to be 1.5
