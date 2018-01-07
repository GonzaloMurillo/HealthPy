 #!/usr/local/lib/python2.7/python
import matplotlib.pyplot as plt
import numpy as np
import os

""" This function clears the screen """

def clear_screen():
    os.system("clear")


""" This funcion makes a tuple from a string. In this case the string is a line read from the file """

def makeittupla(l):
    tupla=tuple()
    if ("X" in l):
        if(l): # Pythonic way of saying not empty string
            tupla=(l) # This is very interesting makes the string a tuple, without splitting its elements
            return tupla
    return (-1) # If we arrive here is because the string was empty

""" Draw the grid and the titles"""
def draw_grid_and_titles(total_minutes):
    plt.grid(True)
    plt.xlabel('MINUTES')
    plt.xlim(1, total_minutes)
    plt.ylabel('BPM')
    plt.title('Training Routine\nZones based in Karvonen Formula')

""" Draw the cardio zones """
def draw_cardio_zones(Z1,Z2,Z3,Z4,Z5,total_minutes):

    plt.axhspan(Z4[1], Z5[1], facecolor='r', alpha=0.5, zorder=0,label="Z5 Maximum")
    plt.axhspan(Z3[1], Z4[1], facecolor='y', alpha=0.5, zorder=0, label="Z4 Anaerobic")
    plt.axhspan(Z2[1], Z3[1], facecolor='g', alpha=0.5, zorder=0, label="Z3 Aerobic")
    plt.axhspan(Z1[1], Z2[1], facecolor='b', alpha=0.5, zorder=0, label="Z2 Burn fat")
    plt.axhspan(Z1[0], Z1[1], facecolor='c', alpha=0.5, zorder=0, label="Z1 Recovery")
    #plt.axhspan(0, Z1[0], facecolor='c', alpha=0.5, zorder=0, label="Z1 Recovery")

    texto1 = "Z1=%d-%d bpm" % (int(Z1[0]), int(Z1[1]))+" (50-60%) FCM"
    texto2 = "Z2=%d-%d bpm" % (int(Z2[0]), int(Z2[1]))+" (60-70%) FCM"
    texto3 = "Z3=%d-%d bpm" % (int(Z3[0]), int(Z3[1]))+" (70-80%) FCM"
    texto4 = "Z4=%d-%d bpm" % (int(Z4[0]), int(Z4[1]))+" (80-90%) FCM"
    texto5 = "Z5=%d-%d bpm" % (int(Z5[0]), int(Z5[1]))+" (90-100%) FCM"
    plt.text(50 - len(texto1), Z1[0] + 5, texto1, size="large", alpha=1)
    plt.text(50 - len(texto2), Z2[0] + 5, texto2, size="large", alpha=1)
    plt.text(50 - len(texto3), Z3[0] + 5, texto3, size="large", alpha=1)
    plt.text(50 - len(texto4), Z4[0] + 5, texto4, size="large", alpha=1)
    plt.text(50 - len(texto5)+1, Z5[0] + 5, texto5, size="large", alpha=1)


""" This function plots the lines in the graph"""
def plot_graph(x,y,total_minutes,plt,MaxBPM,AllChanges,coordinates_to_plot):
    plt.plot(x, color="blue", linewidth=2.5, linestyle="-", label="BPM", zorder=2)
    plt.plot(y, color="red", linewidth=2.5, linestyle=":", label="Cadence",zorder=3)

    plt.legend(loc='upper left', frameon=False)
    plt.xticks(np.arange(0, total_minutes, 5))  # Prints the x axe with intervals of 5
    plt.yticks(np.arange(0, MaxBPM, 5))  # Prints the y axe with intervals of 5
    x = total_minutes - 5
    y = 50;
    for (pos, item) in enumerate(AllChanges):
        y = y - 5
        if (int(item) < len(coordinates_to_plot)):
            text = "Change in minute " + str(item) + " to " + str(
                coordinates_to_plot[int(item)]) + " bpm " + "from " + str(coordinates_to_plot[int(item) - 1])
            plt.text(total_minutes/2, y, text, ha="center",size="medium", alpha=1)

""" This function calculates the heart zones based in Karvonen formula"""

def calc_zones_karvonen():
    clear_screen()
    MaxBPM = raw_input("What is your maximum bpm rate?")
    BPMRest=raw_input("What is your resting heart rate?")
    Age=raw_input("What is your age?")
    BPMRest=int(BPMRest)
    MaxBPM=int(MaxBPM)
    Age=int(Age)
    Z1=Z2=Z3=Z4=Z5=()
    Z1Low=Z1High=Z2Low=Z2High=Z3Low=Z3High=Z4Low=Z4High=Z5Low=Z5High=0
    Z1Low=((MaxBPM-BPMRest)*0.5)+BPMRest
    Z1High=((MaxBPM-BPMRest)*0.6)+BPMRest
    Z1=(Z1Low,Z1High)
    Z2Low = ((MaxBPM - BPMRest) * 0.6) + BPMRest
    Z2High = ((MaxBPM - BPMRest) * 0.7) + BPMRest
    Z2 = (Z2Low, Z2High)
    Z3Low = ((MaxBPM - BPMRest) * 0.7) + BPMRest
    Z3High = ((MaxBPM - BPMRest) * 0.8) + BPMRest
    Z3 = (Z3Low, Z3High)
    Z4Low = ((MaxBPM - BPMRest) * 0.8) + BPMRest
    Z4High = ((MaxBPM - BPMRest) * 0.9) + BPMRest
    Z4 = (Z4Low, Z4High)
    Z5Low = ((MaxBPM - BPMRest) * 0.9) + BPMRest
    Z5High = ((MaxBPM - BPMRest) * 1) + BPMRest
    Z5 = (Z5Low, Z5High)
    return (MaxBPM,Z1,Z2,Z3,Z4,Z5)

""" Main function """
def main():

    rutina=[]
    subrutina=[]
    valores=[]
    minutes=[]
    bpm=[]
    cadena=""
    auxiliar1=[]
    auxiliar2=[]
    auxiliar3=[]
    cadence=[]
    coordinates_to_plot=[]
    clear_screen()
    MaxBPM,Z1,Z2,Z3,Z4,Z5=calc_zones_karvonen()

    file=raw_input("Name of the file:")
    try:
        with open(file,'r') as file_object:
         for l in file_object:
             l=l.upper() # We make it uppercase to avoid problems between 'x' and 'X' as delimiter
             tupla=makeittupla(l.rstrip("\n"))
             if(tupla!=-1):
                 rutina.append(tupla)
    except IOError as e:
        print (e)
    except e as i:
        print(i)


    """ rutina is a list of the tuples in the file, subrutina is a list with all of the elements of each rutina"""
    for element in rutina:
        cadena=str(element)
        subrutina=cadena.split('X')
        for x in subrutina:
            valores.append(x) # valores contains all the independen values.

    for i in range(1, len(valores), 3):
        auxiliar1.append(i)
    for i in range(2, len(valores), 3):
        auxiliar2.append(i)

    for i in range(0, len(valores), 3):
        auxiliar3.append(i)


    Change=()
    AllChanges=[]
    PassedMinutes=int(valores[0])
    """ We calculate the change of intervals"""
    for (pos,k) in enumerate(valores):
        if (pos in auxiliar3):
              if(pos==0):
                  Change=(int(PassedMinutes))
              if(pos!=0):
                PassedMinutes=PassedMinutes+int(k)
                Change = (int(PassedMinutes))
              AllChanges.append(Change)
    print("Were the interval changes:")
    print(AllChanges)
    for (pos,j) in enumerate(valores): #enumerate very useful
        if (pos in auxiliar1): # This is a trick just to extract the bpm
            bpm.append(valores[pos])
        if (pos in auxiliar2): # This is a trick just to extract the cadence
            cadence.append(valores[pos])
        if(pos%3==0): # This is a trick just to extract the minutes
            minutes.append(valores[pos])
    bpm=list(map(int,bpm))
    minutes=list(map(int,minutes)) # Converting a list into integers
    cadence=list(map(int,cadence))

    total_minutes=sum(minutes)


    for (pos,m) in enumerate(minutes):

        for iterator in range(m):
            current=(bpm[pos],cadence[pos])
            coordinates_to_plot.append(current)

    print(coordinates_to_plot)
    xy=[]
    x=[]
    y=[]
    for (pas,parcoordenadas) in enumerate(coordinates_to_plot):
        x.append(parcoordenadas[0])
        y.append(parcoordenadas[1])

    draw_grid_and_titles(total_minutes)
    draw_cardio_zones(Z1, Z2, Z3, Z4, Z5,total_minutes)
    plot_graph(x,y,total_minutes,plt,MaxBPM,AllChanges,coordinates_to_plot)


    """ Annotations
    for item in AllChanges:
        print("t")
        print(item)
        AnnotationText="Minute %s" %(item)
        #plt.annotate("cambio",xy=(25,130),xytext=(3, 1.5),arro180wprops=dict(facecolor='black', shrink=0.05),)
        plt.annotate('local max', xy=(int(item), 150), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.01),)
    """



    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
    plt.show()
if __name__ == "__main__":
    main()
