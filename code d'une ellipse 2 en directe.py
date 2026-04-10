import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Configuration des données de la trajectoire
t = np.linspace(0, 2*np.pi, 100)#vitesse de l'astre
x_trajectoire = 5 * np.cos(t) # Demi-grand axe de 5
y_trajectoire = 3 * np.sin(t) # Demi-petit axe de 3

# 2. Initialisation du graphique
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')

# Dessin du corps central (Terre) et de la ligne de trajectoire (vide au début)
plt.plot(0, 0, 'go', markersize=20, label="Terre") # Centre
line, = ax.plot([], [], 'r--', alpha=0.5)         # Trajectoire passée
point, = ax.plot([], [], 'ko', markersize=8)      # Satellite

# 3. Fonction de mise à jour (appelée à chaque image)
def update(frame):
    # On affiche la trajectoire jusqu'à l'image actuelle
    line.set_data(x_trajectoire[:frame], y_trajectoire[:frame])
    # On affiche la position actuelle du satellite
    point.set_data([x_trajectoire[frame]], [y_trajectoire[frame]])
    return line, point

# 4. Création de l'animation
# frames : nombre d'étapes, interval : temps entre images en millisecondes
ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

plt.title("Simulation de trajectoire spatiale")
plt.legend()
plt.show()