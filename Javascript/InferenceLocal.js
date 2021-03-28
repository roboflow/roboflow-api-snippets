const axios = require("axios");
const fs = require("fs");

// Model Endpoint
var model_endpoint = "xx-your-model--1";
// Enter your API Key Here
var api_key = "";

const image = fs.readFileSync("YOUR_IMAGE.jpg", {
  encoding: "base64",
});

axios({
  method: "POST",
  url: "https://infer.roboflow.com/" + model_endpoint,
  params: {
    access_token: api_key,
  },
  data: image,
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
  },
})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error.message);
  });
