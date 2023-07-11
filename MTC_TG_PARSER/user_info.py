from pyrogram import Client

#Вписываем апишку и токен с сайта телеги
api_id = 22790914
api_hash = "519fcd632126f464ded7865019925235"


#инициализируем клиент
app = Client("my_account", api_id=api_id, api_hash=api_hash)

#получаем чат айди (название канала в телеге без собаки) например chat_id = "selfinvestor" -  канал "Сам ты инвестор!"
chat_id = "selfinvestor"