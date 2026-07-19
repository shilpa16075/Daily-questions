# create a python project to ask 4 question to the user and marks one one every correct answer and display a message
# on every wrong aswer respectively.
print('WELCOME TO THE QUIZ COMPETITION!!!!')
marks = 0
Question1 = input('what is the color of sky: ')
if Question1 == 'blue':
    print('well played!!!moving to next question')
    marks +=1
    print(f'Your score = {marks}')
else:
    print('wrong answer!!!')
    print(f'Your score = {marks}')

