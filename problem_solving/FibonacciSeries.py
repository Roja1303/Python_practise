nums = int(input("Enter the number: "))

n1 = 0
n2 = 1

if nums <= 0:
    print("Please enter a a positive integer")
elif nums == 1:
    print(f" Fibonacci series ; {n}")
else:
    for i in range(nums):
        print(n1,end=" ")
        n = n1+n2
        n1 = n2
        n2 = n