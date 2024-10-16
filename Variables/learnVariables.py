if __name__ == '__main__':
    # Creating Variables
    a = 10
    b = 20
    c = a + b
    print(c)

    # casting
    a = str(10)
    print(type(a))

    b = float(20)
    print(b)
    print(type(b))

    # case sentive

    m = "Roja"
    M = "Shankar"
    print(m == M)
    print(m)

    # Many Values to Multiple Variables
    x, y, z = 10, 20, 30
    print(x)
    print(y)
    print(z)

    # one values to multiple variables
    d = e = f = "Orange"
    print(d)
    print(e)
    print(f)

    #Unpack a Collection

    fruits = ["apple","orange","banana"]
    l,m,n = fruits
    print(l,m,n)
    print(l+m+n)

    # global variables

    x = "awesome"
    def global_variable():
        global x
        x = "Fantastic"


    global_variable()
    print(x)
