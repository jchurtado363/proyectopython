seleccione=input("selecciones +,-,*,/")
n1=int(input("ingrese primer numero"))

n2=int(input("ingrese segundo numero"))

suma=n1+n2
resta=n1-n2
multiplica=n1*n2
div=n1/n2

if(seleccione=="+"):
    print ("resultado de suma es: "+str(suma))
elif(seleccione=="-"):
   print("resultado de resta es: "+str(resta))    
elif(seleccione=="*"):
   print("resultado de multiplicacion es: "+str(multiplica))
elif(seleccione=="/"):   
   print("resultado de division es: "+str(div))

