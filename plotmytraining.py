#!/bin/python

def makeittupla(l):
    tupla=tuple()
    if "x" in l:
        if(l): # Pythonic way of saying not empty string
            if l != "\n":
                t=l.strip(",")
                tupla=(t) # This is very interesting makes the string a tuple, without splitting its elements
                return tupla
    return (-1) # If we arrive here is because the string was empty
def main():

    rutina=[]
    subrutina=[]
    valores=[]
    minutes=[]
    bpm=[]
    cadence=[]
    auxiliar1=[]
    auxiliar2 = []
    file=input("Name of the file:")
    try:
        with open(file,'r') as file_object:
         for l in file_object:
             tupla=makeittupla(l.rstrip("\n"))
             if(tupla!=-1):
                 rutina.append(tupla)
    except IOError as e:
        print (e)
    except e as i:
        print(i)
    for element in rutina:
        cadena=str(element)
        subrutina=cadena.split('x')
        for x in subrutina:
            valores.append(x)


    for i in range(1, len(valores), 3):
        auxiliar1.append(i)
    for i in range(2, len(valores), 3):
        auxiliar2.append(i)
    print(auxiliar1)
    for (pos,j) in enumerate(valores): #enumerate very useful
        if (pos in auxiliar1):
            bpm.append(valores[pos])
        if (pos in auxiliar2):
            cadence.append(valores[pos])
        if(pos%3==0):
            minutes.append(valores[pos])
    minutes=list(map(int,minutes))
    print("Imprimiendo minutos")
    print(minutes)
    print("Total minutos:")
    total_minutes=sum(minutes)
    print(total_minutes)
    print("imprimiendo bpm")
    for y in bpm:
        print(y)

    print("imprimiendo cadence")
    for y in cadence:
        print(y)


if __name__ =="__main__":
    main()
