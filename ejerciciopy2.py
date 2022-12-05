nmclave=int(input('ingrese el numero de referencia:'))
#el numero feliz es 30
for i in range (0,nmclave):
    nmpensado=int(input('ingree el numero que piensa como ganador'))
    if nmpensado==30:
     print('EL NUMERO ES CORRECTO: '+str (nmpensado))
     
    else:
        print('INTENTELO DE NUEVO')

    if nmpensado<30:
        print('EL NUMERO DE GANADOR ES DE MAYOR VALOR')  
    if nmpensado>30:
        print('EL NUMERO DE GANADOR ES DE MENOR VALOR')      
    if nmpensado==30:
        print('NUMERO CORRECTO, FIN DE JUEGO.')
        break