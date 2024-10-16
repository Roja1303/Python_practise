if __name__ == '__main__':
    a = " Hello World"
    print(a[2])
    print(len(a))
    print("World" in  a)
    #slicing
    print(a[::-1])
    print(a[-5:-2])
    print(a.upper())
    print(a.lower())
    print(a.capitalize())
    print(a.strip())
    print(a.replace("d", "ds"))
    print(a.split())
    print(f"The value of a is:  {a}")





    if "Hello" not in a:
        print("True it is present")
    else:
        print("False it is not present")

    #Looping Through a String
    for i in  "Banana":

        print(i,end = "")


