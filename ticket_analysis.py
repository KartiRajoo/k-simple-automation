import pandas as pd

df = pd.read_json("tickets.json")

# calculate slow tickets
slow_tickets = df[df["resolution_time"] > 3600]

# high priority
priority_tickets = df[df["priority"] == "high"]

result = pd.concat([slow_tickets, priority_tickets])

print(result)