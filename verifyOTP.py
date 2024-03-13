import pyotp
import time
import qrcode
key = 'YouCanNeverGuessThis'
totp = pyotp.TOTP(key)
# print(totp.now())
otpCode = input('enter the OTP here ')
verifyOTP = totp.verify(otpCode)
if verifyOTP == True:
    print('OTP verified you can now login')
else:
    print('Invalid OTP')