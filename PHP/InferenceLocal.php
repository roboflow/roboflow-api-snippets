<?php

// Base 64 Encode Image
$data = base64_encode(file_get_contents("YOUR_IMAGE.jpg"));

$api_key = ""; // Set API Key
$model_endpoint = "xx-your-model--1"; // Set model endpoint (Found in Dataset URL)

// URL for Http Request
$url = "https://infer.roboflow.com/" . $model_endpoint
. "?access_token=" . $api_key
. "&name=YOUR_IMAGE.jpg";

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