<?php

// Base 64 Encode Image
$data = base64_encode(file_get_contents("YOUR_IMAGE.jpg"));

$api_key = ""; // Set API Key
$dataset_name = "your-dataset"; // Set Dataset Name (Found in Dataset URL)

// URL for Http Request
$url = "https://api.roboflow.com/dataset/" 
. $dataset_name .  "/upload" 
.  "?api_key="  .  $api_key  
.  "&name=YOUR_IMAGE.jpg" 
. "&split=train";

// Setup + Send Http request
$options = array(
  'http' => array (
    'header' => "Content-type: application/x-www-form-urlencoded\r\n",
    'method'  => 'POST',
    'content' => $data
  ));

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
echo $result;
?>