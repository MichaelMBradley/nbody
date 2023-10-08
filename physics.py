import numpy as np


G = 6.674e-11


def rotations(a: np.ndarray):
    a2 = np.concatenate((a, a))
    for i in range(1, len(a)):
        yield a2[i: i + len(a)]


def n_body(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray):
    for (o_pos, o_mass) in zip(rotations(pos), rotations(mass)):
        dist = o_pos - pos
        vel += G * dist * o_mass / (np.linalg.norm(dist, axis=1) ** 3)[:, np.newaxis]
    pos += vel


def n_body_matrix(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray, constrain=2.):
    n, d = pos.shape
    dist = np.zeros((n - 1, n, d))
    rot_mass = np.zeros((n - 1, n, 1))

    pos2 = np.concatenate((pos, pos))
    mass2 = np.concatenate((mass, mass))

    for i in range(1, len(pos)):
        dist[i - 1] = pos2[i: i + n] - pos
        rot_mass[i - 1] = mass2[i: i + n]

    norms = np.linalg.norm(dist, axis=2)
    if constrain:
        norms[norms < constrain] = constrain

    vel += G * np.sum(
        dist * rot_mass / (norms ** 3)[:, :, np.newaxis],
        axis=0
    )

    pos += vel
