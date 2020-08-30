import smtplib
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YOUR EMAIL ADDRESS', 'YOUR APP GENERATED PASSWORD')

    subject = 'Sales discussion'
    body = 'Hello Team,  quick reminder for tomorrows sales discussion.'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SENDERS EMAIL',
        'RECEIVERS EMAIL',
        msg
    )
    print('Mail sent')
    server.quit()

send_mail()
