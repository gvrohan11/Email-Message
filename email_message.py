import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to_address):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to_address

    user = "[Sender Email]"
    msg['from'] = user
    password = "[Generate in Google Settings]"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() 
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("[Subject Line]",
        "[Body Message]", "[Receiving Address]")
