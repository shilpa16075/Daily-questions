# keyword arbitary parameters : stores all the key-value in dictionary with key and 
# value like name = "shiv" and age = 20 ,here keys are name and age , values are "shilpa" and 20
def information(**info):
    for i, j in info.items():
        print(f'The {i}: {j}')

information(name = 'shilpa',age = 20, subject = 'software engineering',degree = 'BCA')