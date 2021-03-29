require 'base64'
require 'httparty'

encoded = Base64.encode64(File.open("YOUR_IMAGE.jpg", "rb").read)
model_enpoint = "xx-your-model--1" # Set model endpoint
api_key = "" # Your API KEY Here

params = "?access_token=" + api_key
+ "&name=YOUR_IMAGE.jpg"

response = HTTParty.post(
    "https://infer.roboflow.com/" + model_endpoint + params,
    body: encoded, 
    headers: {
    'Content-Type' => 'application/x-www-form-urlencoded',
    'charset' => 'utf-8'
  })

  puts response

 