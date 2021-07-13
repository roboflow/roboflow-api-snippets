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
	model_endpoint := "dataset/v" // Set model endpoint

    // Open file on disk.
    f, _ := os.Open("YOUR_IMAGE.jpg")

    // Read entire JPG into byte slice.
    reader := bufio.NewReader(f)
    content, _ := ioutil.ReadAll(reader)

    // Encode as base64.
    data := base64.StdEncoding.EncodeToString(content)
	uploadURL := "https://detect.roboflow.com/" + model_endpoint + "?api_key=" + api_key + "&name=YOUR_IMAGE.jpg"

	req, _ := http.NewRequest("POST", uploadURL, strings.NewReader(data))
    req.Header.Set("Accept", "application/json")

    client := &http.Client{}
    resp, _ := client.Do(req)
    defer resp.Body.Close()

   	bytes, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(bytes))

}

