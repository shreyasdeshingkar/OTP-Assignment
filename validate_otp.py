import random
import smtplib
from twilio.rest import Client
import keys

class OTPManager:
    def __init__(self):
        pass

    def generate_otp(self):
        """
        + generate_otp(): String
        """
        return ''.join([str(random.randint(0, 9)) for i in range(6)])

    def send_otp_over_email(self, email, otp):
        """
        + send_otp_over_email(email: String, otp: String): void
        """
        if self.validate_email(email):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('shreyasdeshingkar@gmail.com', 'muacwkbygeasmtow')
            msg = f'Hello, your OTP is {otp}\nPlease do not share the OTP with anyone.' \
                  f'\nThis is a system-generated mail, so do not reply.'
            server.sendmail("shreyasdeshingkar@gmail.com", email, msg)
            print("OTP is sent to email via email.")
        else:
            print("Invalid email address.")

    def send_otp_over_mobile(self, mobile, otp):
        """
        + send_otp_over_mobile(mobile: String, otp: String): void
        """
        if self.validate_mobile(mobile):
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

    def validate_email(self, email):
        """
        - validate_email(email: String): bool
        """
        return "@gmail" in email and "." in email

    def validate_mobile(self, mobile):
        """
        - validate_mobile(mobile: String): bool
        """
        return len(mobile) == 10 and mobile.isdigit()


if __name__ == "__main__":
    otp_manager = OTPManager()

    otp = otp_manager.generate_otp()

    email = "manisha.deshingkar@gmail.com"
    otp_manager.send_otp_over_email(email, otp)

    mobile = "8625839939"
    otp_manager.send_otp_over_mobile(mobile, otp)
