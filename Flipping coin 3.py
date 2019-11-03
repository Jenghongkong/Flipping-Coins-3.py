import random
n = int(input("How times would you like to flip the coin?: "))
for i in range(n+1):
    a = random.randint(1,2)
    if a==1:
        print("biased ")
    else:
        print("unbiased ")

