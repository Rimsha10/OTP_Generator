import os                # This is used for system function
import math          # The math library
import random     # For random numbers
import smtplib      # For email functions
import re
def solve(s):
   pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   if re.match(pat,s):
      return True
   return False
def otp(id):
 num = "0123456789"
 val = ""
 for i in range(0,6):
    val+= num[math.floor(random.random()*10)]
 OTP = val + " is your One-Time-Password for verification"
 message = OTP
 email = smtplib.SMTP('smtp.gmail.com', 587)  # To call the gmail account client
 email.starttls()
 #a = input("Enter your email ~~> :  ")
 #b = input("Enter your Password ~~> :  ")
 email.login('rimsha.ishtiaq10@gmail.com', 'kkrbjxuqvmgfstyh')  # To login into your account successfully
 #id = input("Enter your email address : ")
 try:
  email.sendmail("rimsha.ishtiaq10@gmail.com", id, message)   # Sending the OTP email
  #x = input("Enter your One-Time-Password ~~> :  ")
  #if x == val :
   #print("Hurray!! Your account has been successfully verified !! ")
  return val
  #else:
   #print("Please carefully check your OTP once again !! ")
   #print("Resend OTP?")
   #False
 except :
  print('Error occured while generation OTP.Please try again')
  return False
def otpcheck(otp_org,otp_entered):
  if otp_entered==otp_org:
       print("Hurray!! Your account has been successfully verified !! ")
       return True
  else:
       print("Please carefully check your OTP once again !! ")
       False
