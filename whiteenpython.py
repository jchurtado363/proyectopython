nombre = input("como te llamas")
edad1=input("INGRESE EDAD")
while not edad1.isdigit():  
     edad1=input("digita un numero")
edad1=int(edad1)
if(edad1<25):
    print("ERES ESTUDIANTE")
elif(edad1>25):
    print("ERES DOCENTE")
elif(edad1>65):
    print("ERES ADULTO MAYOR")    
