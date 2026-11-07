"""Right panel: top view of Bhumandala, the disc of the earth."""
import math

from matplotlib.patches import Circle, Patch, Polygon

from data import DARK_R, LOKALOKA_R, RINGS


class TopView:
    def __init__(self, ax):
        self.ax = ax
        ax.set_aspect("equal")
        ax.set_xlim(-272, 272)
        ax.set_ylim(-272, 272)
        ax.axis("off")
        ax.set_title("Top view: Bhumandala, the disc of the earth")

        ax.add_patch(Circle((0, 0), DARK_R, fc="#2C2C2A", ec="none"))
        self.loka = Circle((0, 0), LOKALOKA_R, fc="#888780", ec="#F1EFE8", lw=2, ls=(0, (4, 4)))
        ax.add_patch(self.loka)
        for name, r, color, _ in reversed(RINGS):
            ax.add_patch(Circle((0, 0), r, fc=color, ec="white", lw=0.5, alpha=0.95))
        ax.add_patch(Polygon([(0, 13), (-8, -4), (8, -4)], fc="#B67F12", ec="#7A5200", lw=0.8))

        self.sun, = ax.plot([], [], "o", ms=6, color="#F2A623", mec="#B67F12")
        self.bharata, = ax.plot([0], [-21], "o", ms=5, color="#E24B4A", mec="white", mew=0.6)
        ax.annotate("Mount Meru", xy=(0, 2), xytext=(-268, 252), fontsize=8, color="#444441",
                    arrowprops=dict(arrowstyle="-", color="#888780", lw=0.6))
        ax.annotate("Bharatavarsha", xy=(0, -21), xytext=(120, -266), fontsize=8, color="#444441",
                    arrowprops=dict(arrowstyle="-", color="#888780", lw=0.6))

        handles = [Patch(fc=c, ec="#B4B2A9", label=n) for n, _, c, _ in RINGS]
        handles += [Patch(fc="#888780", label="Lokaloka mountains"), Patch(fc="#2C2C2A", label="Darkness")]
        ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=3,
                  fontsize=7.5, frameon=False, handlelength=1.2, columnspacing=1.2)

    def update(self, t):
        self.loka.set_linestyle((t * 12 % 8, (4, 4)))
        self.sun.set_data([21 * math.cos(1.6 * t)], [21 * math.sin(1.6 * t)])
        self.bharata.set_markersize(4.5 + 2 * math.sin(3 * t))
