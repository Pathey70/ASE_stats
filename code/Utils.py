import math
from Main import coerce
import os
import random
from RX import RX


def rnd(n, nPlaces=2):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult


def rand(lo=0, hi=1, Seed=937162211):
    # Seed=937162211
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647, Seed


def rint(lo, hi):
    x, seed = rand(lo, hi)
    return math.floor(0.5 + x)


def csv(src, fun):
    if not os.path.isfile(src):
        print("\nfile " + src + " doesn't exists!")
        sys.exit(2)
    with open(src, 'r') as file1:
        for line in file1:
            temp = []
            for j in line.strip().split(','):
                temp.append(coerce(j))
            fun(temp)


def mp(src, fun):
    for i in src:
        # print(i)
        fun(i)


def kap(t, fun, u={}):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        if not k:
            u[len(u)] = v
        else:
            u[k] = v
    return u


def cosine(a, b, c):
    if c == 0:
        c = 0.5
    x1 = (a ** 2 + c ** 2 - b ** 2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = math.sqrt(abs(a ** 2 - x2 ** 2))
    return x2, y


def samples(t, n=None):
    if not n:
        n = len(t)
    return random.choices(t, k=n)


def any(t, seed=937162211):
    random.seed(seed)
    return random.choices(t)[0]


def per(t, p=0.5):
    p = math.floor((p * len(t)) + .5)
    return t[max(1, min(len(t), p))]


def show(node, what, cols, nPlaces, lvl=0):
    if node:
        print("| " * lvl + str(len(node["data"].rows)) + " ", end='')
        # print(node)
        if "left" not in node or lvl == 0:
            print(node["data"].stats(nPlaces, node["data"].cols.y, "mid"))
        else:
            print("")
        show(None if "left" not in node else node["left"], what, cols, nPlaces, lvl + 1)
        show(None if "right" not in node else node["right"], what, cols, nPlaces, lvl + 1)


def cliffsDelta(ns1, ns2, the):
    if len(ns1) > 128:
        ns1 = samples(ns1, 128)
    if len(ns2) > 128:
        ns2 = samples(ns2, 128)

    n, gt, lt = 0, 0, 0
    for x in ns1:
        for y in ns2:
            n = n + 1
            if x > y:
                gt = gt + 1

            elif x < y:
                lt = lt + 1
    return abs(lt - gt) / n <= the['cliff']


def mid(t):
    if t.has:
        t = t.has
    n = len(t) // 2
    return (t[n] + t[n + 1]) / 2 if len(t) % 2 == 0 else t[n + 1]


def div(t):
    if t.has:
        t = t.has
    return (t[len(t) * 9 // 10] - t[len(t) * 1 // 10]) / 2.56


def merge(rx1, rx2):
    rx3 = RX([], rx1.name)
    for t in (rx1.has, rx2.has):
        for x in t:
            rx3.has.append(x)
    rx3.has.sort()
    rx3.n = len(rx3.has)
    return rx3


def gaussian(mu=0, sd=1):
    return mu + sd * math.sqrt(-2 * math.log(random.rand())) * math.cos(2 * math.pi * random.rand())