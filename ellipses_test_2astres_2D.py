import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 2*np.pi, 250)#vitesse de l'astre
x_trajectoire = 6 * np.cos(t) # Demi-grand axe de 5
y_trajectoire = 3 * np.sin(t) # Demi-petit axe de 3

t2 = np.linspace(0, 2*np.pi, 250)#vitesse de l'astre
x_trajectoire2 = 7 * np.cos(t2) # Demi-grand axe de 5
y_trajectoire2 = 4 * np.sin(t2) # Demi-petit axe de 3

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

plt.plot(0, 0, 'go', markersize=20, label="Terre") # Centre
line, = ax.plot([], [], 'r-', alpha=0.5)         # Trajectoire passée
point, = ax.plot([], [], 'ko', markersize=8)      # Satellite
line2, = ax.plot([], [], 'r-', alpha=0.5)         # Trajectoire passée
point2, = ax.plot([], [], 'ko', markersize=8)      # Satellite


def update(frame):
    # On affiche la trajectoire jusqu'à l'image actuelle
    line.set_data(x_trajectoire[:frame], y_trajectoire[:frame])
    # On affiche la position actuelle du satellite
    point.set_data([x_trajectoire[frame]], [y_trajectoire[frame]])
    # On affiche la trajectoire jusqu'à l'image actuelle
    line2.set_data(x_trajectoire2[:frame], y_trajectoire2[:frame])
    # On affiche la position actuelle du satellite
    point2.set_data([x_trajectoire2[frame]], [y_trajectoire2[frame]])
    return line, point, line2, point2


# 4. Création de l'animation
# frames : nombre d'étapes, interval : temps entre images en millisecondes
ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)
ani2 = FuncAnimation(fig, update, frames=len(t2), interval=30, blit=True)

plt.title("Simulation de trajectoire spatiale")
plt.legend()
plt.show()