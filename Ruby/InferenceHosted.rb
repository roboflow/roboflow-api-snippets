require 'httparty'
require 'cgi'

model_endpoint = "dataset/v" # Set model endpoint
api_key = "" # Your API KEY Here
img_url = "https://i.imgur.com/PEEvqPN.png" # Construct the URL

img_url = CGI::escape(img_url)

params =  "?api_key=" + api_key + "&image=" + img_url

response = HTTParty.post(
    "https://detect.roboflow.com/" + model_endpoint + params,
    headers: {
    'Content-Type' => 'application/x-www-form-urlencoded',
    'charset' => 'utf-8'
  })

puts response