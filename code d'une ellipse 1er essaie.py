import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Création de la figure et des axes
fig, ax = plt.subplots()

# Définition de l'ellipse
# xy : centre (x, y)
# width : largeur totale (diamètre horizontal)
# height : hauteur totale (diamètre vertical)
# angle : rotation en degrés (sens anti-horaire)
ellipse = Ellipse(xy=(5, 5), width=8, height=4, angle=30, 
                  edgecolor='blue', facecolor='white', lw=2)

# Ajout de l'ellipse au graphique
ax.add_patch(ellipse)

# Configuration de l'affichage
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal') # Important pour ne pas déformer l'ellipse
plt.title("Ellipse avec Matplotlib")
plt.show()

