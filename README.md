# How to Send an Email from Python using smtplib
Wouldn’t it be cool sending emails from python to your inbox? Let’s do it then ;)


## **Requirements:**
- Gmail Account
- Two-step verification turned on. -> Go on your google account (Manage Account) -> Security (On the left side of the navigation bar) -> Signing into Google -> Set        up 2-Step verification
- App generated Password

## **Importing Packages:**

``` python
import smtplib
```
## **Send Mail Function:**

### **Getting your App Generated Password:**
-  Now before starting to type this send_mail function let’s create our generated password. Once you have turned on your 2-step verification, you can head back to the security navigation page. Under signing-in to Google, you see a tab called App passwords. Now click on this tab. Under “Select App” select the option “Mail” and under “Select device” select the device you are doing this project on. In my case, I would choose the option “Mac”. Then click generate.

```python
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
```
 
## **Call function**

```python
send_mail()
```

## **END**
Hopefully this tutorial helped you in solving this tricky, but important problem.
Thanks and stay safe!
