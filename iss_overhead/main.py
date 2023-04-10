import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 51.9264108 # Your latitude
MY_LONG = 15.4800003 # Your longitude
MY_EMAIL ="YOUt@gmail.com" # Your email address
PASSWORD = "YOUPASSWORD" # Your password

# Check if the ISS is overheads
def is_iss_overhead(): 
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True
    
# Check if the ISS is night
def is_night(): 
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunrise and time_now <= sunset:
        return True
    

# Send a message to the ISS
def message(): 
    message = "Вийди на вулицю і подивись на небо, десь там летить МКС"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="to_mail@yahoo.com",
            msg=f"Subject:MKC\n\n{message}".encode('utf-8')
                )
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        message()
