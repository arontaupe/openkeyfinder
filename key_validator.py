import openai

def check_openai_api_key(api_key):
    """Check the validity of a single OpenAI API key."""
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True

def check_api_keys_in_list(api_keys):
    """Check the validity of each OpenAI API key in a list."""
    results = {}
    for key in api_keys:
        results[key] = check_openai_api_key(key)
    return results

# Example usage
OPENAI_API_KEY = "sk-7....."

if check_openai_api_key(OPENAI_API_KEY):
    print("Valid OpenAI API key.")
else:
    print("Invalid OpenAI API key.")

# Check a list of keys
keys_to_check = [
    "sk-abcdef1234567890abcdef1234567890abcdef12",
    "sk-1234567890abcdef1234567890abcdef12345678",
    "sk-abcdefabcdefabcdefabcdefabcdefabcdef12",
    "sk-7890abcdef7890abcdef7890abcdef7890abcd",
    "sk-1234abcd1234abcd1234abcd1234abcd1234abcd",
    "sk-abcd1234abcd1234abcd1234abcd1234abcd1234",
    "sk-5678efgh5678efgh5678efgh5678efgh5678efgh",
    "sk-efgh5678efgh5678efgh5678efgh5678efgh5678",
    "sk-ijkl1234ijkl1234ijkl1234ijkl1234ijkl1234",
    "sk-mnop5678mnop5678mnop5678mnop5678mnop5678",
    "sk-qrst1234qrst1234qrst1234qrst1234qrst1234",
    "sk-uvwx5678uvwx5678uvwx5678uvwx5678uvwx5678",
    "sk-1234ijkl1234ijkl1234ijkl1234ijkl1234ijkl",
    "sk-5678mnop5678mnop5678mnop5678mnop5678mnop",
    "sk-qrst5678qrst5678qrst5678qrst5678qrst5678",
    "sk-uvwx1234uvwx1234uvwx1234uvwx1234uvwx1234",
    "sk-1234abcd5678efgh1234abcd5678efgh1234abcd",
    "sk-5678ijkl1234mnop5678ijkl1234mnop5678ijkl",
    "sk-abcdqrstefghuvwxabcdqrstefghuvwxabcdqrst",
    "sk-ijklmnop1234qrstijklmnop1234qrstijklmnop",
    "sk-1234uvwx5678abcd1234uvwx5678abcd1234uvwx",
    "sk-efghijkl5678mnopabcd1234efghijkl5678mnop",
    "sk-mnopqrstuvwxabcdmnopqrstuvwxabcdmnopqrst",
    "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop",
    "sk-abcd1234efgh5678abcd1234efgh5678abcd1234",
    "sk-1234ijklmnop5678ijklmnop1234ijklmnop5678",
    "sk-qrstefghuvwxabcdqrstefghuvwxabcdqrstefgh",
    "sk-uvwxijklmnop1234uvwxijklmnop1234uvwxijkl",
    "sk-abcd5678efgh1234abcd5678efgh1234abcd5678",
    "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop",
    "sk-1234qrstuvwxabcd1234qrstuvwxabcd1234qrst",
    "sk-efghijklmnop5678efghijklmnop5678efghijkl",
    "sk-mnopabcd1234efghmnopabcd1234efghmnopabcd",
    "sk-ijklqrst5678uvwxijklqrst5678uvwxijklqrst",
    "sk-1234ijkl5678mnop1234ijkl5678mnop1234ijkl",
    "sk-abcdqrstefgh5678abcdqrstefgh5678abcdqrst",
    "sk-ijklmnopuvwx1234ijklmnopuvwx1234ijklmnop",
    "sk-efgh5678abcd1234efgh5678abcd1234efgh5678",
    "sk-mnopqrstijkl5678mnopqrstijkl5678mnopqrst",
    "sk-1234uvwxabcd5678uvwxabcd1234uvwxabcd5678",
    "sk-ijklmnop5678efghijklmnop5678efghijklmnop",
    "sk-abcd1234qrstuvwxabcd1234qrstuvwxabcd1234",
    "sk-1234efgh5678ijkl1234efgh5678ijkl1234efgh",
    "sk-5678mnopqrstuvwx5678mnopqrstuvwx5678mnop",
    "sk-abcdijkl1234uvwxabcdijkl1234uvwxabcdijkl",
    "sk-ijklmnopabcd5678ijklmnopabcd5678ijklmnop",
    "sk-1234efghqrstuvwx1234efghqrstuvwx1234efgh",
    "sk-5678ijklmnopabcd5678ijklmnopabcd5678ijkl",
    "sk-abcd1234efgh5678abcd1234efgh5678abcd1234",
    "sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop"
]

results = check_api_keys_in_list(keys_to_check)
for key, is_valid in results.items():
    status = "Valid" if is_valid else "Invalid"
    print(f"API Key: {key} - {status}")
