import requests
import re
import time

API_KEY = 'REPLACE_WITH_KEY'
TOKEN = 'API_TOKEN'
BOARD_ID = 'BOARD_ID'
LIST_NAME = "NAME"  # Replace with the name of your list
RATE_LIMIT_THRESHOLD = 90

request_count = 0

def get_list_id(board_id, list_name):
    global request_count
    url = f"https://api.trello.com/1/boards/{board_id}/lists?key={API_KEY}&token={TOKEN}"
    response = requests.get(url)
    request_count += 1
    check_rate_limit()
    
    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}: {response.content}")
        return None

    if not response.content:
        print("Empty response received.")
        return None

    try:
        lists = response.json()
    except ValueError:
        print(f"Invalid JSON response: {response.content}")
        return None
    
    # Print all list names for debugging
    print("Lists on the board:")
    for lst in lists:
        print(lst['name'])
        if lst['name'] == list_name:
            return lst['id']

    return None

def check_rate_limit():
    global request_count
    if request_count >= RATE_LIMIT_THRESHOLD:
        time.sleep(10)
        request_count = 0

def main():
    print("Reminder: Ensure you've backed up your Trello data before running this script!")
    
    target_list_id = get_list_id(BOARD_ID, LIST_NAME)

    if not target_list_id:
        print(f"List named '{LIST_NAME}' not found on board '{BOARD_ID}'.")
        return

    url = f"https://api.trello.com/1/lists/{target_list_id}/cards?key={API_KEY}&token={TOKEN}"
    response = requests.get(url)
    check_rate_limit()

    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}: {response.content}")
        return

    if not response.content:
        print("Empty response received from card fetch.")
        return

    try:
        cards = response.json()
    except ValueError:
        print(f"Invalid JSON response from card fetch: {response.content}")
        return

    for card in cards:
        description = card['desc']
        card_id = card['id']

        match_name = re.search(r"Name: (.+?)\n", description)
        match_subject = re.search(r"Subject: (.+?)\n", description)

        if match_name and match_subject:
            new_title = f"{match_subject.group(1)} {match_name.group(1)}"
            
            update_url = f"https://api.trello.com/1/cards/{card_id}?key={API_KEY}&token={TOKEN}&name={new_title}"
            response = requests.put(update_url)
            check_rate_limit()
            
            if response.status_code != 200:
                print(f"Error updating card {card_id}: {response.text}")

if __name__ == "__main__":
    main()
