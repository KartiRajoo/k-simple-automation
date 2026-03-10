import json

tickets = [
    {"id": 101, "priority": "high", "resolution_time": 7200, "agent": "APAC"},
    {"id": 102, "priority": "low", "resolution_time": 1800, "agent": "APAC"},
    {"id": 103, "priority": "medium", "resolution_time": 4000, "agent": "APAC"},
    {"id": 104, "priority": "high", "resolution_time": 9000, "agent": "APAC"},
]

with open("tickets.json", "w") as f:
    json.dump(tickets, f)

print("Tickets fetched")
