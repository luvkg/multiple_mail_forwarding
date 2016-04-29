import smtplib, imaplib, email
import socket

imap_host = "imap.gmail.com"
smtp_host = "smtp.gmail.com"
smtp_port = 465
user = "<fromemail>"
passwd = "<passwd>"
msgid = 1
from_addr = "<from_email>"
to_addr = "to_email"


# open IMAP connection and fetch message with id msgid
# store message data in email_data
client = imaplib.IMAP4_SSL(imap_host)
client.login(user, passwd)
client.select('INBOX')
status, data = client.fetch(msgid, "(RFC822)")
email_data = data[0][1]
client.close()
client.logout()
print "complete_1"

# create a Message instance from the email data
message = email.message_from_string(email_data)
# print message

# replace headers (could do other processing here)
# message.replace_header("From", from_addr)
# message.replace_header("To", to_addr)
print message['From']

# open authenticated SMTP connection and send message with
# specified envelope from and to addresses
smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
# smtp.ehlo()
# smtp.starttls()
smtp.login(user, passwd)
print "login"
smtp.sendmail(from_addr, to_addr, message.as_string())
# smtp.quit()
print "complete"
