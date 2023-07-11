from user_info import app
from user_info import chat_id

from datetime import datetime, timedelta

import csv

# EN Name of csv file
# RU Название csv файла
csv_file = "channel_stats.csv"

with app:
    chat = app.get_chat(chat_id)
    followers_count = chat.members_count

    # EN count the number of reposts over the last 50 posts
    # RU считаем количество репостов за последние 50 постов
    total_reposts = 0
    messages = app.get_chat_history(chat_id, limit=50)
    for message in messages:
        reposts_count = message.forwards
        if reposts_count is not None:
            total_reposts += reposts_count

    # EN count the number of posts per week and per day
    # RU считаем количество постов за неделю и за день
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

    # EN Save to csv
    # RU Сохраняем в csv
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Метрика", "Значение"])
        writer.writerow(["Количество подписчиков", followers_count])
        writer.writerow(["Репостов за последние 50 постов", total_reposts])
        writer.writerow(["Постов за недлею", total_publications_week])
        writer.writerow(["Постов в день", total_publications_day])
