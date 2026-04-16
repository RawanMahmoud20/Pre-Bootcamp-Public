class Car:
    def __init__(self, color, engine, wheels = 4):
        self.color = color
        self.wheels = wheels
        self.engine = engine

    def print_info(self):
        print(f"My car has the color {self.color} and has {self.wheels} number of wheels")

# has-a

class Engine:
    def __init__(self, cylinder, horsepower):
        self.cylinder = cylinder
        self.horsepower = horsepower

bmw_engine = Engine(4, 200)
mercedes_engine = Engine(2, 150)

my_car = Car("red", bmw_engine, 3)
nesma_car = Car("blue", mercedes_engine)

my_car.print_info()
nesma_car.print_info()
# anther ex fot inheritance
class Notification:
    def __init__(self, message):
        self.message = message
        
    def send(self):
        print(f"{self.message} has been sent")

class WarningNotification(Notification):
    def __init__(self, message, type):
        super().__init__(message)
        self.type = type

class SMSNotification(Notification):
    def sms_provider_integration(self):
        print("I will return all the different sms provider integration details")

otp_sms_notification = SMSNotification("Here is your otp: 127835")

class NotificationSystem:
    def send_message(self, notification):
        # check type
        # check integration settings
        notification.send()

notification_system = NotificationSystem()

notification_system.send_message(otp_sms_notification)