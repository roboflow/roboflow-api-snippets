const axios = require("axios");
var dataset_name = "your-dataset"; // Set Dataset Name (Found in Dataset URL)
var api_key = ""; // Enter your API key here

axios({
  method: "POST",
  url: "https://api.roboflow.com/dataset/" + dataset_name + " /upload",
  params: {
    api_key: api_key,
    image: "https://i.imgur.com/PEEvqPN.png",
    name: "201-956-1246.png",
    split: "train",
  },
})
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error.message);
  });
