<?php
ob_start();

//اذكر المصدر ل APl/ 
//©️ @PHP_APl 👨🏾‍💻 @Sufi900
$API_KEY = "1675297705:AAGQx9rFVvXRWg1xao3TGQa7F7Y_QNNGEcg";
define('API_KEY',$API_KEY);
function bot($method,$datas=[]){
  $url = "https://api.telegram.org/bot".API_KEY."/".$method;
  $datas = http_build_query($datas);
  $res = file_get_contents($url.'?'.$datas);
  return json_decode($res);

}

echo file_get_contents("https://api.telegram.org/bot$API_KEY/setwebhook?url=".$_SERVER['SERVER_NAME']."".$_SERVER['SCRIPT_NAME']);

$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$id = $message->from->id;
$chat_id = $message->chat->id;
$text = $message->text;
$id = $message->from->id;
$api = json_decode(file_get_contents("https://sufi-mustafa1.000webhostapp.com/api-mail.php?a=newmail"), true);
$mail = $api['result']['mail'];
$id_mail = $api['result']['id'];
mkdir("data");
$data1 = $update->callback_query->message->chat->id;
$data2 = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
$now = json_decode(file_get_contents("data/now.json"), true);
$no = $now['ids'][$data1]['id_mail'];
$chat_id2 = $update->callback_query->message->chat->id;
$message_id2 = $update->callback_query->message->message_id;
$data = $update->callback_query->data;
$id = $message->from->id;
$text = $message->text;
$chat_id = $message->chat->id;
$user = $message->from->username;
$name = $message->from->first_name;
####الاوامر####
$admin = 1397042354;
if($chat_id !== $admin){
bot('forwardMessage',[
'chat_id'=>$admin,
'from_chat_id'=>$chat_id,
'message_id'=>$update->message->message_id,
]);
}
$apidelete = json_decode(file_get_contents("https://sufi-mustafa1.000webhostapp.com/api-mail.php?a=delete&id=" . $no), true);

$apimessage = json_decode(file_get_contents("https://sufi-mustafa1.000webhostapp.com/api-mail.php?a=mails&id=" . $no), true);
foreach($apimessage as $key => $val){
    $result  = $val;
    $id = $val["_id"]['$oid'];
    $from = $val["mail_from"];
    $to = $val["to"];
    $subject = $val["mail_subject"];
    $body = $val["mail_text"];
}

$idi = json_decode(file_get_contents("data/now.json"),true);

if($data == "new"){
