from math import factorial

if __name__ == '__main__':

    num = int(input("Enter the number: "))

    for n in range(num):
        for space in range(1,num-n):
            print(end = " ")
        for r in range(n + 1):
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            print(ncr, end=" ")
        print(" ")

