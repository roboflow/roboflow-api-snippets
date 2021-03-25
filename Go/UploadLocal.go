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
	dataset_name := "Your-Dataset" // Set Dataset Name (Found in Dataset URL)

    // Open file on disk.
    f, _ := os.Open("YOUR_IMAGE.jpg")

    // Read entire JPG into byte slice.
    reader := bufio.NewReader(f)
    content, _ := ioutil.ReadAll(reader)

    // Encode as base64.
    data := base64.StdEncoding.EncodeToString(content)
	uploadURL := "https://api.roboflow.com/dataset/"+ dataset_name + "/upload"+
    "?api_key=" + api_key +
    "&name=YOUR_IMAGE.jpg" +
    "&split=train"

	res, _ := http.Post(uploadURL, "application/x-www-form-urlencoded", strings.NewReader(data))
	fmt.Println(res)

}

