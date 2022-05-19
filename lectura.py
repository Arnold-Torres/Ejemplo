# Lectura de los archivos txt
#
#	ES NECESARIO TENER LOS ARCIVOS GENERADOS POR 
#	INVERTER5.CIR EN EL MISMO DIRECTORIO QUE ESTE CODIGO
#

import matplotlib
import matplotlib.pyplot as plt

tp_98 = open("tp_20_120_98.txt","r")

datos = []
for linea in tp_98:
	datos.append(linea)
#	print(linea)

#print(datos[2])

temp = []
tpLH = []
tpHL = []
for i in range(1,len(datos)):
	dat = datos[i] 
	t = []
	for word in dat.split():
		t.append(word)
		print(word)
	temp.append(t[0])
	tpLH.append(t[1])
	tpHL.append(t[2])

print(temp)
	
fig, ax = plt.subplots(2, 1, sharex=True)
fig.suptitle('Tiempo de propagacion')
ax[0].plot(temp, tpLH, label='tpLH')
ax[1].plot(temp, tpHL, label='tpHL')
ax[1].set_xlabel('Temperatura [°C]')
ax[0].set_xticks([0,10,20,30,40,50,60,70])
ax[1].set_ylabel('Tiempo [s]')
ax[0].set_yticks([0,18,36,54,70])
ax[1].set_yticks([0,18,36,54,70])
ax[0].legend(loc = 'upper left')
ax[1].legend(loc = 'upper left')
ax[0].grid(axis = 'y', color = 'gray', linestyle = 'dashed')
ax[1].grid(axis = 'y', color = 'gray', linestyle = 'dashed')
plt.show()
print(tpHL)
