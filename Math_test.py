import random
import time
import math

OPERATORS = ["+","-","*","/"]
MIN_OPERAND = 3
MAX_OPERAND = 12

print("Maths Quiz Game!")

TOTAL_PROBLEM = int(input("Enter Number of Qustion: "))

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    opertor = random.choice(OPERATORS)
    
    expr = str(left) + " " + opertor + " " + str(right)
    ans = math.floor(eval(expr))
    return expr,ans


wrong = 0
print("Are You Ready To Quiz:")
input("Press enter to start! ")
print("*****************************")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, ans = generate_problem()
    while True:
        guess = input("Problem #" + str(i +1) + " : " + expr + " = ")
        if guess == str(ans):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("********************************")
print("Nice Work! You finished in ",math.floor(total_time), "seconds!")