"""Info text, the night-of-Brahma button, and click / key handling."""
import math
import textwrap

from matplotlib.widgets import Button

from data import CX, DESC, DARK_R, LOKALOKA_R, RINGS
from side_view import edge_x


class Controls:
    def __init__(self, fig, side, top, auto=False):
        self.fig, self.side, self.top = fig, side, top
        self.state = {"night": 0.0, "target": 0.0, "auto": auto}
        self.info = fig.text(0.02, 0.1, "Click any world or ring to read about it.",
                             fontsize=9.5, va="top", ha="left", color="#2C2C2A")
        self.button = Button(fig.add_axes([0.02, 0.125, 0.17, 0.04]), "Start night of Brahma")
        self.button.on_clicked(self.toggle)
        fig.canvas.mpl_connect("key_press_event", self.on_key)
        fig.canvas.mpl_connect("button_press_event", self.on_click)

    def say(self, text):
        self.info.set_text(textwrap.fill(text, 75))

    def toggle(self, _event=None):
        s = self.state
        s["target"] = 0.0 if s["target"] else 1.0
        self.button.label.set_text("Bring back the day" if s["target"] else "Start night of Brahma")
        self.say(DESC["Night" if s["target"] else "Day"])
        self.fig.canvas.draw_idle()

    def on_key(self, event):
        if event.key == "n":
            self.toggle()

    def on_click(self, event):
        if event.inaxes is self.side.ax and event.ydata is not None:
            yv = event.ydata
            if yv >= 100:
                self.say(DESC["Beyond"])
                return
            for row in self.side.rows.values():
                if row["y0"] <= yv < row["y1"] and abs(event.xdata - CX) <= edge_x(yv) - CX:
                    self.say(DESC[row["name"]])
                    return
        elif event.inaxes is self.top.ax and event.xdata is not None:
            r = math.hypot(event.xdata, event.ydata)
            for name, outer, _, text in RINGS:
                if r <= outer:
                    self.say(text)
                    return
            self.say(DESC["Lokaloka"] if r <= LOKALOKA_R else DESC["Dark"] if r <= DARK_R else "")
