numero=int(input("Ingrese un numero de casos: "))
aux=1
while aux<=numero:
    x=float(input("Ingrese el costo del pasaje sin tarjeta: "))
    y=float(input("Ingrese el costo del pasaje con tarjeta: "))
    a=float(input("Ingrese el costo de la tarjeta: "))
    b=float(input("Ingrese la carga inicial de la tarjeta: "))
    if a>b :
        contador=0
        aux2=0
        resto=x-y
        while(b>0):
            b=b-y
            aux2=aux2+resto
            contador+=1
        if aux2>=a:
            if b!=0:
               contador-=1 
            semanas=contador//5
            contador=contador//2
            dias=contador%5
            print("%d semanas %d días" % (semanas,dias))
        else:
           print("No se recupera")
    aux+=1