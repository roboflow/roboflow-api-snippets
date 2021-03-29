package main

import (
    "bufio"
    "encoding/base64"
    "fmt"
    "io/ioutil"
    "os"
	"net/http"
	"strings"
)

func main() {
	api_key := ""  // Your API Key
	model_endpoint := "xx-your-model--1" // Set model endpoint

    // Open file on disk.
    f, _ := os.Open("YOUR_IMAGE.jpg")

    // Read entire JPG into byte slice.
    reader := bufio.NewReader(f)
    content, _ := ioutil.ReadAll(reader)

    // Encode as base64.
    data := base64.StdEncoding.EncodeToString(content)
	uploadURL := "https://infer.roboflow.com/" + model_endpoint
	+ "?access_token=" + api_key
	+ "&name=YOUR_IMAGE.jpg"

	res, _ := http.Post(uploadURL, "application/x-www-form-urlencoded", strings.NewReader(data))
	fmt.Println(res)

}

