import requests
import datetime
import smtplib
import time

MY_LAT = 41.032050
MY_LONG = 28.889961
GMT = 3
EMAIL_ADDRESS = '<EMAIL>'
PASSWORD = '<PASSWORD>'
MY_LOVE = "ecemnurozen03@gmail.com"

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        "formatted": 0,
    }

    response_suntime = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_suntime.raise_for_status()
    data = response_suntime.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) + GMT
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0]) + GMT

    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=MY_LOVE, msg="Subject: Heads Up!\n\nIss is overhead!")