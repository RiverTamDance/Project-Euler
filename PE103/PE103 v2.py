import itertools as it
import time

def bad_sums(values):
    double_sums = (sum(c) for c in it.combinations(values, 2))
    triple_sums = (sum(c) for c in it.combinations(values, 3))
    if has_duplicates(double_sums) or has_duplicates(triple_sums):
        return True
    else:
        return False

def has_duplicates(iterable):
    seen = set()
    return any(x in seen or seen.add(x) for x in iterable)

def size_check(state):
    if sum(state[:3]) > sum(state[-2:]):
        if sum(state[:4]) > sum(state[-3:]):
            return True

start_time = time.perf_counter()

options = []
for s2 in range(2,50):
    for s1 in range(1, s2):
        for s7 in range(s2+1, s1+s2):
            for s3 in range(s2+1, s7):
                if bad_sums((s1,s2,s3,s7)):
                    continue
                for s6 in range(s3+1, s1+s2+s3-s7):
                    if bad_sums((s1,s2,s3,s6,s7)):
                        continue
                    for s4 in range(s3+1, s6):
                        if bad_sums((s1,s2,s3,s4,s6,s7)):
                            continue
                        for s5 in range(s4+1, s1+s2+s3+s4-s6-s7):
                            state = (s1,s2,s3,s4,s5,s6,s7)
                            if bad_sums(state):
                                continue
                            options.append(state)

sums = [(sum(s),s) for s in options]
print(min(sums, key = lambda x: x[0]))

end_time = time.perf_counter()
print("--- %s seconds ---" % (end_time - start_time))