require 'httparty'
require 'cgi'

dataset_name = "your-dataset" # Set Dataset Name (Found in Dataset URL)
api_key = "" # Your API KEY Here
img_url = "https://i.imgur.com/PEEvqPN.png" # Construct the URL

img_url = CGI::escape(img_url)

params = "?api_key=" + api_key + 
"&name=YOUR_IMAGE.jpg" + 
"&split=train" +
"&image=" + img_url

response = HTTParty.post(
    "https://api.roboflow.com/dataset/" + dataset_name + "/upload" + params,
    headers: {
    'Content-Type' => 'application/x-www-form-urlencoded',
    'charset' => 'utf-8'
  })

puts response