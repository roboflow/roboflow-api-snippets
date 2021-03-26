<?php

$api_key = ""; // Set API Key
$dataset_name = "your-dataset"; // Set Dataset Name (Found in Dataset URL)
$img_url = "https://i.imgur.com/PEEvqPN.png";

// URL for Http Request
$url = "https://api.roboflow.com/dataset/" 
. $dataset_name .  "/upload" 
.  "?api_key="  .  $api_key  
.  "&name=YOUR_IMAGE.jpg" 
. "&split=train" 
. "&image=" . urlencode($img_url);

// Setup + Send Http request
$options = array(
  'http' => array (
    'header' => "Content-type: application/x-www-form-urlencoded\r\n",
    'method'  => 'POST'
  ));

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
echo $result;
?>