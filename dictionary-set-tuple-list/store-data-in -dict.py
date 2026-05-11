# Exploring more features of dictionary.
price ={
    'car':'$19',
    'pen': '$2',
    'notebook':'$5',
    'teddy':'$7'
}
#To add one key pair in this dictionary
price['bottle'] = '$3'
print(price)
# To add more then one key pair in this dict at once then their the 3 methods
# Method 1 using .update() method
price.update({
    'rabbit' :'$6',
    'book' : '$8',
    'pencil' : '$1'
})
print(price)
sold_out = {
    'rabbit' :'$6',
    'pencil' : '$1',
    'car':'$19',
}
# Method 2 using |operator : this is used when we want to merge 2 dictionary 
sold_price =price|sold_out
print(sold_price)
# Method 3 using kwargs
soldout_price ={**sold_out,**price}
print(soldout_price)