from __future__ import print_function

import africastalking


class SMS:
    def __init__(self, message, recipients):
        self.username = "MBUGUACALEB"
        self.api_key = "59a9a1674cb64f9d65c380bb3ae6ccd0326eb833bcca0e43cdbefbe7a04c44c9"
        self.recipients = recipients
        self.message = message

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        try:

            # Thats it, hit send and we'll take care of the rest.

            recipients = []
            recipients.append(self.recipients)
            response = self.sms.send(self.message, recipients)
            print("Hello my name is " + self.message + self.recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


# sendMessage = SMS("CALEB", "+254704699193")

# sendMessage.send()
