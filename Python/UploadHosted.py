import requests
import urllib.parse

# Construct the URL
img_url = "https://i.imgur.com/PEEvqPN.png"
# Your API Key
api_key = ""
# Set Dataset Name (Found in Dataset URL)
dataset_name = "your-dataset"

upload_url = "".join([
    "https://api.roboflow.com/dataset/" + dataset_name + "/upload",
    "?api_key=" + api_key,
    "&name=201-956-1246.png",
    "&split=train",
    "&image=" + urllib.parse.quote_plus(img_url)
])

# POST to the API
r = requests.post(upload_url)

# # Output result
print(r.json())