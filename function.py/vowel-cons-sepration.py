# Write a function that takes a string and returns the count of vowels and
# consonants separately.
def vowelconso(a):
    vowel = "aeiouAEIOU"
    vowelc = 0
    consoc = 0
    for eachchar in a:
        if eachchar.isalpha:
            if eachchar in vowel:
                vowelc = vowelc +1 
            else:
                consoc = consoc+1
    return vowelc,consoc
            

vowelc,consoc = vowelconso("shilpa")
print(vowelc , consoc)
    