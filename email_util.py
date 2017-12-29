import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_user = "zhouminping1991@gmail.com"
password = "gmaildemimaZMP31"

# files = ["price_reduction_distribution.csv", "price_reduction_distribution.sql"]

def send(to_user, sub, msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo() 
	server.starttls() 
	server.login(from_user, password)
	message = MIMEText(msg)
	message['Subject'] = sub
	message['From'] = from_user
	message['To'] = to_user
	server.send_message(message)
	server.quit()

# with open('util.py') as fp:
#     # Create a text/plain message
#     msg = MIMEText(fp.read())

def send_files(to_user, sub, msg, files):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo() 
	server.starttls() 
	server.login(from_user, password)
	message = MIMEMultipart()
	message['Subject'] = sub
	message['From'] = from_user
	message['To'] = to_user
	body = MIMEText(msg)
	message.attach(body)
	for file in files:
		with open(file) as fp:
			attachment = MIMEText(fp.read())
			attachment.add_header('Content-Disposition', 'attachment', filename=file)
		message.attach(attachment)
	server.send_message(message)
	server.quit()