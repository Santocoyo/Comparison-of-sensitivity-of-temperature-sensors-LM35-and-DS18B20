import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def model(x,Ta,T0,k):
    return Ta+(T0-Ta)*np.exp(-k*x)
def lineal(x,k0, k1):
    return (k0+k1*x)

x=np.linspace(1,220,220)
x1=np.linspace(1,69,69)
x2=np.linspace(69,136,68)
x3=np.linspace(137,204,68)
data=np.genfromtxt("RawData.txt",names=True,delimiter=",",dtype=None)
#---------------------------------------------------------------------------#
plt.figure("DS18B20")
plt.subplot(3,1,1)
valores_inicialesDS18B20_1=[1,1,1]
fitDS18B20_1=curve_fit(model,x1,data["DS18B20"][1:70],p0=valores_inicialesDS18B20_1)
parametrosDS18B20_1, cov_DS18B20_1=fitDS18B20_1
Ta_DS18B20_1, T0_DS18B20_1, k_DS18B20_1 = parametrosDS18B20_1
plt.plot(x1,data["DS18B20"][1:70], "g--o",label="Datos")
promedioDS18B20=np.mean(data["DS18B20"][1:70])
plt.plot(x1,np.linspace(promedioDS18B20,promedioDS18B20,69),"g", label="Modelo")
plt.title("DS18B20")
plt.legend(loc="upper right")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.text(40, 28.625, 'Zona a temperatura ambiente', style='italic')
plt.text(40,28.125,"T$_{promedio}$ = %.1f"%promedioDS18B20)
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
#----------------------------------------------------------------------------#
plt.subplot(3,1,2)
valores_inicialesDS18B20_2 = parametrosDS18B20_1
fitDS18B20_2=curve_fit(model,x2,data["DS18B20"][69:137],p0=valores_inicialesDS18B20_2)
parametrosDS18B20_2, cov_DS18B20_2=fitDS18B20_2
Ta_DS18B20_2, T0_DS18B20_2, k_DS18B20_2 = parametrosDS18B20_2
plt.plot(x2,data["DS18B20"][69:137], "b:D", label="Datos")
plt.plot(x2,model(x2,Ta_DS18B20_2,T0_DS18B20_2, k_DS18B20_2), "b", label="Modelo")
plt.ylabel("Temperatura [°C]")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.text(100, 22.5, 'Zona de enfriamiento', style='italic')
plt.text(100, 12.5, 'T$_{0}$= %.1f'%T0_DS18B20_2)
plt.text(110, 12.5, 'T$_{a}$= %.1f'%Ta_DS18B20_2)
plt.text(120, 12.5, 'k= %.3f'%k_DS18B20_2)
plt.legend(loc="upper right")
#-----------------------------------------------------------------------------#
plt.subplot(3,1,3)
valores_inicialesDS18B20_3 = parametrosDS18B20_2
fitDS18B20_3=curve_fit(model,x2,data["DS18B20"][137:205],p0=valores_inicialesDS18B20_3)
parametrosDS18B20_3, cov_DS18B20_3=fitDS18B20_3
Ta_DS18B20_3, T0_DS18B20_3, k_DS18B20_3 = parametrosDS18B20_3
plt.plot(x3,data["DS18B20"][137:205],"r-.*", label="Datos")
plt.plot(x3,model(x2,Ta_DS18B20_3,T0_DS18B20_3, k_DS18B20_3), "r", label="Modelo")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(loc="lower right")
plt.text(150, 25, 'Zona de calentamiento', style='italic')
plt.text(160, 35, 'T$_{0}$= %.1f'%T0_DS18B20_3)
plt.text(170, 35, 'T$_{a}$= %.1f'%Ta_DS18B20_3)
plt.text(180, 35, 'k= %.3f'%k_DS18B20_3)
#-----------------------------------------------------------------------------#
plt.figure("LM35")
plt.subplot(3,1,1)
promedioLM35=np.mean(data["LM35"][1:70])
plt.plot(x1,data["LM35"][1:70], "g--o",label="Datos")
plt.plot(x1,np.linspace(promedioLM35,promedioLM35,len(x1)), "g",label="Modelo")
plt.xlabel("Tiempo [s]")
plt.legend(loc="upper left")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("LM35")
plt.text(40, 23.825, 'Zona a temperatura ambiente', style='italic')
plt.text(40,24.125,"T$_{promedio}$ = %.1f"%promedioLM35)
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
#-----------------------------------------------------------------------------#
plt.subplot(3,1,2)
valores_inicialesLM35_2=[1,1,0.01]
fitLM35_2=curve_fit(model,x2,data["LM35"][69:137],p0=valores_inicialesLM35_2)
parametrosLM35_2, cov_LM35_2=fitLM35_2
Ta_LM35_2, T0_LM35_2, k_LM35_2 = parametrosLM35_2
plt.plot(x2,data["LM35"][69:137], "b:D", label="Datos")
plt.plot(x2,model(x2,Ta_LM35_2,T0_LM35_2, k_LM35_2),"b",label="Modelo")
plt.ylabel("Temperatura [°C]")
plt.legend(loc="upper right")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.text(110, 18.75, 'Zona de enfriamiento', style='italic')
plt.text(100, 11.25, 'T$_{0}$= %.1f'%T0_LM35_2)
plt.text(110, 11.25, 'T$_{a}$= %.1f'%Ta_LM35_2)
plt.text(120, 11.25, 'k= %.3f'%k_LM35_2)
#-----------------------------------------------------------------------------#
plt.subplot(3,1,3)
valores_inicialesLM35_3=[1,1,0.01]
fitLM35_3=curve_fit(model,x3,data["LM35"][137:205],p0=valores_inicialesLM35_3)
parametrosLM35_3, cov_LM35_3=fitLM35_3
Ta_LM35_3, T0_LM35_3, k_LM35_3 = parametrosLM35_3
plt.plot(x3,data["LM35"][137:205], "r-.*", label="Datos")
plt.plot(x3,model(x3,Ta_LM35_3,T0_LM35_3, k_LM35_3), "r", label="Modelo")
plt.xlabel("Tiempo [s]")
plt.legend(loc="lower right")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.text(170, 22.5, 'Zona de calentamiento', style='italic')
plt.text(160, 32.5, 'T$_{0}$= %.1f'%T0_DS18B20_3)
plt.text(170, 32.5, 'T$_{a}$= %.1f'%Ta_DS18B20_3)
plt.text(180, 32.5, 'k= %.3f'%k_DS18B20_3)
plt.show()
