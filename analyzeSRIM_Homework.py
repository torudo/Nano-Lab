"""Programm analyses SRIM simulations and plots the results """
import os,sys, csv
import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

# input in nm
def enviroment(streuoxid=20,BOX =140, SIO=85, NO=2 ):
    #change unit to angstrom (10^-10)
    streuoxid*=10
    BOX*=10
    SIO*=10
    NO *=10
    # Defines the Substrate and Layers
    #ax.axvspan(0, streuoxid, alpha=0.5, edgecolor='pink',facecolor= 'None',hatch='\\')
    ax.axvspan(0,NO, alpha=0.5, color='pink',hatch='////',label='NO') #,facecolor= 'None',edgecolor='pink'
    ax.axvspan(NO,NO+SIO, alpha=0.5, edgecolor='grey',
                    facecolor= 'None',hatch='/',label='SOI')
    ax.axvspan(NO+SIO,NO+SIO+BOX, alpha=0.5, edgecolor='blue',
                    facecolor= 'None',hatch='///',label='BOX')
    ax.axvspan(NO+SIO+BOX,4000, alpha=0.5, edgecolor='green',
                    facecolor= 'None',hatch='//', fill =False,label='Substrat')
# reads SRIM file and just quickly pprints parameters
def get_data_and_plot(path, dir):
    N = 10e20 #cm^-3
    filename = path+ dir +r"\RANGE.txt"
    deph, ions, distirb  = np.genfromtxt(filename,usecols=(0,1,2), comments="#",  unpack="True", dtype=float, skip_header = 48)# delimiter='   '' )
    plt.plot(deph,ions, ".", label=dir[1:])
    #print("For a dopand concentration of {0:1.0e} we get Atoms {1:6.0f} with a energy E = {2}".format(N,max(ions),dir[4:]) )
    #print("Dosos: {:e}".format(N/max(ions))  )
    #print(N/ions[0],"\t",N/max(ions),"\t")
    print("{0}\t{1}\t{2}\t{3:2.3e}\t{4:2.3e}\t".format(dir[4:],ions[0],max(ions),N/ions[0],N/max(ions)))

# Main
fig, ax = plt.subplots()
#substrat,topSI,BOX = 0,0,0
enviroment()
path = sys.path[0]+r"\Sample 140x85x2nm/"
print("E \t A first \t A max \t D first \t D max")
dir = r"\Ph 1keV"
get_data_and_plot(path,dir)
dir = r"\Ph 1.5keV"
get_data_and_plot(path,dir)
dir = r"\Ph 2keV"
get_data_and_plot(path,dir)
dir = r"\Ph 2.5keV"
get_data_and_plot(path,dir)
dir = r"\Ph 5keV"
get_data_and_plot(path,dir)
dir = r"\Ph 10keV"
get_data_and_plot(path,dir)
dir = r"\Ph 20keV"
get_data_and_plot(path,dir)
dir = r"\Ph 30keV"
get_data_and_plot(path,dir)
dir = r"\Ph 40keV"
get_data_and_plot(path,dir)

# Plot
plt.xlim(0, 3200)
ax.xaxis.set_minor_locator(AutoMinorLocator())
plt.yscale('log')
plt.xlabel(r"$Depth\, /\, Ang. $")
plt.ylabel(r"PH / $(atoms/cm^3)\, /\, (atoms/cm^2) $")
plt.title("2nm NO (SiO2), 85nm SOI (Si), 140nm BOX (SiO2), 675um Si-Substrat")
plt.legend()

#plt.savefig('all.pdf', bbox_inches='tight')
#plt.savefig('all_last.png', bbox_inches='tight')

#plt.savefig('spare.pdf', bbox_inches='tight')
#plt.savefig('spare_last.png', bbox_inches='tight')

#plt.xlim(0,1500)
#plt.savefig('only_first_last.png', bbox_inches='tight')

#plt.show()
