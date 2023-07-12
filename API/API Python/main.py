import requests

url: str = "https://api.github.com"
result = requests.get(url)
print(result)
print(f"status code {result.status_code}")
