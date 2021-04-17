import smtplib
from email.message import EmailMessage


def email_alert(whofrom, password, name='Sum Yung Nguy', subject, body, to):
    user = whofrom
    msg['from'] = name
    password = password

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to


    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    exit(-2)