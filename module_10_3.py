
import threading
import random
import time
from threading import Thread, Lock



class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        count=0
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            positive = random.randint(50, 500)
            self.balance += positive
            count+=positive
            print(f'Пополнение: {positive}. Баланс: {self.balance}')
            time.sleep(0.001)
        return count


    def take(self):
        count = 0
        for i in range(100):
            negative = random.randint(50,500)
            print(f'Запрос на {negative}')
            if self.balance >= negative:
                self.balance -= negative
                count-=negative
                print(f'Снятие: {negative}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
            time.sleep(0.001)




bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

