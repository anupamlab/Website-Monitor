import requests
from bs4 import BeautifulSoup
import time

# Website to monitor
URL = "https://sofed.tripura.gov.in/recruitment"

# Telegram credentials
BOT_TOKEN = "8666787831:AAGrZyh8QJu2vOmPY61XcyTNUffoLY_YWBo"
CHAT_ID = "1199265793"


def send_telegram_alert(alert_text):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": alert_text
    }

    requests.post(telegram_url, data=payload)


def fetch_page_text():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()


print("SOFED recruitment monitor started...")

# Get initial page content
previous_content = fetch_page_text()

# Send startup message
send_telegram_alert("SOFED Job Monitor Started")

while True:
    time.sleep(3600) # 1 hour

    print("Checking for updates...")

    current_content = fetch_page_text()

    if current_content != previous_content:
        alert_message = "New update detected\nBot developed by infoanupampal@gmail.com\nCheck here:\nhttps://sofed.tripura.gov.in/recruitment"

        send_telegram_alert(alert_message)

        print("Update found. Telegram alert sent.")

        previous_content = current_content

    else:
        print("No new updates.")