<?php

$API_KEY = "8266684590:AAFRZDWigKR7ztkhOG9ZR86gt7655cBSlKk"; // Mana bu tokeningiz

function bot($method, $datas = []){
    global $API_KEY;
    $url = "https://api.telegram.org/bot$API_KEY/$method";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $datas);
    $res = curl_exec($ch);
    curl_close($ch);
    return json_decode($res);
}

// Foydalanuvchi yuborgan malumotni olish
$update = json_decode(file_get_contents('php://input'), true);
$chat_id = $update["message"]["chat"]["id"];
$text = $update["message"]["text"];

// Javob qaytarish
if ($text == "/start") {
    bot("sendMessage", [
        "chat_id" => $chat_id,
        "text" => "Salom! Bu PHP bot ishga tushdi ✅"
    ]);
}
