import pyotp
import time
import qrcode
# totp = pyotp.TOTP('base32secret3232')
# print(totp.now())
key = 'YouCanNeverGuessThis'

uri = pyotp.totp.TOTP(key).provisioning_uri(name='femmyte@google.com', issuer_name='Femmyte App')
qrcode.make(uri).save('totp.png')
print(uri)