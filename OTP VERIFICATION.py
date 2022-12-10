import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
otp = OTP + " is your OTP"
msg = otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("omaradamissack@gmail.com", "dusntyxqmmeadisj")
email_id = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', email_id, msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
