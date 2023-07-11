from datetime import datetime, timedelta
import csv


def generate_csv_files(chat_id):
    # EN Run the client from user_info.py
    # RU Запускаем клиент из user_info.py
    from user_info import app

    # EN Name of the csv file for statistics.py
    # RU Название csv файла для statistics.py
    stats_csv_file = "channel_stats.csv"
    # EN Name of the csv file for reactions.py
    # RU Название csv файла для reactions.py
    reactions_csv_file = "messages_with_reactions.csv"

    with app:
        # statistics.py
        chat = app.get_chat(chat_id)
        followers_count = chat.members_count

        total_reposts = 0
        messages = app.get_chat_history(chat_id, limit=50)
        for message in messages:
            reposts_count = message.forwards
            if reposts_count is not None:
                total_reposts += reposts_count

        total_publications_week = 0
        total_publications_day = 0

        end_date = datetime.now()
        start_date_week = end_date - timedelta(days=7)
        start_date_day = end_date - timedelta(days=1)

        messages = app.get_chat_history(chat_id, limit=100, offset_date=end_date)
        for message in messages:
            if start_date_week <= message.date <= end_date:
                total_publications_week += 1
            if start_date_day <= message.date <= end_date:
                total_publications_day += 1

        with open(stats_csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Метрика", "Значение"])
            writer.writerow(["Количество подписчиков", followers_count])
            writer.writerow(["Репостов за последние 50 постов", total_reposts])
            writer.writerow(["Постов за неделю", total_publications_week])
            writer.writerow(["Постов в день", total_publications_day])

        # reactions.py
        message_limit = 15
        messages = app.get_chat_history(chat_id, limit=message_limit)

        with open(reactions_csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Пост", "Просмотры", "Репосты", "Сообщение было отправлено вами", "Реакции"])

            for message in messages:
                text = message.text or ""
                caption = message.caption or ""
                views = message.views if hasattr(message, "views") else 0
                forwards = message.forwards if hasattr(message, "forwards") else 0
                outgoing = message.outgoing if hasattr(message, "outgoing") else False

                reactions = {}
                if hasattr(message, "reactions") and message.reactions is not None:
                    for reaction in message.reactions.reactions:
                        reactions[reaction.emoji] = reaction.count

                writer.writerow([text + caption, views, forwards, outgoing, reactions])

# EN An example of a channel with "You're an investor yourself!"
# RU Пример канала с "Сам ты инвестор!"
chat_id = "selfinvestor"
generate_csv_files(chat_id)