import pytesseract
import re
from send_mail import send_mail
driving_license = pytesseract.image_to_string('/home/billion/Downloads/driving3.jpeg')
print(driving_license)

expiry_pattern1 = r"Valid Till (\d{2}-\d{2}-\d{4})"
expiry_pattern2 = r"Validity\s*\+\s*(\d{2}/\d{2}/\d{4})"

expiry_date_match1 = re.search(expiry_pattern1, driving_license, re.IGNORECASE)
expiry_date_match2 = re.search(expiry_pattern2, driving_license, re.IGNORECASE)

if expiry_date_match1:
    expiry_date = expiry_date_match2.group(1)
    print("Expiry date:", expiry_date)
    send_mail(expiry_date)

if expiry_date_match2:
    expiry_date = expiry_date_match2.group(1)
    print("Expiry date:", expiry_date)
    send_mail(expiry_date)

else:
    print("Expiry date not found")
