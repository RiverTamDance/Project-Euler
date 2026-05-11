import time
import itertools as it

def search(state, pair_sums, triple_sums):
    if len(state) == 7:
        return [state]
    states = []
    for new_state, new_pairs, new_triples in get_choices(state, pair_sums, triple_sums):
        states += search(new_state, new_pairs, new_triples)
    return states

def get_choices(state, pair_sums, triple_sums):
    candidates = range(state[-2] + 1, state[-1])
    choices = []
    for v in candidates:
        # Pair sums introduced by v: v + e for each existing element e
        added_pairs = set()
        ok = True
        for e in state:
            s = v + e
            if s in pair_sums or s in added_pairs:
                ok = False
                break
            added_pairs.add(s)
        if not ok:
            continue
        # Triple sums introduced by v: v + a + b for each existing pair (a, b)
        added_triples = set()
        for a, b in it.combinations(state, 2):
            s = v + a + b
            if s in triple_sums or s in added_triples:
                ok = False
                break
            added_triples.add(s)
        if not ok:
            continue
        new_state = state[:-1] + [v] + state[-1:]
        choices.append((new_state, pair_sums | added_pairs, triple_sums | added_triples))
    return choices

def size_check(state):
    if sum(state[:3]) > sum(state[-2:]):
        if sum(state[:4]) > sum(state[-3:]):
            return True

# -----------------------------------------------------------
start_time = time.perf_counter()
successes = []
for s2 in range(2, 50):
    for s1 in range(1, s2):
        for m in range(s2 + 1, s1 + s2):
            state = [s1, s2, m]
            # Seed sums for the 3-element starting state.
            # Distinctness is automatic since s1 < s2 < m.
            pair_sums = {s1 + s2, s1 + m, s2 + m}
            triple_sums = {s1 + s2 + m}
            successes += search(state, pair_sums, triple_sums)
sums = [(sum(s), s) for s in successes if size_check(s)]
print(min(sums, key=lambda x: x[0]))
end_time = time.perf_counter()
print("--- %s seconds ---" % (end_time - start_time))