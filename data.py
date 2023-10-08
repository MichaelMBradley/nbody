import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import physics


def parse_csv(filename: str, dimensions=2):
    if not (1 < dimensions < 4):
        raise ValueError(f"Can only show 2or 3 dimensional scenes, not {dimensions}")
    with open(filename, 'r') as file:
        lines = file.read().strip().splitlines()
    pos = np.zeros((len(lines), dimensions))
    vel = np.zeros((len(lines), dimensions))
    rad = np.zeros((len(lines), 1))
    for i, values in enumerate(map(lambda l: map(float, l.split(',')), lines)):
        if dimensions == 2:
            [x, y, vx, vy, r] = values
            pos[i] = [x, y]
            vel[i] = [vx, vy]
            rad[i] = r
        elif dimensions == 3:
            [x, y, z, vx, vy, vz, r] = values
            pos[i] = [x, y, z]
            vel[i] = [vx, vy, vz]
            rad[i] = r
    return pos, vel, rad


class Animator:
    def __init__(self, pos: np.ndarray, vel: np.ndarray, rad: np.ndarray):
        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.mass = np.pi * 4 / 3 * rad ** 3

        n, d = self.pos.shape

        self.scat: plt.PathCollection = None
        self.colours = cm.rainbow(
            np.random.random(
                (n,)
            )
        )

        self.fig = plt.figure()
        if d == 2:
            self.ax = self.fig.add_subplot()
        else:
            self.ax = self.fig.add_subplot(projection="3d")
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update,
            interval=1000 / (15 * 2 ** 4),
            init_func=self.setup_plot,
            blit=True,
            cache_frame_data=False
        )

    def setup_plot(self):
        _n, d = self.pos.shape
        if d == 2:
            self.scat = self.ax.scatter(
                self.pos[:, 0],
                self.pos[:, 1],
                c=self.colours,
                s=self.rad * 10
            )
            self.ax.axis([-950, 950, -500, 500])
        else:
            self.scat = self.ax.scatter(
                self.pos[:, 0],
                self.pos[:, 1],
                self.pos[:, 2],
                c=self.colours,
                s=self.rad * 10
            )
            self.ax.axis([-500, 500, -500, 500, -500, 500])
        return self.scat,

    def update(self, *_args, **_kwargs):
        _n, d = self.pos.shape
        physics.n_body_matrix(self.pos, self.vel, self.mass, constrain=2.)
        self.scat.set_offsets(self.pos[:, :2])
        if d == 3:
            self.scat.set_3d_properties(self.pos[:, 2], 'z')
            self.fig.canvas.draw()
        return self.scat,

    def show(self):
        plt.show()
