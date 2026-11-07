"""
Animated map of the Hindu cosmos (common Puranic model).

Left  : side view - the Brahmanda (cosmic egg) with its 14 worlds, Mount Meru,
        sun and moon circling, twinkling stars and gems, flickering flames in
        Naraka, and Shesha swaying beneath everything.
Right : top view  - Bhumandala, the disc of the earth: Jambudvipa in the centre,
        then alternating continents and oceans out to the Lokaloka mountains.

Controls (window mode)
    n key / "Night of Brahma" button : fade the three lower worlds (Bhur, Bhuvar, Svar)
    click any layer or ring           : read about it at the bottom left

Run:   python hindu_cosmos.py
Save:  python hindu_cosmos.py --gif cosmos.gif      (needs pillow)
       python hindu_cosmos.py --png cosmos.png
"""
import argparse
import itertools

parser = argparse.ArgumentParser(description="Animated map of the Hindu cosmos")
parser.add_argument("--gif", metavar="FILE", help="save an animated GIF instead of opening a window")
parser.add_argument("--png", metavar="FILE", help="save a still image instead of opening a window")
args = parser.parse_args()

# The backend must be chosen before pyplot is imported.
import matplotlib

if args.gif or args.png:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from controls import Controls
from side_view import SideView
from top_view import TopView

GIF_FRAMES, FPS = 240, 20

fig = plt.figure(figsize=(15, 9.5))
fig.subplots_adjust(left=0.01, right=0.99, top=0.93, bottom=0.2, wspace=0.02)
side = SideView(fig.add_subplot(1, 2, 1))
top = TopView(fig.add_subplot(1, 2, 2))
controls = Controls(fig, side, top, auto=bool(args.gif))


def update(frame):
    t = frame / FPS
    state = controls.state
    if state["auto"]:
        state["target"] = 1.0 if 90 <= frame % GIF_FRAMES < 170 else 0.0
    n = state["night"]
    n += max(-0.05, min(0.05, state["target"] - n))
    state["night"] = n
    side.update(t, 1 - 0.92 * n, n)
    top.update(t)
    return []


if args.png:
    update(60)
    fig.savefig(args.png, dpi=130)
    print(f"Saved {args.png}")
elif args.gif:
    anim = FuncAnimation(fig, update, frames=GIF_FRAMES, interval=1000 / FPS)
    anim.save(args.gif, writer=PillowWriter(fps=FPS), dpi=70)
    print(f"Saved {args.gif}")
else:
    anim = FuncAnimation(fig, update, frames=itertools.count(), interval=1000 / FPS, cache_frame_data=False)
    plt.show()
