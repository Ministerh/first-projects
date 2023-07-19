import smtplib

my_email = "pythonminister@gmail.com"
email_password = "lcxbdeqooiewjqkl"
receiver = "mountain_ash@yahoo.com"
# Create a message





# Create a connection and include your e-mail server into it for smtp
# fro gmail is smtp.gmail.com
#for hotmail is smtp.live.com
#for yahoomail is smtp.mail.yahoo.com
connection = smtplib.SMTP("smtp.gmail.com", 587)
#to help create security
connection.starttls()
connection.login(user=my_email, password=email_password)
connection.sendmail(from_addr=my_email, 
                    to_addrs="mountain_ash@yahoo.com",
                      msg="subject:SMTP\n\nThis is python smtp program to automate sebding of mails")
connection.close()
