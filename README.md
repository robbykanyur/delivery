# delivery

a python script to text me when my package is delivered

--

ENV VARIABLES:

- TRACKING_NUMBER - your UPS tracking number
- TWILIO_SID - your Twilio SID
- TWILIO_TOKEN - your Twilio auth token
- NUMBER_FROM - your Twilio phone number ("+1555555555")
- NUMBER_TO - number to send notification text to ("+15555555555")
- MESSAGE_TEXT - content of notification message
- TIMEZONE - your current timezone ("America/Phoenix")
