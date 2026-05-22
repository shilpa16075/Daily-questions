# Create a function show_employee() that accepts an employee’s name and salary. 
# If the salary is not provided in the function call, the function should automatically assign a default 
# value of 9000.
def show_employee(name,salary=9000):
    print(f'Employee name is {name} and the salary is {salary}')

show_employee('kunal',10000)
show_employee('karan')

