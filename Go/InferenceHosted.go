package main

import (
    "fmt"
	"net/http"
	"net/url"
)

func main() {
	api_key := ""  // Your API Key
	model_endpoint := "your-dataset" // Set model endpoint
	img_url := "https://i.imgur.com/PEEvqPN.png"


	uploadURL := "https://infer.roboflow.com/" + model_endpoint
	+ "?access_token=" + api_key
	+ "&image=" + url.QueryEscape(img_url)

	res, _ := http.Post(uploadURL, "application/x-www-form-urlencoded", nil)
	fmt.Println(res)

}

