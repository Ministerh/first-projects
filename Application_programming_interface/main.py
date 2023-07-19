import requests
from datetime import datetime
import time
import smtplib

my_email = "pythonminister@gmail.com"
email_password = "lzllilhtxhxnktoe"
MY_LAT =  6.723720
MY_LONG =  3.163710
def  iss_position_overhead():
    #this will fetch from the api
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # #response code tells a lot 
    # # 1xx code says hold on, 2xx says here you go thst means it"s available,
    # #  3xx says you don.t have access, 4xx says it"s not available or it doesn't exsit, 5xx says te server nto availble
    # # to raise an exception,  you can use the in build function of the requests module
    response.raise_for_status()

    iss_data = response.json()
    iss_longitude =float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    print((iss_longitude, iss_latitude))

    # check the position of iss to my position
    if MY_LAT-5 <= iss_latitude <= MY_LAT +5 and MY_LONG-5 <= iss_longitude <= MY_LONG +5:
        return True
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response =requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    iss_data = response.json()
    # to isolate the hour from the result
    sunrise =int(iss_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset =int(iss_data['results']['sunset'].split("T")[1].split(":")[0])

    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True
    
# to make the code send email
while True:
    time.sleep(120)
    if iss_position_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")

    connection.starttls()
    connection.login(user=my_email, password=email_password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=my_email,
                        msg="subject:Hey! look up\n\nThe iss is above you")
    

    
