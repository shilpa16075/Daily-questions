#  create menu-driven using match:
num = int(input("enter number between 1 to 4: "))
match num:
    case 1:
        print("add")
    case 2:
        print("sub")
    case 3:
        print("multiply")
    case 4:
        print("Division")
    case 5:
        print("invalid choice")