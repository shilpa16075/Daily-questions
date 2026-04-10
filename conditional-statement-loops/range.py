# Range function in python populates its range list whenever it is employing such as for loop.
#  range( start-value, end value, difference between the values)
# for example: 
range(1, 30, 3)
print(list(range(1,30, 3)))
print(set(range(1,30, 3)))
print(tuple(range(1,30, 3)))
#  range ko hum increment aur decrement dono kr skte hai 
print(set(range(0,6,1) )  )      # increment k liye
print(set(range(10,0,-1) ) )       # decrement 