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


def eg_num(the):
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
        cl = cliffsDelta(a, b, the)
        bs = bootstrap(a, b, the)
        print(mu, 1, cl, bs, cl and bs)


def eg_basic(the):
    print("\t\ttrue", bootstrap([8, 7, 6, 2, 5, 8, 7, 3],
                                [8, 7, 6, 2, 5, 8, 7, 3], the),
          cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3],
                      [8, 7, 6, 2, 5, 8, 7, 3], the))
    print("\t\tfalse", bootstrap([8, 7, 6, 2, 5, 8, 7, 3],
                                 [9, 9, 7, 8, 10, 9, 6], the),
          cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3],
                      [9, 9, 7, 8, 10, 9, 6], the))
    print("\t\tfalse",
          bootstrap([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6],
                    [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9], the),
          cliffsDelta([0.34, 0.49, 0.51, 0.6, .34, .49, .51, .6],
                      [0.6, 0.7, 0.8, 0.9, .6, .7, .8, .9], the))


def eg_pre(the):
    print("\neg3")
    d = 1
    for i in range(10):
        t1, t2 = [], []
        for j in range(32):
            t1.append(gaussian(10, 1))
            t2.append(gaussian(d * 10, 1))
        print('\t', round(d, 2), d < 1.1, bootstrap(t1, t2, the), bootstrap(t1, t1, the))
        d += 0.05


def eg_tiles(the):
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    high = 1001
    for i in range(1, high):
        a.append(gaussian(10, 1))
    for i in range(1, high):
        b.append(gaussian(10.1, 1))
    for i in range(1, high):
        c.append(gaussian(20, 1))
    for i in range(1, high):
        d.append(gaussian(30, 1))
    for i in range(1, high):
        e.append(gaussian(30.1, 1))
    for i in range(1, high):
        f.append(gaussian(10, 1))
    for i in range(1, high):
        g.append(gaussian(10, 1))
    for i in range(1, high):
        h.append(gaussian(40, 1))
    for i in range(1, high):
        j.append(gaussian(40, 3))
    for i in range(1, high):
        k.append(gaussian(10, 1))
    for k, v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v, "rx" + str(k + 1)))
    rxs.sort(key=lambda x: mid(x))
    for rx in tiles(rxs, the):
        print("", rx.name, rx.show)
