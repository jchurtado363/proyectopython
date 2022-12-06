numusu1=int#(input('ingrese el primer numero :'))
numusu2=int#(input('ingrese el segundo  numero :'))
numusu3=int#(input('ingrese el tercer numero :'))

for i in (numusu1,numusu2,numusu3):
 numusu1=int(input('ingrese el primer numero :'))
 numusu2=int(input('ingrese el segundo  numero :'))
 numusu3=int(input('ingrese el tercer numero :'))
 num1par=numusu1%2
 num2par=numusu2%2
 num3par=numusu3%2

 if num1par!=0 and num2par!=0 and num3par!=0:
    print('Felicidades los 3 numeros son impares; fin del juego  ')
 else: 
    print("Ingrese los numeros de nuevo")
    
 if num1par==0 and num2par==0 and num3par==0:
    print('los 3 numeros son pares ')
 elif num1par==0 and num2par!=0 and num3par!=0:
    print('Solo hay dos numeros impares ingrese de nuevo ')
 elif num1par!=0 and num2par==0 and num3par!=0:
    print( 'Solo hay dos numeros impares ingrese de nuevo ')
 elif num1par!=0 and num2par!=0 and num3par==0:
    print('Solo hay dos numeros impares ingrese de nuevo ')
    break 
 
     

