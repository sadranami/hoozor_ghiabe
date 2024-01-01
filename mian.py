import json
import requests

def sender(chat_id, message, keyboard=None):
    api_token = "YOUR_API_TOKEN"  # Replace with your actual API token
    url = f"https://api.telegram.org/bot{api_token}/sendmessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    if keyboard:
        data["reply_markup"] = json.dumps({"inline_keyboard": keyboard})
    response = requests.get(url, params=data)

def menu(id, namex):
    text = "⁣\u2733\ufe0f" + json.loads('"' + namex + '"') + " عزیز برای ثبت حضور در کلاس خود بر روی دکمه زیر کلیک کنید"
    keyboard = [
        [
            {
                "text": "ثبت حضور در کلاس",
                "callback_data": md5(id)
            }
        ]
    ]
    sender(id, text, keyboard)

def exist(x, y):
    return x.count(y)

data = input()

with open('exam.json', 'w') as file:
    file.write(data)

datacod = json.loads(data)

if "callback_query" in data:
    id = datacod["callback_query"]["from"]["id"]
    if exist(data, md5(id)):
        namex = data.split('#' + md5(id))[1].split('-')[1]
        uifjj = requests.get(f"https://api.telegram.org/bot{api_token}/sendmessage?chat_id=@HOZOORGHIAB2&text={json.loads('"' + hex2bin(namex) + '"')}")

else:
    id = datacod["message"]["from"]["id"]
    message = datacod["message"]["text"]
    text = "❇️لطفاً کد دانشجویی و نام و نام خانوادگی خود را وارد کنید"
    if not exist(db, '#' + md5(id) + '-'):
        uifjj = requests.get(f"https://api.telegram.org/bot{api_token}/sendmessage?chat_id={id}&text={text}")
        with open('hozor.txt', 'a') as file:
            file.write('#' + md5(id) + '-0x80-')
    else:
        namex = data.split('#' + md5(id))[1].split('-')[1]
        if namex == '0x80':
            message = binascii.hexlify(message.encode()).decode()
            lastest = db.replace('#' + md5(id) + "-0x80-", '#' + md5(id) + "-" + message + "-")
            with open('hozor.txt', 'w') as file:
                file.write(lastest)
            menu(id, namex)
        else:
            menu(id, namex)
