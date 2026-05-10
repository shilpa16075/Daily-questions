# positional vs keyword argument 
def positional_para(name , age):
    print(f'New student with name {name} and age {age}')

positional_para("shilpa",20)
positional_para(90,"shiva")
# Keyword argument
def keyword_agrs(name,subject):
    print(f'Student {name} has suject {subject}')

keyword_agrs(name = "Shiva",subject="Cloud computing")
keyword_agrs(subject="Software engineering",name="Ravi")