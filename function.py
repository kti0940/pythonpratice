def open_account():
    print("새로운 계좌가 개설되었습니다")
    
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원 입니다".format(balance))
        
def withdraw_night(balance, money): #저녁에 출금
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))