from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

def send_sms(to_phone, from_phone, message):
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message,
            from_=from_phone,
            to=to_phone
        )
        print(f"Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage
if __name__ == "__main__":
    to_phone = '+1234567890'  # Replace with recipient's phone number
    from_phone = '+0987654321'  # Replace with your Twilio phone number
    message = 'Hello from DriveXpert!'
    send_sms(to_phone, from_phone, message)