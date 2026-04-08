def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in text:
        if ch in vowels:
            count += 1
            
    return count

# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))