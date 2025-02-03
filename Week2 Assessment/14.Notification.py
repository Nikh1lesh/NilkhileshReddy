class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        pass
class EmailNotification(Notification):
    def send(self):
        print(f'Email: {self.message}')
class SMSNotification(Notification):
    def send(self):
        print(f'SMS: {self.message}')
def main():
    e = EmailNotification('This is an email')
    e.send()
    s = SMSNotification('This is an SMS')
    s.send()
main()