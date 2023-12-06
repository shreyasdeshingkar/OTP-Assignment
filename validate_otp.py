import random
import smtplib
from twilio.rest import Client
import keys  # assuming keys.py contains necessary credentials

class OTPManager:
    def __init__(self):
        self.email_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.email_server.starttls()
        self.email_server.login('shreyasdeshingkar@gmail.com', 'muacwkbygeasmtow')

        self.sms_client = Client(keys.account_sid, keys.auth_token)

    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def send_otp_over_email(self, email, otp):
        if self.validate_email(email):
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.' \
                  f'\nThis is a system-generated mail, so do not reply.'
            self.email_server.sendmail("shreyasdeshingkar@gmail.com", email, msg)
            print("OTP is sent to email via email.")
        else:
            print("Invalid email address.")

    def send_otp_over_mobile(self, mobile, otp):
        if self.validate_mobile(mobile):
            msg = self.sms_client.messages.create(
                body=f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.'
                     f'\nThis is a system-generated message, so do not reply.',
                from_=keys.twilio_number,
                to=mobile
            )
            print(msg.body)
        else:
            print("Invalid mobile number.")

    @staticmethod
    def validate_email(email):
        return "@gmail" in email and "." in email

    @staticmethod
    def validate_mobile(mobile):
        return len(mobile) == 10 and mobile.isdigit()

if __name__ == "__main__":
    otp_manager = OTPManager()

    otp = otp_manager.generate_otp()

    email = "manisha.deshingkar@gmail.com"
    otp_manager.send_otp_over_email(email, otp)

    mobile = "8625839939"
    otp_manager.send_otp_over_mobile(mobile, otp)
