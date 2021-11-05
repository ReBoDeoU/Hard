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

$idi['ids'][$data1] = ["mail"=>$mail,"id_mail"=>$id_mail];

file_put_contents("data/now.json", json_encode($idi));

}

$idi1 = json_decode(file_get_contents("data/now.json"),true);

if($data == "delete"){

$idi1['ids'][$data1] = ["mail"=>"لا يوجد بريد إلكتروني","id_mail"=>"error"];

file_put_contents("data/now.json", json_encode($idi1));

}

$viue = $idi['ids'][$data1]['mail'];
$sudo = 1397042354;
//تعديلاتي @Sufi900 
if($text == "/start" and $from_id !=$sudo and !in_array($id, $m)){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"
• *مرحبا بك في بوت الايميل الوهمي* 
• *يمكنك الان انشاء جميع مواقع التواصل*
• *سريع في  استلام جميع الرسائل*  
• *يمكنك انشاء حسابات فيسبوك+انستا وآلخ*
⠀",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'انشاء اميل 📨','callback_data'=>'new']],
[['text'=>'عرض الايميل 📧','callback_data'=>'viue'],['text'=>'حذف الايميل 🗃️','callback_data'=>'delete']],
[['text'=>'الرسائل 📩','callback_data'=>'msgs']],
[['text'=>'مطور البوت 👨🏾‍💻','url'=>'t.me/Sufi900'], ['text'=>'قناه البوت 📡','url'=>'t.me/alsh_3k']]
]
])
]);
}
if($data == "ba" and $from_id !=$sudo){
bot('editmessagetext',[
'chat_id'=>$data1,
'message_id'=>$data2,
'text'=>"
• *مرحبا بك في بوت الايميل الوهمي* 
• *يمكنك الان انشاء جميع مواقع التواصل*
• *سريع في  استلام جميع الرسائل*  
• *يمكنك انشاء حسابات فيسبوك+انستا وآلخ*
⠀",
'parse_mode'=>"MarkDown",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'تغير الايميل 📨️','callback_data'=>'new']],
[['text'=>'عرض الايميل 📧','callback_data'=>'viue'],['text'=>'حذف الايميل 🗃️','callback_data'=>'delete']],
[['text'=>'الرسائل 📩','callback_data'=>'msgs']],
[['text'=>'مطور البوت 👨🏾‍💻','url'=>'t.me/Sufi900'], ['text'=>'قناه البوت 📡','url'=>'t.me/alsh_3k']]
]
])
]);
}


if($data == "new" and !in_array($from_id, $now['ids'])){
file_put_contents("data/now.json", json_encode($idi));
bot('editmessagetext',[
'chat_id'=>$data1,
'message_id'=>$data2,
'text'=>" 

الاميل الخاص بك : 
" . $api['result']['mail'] . " 

✔️⠀",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'رجوع','callback_data'=>'ba']],
]
])
]);
}




if($data == "msgs" and !in_array($apimessage["error"], $apimessage)  and !in_array($apimessage["result"], $apimessage) ){
bot('editmessagetext',[
'chat_id'=>$data1,
'message_id'=>$data2,
'text'=>"🆔 iD : $id 
   - - - - - - - - - - - - - - -
   🔖 From : $from 
   - - - - - - - - - - - - - - -
   🖇 To : $mail 
   - - - - - - - - - - - - - - -
   📨 Subject : $subject
   - - - - - - - - - - - - - - -
   ✉️ Message : $body
   - - - - - - - - - - - - - - -
",
'reply_to_message_id'=>$message->message_id,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'رجوع','callback_data'=>'ba']],
]
])
]);
}else 

if($data == "msgs" and !in_array($apimessage["result"], $apimessage) ){
bot('answercallbackquery',[
        'callback_query_id'=>$update->callback_query->id,
        'text'=>"
‎ • » لا يوجد رسائل حاليا « •
        ",
        'show_alert'=>true,
]);
}else 

if($data == "msgs"){
bot('answercallbackquery',[
        'callback_query_id'=>$update->callback_query->id,
        'text'=>"
‎ • » لايوجد ايميل حاليا« •
        ",
        'show_alert'=>true,
]);
}



if($data == "viue"){
bot('editmessagetext',[
'chat_id'=>$data1,
'message_id'=>$data2,
'text'=>"الاميل الخاص بك : 
" . $viue,
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[['text'=>'رجوع','callback_data'=>'ba']],
]
])
]);
}

$mo = $apidelete['result'];

print_r($apidelete);

if($data == "delete"){
file_put_contents("data/now.json", json_encode($idi1));
bot('answercallbackquery',[
        'callback_query_id'=>$update->callback_query->id,
        'text'=>"
‎ • » $mo « •
        ",
        'show_alert'=>true,
]);
}
//اذكر المصدر ل صوفي// 
//©️ @PHP_APl 👨🏾‍💻 @Sufi900 //
