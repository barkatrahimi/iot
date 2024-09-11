start = int(input("give start value: "))
end = int(input("Ange end value: "))

# FizzBuzz loop
for i in range(start, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)