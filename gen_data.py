#!./venv/bin/python
import argparse
from random import uniform, randint


class Args:
    width: int
    height: int
    depth: int
    velocity: float
    mass: float
    count: int


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="n-body data generator",
        description="Generates data for the n-body simulator.",
        add_help=False
    )

    parser.add_argument("-w", "--width", type=int, default=1900)
    parser.add_argument("-h", "--height", type=int, default=1000)
    parser.add_argument("-d", "--depth", type=int, default=0)
    parser.add_argument("-v", "--velocity", type=float, default=1.)
    parser.add_argument("-m", "--mass", type=float, default=1.)
    parser.add_argument("-c", "--count", type=int, default=500)

    args: Args = parser.parse_args()

    for _ in range(args.count):
        print(f"{randint(-args.width // 2, args.width // 2)},"
              f"{randint(-args.height // 2, args.height // 2)},"
              f"{f'{randint(-args.depth // 2, args.depth // 2)},' if args.depth else ''}"
              f"{uniform(-args.velocity, args.velocity)},"
              f"{uniform(-args.velocity, args.velocity)},"
              f"{f'{uniform(-args.velocity, args.velocity)},' if args.depth else ''}"
              f"{uniform(1e-2, args.mass)}")
