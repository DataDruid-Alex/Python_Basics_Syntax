from email.message import EmailMessage  # create message
import smtplib  # send message
from string import Template
from pathlib import Path

my_email = EmailMessage()
html_template = Template(
    Path('Send_Email_SMTP_lib/templates/index.html').read_text())
html_content = html_template.substitute(
    {'name': "Oleksandr", 'date': "tomorrow"})

my_email['from'] = "Oleksandr <myemail@gmail.com>"
my_email['to'] = "friend@gmail.com"
my_email['subject'] = "Email with image"
my_email.set_content(html_content, 'html')
with open('Send_Email_SMTP_lib/images/really-good-emails.png', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image',
                            subtype='png', filename="really-good-emails")

with smtplib.SMTP(host='localhost', port=2525) as smpt_server:
    smpt_server.ehlo()
    # smpt_server.starttls()
    # smpt_server.login('username','password')
    smpt_server.send_message(my_email)
print("Email was sent!")
