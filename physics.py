import numpy as np


G = 6.674e-11


def rotations(a: np.ndarray):
    a2 = np.concatenate((a, a))
    for i in range(1, len(a)):
        yield np.split(a2, [i, i + len(a)])[1]


def n_body(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray):
    for (o_pos, o_mass) in zip(rotations(pos), rotations(mass)):
        dist = o_pos - pos
        vel += G * (dist / np.linalg.norm(dist, axis=1)[:, np.newaxis]) * o_mass[:, np.newaxis] / np.sum(dist ** 2, axis=1)[:, np.newaxis]
    pos += vel
