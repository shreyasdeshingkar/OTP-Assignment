import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    @staticmethod
    def generate_otp():
        return ''.join([str(random.randint(0, 9)) for i in range(6)])

class EmailSender:
    @staticmethod
    def send_otp(email, otp):
        if EmailValidator.validate_email(email):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('shreyasdeshingkar@gmail.com', 'muacwkbygeasmtow')
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.' \
                  f'\nThis is a system-generated mail, so do not reply.'
            server.sendmail("shreyasdeshingkar@gmail.com", email, msg)
            print("OTP is sent to email via email.")
        else:
            print("Invalid email address.")

class MobileSender:
    @staticmethod
    def send_otp(mobile, otp):
        if MobileValidator.validate_mobile(mobile):
            client = Client(keys.account_sid, keys.auth_token)
            msg = client.messages.create(
                body=f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.'
                     f'\nThis is a system-generated message, so do not reply.',
                from_=keys.twilio_number,
                to=mobile
            )
            print(msg.body)
        else:
            print("Invalid mobile number.")

class EmailValidator:
    @staticmethod
    def validate_email(email):
        return "@gmail" in email and "." in email

class MobileValidator:
    @staticmethod
    def validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

if _name_ == "_main_":
    otp = OTPGenerator.generate_otp()

    email = "manisha.deshingkar@gmail.com"
    EmailSender.send_otp(email, otp)

    mobile = "8625839939"
    MobileSender.send_otp(mobile, otp)
