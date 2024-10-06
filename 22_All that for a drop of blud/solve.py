import requests

url_base = "https://startgame.oasis.cryptonite.live"
headers = {"User-Agent": "OASISPlayer"}

# Step 1: POST to /game endpoint
response1 = requests.post(f"{url_base}/game", headers=headers)
print("Step 1 Response:", response1.json())

# Step 2: POST to /game with name parameter
params2 = {"name": "Cryptonite"}
response2 = requests.post(f"{url_base}/game", headers=headers, params=params2)
print("Step 2 Response:", response2.json())

# Step 3: POST to /givemetheFlag with name and rank parameters
params3 = {"name": "Cryptonite", "rank": "4"}
response3 = requests.post(f"{url_base}/givemetheFlag", headers=headers, params=params3)
print("Flag Response:", response3.json())
