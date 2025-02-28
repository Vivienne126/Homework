def check_age():
    while True:
        try:
            age=int(input("Enter your age"))
            if age<0:
                raise ValueError
            break
        except ValueError:
            print("Input is not valid please enter a valid input")

    if age % 2 == 0:
        print("The age entered is even")
    else:
        print("The age entered is odd")
check_age()
