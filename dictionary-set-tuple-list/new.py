intro = {
    "Name":"Shilpa",
    "Age":"21",
    "City":"Jaipur",
    "Sport":"Badminton"
}
intro["day"]="Friday"
print(intro['City'])
print(intro)
del intro['Name']
print(intro)
for i in intro.keys():    #to access the keys only
    print(i)

for i in intro.values():  #to access the value only
    print(i)

for keys,values in intro.items():   # to access both 
    print(f'{keys}:{values}')
print(intro["Age"])
print(intro.get('state'))   # .get specify a default value if the key doesn't exist 
print(intro.get('state','not exist'))  