def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print "Enter a number for factorial calc: "
num = raw_input()
print(factorial(int(num)))
