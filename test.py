import requests

url = "https://engine.prod.bria-api.com/v1/prompt_enhancer"

payload = {
  "prompt": "an old man fishing"
}

headers = {
  "Content-Type": "application/json",
  "api_token": "550b80f24a304b8db6cf59bccaaf677b"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(response.text)