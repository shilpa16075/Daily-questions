# You have a list of friends attending a dinner party: Farah, Alex, Charlie, Dana, Brooke, Eli.

# Create the list, then:

# Use slicing to print only the middle guests (Charlie, Dana, Eli).
# Add a new friend "Gina" to the end of the list.
# Remove "Alex" from the list.
# Print the final sorted list in alphabetical order.
friends = ['farah','alex','charlie','dana','brooke','eli']

print(friends[2:])
friends.append('gina')
print(friends)
friends.remove("alex")
print(friends)
friends.sort()
print(friends)