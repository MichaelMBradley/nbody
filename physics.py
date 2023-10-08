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


def n_body_matrix(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray):
    dist = np.zeros((len(pos) - 1, len(pos), 2))
    rot_mass = np.zeros((len(mass) - 1, len(mass), 1))

    pos2 = np.concatenate((pos, pos))
    mass2 = np.concatenate((mass, mass))

    for i in range(1, len(pos)):
        dist[i - 1] = pos2[i: i + len(pos)] - pos
        rot_mass[i - 1] = mass2[i: i + len(mass)]

    vel += G * np.sum(
        dist * rot_mass / (np.linalg.norm(dist, axis=2) ** 3)[:, :, np.newaxis],
        axis=0
    )

    pos += vel


def n_body_matrix_constrained(pos: np.ndarray, vel: np.ndarray, mass: np.ndarray, close=2.):
    dist = np.zeros((len(pos) - 1, len(pos), 2))
    rot_mass = np.zeros((len(mass) - 1, len(mass), 1))

    pos2 = np.concatenate((pos, pos))
    mass2 = np.concatenate((mass, mass))

    for i in range(1, len(pos)):
        dist[i - 1] = pos2[i: i + len(pos)] - pos
        rot_mass[i - 1] = mass2[i: i + len(mass)]

    a = np.linalg.norm(dist, axis=2)
    a[a < close] = close
    vel += G * np.sum(
        dist * rot_mass / (a ** 3)[:, :, np.newaxis],
        axis=0
    )

    pos += vel
