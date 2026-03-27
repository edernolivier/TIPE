import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

G = 6.67e-11 ### Constante de gravitation

# PARAMETRES D'URANUS
M_u = 8.681e25 ## Masse d'Uranus (en kg)
R_u = 25362e3  ### Rayon d'Uranus (en m)

#PARAMETRES DE TITANIA
M_t = 34.2e20 ## Masse de Titania(en kg)
R_t = 461.8e3  ### Rayon de Titania (en m)

K_u=G*M_u
K_t=G*M_t

### ED d'Uranus
def centrale_uranus(Y_u,t):
    x_u = Y_u[0]
    y_u = Y_u[1]
    vx_u = Y_u[2]
    vy_u = Y_u[3]
    r_u = np.sqrt(x_u**2+y_u**2)
    ax_u = -K_u*r_u**(-3)*x_u #PFD
    ay_u = -K_u*r_u**(-3)*y_u
    
    return([vx_u,vy_u,ax_u,ay_u])

### ED de Titania
def centrale_titania(Y_t,t):
    x_t = Y_t[0]
    y_t = Y_t[1]
    vx_t = Y_t[2]
    vy_t = Y_t[3]
    r_t = np.sqrt(x_t**2+y_t**2)
    ax_t = -K_t*r_t**(-3)*x_t #PFD
    ay_t = -K_t*r_t**(-3)*y_t

    return([vx_t,vy_t,ax_t,ay_t])

### Paramètres de la simulation

Tmax= 12536*1000 ### Temps de la simulation en secondes: temps de 12536000 minutes, 1000 fois la période de la sonde)
N = 100000
t = np.linspace(0,Tmax,N)

### Condition initiale 1
Ru= 218400e3  ### Distance initiale de la sonde
vu= 6000    ### Vitesse orthoradiale initiale du système en m/s (test)
Yu = [Ru,0,0,vu]

### Condition initiale 2
Rt= 218400e3   ### Distance initiale du système en m (test)
vt= 1    ### Vitesse orthoradiale initiale du système en m/s (test)
Yt = [Rt,0,0,vt]

###Résolution
Y_u = odeint(centrale_uranus,Yu,t)
Y_t = odeint(centrale_titania,Yt,t)


###-----------------Plot-----------------###

fig,ax = plt.subplots()

#trajectoire de miranda
theta = np.linspace(0, 2*np.pi, 100) #epaisseur,rayon,nb de pts du cercle
r_mi = 154.9e3 #Distance Uranus-Miranda
x1 = r_mi*np.cos(theta)
x2 = r_mi*np.sin(theta)
ax.plot(x1, x2,color='grey')

#trajectoire d'ariel
theta = np.linspace(0, 2*np.pi, 100) #epaisseur,rayon,nb de pts du cercle
r_ar = 215e3 #Distance Uranus-Ariel
x1 = r_ar*np.cos(theta)
x2 = r_ar*np.sin(theta)
ax.plot(x1, x2,color='orange')

#trajectoire d'umbriel
theta = np.linspace(0, 2*np.pi, 100) #epaisseur,rayon,nb de pts du cercle
r_um = 291e3 #Distance Uranus-Umbriel
x1 = r_um*np.cos(theta)
x2 = r_um*np.sin(theta)
ax.plot(x1, x2,color='green')

#trajectoire de titania
theta = np.linspace(0, 2*np.pi, 100) #epaisseur,rayon,nb de pts du cercle
r_ti = 461.8e3 #Distance Uranus-Titania
x1 = r_ti*np.cos(theta)
x2 = r_ti*np.sin(theta)
ax.plot(x1, x2,color='blue')

#trajectoire d'obéron
theta = np.linspace(0, 2*np.pi, 100) #epaisseur,rayon,nb de pts du cercle
r_ob = 609e3 #Distance Uranus-Obéron
x1 = r_ob*np.cos(theta)
x2 = r_ob*np.sin(theta)
ax.plot(x1, x2,color='purple')



plt.plot(Y_u[:,0]*1e-3,Y_u[:,1]*1e-3,'pink')   #trajectoire de la sonde autour d'Uranus
plt.plot(Y_t[:,0]*1e-3,Y_t[:,1]*1e-3,'r-')     #trajectoire du satellite autour de titania
ax.set_aspect('equal')
plt.xlabel('x (en km)',fontsize=16)
plt.ylabel('y (en km)',fontsize=16)

#inutile ?
#xu=Y_u[:,0]*1e-2
#yu=Y_u[:,1]*1e-2
#min=np.min([np.min(xu),np.min(yu)])
#max=np.max([np.max(xu),np.max(yu)])
#plt.xlim(min,max)
#plt.ylim(min,max)

draw_uranus = plt.Circle((0,0), 25362,color='lightblue')   #modelisation Uranus
draw_miranda = plt.Circle((154.9e3,0), 235.8,color='grey') #modelisation Miranda
draw_ariel = plt.Circle((215e3,0), 581,color='orange')     #modelisation Ariel
draw_umbriel = plt.Circle((291e3,0), 600,color='green')    #modelisation Umbriel
draw_titania = plt.Circle((-461.8e3,0), 789,color='blue')  #modelisation Titania
draw_oberon = plt.Circle((609e3,0), 761,color='purple')    #modelisation Obéron

ax.set_aspect(1)
ax.add_artist(draw_uranus)
ax.add_artist(draw_miranda)
ax.add_artist(draw_ariel)
ax.add_artist(draw_umbriel)
ax.add_artist(draw_titania)
ax.add_artist(draw_oberon)

plt.grid()
plt.show()
