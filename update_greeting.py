# update_greeting.py

import os
from datetime import datetime
from notion_client import Client

# Load secrets from environment (GitHub Actions)
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
PAGE_ID = "278b3ee4-0ced-80b4-9b6f-c066d09931cb"  # Your page ID formatted with hyphens

# Initialize Notion client
notion = Client(auth=NOTION_TOKEN)

# Determine greeting based on current time (Gainesville timezone)
now = datetime.now()  # local time; adjust if needed for Gainesville
hour = now.hour

if 5 <= hour < 12:
    greeting = "Good Morning, Gainesville"
elif 12 <= hour < 17:
    greeting = "Good Afternoon, Gainesville"
elif 17 <= hour < 22:
    greeting = "Good Evening, Gainesville"
else:
    greeting = "See You Tomorrow, Gainesville"

# Update the **title** of the page
notion.pages.update(
    PAGE_ID,
    properties={
        "Name": {  # Replace "Name" with your row's title property if different
            "title": [{"text": {"content": greeting}}]
        }
    }
)

print(f"Greeting updated to: {greeting}")
