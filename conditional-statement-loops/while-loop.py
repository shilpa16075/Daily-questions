#  sometimes it is uncertain to determine, in how many iteration can a program complete its task. The loop 
# ultimately ends its job, but only when a condition changes.
#  In some situations, you use an infite loop and inside the loop, some condition determine when to terminate the loop.
#  this is called condition iteration 
#  while <conditon>:
#  <sequence of statement>

#  for example:
name = input("enter your name: ")
while name!= "point break":
    print("wrong password")
    name = input("enter the password again: ")
print("welcome Thor")
