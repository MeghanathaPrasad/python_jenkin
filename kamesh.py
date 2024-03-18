# class Account:
#     def __init__(self, account_id, balance=0):
#         self.account_id = account_id
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount} into Account {self.account_id}. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ${amount} from Account {self.account_id}. New balance: ${self.balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")

#     def get_balance(self):
#         return self.balance


# class Transaction:
#     @staticmethod
#     def transfer(source, target, amount):
#         if source.get_balance() >= amount:
#             source.withdraw(amount)
#             target.deposit(amount)
#             print(f"Transferred ${amount} from Account {source.account_id} to Account {target.account_id}")
#         else:
#             print("Insufficient funds for transfer.")


# # Example usage:
# account1 = Account(1, 1000)
# account2 = Account(2, 500)

# account1.deposit(200)
# account1.withdraw(100)

# account2.deposit(300)
# account2.withdraw(50)

# Transaction.transfer(account1, account2, 3000000)

# import copy

# l=[1,2,3,[100,200]]
# l2=copy.copy(l)

# l2[0]=100
# l2[3][0]=0
# print(l)
# print(l2)


# d={(1,2,3,4):"hi",(2,):"good"}

# print(d[(1,2,3,4)])

# l=[]


# l=[10,20,30]
# def sum(l):
#     return sum(l)





# sum = lambda l : sum(l)
# print(sum(l))

# l=[]
# for i in range(10):
#     if i%2==0:
#         l.append(i)
#     else:
#         l.append(i+100)
# print(l)


# only if condition is there
# number = [i for i in range(5) if i%2==0]

# if and else condition
# number = {i:i+5000 if i%2==0 else i+100 for i in range(10)}
# print(number)


# def number():
#     i = 0
#     while True:
#         yield i
#         i+=1

# num = number()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# for i in range(5):
#     print(next(num))

# print("continue")

# # print(next(num))


# l=[1,2,3,"",None,"a"]
# l2=[]

# for i in l:
#     if i:
#         pass
#     else:
#         l.remove(i)

# print(l)

# g=None

# if g:
#     print("undi")

# else:
#     print("ledu")

# t={{1,2}: }
# t.add(6)
# print(t)

s = set()
print(type(s))

