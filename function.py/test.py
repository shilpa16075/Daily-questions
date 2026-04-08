# def sum(*arg):
#     print(arg[0])
#     return 


# sum(2,3,0,7)

def userDetails(**arg):
    print("name:"+arg["name"])
    print("roll:"+arg["roll"])
    print("sports:"+arg["sports"])
    print("dance:"+arg["dance"])


userDetails(name="Shilap" ,roll="12", dance="...",sports="yes")
# userDetails("Sahil" ,"19","no")
