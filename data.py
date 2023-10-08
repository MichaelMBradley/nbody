import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

import physics


def parse_csv(filename: str):
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()
    pos = np.zeros((len(lines), 2))
    vel = np.zeros((len(lines), 2))
    rad = np.zeros((len(lines), 1))
    for i, [x, y, vx, vy, r] in enumerate(map(lambda l: map(float, l.split(',')), lines)):
        pos[i] = [x, y]
        vel[i] = [vx, vy]
        rad[i] = r
    return pos, vel, rad


class Animator:
    def __init__(self, pos: np.ndarray, vel: np.ndarray, rad: np.ndarray):
        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.mass = np.pi * 4 / 3 * rad ** 3

        self.scat = None
        self.colours = cm.rainbow(
            np.random.random(
                (len(self.rad),)
            )
        )

        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update,
            interval=1000 / (15 * 2 ** 4),
            init_func=self.setup_plot,
            blit=True,
            cache_frame_data=False
        )

    def setup_plot(self):
        self.scat = self.ax.scatter(
            self.pos[:, 0],
            self.pos[:, 1],
            c=self.colours,
            s=self.rad * 10
        )
        self.ax.axis([-950, 950, -500, 500])
        return self.scat,

    def update(self, *_args, **_kwargs):
        physics.n_body_matrix_constrained(self.pos, self.vel, self.mass)
        self.scat.set_offsets(self.pos)
        return self.scat,

    def show(self):
        plt.show()
