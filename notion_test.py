import os
import requests
import json
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_API_VERSION = "2022-06-28" # Use the version from the documentation
BASE_URL = "https://api.notion.com/v1"

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_API_VERSION,
}

# --- API Functions ---
def get_me():
    """Calls the GET /users/me endpoint."""
    print("\n--- Testing GET /users/me ---")
    if not NOTION_API_TOKEN:
        print("Error: NOTION_API_TOKEN environment variable not set.")
        return

    url = f"{BASE_URL}/users/me"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        print("Status Code:", response.status_code)
        print("Response JSON:")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error calling GET /users/me: {e}")
        if e.response is not None:
            print("Response Status Code:", e.response.status_code)
            try:
                print("Response Body:", json.dumps(e.response.json(), indent=2))
            except json.JSONDecodeError:
                print("Response Body:", e.response.text)

def search(query=None):
    """Calls the POST /search endpoint."""
    if query:
        print(f"\n--- Testing POST /search (Query: '{query}') ---")
        payload = {"query": query}
    else:
        print("\n--- Testing POST /search (No Query) ---")
        payload = {} # No query searches all shared pages/databases

    if not NOTION_API_TOKEN:
        print("Error: NOTION_API_TOKEN environment variable not set.")
        return

    url = f"{BASE_URL}/search"
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes
        print("Status Code:", response.status_code)
        print("Response JSON:")
        print(json.dumps(response.json(), indent=2))

        # Check if the specific page was found when searching
        if query and 'results' in response.json():
            found = any(query.lower() in result.get('properties', {}).get('title', {}).get('title', [{}])[0].get('plain_text', '').lower()
                        for result in response.json()['results'] if result.get('object') == 'page')
            if found:
                print(f"\nSuccessfully found a page containing '{query}' in the title.")
            else:
                print(f"\nCould not find a page containing '{query}' in the title within the results.")

    except requests.exceptions.RequestException as e:
        print(f"Error calling POST /search: {e}")
        if e.response is not None:
            print("Response Status Code:", e.response.status_code)
            try:
                print("Response Body:", json.dumps(e.response.json(), indent=2))
            except json.JSONDecodeError:
                print("Response Body:", e.response.text)

# --- Main Execution ---
if __name__ == "__main__":
    if not NOTION_API_TOKEN:
        print("Error: Please set the NOTION_API_TOKEN environment variable before running the script.")
    else:
        print("Notion API Test Script")
        print(f"Using Token: ...{NOTION_API_TOKEN[-4:]}") # Show last 4 chars for confirmation

        # Test 1: Get Bot User Info
        get_me()

        # Test 2: Search for the specific page title
        search(query="QLiMBer")

        # Test 3: Search without a query (list accessible items)
        search() 