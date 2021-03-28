const axios = require("axios");

// Model Endpoint
var model_endpoint = "xx-your-model--1";
// Enter your API Key Here
var api_key = "";

axios({
  method: "POST",
  url: "https://infer.roboflow.com/" + model_endpoint,
  params: {
    access_token: api_key,
    image: "https://i.imgur.com/PEEvqPN.png",
  },
})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error.message);
  });
