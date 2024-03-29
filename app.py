import os
import json
import requests
import time
from datetime import datetime
import pytz

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

tracking_number = os.getenv('TRACKING_NUMBER')
twilio_sid = os.getenv('TWILIO_SID')
twilio_token = os.getenv('TWILIO_TOKEN')
number_from = os.getenv('NUMBER_FROM')
number_to = os.getenv('NUMBER_TO')
message_text = os.getenv('MESSAGE_TEXT')
timezone = os.getenv('TIMEZONE')

tz = pytz.timezone(timezone)

def send_message(text):
    client = Client(twilio_sid, twilio_token)
    message = client.messages.create(
        to=number_to,
        from_=number_from,
        body=text
    )

def get_current_time():
    return datetime.now(tz)

if __name__ == "__main__":
    url = 'https://www.ups.com/track/api/Track/GetStatus'
    headers = {'Content-Type':'application/json'}
    data = {"Locale":"en_US","TrackingNumber":[tracking_number]}

    package_has_been_delivered = False
    while package_has_been_delivered == False:
        r = requests.post(url=url,data=json.dumps(data),headers=headers).json()
        time_delivered = r['trackDetails'][0]['deliveredTime']
        if time_delivered != "":
            send_message(message_text)
            package_has_been_delivered = True
        else:
            time_now = get_current_time()
            print(f'nothing happened - {time_now}')
            time.sleep(60)
