import os
from notion_client import Client
from datetime import datetime
import pytz

# Secrets from GitHub
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

notion = Client(auth=NOTION_TOKEN)

# Time in Gainesville (Eastern)
tz = pytz.timezone("America/New_York")
now = datetime.now(tz)
hour = now.hour

if 5 <= hour < 12:
    greeting = "Good Morning, Gainesville"
elif 12 <= hour < 17:
    greeting = "Good Afternoon, Gainesville"
elif 17 <= hour < 21:
    greeting = "Good Evening, Gainesville"
else:
    greeting = "See You Tomorrow, Gainesville"

notion.pages.update(
    PAGE_ID,
    properties={
        "Greeting": {
            "title": [{"text": {"content": greeting}}]
        }
    }
)

print(f"Updated Notion row with: {greeting}")
