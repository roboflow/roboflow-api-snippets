package main

import (
    "fmt"
	"net/http"
	"net/url"
	"io/ioutil"

)

func main() {
	api_key := ""  // Your API Key
	dataset_name := "Your-Dataset" // Set Dataset Name (Found in Dataset URL)
	img_url := "https://i.imgur.com/PEEvqPN.png"


	uploadURL := "https://api.roboflow.com/dataset/"+ dataset_name + "/upload"+
    "?api_key=" + api_key +
    "&name=YOUR_IMAGE.jpg" +
    "&split=train" + "&image=" + url.QueryEscape(img_url)

	res, _ := http.Post(uploadURL, "application/x-www-form-urlencoded", nil)
	body, _ := ioutil.ReadAll(res.Body)
    fmt.Println(string(body))


}

