# nbody

Threw this together in a day or two cause I thought it would be fun to mess around with.
Can simulate a few hundred bodies in 2 or 3 dimensions without much hassle (hardware dependent of course).

Comments are non-existent, sorry about that.


To set up:
```shell
python -m venv venv
source venv/bin/activate
pip -r requirements.txt
```

To run:
```shell
# 2d simulation
./main.py -f 2d/simple.csv

# 3d simulation, increased gravity
./main.py -f 3d/some.csv -d 3 -g 30
```

To create a new start state:
```shell
# New 3d simulation of 100 particles in 300x200 box with max velocity components 2 and mass up to 3
./gen_data.py -c 100 -w 300 -h 200 -v 2 -m 3 > data/2d/new.csv

# New 3d simulation of 500 particles in 1000^3 box with velocity components up to 3 and mass up to 5
./gen_data.py -c 500 -d 1000 -w 1000 -h 1000 -v 3 -m 5 > data/3d/new.csv
```
