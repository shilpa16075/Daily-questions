def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

# Example usage
num = int(input("Enter a number: "))
print(is_prime(num))