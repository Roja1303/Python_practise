from debugpy.server.cli import in_range

if __name__ == '__main__':

    # Right angled triangle
    n = int(input("Enter the number: "))

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

    # 2

    num = int(input("Enter the number: "))

    for m in range(1,num+1):
        for l in range(1,m+1):
            print(l,end= " ")
        print( )


    #3

    row = int(input("Enter the number: "))

    for p in range(1,row+1):
        for q in range(1,p+1):
            print("*",end = " ")
        print( )

    #4

    col = int(input("Enter the number: "))

    for s in range(1,col+1):
        print(" "*(col-s)+ "*"*s)
    print( )

    #5 multiplication table pattern
    p = int(input("Enter the number: "))

    for o in range(1,p+1):
        for t in range(1,o+1):
            print(o*t,end = " ")
        print( )


    #6 pyramid patterns
    star =  int(input("Enter the number: "))
    for x in range(1,star+1):
        for space in range(1,star-x+1):
            print(end = " ")
        for y in range(1,x+1):
            print("*",end = " ")
        print()

    #7
    rows = int(input("Enter the number: "))

    for e in range(rows,0,-1):
        for spaces in range(1,rows-e+1):
            print(end = " ")
        for f in range(1,e+1):
            print("*",end = " ")
        print( )

    #8
    r = int(input("Enter the number: "))

    for u in range(r,0,-1):
        for v in range(1,u+1):
            print("*",end = " ")
        print( )

    #9
    c = int(input("Enter the number: "))

    for g in range(c, 0, -1):
        print(" "*(c-g),end = "")
        for h in range(1, g + 1):
            print("*", end="")
        print()



