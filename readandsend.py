import json
import smtplib, ssl

with open("newemails.json", "r") as f:
    newdict = json.load(f)

port = 587
smtp_server = "smtp.mail.ru"
sender_email = "python.2020@mail.ru"
password = "gbnjy!!!"

errors = []

for email in newdict:
    try:
    	reciever_email = email['reciever_email']
    	message = "Subject: " + email["subject"] + "\n\nMessage: " + email["text"]
    	context = ssl.create_default_context()
    	with smtplib.SMTP(smtp_server, port) as server:
        	server.starttls(context=context)
        	server.login(sender_email, password)
        	server.sendmail(sender_email, reciever_email, message)
    except Exception as e:
        errors.append({"error": {"type": e.__class__.__name__, "message": str(e)}})
    else:
        errors.append({"data": True})

with open ('results.json', 'w') as f:
    json.dump(errors, f)
