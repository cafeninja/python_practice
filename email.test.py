# email.test.py

import smtplib, ssl
test_block = "Stuff in the middle."
m = open("message.txt", "r")
body = m.read()

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "emmettstewart1@gmail.com"
receiver_email = "emmett@ce3ps.com"
password = "prnzxturkdvipwby"
message = "Subject: Hi there\n\n" + str(body) + "\n\nThis message is sent from Python."

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)