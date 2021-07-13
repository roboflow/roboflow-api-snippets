const axios = require("axios");

// Model Endpoint
var model_endpoint = "dataset/v";
// Enter your API Key Here
var api_key = "";

axios({
  method: "POST",
  url: "https://detect.roboflow.com/" + model_endpoint,
  params: {
    api_key: api_key,
    image: "https://i.imgur.com/PEEvqPN.png",
  },
})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error.message);
  });
