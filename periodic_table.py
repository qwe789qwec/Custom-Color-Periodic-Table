import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define colors for priorities
colors = {
    "Storage": "#2dff00ff", # light red
    "High": "#25d000ff",   # light green
    "Medium": "#167e00ff", # violet
    "Low": "#d3d3d3",    # gray
    "Empty": "white"     # unused cells
}

# Define all elements with position and priority
# Format: (row, col, symbol, priority)
elements = [
    # Row 0
    (0, 0, "H", "Low"), (0, 17, "He", "Low"),
    # Row 1
    (1, 0, "Li", "Low"), (1, 1, "Be", "Low"),
    (1, 12, "B", "Storage"), (1, 13, "C", "High"), (1, 14, "N", "Low"),
    (1, 15, "O", "Low"), (1, 16, "F", "Low"), (1, 17, "Ne", "Low"),
    # Row 2
    (2, 0, "Na", "Low"), (2, 1, "Mg", "Low"),
    (2, 12, "Al", "Storage"), (2, 13, "Si", "Storage"),
    (2, 14, "P", "Low"), (2, 15, "S", "Low"),
    (2, 16, "Cl", "Low"), (2, 17, "Ar", "Low"),
    # Row 3
    (3, 0, "K", "Low"), (3, 1, "Ca", "Low"),
    (3, 2, "Sc", "High"), (3, 3, "Ti", "Storage"), (3, 4, "V", "Storage"),
    (3, 5, "Cr", "High"), (3, 6, "Mn", "High"), (3, 7, "Fe", "High"),
    (3, 8, "Co", "Storage"), (3, 9, "Ni", "High"), (3, 10, "Cu", "High"),
    (3, 11, "Zn", "High"), (3, 12, "Ga", "Low"),
    (3, 13, "Ge", "Storage"), (3, 14, "As", "Low"), (3, 15, "Se", "Low"),
    (3, 16, "Br", "Low"), (3, 17, "Kr", "Low"),
    # Row 4
    (4, 0, "Rb", "Low"), (4, 1, "Sr", "Low"),
    (4, 2, "Y", "High"), (4, 3, "Zr", "High"), (4, 4, "Nb", "Storage"),
    (4, 5, "Mo", "High"), (4, 6, "Tc", "Low"), (4, 7, "Ru", "Medium"),
    (4, 8, "Rh", "Medium"), (4, 9, "Pd", "Medium"), (4, 10, "Ag", "Medium"),
    (4, 11, "Cd", "Low"), (4, 12, "In", "High"), (4, 13, "Sn", "High"),
    (4, 14, "Sb", "Low"), (4, 15, "Te", "Low"), (4, 16, "I", "Low"),
    (4, 17, "Xe", "Low"),
    # Row 5
    (5, 0, "Cs", "Low"), (5, 1, "Ba", "Low"),
    (5, 2, "La", "Low"), (5, 3, "Hf", "Medium"), (5, 4, "Ta", "Storage"),
    (5, 5, "W", "Low"), (5, 6, "Re", "Medium"), (5, 7, "Os", "Medium"),
    (5, 8, "Ir", "Medium"), (5, 9, "Pt", "Medium"), (5, 10, "Au", "Medium"),
    (5, 11, "Hg", "Low"), (5, 12, "Tl", "Low"), (5, 13, "Pb", "High"),
    (5, 14, "Bi", "High"), (5, 15, "Po", "Low"), (5, 16, "At", "Low"),
    (5, 17, "Rn", "Low"),
    # Row 6
    (6, 0, "Fr", "Low"), (6, 1, "Ra", "Low"),
    (6, 2, "Ac", "Low"), (6, 3, "Rf", "Low"), (6, 4, "Db", "Low"),
    (6, 5, "Sg", "Low"), (6, 6, "Bh", "Low"), (6, 7, "Hs", "Low"),
    (6, 8, "Mt", "Low"), (6, 9, "Ds", "Low"), (6, 10, "Rg", "Low"),
    (6, 11, "Cn", "Low"), (6, 12, "Uut", "Low"), (6, 13, "Fl", "Low"),
    (6, 14, "Uup", "Low"), (6, 15, "Lv", "Low"), (6, 16, "Uus", "Low"),
    (6, 17, "Uuo", "Low"),
    # Lanthanides
    (8, 2, "Ce", "Low"), (8, 3, "Pr", "Low"), (8, 4, "Nd", "Low"),
    (8, 5, "Pm", "Low"), (8, 6, "Sm", "Low"), (8, 7, "Eu", "Low"),
    (8, 8, "Gd", "High"), (8, 9, "Tb", "Medium"), (8, 10, "Dy", "High"),
    (8, 11, "Ho", "High"), (8, 12, "Er", "High"), (8, 13, "Tm", "Medium"),
    (8, 14, "Yb", "Low"), (8, 15, "Lu", "Low"),
    # Actinides
    (9, 2, "Th", "Low"), (9, 3, "Pa", "Low"), (9, 4, "U", "Low"),
    (9, 5, "Np", "Low"), (9, 6, "Pu", "Low"), (9, 7, "Am", "Low"),
    (9, 8, "Cm", "Low"), (9, 9, "Bk", "Low"), (9, 10, "Cf", "Low"),
    (9, 11, "Es", "Low"), (9, 12, "Fm", "Low"), (9, 13, "Md", "Low"),
    (9, 14, "No", "Low"), (9, 15, "Lr", "Low")
]

# Create figure
fig, ax = plt.subplots(figsize=(16, 9))

# Draw cells
for row, col, sym, priority in elements:
    x, y = col, -row
    rect = Rectangle((x, y), 1, 1, facecolor=colors[priority], edgecolor="black")
    ax.add_patch(rect)
    ax.text(x+0.5, y+0.5, sym, ha="center", va="center", fontsize=10, weight="bold")

# Adjust plot
ax.set_xlim(-0.5, 18.5)
ax.set_ylim(-10.5, 1.5)
ax.set_aspect("equal")
ax.axis("off")

plt.show()
