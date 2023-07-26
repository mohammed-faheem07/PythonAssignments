#Python program for Fibonacci numbers 
n = int(input("Enter the N value: "))
f1 = 0
f2 = 1

for i in range(n):
    f3 = f1+f2
    print(f1)

    f1 = f2
    f2 = f3
