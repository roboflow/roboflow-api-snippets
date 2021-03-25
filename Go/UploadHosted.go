package main

import (
    "fmt"
	"net/http"
	"net/url"
)

func main() {
	api_key := ""  // Your API Key
	dataset_name := "your-dataset" // Set Dataset Name (Found in Dataset URL)
	img_url := "https://i.imgur.com/PEEvqPN.png"


	uploadURL := "https://api.roboflow.com/dataset/"+ dataset_name + "/upload"+
    "?api_key=" + api_key +
    "&name=YOUR_IMAGE.jpg" +
    "&split=train" + "&image=" + url.QueryEscape(img_url)

	res, _ := http.Post(uploadURL, "application/x-www-form-urlencoded", nil)
	fmt.Println(res)

}

