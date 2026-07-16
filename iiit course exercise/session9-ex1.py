numbers = [10, 20, 30, 40, 50]
total = 0
for i in range(5):  # BUG HERE!
    total += numbers[i]
print(f"Total: {total}")