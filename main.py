#!./venv/bin/python
import argparse
import typing

import data
import physics


class Args:
    filename: str
    gravity: float
    dimensions: typing.Literal[2, 3]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="n-body simulation",
        description="Simulating gravitational effects"
    )

    parser.add_argument(
        "-f",
        "--filename",
        default="data/2d/simple.csv"
    )
    parser.add_argument(
        "-g",
        "--gravity",
        type=float,
        default=1.
    )
    parser.add_argument(
        "-d",
        "--dimensions",
        type=int,
        choices=[2, 3],
        default=2
    )

    args: Args = parser.parse_args()

    physics.G = args.gravity

    objects = data.parse_csv(args.filename, dimensions=args.dimensions)
    a = data.Animator(*objects)
    a.show()
