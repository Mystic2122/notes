import numpy as np
import matplotlib.pyplot as plt

# Grid for the regions
t = np.linspace(-1.6, 1.6, 801)
X1, X2 = np.meshgrid(t, t)
L1 = np.abs(X1) + np.abs(X2)
L2 = np.sqrt(X1**2 + X2**2)

fig, ax = plt.subplots(figsize=(6, 6))

# Regions: ||x||_2 < 1 and ||x||_2 > 1
ax.contourf(X1, X2, L2, levels=[0, 1], colors=["#a6cee3"], alpha=0.6)
ax.contourf(X1, X2, L2, levels=[1, L2.max()], colors=["#fdbf6f"], alpha=0.45)

# Boundary ||x||_2 = 1
ax.contour(X1, X2, L2, levels=[1], colors="#1f78b4", linewidths=2, linestyles="--")

# Contour ||x||_1 = 1
ax.contour(X1, X2, L1, levels=[1], colors="#e31a1c", linewidths=2.5)

# Intersection points: (±1, 0), (0, ±1)
pts = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
ax.scatter(pts[:, 0], pts[:, 1], s=60, color="black", zorder=5)
for x, y in pts:
    ax.annotate(f"({x}, {y})", (x, y), textcoords="offset points",
                xytext=(8 if x >= 0 else -42, 8 if y >= 0 else -16), fontsize=9)

# Legend via proxy artists
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
handles = [
    Line2D([0], [0], color="#e31a1c", lw=2.5, label=r"$\|x\|_1 = 1$"),
    Line2D([0], [0], color="#1f78b4", lw=2, ls="--", label=r"$\|x\|_2 = 1$"),
    Patch(facecolor="#a6cee3", alpha=0.6, label=r"$\|x\|_2 < 1$"),
    Patch(facecolor="#fdbf6f", alpha=0.45, label=r"$\|x\|_2 > 1$"),
    Line2D([0], [0], marker="o", color="black", lw=0, label="intersections"),
]
ax.legend(handles=handles, loc="upper right", fontsize=9, framealpha=0.95)

ax.axhline(0, color="gray", lw=0.6)
ax.axvline(0, color="gray", lw=0.6)
ax.set_aspect("equal")
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_title(r"Contour $\|x\|_1 = 1$ vs. regions of $\|x\|_2$")

plt.tight_layout()
plt.savefig("l1_l2_contour.pdf")   # for \includegraphics in LaTeX
# plt.savefig("l1_l2_contour.png", dpi=200)