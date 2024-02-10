import requests
import json
from datetime import datetime
import sys

if len(sys.argv) != 2:
    print("No Discord webhook URL provided. Please run the script with a webhook URL as an argument.")
    sys.exit(1)

def generate_report(repo):
    url = "https://api.github.com/repos/DevOps-2023-TeamA/" + repo + "/pulls"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    current_date = datetime.now()

    tmp_report = ""
    for item in data:
        if item['merged_at'] == None: continue
        merge_date = datetime.fromisoformat(item['merged_at'].replace('Z', ''))
        time_difference = current_date - merge_date
        
        if time_difference.total_seconds() > 86400: continue
        
        tmp_report += f"- [{item['title']}](<{item['html_url']}>)\n"
        
    if tmp_report == "": return
    
    tmp_report = f"## [{repo}](<https://github.com/DevOps-2023-TeamA/{repo}>)\n{tmp_report}\n"
    return tmp_report

def send_message(report):
    discord_webhook_url = sys.argv[1]
    # Payload to send to Discord
    data = {
        'content': report,
        'username': 'Daily Reports'
    }

    # POST request to the Discord webhook URL
    response = requests.post(discord_webhook_url, json=data)

    # Check the response
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message, status code: {response}")
        try:
            error_message = response.json()  # Attempt to get JSON error response
            print("Error details:", error_message)
        except ValueError:  # In case the response isn't in JSON format
            print("Error details:", response.text)
        sys.exit(1)

reports = [
    generate_report("tsao-frontend-svc"),
    generate_report("tsao-backend-svc"),
    generate_report("tsao-db"),
    generate_report("tsao-tests")
]
filtered_reports = [element for element in reports if element is not None]

for i in range(0, len(filtered_reports)):
    if i == 0:
        send_message("# Daily Report\n" + i)
    else:
        send_message(i)

if len(filtered_reports) == 0:
    send_message("# Daily Report\nNo progress was made.")
