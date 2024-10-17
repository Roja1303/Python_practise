from math import factorial

if __name__ == '__main__':

    nums = int(input("Enter the number: "))

    for n in range(nums):
        for space in range(1,nums-n):
            print(end = " ")
        for r in range(n + 1):
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            print(ncr, end=" ")
        print(" ")

