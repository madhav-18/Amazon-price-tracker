from bs4 import BeautifulSoup
import requests
import lxml

bot_token = "Your telegram bot token"
BOT_ENDPOINT = f"https://api.telegram.org/bot{bot_token}/sendMessage"
bot_chatID = "Telegram bot chat id"
URL = "link of amazon product you want to track"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


def send_msg():
    parameters_bot = {
        "chat_id": bot_chatID,
        "text": f"The Current price of the product is {price_as_float}",
    }
    send_text = requests.post(BOT_ENDPOINT, params=parameters_bot)
    send_text.raise_for_status()


response = requests.get(url=URL)

soup = BeautifulSoup(response.text, parser=lxml)
# print(soup)

price = soup.find(name="span", class_="a-offscreen").getText()
price_without_paise = price.split(".")[0]
price_without_currency = price_without_paise.split("₹")[1]
price_as_float = float(price_without_currency.replace(",", "."))
print(price_as_float)
#i have replace "," with "." because float do not use "," in it  
if price_as_float < 3.780:  #so 3.780 is 3 thousand and 780 rupees
    send_msg()