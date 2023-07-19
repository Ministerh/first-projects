import requests
from bs4 import BeautifulSoup
from lxml import html

URL = "https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09MSRJ97Y/ref=sr_1_7?keywords=mac+book&qid=1689352816&refinements=p_89%3AApple&rnid=2528832011&s=electronics&sr=1-7"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")
price = soup.select_one("span .a-price-whole").getText().split(",")
price_as_float  = float("".join(price))


import smtplib

my_email = "pythonminister@gmail.com"
email_password = "lcxbdeqooiewjqkl"
receiver = "ministerhussein@gmail.com"
if price_as_float < 1850:

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=email_password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=receiver,
                        msg=f"subject:Mac book Price\n\nYour favourite mac book price has reduced to {price_as_float}\n order through here {URL}")
    connection.close()


