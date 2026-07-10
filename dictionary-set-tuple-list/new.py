intro = {
    "Name":"Shilpa",
    "Age":"21",
    "Sport":"Badminton"
}
print(intro["Age"])
print(intro.get('state'))   # .get specify a default value if the key doesn't exist 
print(intro.get('state','not exist'))  