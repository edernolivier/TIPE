import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configuration des données de la trajectoire
t = np.linspace(0, 2*np.pi, 100)#vitesse de l'astre
x_trajectoire = 5 * np.cos(t) # Demi-grand axe de 5
y_trajectoire = 3 * np.sin(t) # Demi-petit axe de 3
z_trajectoire = 2 * np.sin(t) #essaie d'un axe en 3e dimension

# 2. Initialisation du graphique
fig = plt.figure(figsize=(7, 7))
ax3D = fig.add_subplot(111, projection='3d') # Changement crucial ici

ax3D.set_xlim(-6, 6)
ax3D.set_ylim(-6, 6)
ax3D.set_zlim(-6, 6)

# Dessin du corps central
ax3D.plot([0], [0], [0], 'go', markersize=20, label="Terre")

# Initialisation des objets vides
line, = ax3D.plot([], [], [], 'r--', alpha=0.5)
point, = ax3D.plot([], [], [], 'ko', markersize=8)

# 3. Fonction de mise à jour
def update(frame):
    # Mise à jour X et Y
    line.set_data(x_trajectoire[:frame], y_trajectoire[:frame])
    point.set_data([x_trajectoire[frame]], [y_trajectoire[frame]])
    
    # Mise à jour Z (méthode spécifique à la 3D)
    line.set_3d_properties(z_trajectoire[:frame])
    point.set_3d_properties([z_trajectoire[frame]])
    
    return line, point

# 4. Création de l'animation
# Note: blit=False est souvent plus stable en 3D
ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=False)

plt.title("Simulation de trajectoire spatiale 3D")
plt.legend()
plt.show()