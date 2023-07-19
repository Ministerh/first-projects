import requests
import math
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
vantage_api_key = "E81BWOHESD29ODIQ"
newsapi_key = " 7f7da9ecedf94c3b851c6a61e60c5a8e"
stock_endpoint=  'https://www.alphavantage.co/query'
URL = "https://newsapi.org/v2/everything?q=Tesla Inc&apiKey=7f7da9ecedf94c3b851c6a61e60c5a8e"

stock_parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey":vantage_api_key
    }

def percentage_calc(day_before, yesterday):
    difference= day_before - yesterday
    difference *= -1
    increase = (difference/day_before) * 100
    if increase > 5:
        print("Get News")
        
    


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(stock_endpoint, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
new_data = [value for (key,value)in data.items()]
yesterday_stock_price = float(new_data[0]["4. close"])
dayb4_yesterday_stock_price = float(new_data[1]["4. close"])
#percentage_calc(dayb4_yesterday_stock_price, yesterday_stock_price)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response = requests.get(URL)
news = response.json()["articles"]
difference= round(yesterday_stock_price - dayb4_yesterday_stock_price)
position = None
if  difference > 0:
    position =f"TSLA: 🔺{difference}"
else:
    position = f"TSLA: 🔺{difference}"

increase = abs((difference/yesterday_stock_price) * 100)
if increase > 5 :
    headlines = news[:3]
    print(headlines)

formatted_article = [f"{position}\nHeadlines: {news['title']}. \n Brief: {news['description']}" for news in headlines ]
print(formatted_article)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
from twilio.rest import Client

# Account sid  annd auth tokeen from twilio.com/console
#do not use the auth token openly
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "auth token"

client = Client(account_sid, auth_token)  
for article in formatted_article:
    message = client.message.create(
        body= "my formatted articles",
        from_= "my  twilio user number",
        to = "my  twilio veried number(personal numbber)"
    )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

