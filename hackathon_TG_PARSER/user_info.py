from pyrogram import Client

# EN Enter the api and token from the cart's website
# RU Вписываем апишку и токен с сайта телеги
api_id = 123
api_hash = "123"

# EN Initialize the client  
# RU Инициализируем клиент
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# EN Get chat_id (channel name in the cart without the dog) e.g. chat_id = "selfinvestor" - channel "You are an investor yourself!".
# RU Получаем чат айди (название канала в телеге без собаки) например chat_id = "selfinvestor" -  канал "Сам ты инвестор!"
chat_id = "selfinvestor" 