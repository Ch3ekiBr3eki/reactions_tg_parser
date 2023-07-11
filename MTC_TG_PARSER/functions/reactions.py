from user_info import app
from user_info import chat_id

import csv

#Название csv файла
csv_file = "messages_with_reactions.csv"
#Сколько первых сообщений из канала берём
message_limit = 20

with app:
    messages = app.get_chat_history(chat_id, limit=message_limit)

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Пост", "Просмотры", "Репосты", "Сообщение было отправлено вами", "Реакции"])

        for message in messages:
            text = message.text or ""
            caption = message.caption or ""
            views = message.views if hasattr(message, "views") else 0
            forwards = message.forwards if hasattr(message, "forwards") else 0
            outgoing = message.outgoing if hasattr(message, "outgoing") else False

            reactions = ""
            if hasattr(message, "reactions") and message.reactions is not None:
                reactions = ", ".join([f"{r.emoji}: {r.count}" for r in message.reactions.reactions])

            writer.writerow([text + caption, views, forwards, outgoing, reactions])