import requests

url = "https://api.github.com/repos/DevOps-2023-TeamA/tsao-frontend-svc/pulls"
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

# If you want to print the JSON response
print(data)

