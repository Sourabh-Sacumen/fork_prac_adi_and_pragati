#creating fibonacci series using generators
def fibo(first_value, second_value, limit):
    c=0
    while c<=limit:
        yield first_value
        first_value, second_value = second_value, first_value + second_value
        c+=1

FO = fibo(0,1,10)
for i in FO:
    print(i)