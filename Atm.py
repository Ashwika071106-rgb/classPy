class Atm(object):
    kind = "Automated Teller Machine"
    def __init__(self,name,bank,cardNo,pin):
        self.bank = bank
        self.cardNo = cardNo
        self.pin = pin
        self.name = name

    def withdrawal(self,amount):
        print("I am {} and I wish to make a withdrawal of {} from {}".format(self.name,amount,self.bank))
        print("My card number is {}. My pincode is {}.".format(self.cardNo,self.pin))
        print("Your request is being processed")
        return "Withdrawal Successful"

    def deposit(self,amount):
        print("I am {} and I wish to make a deposit of {} in my acoount of {}".format(self.name,amount,self.bank))
        print("My card number is {}. My pincode is {}".format(self.cardNo,self.pin))
        print("Your request is being processed")
        print("Money has been deposited")

person1 = Atm("Ashwika","Axis Bank",1678930,255591)

print("This is an {} ".format(person1.__class__.kind))

print(person1.withdrawal(100000))

print(person1.deposit(23760))

person2 = Atm("Aishani","Union Bank",7865140,711067)

print("This is an {} ".format(person2.__class__.kind))

print(person2.withdrawal(987650))

print(person2.deposit(1000098))