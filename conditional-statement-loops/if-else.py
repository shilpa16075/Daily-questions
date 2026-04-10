# if-else statement when the condition of if statement is true then statement inside if block will be executed and if the condition of the if block is false then the else block is executed.
age = int(input("enter your age: "))   # user enter age = 18 
if age>=18:                            # which means the condition is true, now the if block will be executed
    print("You are eligible to Vote")
    print("Press the voting Button")
else:                                   # Now the user entered age = 13 means the condition of if block is false,so the else block will be executed
    print("You are not Eligible")

print("Program Ends here")

