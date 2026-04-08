num = int(input("Enter a number for table: "))

for i in range(1, 11):
    # f-string use karke formatting aasan ho jati hai
    print(f"{num} x {i} = {num * i}")