def hola(nombre):
    print("hola mundo",nombre)
hola("juan")    


def hola(nombre,num):
    print("hola mundo",nombre,num)
hola("juan",20)  


# 1. calcular los segundo de un tiempo dado (horas,min,seg)
# 2. escribir una funcion que reciba como parametro una frace establecida y la repita un numero n de veces  

# 1. calcular los segundo de un tiempo dado (horas,min,seg)
def tiempo(hora,min,seg):
    resulado=(hora*3600)+(min*60)+(seg)
    print ("el tiempo es ;", resulado, "segundos")
tiempo(2,30,20)    

# 2 FUNCION QUE REPITE N VECES UNA FRACE
def frace(frace1,n):
    repite=frace1*n
    print(repite)
frace("Buenos dias. ",5)


# 3 FUNCION DE TIEMPO EN MINUTOS 
def tiempo2(hora,min,seg):
    resulado=(hora*60)+(min)+(seg/60)
    print ("el tiempo es ;", resulado, "Minutos")
tiempo2(2,0,60)    

# 4 FUNCION PASAR DE SEGUNDOS A HORAS Y MINUTOS 
def tiempo3(segdados):
    horas1=segdados/3600
    min2=segdados/60
    print("El tiempo dado es ",horas1," horas ",min2," minutos")
tiempo3(200360), 

# 5 EJERCICIO NUMEROS PARES ENTRE DOS NUMEROS DADOS 
def numeros3(n1,n2):
    cont=0
    for i in range (n1,n2):
        if (i%2==0):
            cont=cont + 1
            print("Numero par: ",i)
    print("Los numeros pares entre ",n1," y ",n2," total: ",cont), 
numeros3(7,20)

# 6 FUNCION FICHAS DEL DOMIO

def domino (na,nx):

 print("FICHAS DEL DOMINO")
 for i in range(na,nx):
    for j in range (0,i+1):
        print("/"+str(i)+"/"+str(j),end="\n" )

domino(0,7)


        