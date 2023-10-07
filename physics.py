import numpy as np


G = 6.674e-11


def rotate(a: np.ndarray, n: int):
    return np.concatenate(np.split(a, [n])[::-1])


def rotations(a: np.ndarray):
    for i in range(1, len(a)):
        yield rotate(a, i)


def n_body(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray):
    for (o_pos, o_mass) in zip(rotations(pos), rotations(mass)):
        dist = o_pos - pos
        vel += G * (dist / np.linalg.norm(dist, axis=1)[:, np.newaxis]) * o_mass[:, np.newaxis] / np.sum(dist ** 2, axis=1)[:, np.newaxis]
    pos += vel
