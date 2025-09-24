# update_greeting.py

import os
from datetime import datetime
from notion_client import Client

# Load Notion token from environment variable
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
PAGE_ID = "278b3ee4-0ced-80b4-9b6f-c066d09931cb"  # Your page (row) ID with hyphens

# Initialize Notion client
notion = Client(auth=NOTION_TOKEN)

# Determine greeting based on Gainesville time
now = datetime.now()  # adjust if your server is in a different timezone
hour = now.hour

if 5 <= hour < 12:
    greeting = "Good Morning, Gainesville"
elif 12 <= hour < 17:
    greeting = "Good Afternoon, Gainesville"
elif 17 <= hour < 22:
    greeting = "Good Evening, Gainesville"
else:
    greeting = "See You Tomorrow, Gainesville"

# Update the "Greeting" column as a Rich Text property
notion.pages.update(
    PAGE_ID,
    properties={
        "Greeting": {
            "rich_text": [
                {"text": {"content": greeting}}
            ]
        }
    }
)

print(f"Greeting updated to: {greeting}")