import imaplib
import email
import smtplib
import pprint

#-----------------------mail retreive----------------------

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('lovekush@innovaccer.com', '<password>')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("INBOX") # connect to inbox.

print "success"
result, data = mail.uid('search', None, "ALL") # search and return uids instead
latest_email_uid = data[0].split()[-1]
email_uid = data[0].split()
# for i in email_uid:
# 	print i#email_uid
print data[0]
print latest_email_uid
for uid in email_uid:
	print uid
	result, data = mail.uid('fetch', uid, '(RFC822)')
	raw_email = data[0][1]

	email_message = email.message_from_string(raw_email)
	# print email_message
	print email_message['To']
	print email.utils.parseaddr(email_message['From'])
# print email_message.items() # print all headers
# pprint.pprint(email_message.items())


#--------------------send mail--------------------------------

sm = smtplib.SMTP_SSL()
sm.connect('smtp.gmail.com',465)

s = sm.login("lovekush@innovaccer.com", "<password>")
print "login Succesfully"
# print s
text = email_message.as_string()
# print text
fromadd = "lovekush@innovaccer.com"
toadd= ["gangwarlovekush@gmail.com"]
sa = sm.sendmail(fromadd,toadd,text)
# print sa
print "sent"




