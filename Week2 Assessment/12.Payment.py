from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass
class CreditCardPayment(Payment):
    def process_payment(self):
        print('Credit card payment processed')
class PayPalPayment(Payment):
    def process_payment(self):
        print('PayPal payment processed')
class BitcoinPayment(Payment):
    def process_payment(self):
        print('Bitcoin payment processed')
def main():
    c = CreditCardPayment()
    c.process_payment()
    p = PayPalPayment()
    p.process_payment()
    b = BitcoinPayment()
    b.process_payment()
main()