import requests
import urllib.parse

# Your API Key
api_key = ""

# Model Endpoint
model_endpoint = "dataset/v"

# Construct the URL
img_url = "https://i.imgur.com/PEEvqPN.png"
upload_url = "".join([
    "https://detect.roboflow.com/" + model_endpoint,
    "?api_key=" + api_key,
    "&image=" + urllib.parse.quote_plus(img_url)
])

# POST to the API
r = requests.post(upload_url)

# Output result
print(r.json())