import requests

url_base = "https://blogpost.oasis.cryptonite.live"

headers = {}
session = requests.Session()

home = session.get(f"{url_base}")
# Capture the cookie
cookies = session.cookies.get_dict()
print("Initial Cookies:", cookies)


robots = session.get(f"{url_base}/robots.txt", headers=headers, cookies=cookies)
print("Robots Response:", robots.text)



endpoint_from_robots = "/hiddenFlag"

# PATCH request
patch_response = session.patch(f"{url_base}{endpoint_from_robots}", headers=headers, cookies=cookies)
print("PATCH Response:", patch_response.text)

# PUT request
put_response = session.put(f"{url_base}{endpoint_from_robots}", headers=headers, cookies=cookies)
print("PUT Response:", put_response.text)

# OPTIONS request
options_response = session.options(f"{url_base}{endpoint_from_robots}", headers=headers, cookies=cookies)
print("OPTIONS Response:", options_response.text)

# Final request to get the flag
flag_response = session.options(f"{url_base}{endpoint_from_robots}", headers=headers, cookies=cookies)
print("Flag Response:", flag_response.text)
