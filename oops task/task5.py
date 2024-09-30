
from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processpayment(self):
        pass
class Credit(PaymentMethod):
    def processpayment(self):
        print("Payment using Credit card")
class Paypol(PaymentMethod):
    def processpayment(self):
        print("Payment using Paypol")

def process_payment(payment_method: PaymentMethod):
    payment_method.processpayment() 

credit=Credit()
process_payment(credit)
paypol=Paypol()
process_payment(paypol)
