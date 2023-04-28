def greet():
    print("Hello From Sourabh")

def greet_p():
    print("Hi pragati this side")

# creating pattern 

# taking int input from user
num=int(input("enter number:"))

# looping num
for row in range(num):
    for col in range(num):
        if row+col<=num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

def my_hello():
    print("Hellooo... from my side.")
