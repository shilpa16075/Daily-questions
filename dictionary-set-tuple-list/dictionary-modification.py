# Here we see dictionary modification,.
phone_no = {
    'shilpa': 123453,
    'shilon': 385348,
    'ajay': 382496,
    'yogesh': 845863
}
print(phone_no)
phone_no['shilon'] = {'shilon home': 589643,'shilon work':83552 } # dictionary in dictionary
print(phone_no['shilon'])
phone_no['ajay'] = 21342   # changing the value of a particular key 
print(phone_no)
phone_no['priti'] = phone_no['ajay'] # replace and delete
del phone_no['ajay']
print(phone_no)
phone_no['shilon'] =[124674,4562344,689472]    # storing list in dictionary
print(phone_no['shilon'])
phone_no['ravi'] = 24715   # add new key-value pair
print(phone_no)
phone_no.clear()   # clear the whole dictionary
print(phone_no)
del phone_no        # delete the dictionary entirely means if you run the print command to print the previously existing dictionary it will give you a nameerror
print(phone_no)     # because the phone_no dictionary is no longer exist