import requests
from bs4 import BeautifulSoup
import os

URL = "https://sofed.tripura.gov.in/recruitment"

BOT_TOKEN = "8666787831:AAGrZyh8QJu2vOmPY61XcyTNUffoLY_YWBo"
CHAT_ID = "1199265793"

FILE = "page.txt"


def send_alert(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )


def get_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text()


print("Checking website page please wait...")

current = get_page()

old = ""
if os.path.exists(FILE):
    old = open(FILE, "r", encoding="utf-8").read()

if current != old:
    send_alert(" New update detected on website!\nBot developed by infoanupampal@gmail.com\nCheck here  :\nhttps://sofed.tripura.gov.in/recruitment")
    print("Update detected")

open(FILE, "w", encoding="utf-8").write(current)
