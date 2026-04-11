 # You have two lists of team members:

# Team A: Liam, Olivia, Noah
# Team B: Emma, Ava, Sophia
# Create one list for each team, then:

# Combine both lists into a new list called all_members and print this new list.
# Add "Mason" to the combined list.
# Remove "Olivia" from the list.
# Print the total number of members using the len() function.
# Print the sorted list of all members.
Team_A = ['Liam', 'Olivia', 'Noah']
Team_B = ['Emma','Ava','Sophia']
all_members = Team_A + Team_B
print(all_members)
all_members.append("Mason")
print(all_members)
all_members.remove('Olivia')
print(len(all_members))
all_members.sort()
print(all_members)