import pandas as pd

df = pd.read_csv("analyzed_tickets.csv")

priorities = df.sort_values(
    by=["priority", "resolution_time"],
    ascending=[False, False]
)

print("\nToday's Priority Tasks:\n")

for i, row in priorities.head(5).iterrows():
    print(f"- Follow up Ticket {row['id']} ({row['priority']})")