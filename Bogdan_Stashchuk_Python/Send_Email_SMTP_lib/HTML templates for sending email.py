from email.message import EmailMessage  # create message
import smtplib  # send message
from string import Template
from pathlib import Path

my_email = EmailMessage()
html_template = Template(
    Path('Send_Email_SMTP_lib/templates/index.html').read_text())
html_content = html_template.substitute(
    {'name': "Oleksandr", 'date': "tomorrow"})

my_email['from'] = "Oleksandr"
my_email['to'] = "friend@gmail.com"
my_email['subject'] = "Let's go out"
my_email.set_content(html_content, 'html')
with smtplib.SMTP(host='localhost', port=2525) as smpt_server:
    smpt_server.ehlo()
    # smpt_server.starttls()
    # smpt_server.login('username','password')
    smpt_server.send_message(my_email)
print("Email was sent!")
