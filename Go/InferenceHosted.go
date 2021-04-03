package main

import (
    "fmt"
	"net/http"
	"net/url"
  "io/ioutil"
)

func main() {
	api_key := ""  // Your API Key
	model_endpoint := "xx-your-model--1" // Set model endpoint
	img_url := "https://i.ibb.co/jzr27x0/YOUR-IMAGE.jpg"


	uploadURL := "https://infer.roboflow.com/" + model_endpoint + "?access_token=" + api_key + "&image=" + url.QueryEscape(img_url)

	req, _ := http.NewRequest("POST", uploadURL, nil)
    req.Header.Set("Accept", "application/json")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

   	bytes, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(bytes))


}

