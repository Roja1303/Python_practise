num = int(input("Enter the number: "))

n1 = 0
n2 = 1

if num <= 0:
    print("Please enter a apositive integer")
elif num == 1:
    print(f" Fibonacci series ; {n}")
else:
    for i in range(num):
        print(n1,end=" ")
        n = n1+n2
        n1 = n2
        n2 = n