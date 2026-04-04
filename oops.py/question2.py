# Create a class Laptop with attributes: brand, RAM,Price. Create 2 object with different values.
class Laptop():
    brand = "Dell"
    RAM = "8gb"
    price = "1.2lac"

laptop1 = Laptop()
Laptop.RAM = "8gb"
print(Laptop.RAM,Laptop.price)

laptop2 = Laptop()
Laptop.brand = "lenovo"
print(Laptop.brand,Laptop.price)


