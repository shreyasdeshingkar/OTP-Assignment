import smtplib
import random
otp = ''.join([str(random.randint(0,9)) for i in range(4)])
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('shreyasdeshingkar@gmail.com', 'muacwkbygeasmtow')
msg = 'Hello, your OTP is '+ str(otp) +  '\nPlease do not share the OTP with anyone.' +  '\nThis is System generated mail so do not reply.'
server.sendmail('shreyasdeshingkar@gmail.com', 'manisha.deshingkar@gmail.com', msg)

