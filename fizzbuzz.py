for n in range(1,1000):
    if ((n % 3 == 0) & (n % 5 == 0)):
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
