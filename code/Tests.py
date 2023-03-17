import sys

import TestEngine
from Num import Num
from Utils import *
from stats import *

tot = 0


def count(t):
    global tot
    tot = tot + len(t)


def eg_sample(the):
    for i in range(10):
        print(''.join(samples(['a', 'b', 'c', 'd', 'e'])))


def eg_nums(the):
    """Tests Num"""
    n = Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)


def eg_gauss(the):
    t = []
    for i in range(10000):
        t.append(gaussian(10, 2))
    n = Num(t)
    print(n.n, n.mu, n.sd)


def eg_bootmu(the):
    a, b = [], []
    for i in range(100):
        a.append(gaussian(10, 1))
    print("mu", "sd", "cliffs", "boot", "both")
    print("--", "--", "------", "----", "----")
    for mu in [x / 10.0 for x in range(100, 111)]:
        b = []
        for i in range(100):
            b.append(gaussian(mu, 1))
        cl = cliffs_delta(a, b, the)
        bs = bootstrap(a, b, the)
        print(mu, 1, cl, bs, cl and bs)
