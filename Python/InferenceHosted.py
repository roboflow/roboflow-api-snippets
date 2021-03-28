import requests
import urllib.parse

# Your API Key
api_key = ""

# Model Endpoint
model_endpoint = "xx-your-model--1"

# Construct the URL
img_url = "https://i.imgur.com/PEEvqPN.png"
upload_url = "".join([
    "https://infer.roboflow.com/" + model_endpoint,
    "?access_token=" + api_key,
    "&image=" + urllib.parse.quote_plus(img_url)
])

# POST to the API
r = requests.post(upload_url)

# Output result
print(r.json())