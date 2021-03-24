require 'base64'
require 'httparty'

encoded = Base64.encode64(File.open("YOUR_IMAGE.jpg", "rb").read)
dataset_name = "your-dataset" # Set Dataset Name (Found in Dataset URL)
api_key = "" # Your API KEY Here

params = "?api_key=" + api_key + 
"&name=YOUR_IMAGE.jpg" + 
"&split=train"

response = HTTParty.post(
    "https://api.roboflow.com/dataset/" + dataset_name + "/upload" + params,
    body: encoded, 
    headers: {
    'Content-Type' => 'application/x-www-form-urlencoded',
    'charset' => 'utf-8'
  })

  puts response

 