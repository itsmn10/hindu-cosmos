"""Left panel: side view of the Brahmanda (cosmic egg) with its 14 worlds."""
import math

import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle

from data import CX, CY, EH, EW, LAYERS, TOP

rng = np.random.default_rng(7)


class Twinkle:
    """A group of small points whose brightness pulses."""

    def __init__(self, ax, egg, xs, ys, color, size, group):
        self.sc = ax.scatter(xs, ys, s=size, c=[color] * len(xs), zorder=8, linewidths=0)
        self.sc.set_clip_path(egg)
        self.base = np.array(to_rgb(color))
        self.phase = rng.uniform(0, 6.28, len(xs))
        self.group = group

    def update(self, t, level):
        a = 0.3 + 0.7 * (0.5 + 0.5 * np.sin(t * 2.2 + self.phase))
        if self.group == "tri":
            a = a * level
        self.sc.set_facecolors(np.column_stack([np.tile(self.base, (len(a), 1)), a]))


def edge_x(y):
    """Right edge of the egg at height y."""
    d = (y - CY) / (EH / 2)
    return CX + (EW / 2) * math.sqrt(max(0.0, 1 - d * d))


class SideView:
    def __init__(self, ax):
        self.ax = ax
        ax.set_xlim(0, 125)
        ax.set_ylim(-3, 111)
        ax.axis("off")

        self.egg = Ellipse((CX, CY), EW, EH, fc="white", ec="none", zorder=0)
        ax.add_patch(self.egg)
        self.fade = []  # (artist, base alpha): things that fade in the night of Brahma

        self.rows = {}
        y = TOP
        for name, sub, h, color, grp in LAYERS:
            self.rows[name] = dict(name=name, sub=sub, y0=y - h, y1=y, h=h, color=color, grp=grp)
            y -= h

        self._bands()
        self._earth()
        self._meru_and_clouds()
        self._sun_moon()
        self._twinkles()
        self._lotus()
        self._flames()
        self._shesha()
        self._outline_and_beyond()
        self._labels()

    # ---- building blocks --------------------------------------------------
    def _add_band(self, row, color=None, y0=None, h=None):
        r = Rectangle((0, y0 if y0 is not None else row["y0"]), 100, h if h is not None else row["h"],
                      fc=color or row["color"], ec="white", lw=0.5, zorder=1)
        self.ax.add_patch(r)
        r.set_clip_path(self.egg)
        if row["grp"] == "tri":
            self.fade.append((r, 1.0))
        return r

    def _bands(self):
        for row in self.rows.values():
            self._add_band(row)

    def _earth(self):
        """Bhurloka: ground, then the strip of continents and oceans."""
        bhur = self.rows["Bhurloka"]
        ground_h = bhur["h"] * 0.42
        self._add_band(bhur, "#B8946A", bhur["y0"], ground_h)
        self.y_surface = bhur["y0"] + ground_h
        strip = [(8, "#9FD8E8"), (9, "#7FB069"), (6, "#F4F0E6"), (8, "#5C9E5C"), (5, "#85B7EB"), (14, "#E9B949"),
                 (5, "#85B7EB"), (8, "#5C9E5C"), (6, "#F4F0E6"), (9, "#7FB069"), (8, "#9FD8E8")]
        scale, x = EW / sum(w for w, _ in strip), CX - EW / 2
        for w, c in strip:
            seg = Rectangle((x, self.y_surface), w * scale, 1.5, fc=c, ec="none", zorder=2)
            self.ax.add_patch(seg)
            seg.set_clip_path(self.egg)
            self.fade.append((seg, 1.0))
            x += w * scale

    def _meru_and_clouds(self):
        """Mount Meru, Indra's city Amaravati, and clouds drifting in Svarloka."""
        svar = self.rows["Svarloka"]
        peak = svar["y1"] - 2.2
        meru = Polygon([(46.5, self.y_surface), (53.5, self.y_surface), (57, peak), (43, peak)],
                       fc="#E2A92B", ec="#B67F12", lw=1, zorder=3)
        city = Rectangle((44.2, peak), 11.6, 1.5, fc="#F5D47A", ec="#B67F12", lw=0.8, zorder=3)
        for art in (meru, city):
            self.ax.add_patch(art)
            self.fade.append((art, 1.0))

        self.clouds = []
        for bx, by in [(24, svar["y0"] + 7), (72, svar["y0"] + 3.2), (30, svar["y0"] + 2.2)]:
            for dx, dy, w, h in [(0, 0, 7, 2.2), (2.2, 0.9, 4.6, 2.0)]:
                e = Ellipse((bx + dx, by + dy), w, h, fc="white", ec="none", zorder=4)
                self.ax.add_patch(e)
                e.set_clip_path(self.egg)
                self.clouds.append((e, bx + dx))
                self.fade.append((e, 0.9))

    def _sun_moon(self):
        bh = self.rows["Bhuvarloka"]
        self.orbit_cy = (bh["y0"] + bh["y1"]) / 2
        self.sun = self.ax.plot([], [], "o", ms=11, color="#F2A623", mec="#B67F12", zorder=9)[0]
        self.moon = self.ax.plot([], [], "o", ms=9, color="#F1EFE8", mec="#888780", zorder=9)[0]
        self.fade += [(self.sun, 1.0), (self.moon, 1.0)]

    def _rand_in(self, row, n, x0=22, x1=78):
        return rng.uniform(x0, x1, n), rng.uniform(row["y0"] + 0.8, row["y1"] - 0.8, n)

    def _twinkles(self):
        bh = self.rows["Bhuvarloka"]
        self.twinkles = [Twinkle(self.ax, self.egg, *self._rand_in(bh, 14), "#C98A12", 14, "tri")]
        for nm in ("Tapoloka", "Janaloka", "Maharloka"):
            self.twinkles.append(Twinkle(self.ax, self.egg, *self._rand_in(self.rows[nm], 5, 32, 68), "#854F0B", 16, "up"))
        for nm in ("Atala", "Vitala", "Sutala", "Talatala", "Mahatala", "Rasatala", "Patala"):
            self.twinkles.append(Twinkle(self.ax, self.egg, *self._rand_in(self.rows[nm], 4, 28, 72), "#FFFFFF", 10, "pat"))

    def _lotus(self):
        """Satyaloka: a lotus with a pulsing glow."""
        sat = self.rows["Satyaloka"]
        lot_y = (sat["y0"] + sat["y1"]) / 2
        self.glow = Circle((CX, lot_y), 6.5, fc="#F2A623", ec="none", alpha=0.25, zorder=3)
        self.ax.add_patch(self.glow)
        for k in range(8):
            a = k * 45
            px, py = CX + 3.4 * math.sin(math.radians(a)), lot_y + 3.4 * math.cos(math.radians(a))
            self.ax.add_patch(Ellipse((px, py), 1.8, 5.2, angle=-a, fc="#F4C0D1", ec="#993556", lw=0.5, zorder=4))
        self.ax.add_patch(Circle((CX, lot_y), 1.5, fc="#EF9F27", ec="#854F0B", lw=0.6, zorder=5))

    def _flames(self):
        """Naraka: flickering flames."""
        self.nar = self.rows["Naraka"]
        self.flames = []
        for i, fx in enumerate(np.arange(25, 76, 5.0)):
            p = Polygon([(fx - 2, self.nar["y0"]), (fx, self.nar["y0"] + 4), (fx + 2, self.nar["y0"])],
                        fc="#E8593C" if i % 2 else "#F2A623", ec="none", zorder=3)
            self.ax.add_patch(p)
            p.set_clip_path(self.egg)
            self.flames.append((p, fx, i))

    def _shesha(self):
        """Shesha: head with fanned hood, body waving."""
        self.body, = self.ax.plot([], [], color="#1D9E75", lw=6, solid_capstyle="round", zorder=4)
        self.ax.add_patch(Circle((CX, 9.8), 1.2, fc="#1D9E75", ec="#0F6E56", zorder=6))
        self.hood = []
        for a in (-50, -25, 0, 25, 50):
            e = Ellipse((CX, 12.8), 2.2, 5.0, fc="#0F6E56", ec="#085041", lw=0.5, zorder=5)
            self.ax.add_patch(e)
            self.hood.append((e, a))

    def _outline_and_beyond(self):
        ax = self.ax
        ax.add_patch(Ellipse((CX, CY), EW, EH, fc="none", ec="#444441", lw=1.8, zorder=20))
        for extra in (2, 4):
            ax.add_patch(Ellipse((CX, CY), EW + extra, EH + extra, fc="none", ec="#888780", lw=0.7, ls="--", zorder=2))
        ax.text(CX, -1.8, "Dashed shells: earth, water, fire, air, space, ego, intellect, matter (shown as two)",
                ha="center", va="center", fontsize=7, color="#5F5E5A")
        for (bx, nm, sub, fc, ec) in [(22, "Vaikuntha", "Vishnu", "#E1F5EE", "#0F6E56"),
                                      (42, "Kailasa", "Shiva", "#EEEDFE", "#534AB7"),
                                      (62, "Goloka", "Krishna", "#FAEEDA", "#854F0B")]:
            ax.add_patch(Rectangle((bx, 101), 18, 8, fc=fc, ec=ec, lw=1))
            ax.text(bx + 9, 106.3, nm, ha="center", va="center", fontsize=9, weight="bold", color=ec)
            ax.text(bx + 9, 103.2, sub, ha="center", va="center", fontsize=7.5, color=ec)
        ax.text(90, 105, "Beyond the egg", fontsize=8, color="#5F5E5A", va="center")

    def _labels(self):
        """Labels on the right, with leader lines."""
        for row in self.rows.values():
            ym = (row["y0"] + row["y1"]) / 2
            ln, = self.ax.plot([edge_x(ym) + 0.5, 89], [ym, ym], color="#B4B2A9", lw=0.5, ls=":", zorder=1)
            if row["h"] >= 6:
                t1 = self.ax.text(90, ym + 1.0, row["name"], fontsize=9, weight="bold", va="center", color="#2C2C2A")
                t2 = self.ax.text(90, ym - 1.3, row["sub"], fontsize=7.5, va="center", color="#5F5E5A")
                texts = [t1, t2]
            else:
                texts = [self.ax.text(90, ym, row["name"], fontsize=7.5, va="center", color="#2C2C2A")]
            if row["grp"] == "tri":
                self.fade += [(ln, 1.0)] + [(t, 1.0) for t in texts]

    # ---- animation --------------------------------------------------------
    def update(self, t, level, night):
        for art, base in self.fade:
            art.set_alpha(base * level)
        for tw in self.twinkles:
            tw.update(t, level)

        th = 1.1 * t
        self.sun.set_data([CX + 12 * math.cos(th)], [self.orbit_cy + 3.5 * math.sin(th)])
        self.moon.set_data([CX + 12 * math.cos(th + math.pi)], [self.orbit_cy + 3.5 * math.sin(th + math.pi)])
        for e, bx in self.clouds:
            e.center = (bx + 3.0 * math.sin(0.4 * t + bx), e.center[1])
        self.glow.set_radius(6 + 1.2 * math.sin(2 * t))
        y0 = self.nar["y0"]
        for p, fx, i in self.flames:
            hgt = 3.6 + 1.8 * math.sin(7 * t + i * 1.7)
            p.set_xy([(fx - 2, y0), (fx + 0.4 * math.sin(5 * t + i), y0 + hgt), (fx + 2, y0)])
        xs = np.linspace(37, 63, 80)
        self.body.set_data(xs, 6.2 + 1.0 * np.sin((xs - 37) * 0.8 + 2 * t))
        sway = 4 * math.sin(0.9 * t)
        for e, a in self.hood:
            ang = math.radians(a + sway)
            e.center = (CX + 3.0 * math.sin(ang), 9.8 + 3.0 * math.cos(ang))
            e.angle = -(a + sway)
        self.ax.set_title("Side view: the 14 worlds inside the Brahmanda  |  "
                          + ("night of Brahma" if night > 0.5 else "day of Brahma") + "  (press n)")
