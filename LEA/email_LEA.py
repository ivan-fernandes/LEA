import smtplib


def send_email():
    gmail_user = 'your_email@gmail.com'
    gmail_password = 'your_gmail_app_password' # set your app password in your Google Account as a 2FA

    sent_from = 'LEA@LEA.de'
    to = ['your_email@your_provider.com']
    subject = 'APPOINTMENT AVAILABLE'
    body = "Hey,\n\n An appointment might be available! \n Go grab it!!\n\n Best regards, \n\n Ivan"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Email not sent. Something went wrong...')
