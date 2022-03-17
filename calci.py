
print("--------------------------WELCOME TO MAYANK'S CALCI---------------------------------------------")
def check(a):
    f = "false"
    t = "true"
    for i in a:
        if(ord(i) >= 48 and ord(i) <= 57):
            return t
        else:
            return f


def add(a, b):
    return(a+b)


def sub(a, b):
    return(a-b)


def mul(a, b):
    return(a*b)


def div(a, b):
    # checking zero divisor error
    if(b == 0):
        print("since the denominator is zero division cannot be performed it will throw a zero division error")
        exit()
    else:
        return(a/b)


def mod(a, b):
    if(b == 0):
        print("since the denominator is zero modulus cannot be performed it will throw a zero division error")
    else:
        return(a % b)


print("print i or I to operate on integer numbers")
print("print F or f to operate on float numbers")
print("-----------------------------------------------------------------------")
print("print '+' to perform addition")
print("print '-' to perform subtraction")
print("print '/' to perform division")
print("print '%' to perform modulus")
print("----------------------------------------------------------------------")

choice1 = input("enter your choice for integer or float    ")
choice1.lower()
choice2 = input("enter your choice for operations     ")

if(choice1 == 'i' or choice1 == 'I'):
    a1 = input("enter the first integer ")
    a2 = input("enter the second integer  ")
    if(choice2 == '+'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = int(a1)
            a2 = int(a2)
            print("addition is", add(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '-'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = int(a1)
            a2 = int(a2)
            print("subtratction is", sub(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '/'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = int(a1)
            a2 = int(a2)
            print("divissionm is", div(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '*'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = int(a1)
            a2 = int(a2)
            print("multiplication is is", mul(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '%'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = int(a1)
            a2 = int(a2)
            print("modulus is", mod(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
if(choice1=='f' or choice1=='F'):
    a1 = input("enter the first floating point numnber ")
    a2 = input("enter the second floating point number  ")
    if(choice2 == '+'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = float(a1)
            a2 = float(a2)
            print("addition is", add(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '-'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = float(a1)
            a2 = float(a2)
            print("subtratction is", sub(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '/'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = float(a1)
            a2 = float(a2)
            print("division is", div(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '*'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = float(a1)
            a2 = float(a2)
            print("multiplication is is", mul(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
    elif (choice2 == '%'):
        c = check(a1)
        d = check(a2)
        if(c == "true" and d == "true"):
            a1 = float(a1)
            a2 = float(a2)
            print("modulus is", mod(a1, a2))
        elif(c == "false" or d == "false"):
            print("invalid input")
            exit()
