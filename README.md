# How to Send an Email from Python using smtplib
Wouldn’t it be cool sending emails from python? Let’s do it then ;)


## **Requirements:**
- Gmail Account
- Two-step verification turned on. -> Go on your google account (Manage Account) -> Security (On the left side of the navigation bar) -> Signing into Google -> Set        up 2-Step verification
- App generated Password

## **Importing Packages:**
import smtplib

## **Send Mail Function:**
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('#YOUR EMAIL ADDRESS', '#YOUR APP GENERATED PASSWORD')
    subject = 'Sales discussion'
    body = 'Hello Team,  quick reminder for tomorrows sales discussion.'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
    '#SENDERS EMAIL',
    '#RECEIVERS EMAIL',
    msg)
    print('Mail sent')
    server.quit()
    
 
