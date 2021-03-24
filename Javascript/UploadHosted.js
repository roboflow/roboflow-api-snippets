const axios = require("axios");
const dataset_name = "your-dataset"; // Set Dataset Name (Found in Dataset URL)

axios({
  method: "POST",
  url: "https://api.roboflow.com/dataset/" + dataset_name + " /upload",
  params: {
    api_key: "YOUR_KEY", // Enter your API Key Here
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
