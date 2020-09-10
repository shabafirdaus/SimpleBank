'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class Bank:
    print("Enter Your Name:")
    owner=input()
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,newamount):
        print('Deposit Amount:')
        newamount=int(input())
        self.balance=newamount+self.balance
        print('We have added {} to your account'.format(newamount))
        print('Updated Balance is {}'.format(self.balance))
        print('Have a nice Day!')
    def withdraw(self,need):
        print('Withdraw Amount:')
        need=int(input())
        if need<=self.balance:
            self.balance=self.balance-need
            print('Please collect the cash')
            print('Updated balance is {}'.format(self.balance))
            print('Have a nice Day!')
        else:
            print('Oops,Low Balance!!!')
acc1=Bank(balance=1000)
print("Welcome to Your Bank Account,{}".format(acc1.owner))
def start():
    print('This bank has given you a Balance of Rs{}'.format(acc1.balance))
    print("Press 'd' for Deposit or 'w' for the Withdrawal")
def bank():
    a=str(input())
    if a=='d':
        acc1.deposit(1)
        start()
        bank()
    elif a=='w':
        acc1.withdraw(1)
        start()
        bank()
    else:
        print("Press only 'd' or 'w'")
        bank()
start()
bank()
