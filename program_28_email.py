import smtplib as mail

mailserver = mail.SMTP("smtp.gmail.com",587)

mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

mailserver.login('gdnetamazon@gmail.com', '2432gjmjaw')

msg = '''FROM: Sender Name <gdnetamazon@gmail.com>
       To: <gdappwanck@gmail.com>
       Subject: A Test email Message from pyhton course
       Content-type: text/html
       MIME-Version:1.0

       This wil be the body of your email message'''

mailserver.sendmail("gdnetamazon@gmail.com","gdappwanck@gmail.com",msg)
