<?php
$url = "http://localhost:8086/upload";
header('Location: '.$url);
die();

$input = json_encode($_FILES);//file_get_contents('php://input');

if(isset($input)){
    send_requests($input, $url);
}

#echo "OK";

/**
 * Send post request
 */
function send_requests($json_payload, $url){
        $ch = curl_init("$url");
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
        curl_setopt($ch, CURLOPT_POSTFIELDS, $json_payload);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-Type: application/json',
                'Content-Length: ' . strlen($json_payload))
        );                                                                                                                                                                                                          
        return curl_exec($ch);
}
