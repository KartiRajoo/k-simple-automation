import requests
from datetime import datetime, timedelta

ACCESS_TOKEN = "YOUR_INTERCOM_ACCESS_TOKEN"

url = "https://api.intercom.io/conversations"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

tickets = []

for convo in data["conversations"]:
    ticket = {
        "id": convo["id"],
        "priority": convo.get("priority", "normal"),
        "created_at": convo["created_at"],
        "assignee": convo.get("assignee", {}).get("name"),
    }

    tickets.append(ticket)

print(tickets)