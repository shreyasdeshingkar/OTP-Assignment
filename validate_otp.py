import random
import smtplib
from twilio.rest import Client
import keys

class OTPManager:
    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def send_otp_over_email(self, email, otp):
        email_sender = EmailSender()
        email_sender.send_otp(email, otp)

    def send_otp_over_mobile(self, mobile, otp):
        mobile_sender = MobileSender()
        mobile_sender.send_otp(mobile, otp)

class EmailSender:
    def send_otp(self, email, otp):
        if EmailValidator().validate_email(email):
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
    def send_otp(self, mobile, otp):
        if MobileValidator().validate_mobile(mobile):
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
    def validate_email(self, email):
        return "@gmail" in email and "." in email

class MobileValidator:
    def validate_mobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

if _name_ == "_main_":
    otp_manager = OTPManager()
    otp = otp_manager.generate_otp()

    email = "manisha.deshingkar@gmail.com"
    otp_manager.send_otp_over_email(email, otp)

    mobile = "8625839939"
    otp_manager.send_otp_over_mobile(mobile, otp)
