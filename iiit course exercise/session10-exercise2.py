temp = int(input("Enter today's temperature in °C: "))

if temp >= 30:
    print("It's hot outside!")
elif temp >= 20:
    print("Nice and warm.")
elif temp >= 10:
    print("A bit cool, bring a jacket.")
else:
    print("It's cold, stay warm!")