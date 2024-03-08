#fdgc ebmv xelp cunt 
import smtplib, ssl
from email.message import EmailMessage
smtp_server="smpt.gmail.com"
port= 587
sender_email="jelizaveta.ostapjuk.work@gmail.com"
password=input("Type your password and press enter: ")
context=ssl.create_default_context()
msg=EmailMessage()
msg.set_content("Tere tulemast!")
msg['Subject']="Kirje teema"
msg['From']="jelizaveta.ostapjuk.work@gmail.com"
msg['To']=""
try:
    server=smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email,password)
    server.send_message(msg)
except Exception as e:
    print(e)
finally:
    server.quit()