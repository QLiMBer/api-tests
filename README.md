# Notion API Test Script

This is a simple Python script designed to test basic connectivity and authorization with the Notion API. It demonstrates how to make authenticated calls to retrieve user information and search for pages shared with a Notion integration.

## Features

*   Reads the Notion API token securely from a `.env` file.
*   Tests the `GET /v1/users/me` endpoint to verify the API token.
*   Tests the `POST /v1/search` endpoint:
    *   With a specific query (`QLiMBer` in the example).
    *   Without a query (to list all accessible pages/databases).
*   Prints the API responses (or errors) to the console.

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    ```
    *(Use `python3` if needed)*
3.  **Activate the Virtual Environment:**
    *   Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
    *   macOS/Linux: `source .venv/bin/activate`
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Use `pip3` if needed)*
5.  **Create `.env` file:** Create a file named `.env` in the project root directory.
6.  **Add API Token:** Add your Notion integration token to the `.env` file:
    ```dotenv
    NOTION_API_TOKEN="YOUR_SECRET_TOKEN_HERE"
    ```
    *(Replace `YOUR_SECRET_TOKEN_HERE` with your actual token. The `.gitignore` file prevents this file from being committed.)*

## Running the Script

Ensure your virtual environment is activated. Then, run:

```bash
python notion_test.py
```
*(Use `python3` if needed)*

The script will execute the API calls and print the results to your terminal.

## Notion Integration Setup

*   You need to have a Notion integration created ([Notion Integration Guide](https://developers.notion.com/docs/create-a-notion-integration)).
*   Ensure you have shared at least one page with your integration from your Notion workspace for the search endpoints to return results. 