class BankAccount:

    def __init__(self , name , number , balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw_money (self , money):
        self.balance -= money

    def deposit_money (self , money):
        self.balance += money

    def display_information(self):
        print(f"Account Holder name :  {self.name} " )
        print(f" Account Number : {self.number}")
        print(f" Balance : {self.balance}")



if __name__ == "__main__":
    warner = BankAccount("David Warner" ,31 , 800)
    warner.deposit_money(1)
    warner.withdraw_money(100)
    warner.display_information()

