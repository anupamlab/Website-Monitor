from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://www.bbc.com/news"

BOT_TOKEN = "8666787831:AAGrZyh8QJu2vOmPY61XcyTNUffoLY_YWBo"
CHAT_ID = "1199265793"

FILE = "page.txt"


def send_alert(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, data=data)


def get_page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(URL)

        content = page.content()

        browser.close()

        return content


print("Checking website...")

current = get_page()

old = ""

if os.path.exists(FILE):

    with open(FILE, "r", encoding="utf-8") as f:
        old = f.read()


if current != old:

    send_alert("🚨 Website updated!\nBot developed by infoanupampal@gmail.com\nCheck here:\n" + URL)

    print("Update detected!")

else:

    print("No change detected.")


with open(FILE, "w", encoding="utf-8") as f:
    f.write(current)
