from __future__ import print_function

import africastalking
from django.conf import settings


class SMS:
    def __init__(self, message, recipients):
        self.username = settings.AFRICAS_TALKING_USERNAME
        self.api_key = settings.AFRICAS_TALKING_API_KEY
        self.recipients = recipients
        self.message = message

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        try:
            recipients = []
            recipients.append(self.recipients)
            response = self.sms.send(self.message, recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


# sendMessage = SMS("CALEB", "+254704699193")

# sendMessage.send()
