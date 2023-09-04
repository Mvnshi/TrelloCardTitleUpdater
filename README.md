# TrelloCardTitleUpdater

This script helps in updating the title of Trello cards on a specific list by fetching details from the card's description. It ensures that rate limits for API calls are adhered to and provides helpful debug prints.

## Features:
1. Retrieve all lists from a given board.
2. Find a specific list based on the name.
3. Retrieve all cards from the chosen list.
4. Extract specific details ("Name" and "Subject") from the description of each card.
5. Update the card's title with the extracted details.

## Prerequisites:

1. Python 3.x
2. `requests` library. Install via pip:
    ```bash
    pip install requests
    ```

## Usage:

1. Clone the repository.
2. Replace `REPLACE_WITH_KEY`, `API_TOKEN`, `BOARD_ID`, and `NAME` placeholders in the script with your respective Trello API Key, Token, Board ID, and List Name.
3. Run the script:
    ```bash
    python TrelloCardTitleUpdater.py
    ```

## Precautions:

- Always back up your Trello data before running this or any script that makes modifications to it.

## Contribution:

Feel free to fork, raise issues, and submit PRs. Any feedback or suggestions are welcome!

## License:

MIT

