import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'BAAF Company'
email['to'] = 'abdoulfaridbassirou7898@gmail.com'
email['subject'] = 'Promotion'

email.set_content(html.substitute({'name':'Farid'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls() # tls is an encryption mecanism, and allows us to connect securely to the server.
	smtp.login('<your email address>', '<your password>')
	smtp.send_message(email)
