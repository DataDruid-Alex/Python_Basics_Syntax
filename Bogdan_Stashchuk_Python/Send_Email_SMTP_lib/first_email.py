from email.message import EmailMessage  # create message
# ALT+ESCAPE                  225video?????
import smtplib  # send message
my_email = EmailMessage()
my_email['from'] = "Oleksandr"
my_email['to'] = "test@gmail.com"
my_email['subject'] = "Hello from Python"
my_email.set_content("Hey!How are you doing?")
with smtplib.SMTP(host='localhost', port=2525) as smpt_server:
    smpt_server.ehlo()
    # smpt_server.starttls()
    # smpt_server.login('username','password')
    smpt_server.send_message(my_email)
print("Email was sent!")
