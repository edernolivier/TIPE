import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. TRAJECTOIRES RECTILIGNES UNIFORMES ---
t = np.linspace(0, 10, 200) 
x_trajectoire = 5 * t
y_trajectoire = 5 * t
z_trajectoire = (1/2) * t  

t2 = np.linspace(0, 10, 200) 
x2_trajectoire = 4 * t
y2_trajectoire = 6 * t
z2_trajectoire = (1/3) * t  

# --- 2. CONFIGURATION DE LA SCÈNE ---
plt.style.use('dark_background') 
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Uranus (Point bleu, Trace rouge)
point_uranus, = ax.plot([], [], [], 'bo', markersize=8, label='Uranus')
trace_uranus, = ax.plot([], [], [], 'r--', lw=1)

# Satellite (Point cyan, Trace orange)
point_satellite, = ax.plot([], [], [], 'co', markersize=5, label='Satellite') 
trace_satellite, = ax.plot([], [], [], 'orange', linestyle='--', lw=1) 

# Zone de texte pour la distance
texte_distance = ax.text2D(0.05, 0.95, "", transform=ax.transAxes, color='white', fontsize=12)

ax.set_xlim(0, 55)
ax.set_ylim(0, 65)
ax.set_zlim(0, 6)
ax.legend(loc='upper right')

# --- 3. FONCTION DE CALCUL DE DISTANCE ---
def calculer_distance(p1x, p1y, p1z, p2x, p2y, p2z):
    return np.sqrt((p2x - p1x)**2 + (p2y - p1y)**2 + (p2z - p1z)**2)

# --- 4. BOUCLE D'ANIMATION EN DIRECT ---
def mettre_a_jour(frame):
    # Positions actuelles
    u_x, u_y, u_z = x_trajectoire[frame], y_trajectoire[frame], z_trajectoire[frame]
    s_x, s_y, s_z = x2_trajectoire[frame], y2_trajectoire[frame], z2_trajectoire[frame]

    # Mise à jour des points
    point_uranus.set_data([u_x], [u_y])
    point_uranus.set_3d_properties([u_z])
    
    point_satellite.set_data([s_x], [s_y])
    point_satellite.set_3d_properties([s_z])
    
    # Mise à jour des traces
    trace_uranus.set_data(x_trajectoire[:frame], y_trajectoire[:frame])
    trace_uranus.set_3d_properties(z_trajectoire[:frame])
    
    trace_satellite.set_data(x2_trajectoire[:frame], y2_trajectoire[:frame])
    trace_satellite.set_3d_properties(z2_trajectoire[:frame])
    
    # CALCUL DE LA DISTANCE
    dist = calculer_distance(u_x, u_y, u_z, s_x, s_y, s_z)
    
    # Affichage sur le graphique
    texte_distance.set_text(f"Distance : {dist:.2f} km")
    
    # Affichage dans la console (pour être sûr que tu l'aies)
    print(f"Frame {frame} | Distance calculee = {dist:.2f}")
    
    return point_uranus, trace_uranus, point_satellite, trace_satellite

# MODIFICATION ICI : blit=False pour forcer le texte à se mettre à jour
ani = FuncAnimation(fig, mettre_a_jour, frames=200, interval=25, blit=False)

plt.show()