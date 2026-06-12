import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Constantes et paramètres ---
G = 6.6743e-11  # Constante gravitationnelle (m^3 kg^-1 s^-2)
M_planete = 5.972e24  # Masse de la Terre (kg)

# Conditions initiales du satellite (ex: l'altitude de l'ISS environ)
x = 7000000.0  # Position x initiale (mètres)
y = 0.0  # Position y initiale
vx = 0.0  # Vitesse x initiale (m/s)
vy = 7500.0  # Vitesse y initiale (m/s) - vitesse orbitale standard

dt = 10  # Pas de temps pour la simulation (en secondes)

# Listes pour stocker la trajectoire
x_points, y_points = [], []

# --- Configuration de la figure Matplotlib ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1e7, 1e7)
ax.set_ylim(-1e7, 1e7)
ax.set_aspect("equal")
ax.grid(True)

# Dessin de la planète (au centre) et du satellite
planete_plot = ax.plot(0, 0, "bo", markersize=15, label="Planète")[0]
(satellite_plot,) = ax.plot([], [], "ro", markersize=6, label="Satellite")
(trajectoire_plot,) = ax.plot([], [], "r--", alpha=0.5)
ax.legend()


# --- Fonction de mise à jour (Animation) ---
def update(frame):
    global x, y, vx, vy

    # 1. Calcul de la distance r
    r = np.sqrt(x**2 + y**2)

    # 2. Calcul de l'accélération (Loi de Newton)
    ax_grav = -G * M_planete * x / r**3
    ay_grav = -G * M_planete * y / r**3

    # 3. Mise à jour de la vitesse (Méthode d'Euler)
    vx += ax_grav * dt
    vy += ay_grav * dt

    # 4. Mise à jour de la position
    x += vx * dt
    y += vy * dt

    # Stockage de la trajectoire
    x_points.append(x)
    y_points.append(y)

    # Mise à jour du graphique
    satellite_plot.set_data([x], [y])
    trajectoire_plot.set_data(x_points, y_points)

    return satellite_plot, trajectoire_plot
# Lancement de l'animation
ani = FuncAnimation(fig, update, frames=2000, interval=10, blit=True)
plt.show()