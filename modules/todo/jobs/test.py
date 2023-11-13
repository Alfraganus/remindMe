import datetime
import requests
from apscheduler.schedulers.background import BackgroundScheduler



def test():
    telegram_api_url = "https://api.telegram.org/bot6734724387:AAF_hb0RnTlkuQKxjUgQadQc5wXPBf-VEkk/sendMessage"
    chat_id = "1244682"
    text = "hello world"

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(telegram_api_url, params=payload)

    # Check the response status if needed
    if response.status_code == 200:
        print(f"Message sent successfully at {datetime.datetime.now()}")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


schedular = BackgroundScheduler()
schedular.add_job(test,'interval',seconds=5)