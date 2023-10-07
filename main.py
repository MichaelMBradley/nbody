#!./venv/bin/python
import argparse

import data
import physics


class Args:
    filename: str
    gravity: float


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="n-body simulation",
        description="Simulating gravitational effects"
    )

    parser.add_argument(
        "-f",
        "--filename",
        default="data/simple.csv"
    )
    parser.add_argument(
        "-g",
        "--gravity",
        type=float,
        default=1.
    )

    args: Args = parser.parse_args()

    physics.G = args.gravity

    objects = data.parse_csv(args.filename)
    a = data.Animator(*objects)
    a.show()
