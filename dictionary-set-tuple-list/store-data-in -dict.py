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
# Method 1
price.update({
    'rabbit' :'$6',
    'book' : '$8',
    'pencil' : '$1'
})
print(price)