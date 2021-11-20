'''Enter a number and have the program generate 'PI' and 'e' up to that many decimal places. \
Keep a limit to how far the program will go.'''

pi = 3.142857142857143
e = 2.718281828459045

def print_pi(limit):
    print('Value of Pi upto',limit,'decimal places: ',round(pi, limit))  

def print_e(limit):
    print('Value of e upto',limit,'decimal places: ', round(e, limit))


try:
    print("-- Welcome to my program--")
    print("1. Pi")
    print("2. e")
    choice = int(input("Enter your choice: "))
    
    if choice>2:
        print("Wrong choice!")
    else:
        limit = int(input("Enter required number of digits after decimal: "))
        if limit>0 and limit<=15:
            if choice == 1:
                print_pi(limit)
            elif choice == 2:
                print_e(limit)
            else:
                print("Wrong choice")
        else:
            print("Invalid index range!")
except:
    print("Error")

