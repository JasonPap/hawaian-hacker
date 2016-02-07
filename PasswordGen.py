from __future__ import division
import random


def generate_passwords(frequencies, amount, length):
    pdf = frequencies.items()
    cdf = []
    total = sum(frequencies.values())
    results = []
    for letter in pdf:
        cdf.append((letter[0], letter[1]/total))
    for i in range(0, amount):
        lpwd = []
        for j in range(0, length):
            r, s = random.random(), 0
            for num in cdf:
                s += num[1]
                if s >= r:
                    lpwd.append(num[0])
                    break
        results.append(''.join(lpwd))
    return results
