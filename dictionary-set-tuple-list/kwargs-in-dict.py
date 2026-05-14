# program using kwargs
def Hostel_details(**info):
    for i,j in info.items():
        print(f'The hostel details are {i} : {j}')

Hostel_details(hostel_name= 'Ganga' ,Total_seats= 360,Mess_no= 1, rooms= 200) # function call use =
Hostel_details(hostel_name= 'Ganga' ,warden ='Dr.priyanka', rooms= 200)       # using {}brackets use : colon
Hostel_details(hostel_name= 'Meghna', warden = 'Dr.kirti Desai', rooms = 160)
