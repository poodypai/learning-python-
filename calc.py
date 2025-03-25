import os
def menu():
    os.system('clear')
    print("Simple Calculator \n")
    print("1. Add 2 Numbers \n")
    print("2. Substract 2 Numbers \n")
    print("3. Multiply 2 Numbers \n")
    print("4. Divide 2 Numbers \n")
    print("5. Exit the program \n")
    choice = input("Choose a number: ")
    if choice == '1':
        add()
    elif choice == '2':
        sub()
    elif choice == '3':
        mul()
    elif choice == '4':
        div()
    elif choice == '5':
        exit()
    else:
        print("Wrong Choice!")

def add():
    os.system("clear")
    x, y = map(int,input("Enter 2 Numbers: ").split())
    print("The output is ", x + y)
    os.system("read -p 'Press Enter to continue...'")
    menu()

def sub():
    os.system("clear")
    x, y = map(int,input("Enter 2 Numbers: ").split())
    print("The output is ", x - y)
    os.system("read -p 'Press Enter to continue...'")
    menu()

def mul():
    os.system("clear")
    x, y = map(int,input("Enter 2 Numbers: ").split())
    print("The output is ", x * y)
    os.system("read -p 'Press Enter to continue...'")
    menu()

def div():
    os.system("clear")
    x, y = map(int,input("Enter 2 Numbers: ").split())
    print("The output is ", x / y)
    os.system("read -p 'Press Enter to continue...'")
    menu()

menu()
