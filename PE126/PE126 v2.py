import time
import numpy as np
import itertools as it
from multiprocessing import Pool
from numba import njit, prange
import numba


def unique_starting_cuboids(limit):
    i=0
    count = 0
    while count < limit:
        i+=1
        for j in range(1,i+1):
            for k in range(1, j+1):
                count += 1
                yield (i,j,k)
   
 
def equation_fit(cube, sample):
    #let s be the sample of covering lengths for the given cube
    s = sample
    #for x = 1, 4+a+c = s[0]
    #for x = 2, 16+2a+c = s[1]
    #therefore, 12+a=s[1]-s[0] => a = s[1]-s[0]-12
    #and c = s[0]-4-s[1]+s[0]+12 = 2s[0]-s[1]+8
    return s[1]-s[0]-12, 2*s[0]-s[1]+8


def coefficients(w,l,h):
    first_layer = 2*w*l+2*w*h+2*l*h
    second_layer = first_layer + 4*(w+l+h)
    s = [first_layer, second_layer]
    b,c = equation_fit((w,l,h), s)
       
    return(b,c)

def cuboids_for_i(i):
    j_idx, k_idx = np.tril_indices(i)  # 0-indexed pairs with k <= j
    n = len(j_idx)
    out = np.empty((n, 3), dtype=np.int64)
    out[:, 0] = i
    out[:, 1] = j_idx + 1
    out[:, 2] = k_idx + 1
    return out



def chunked_cuboids(max_i, target):
    buffer = []
    buffered_rows = 0
    for i in range(1, max_i + 1):
        rows = cuboids_for_i(i)
        if len(rows) > target:
            # Split a big i across multiple tasks
            for start in range(0, len(rows), target):
                yield rows[start:start + target]
        else:
            buffer.append(rows)
            buffered_rows += len(rows)
            if buffered_rows >= target:
                yield np.concatenate(buffer)
                buffer = []
                buffered_rows = 0
    if buffer:
        yield np.concatenate(buffer)

#-------------------------------


LAYER_UBOUND = 100
CUBOID_UBOUND = 9000  + 1
CHUNK_SIZE = 1_000_000
X = np.arange(1, LAYER_UBOUND + 1, dtype=np.int64)
FOUR_X_SQ = 4 * X * X
MAX_VALUE = 20_000

# @njit(cache=True)
# def get_coverings(cubes, max_value=MAX_VALUE, layer_ubound=LAYER_UBOUND):
#     counts = np.zeros(max_value + 1, dtype=np.int64)
#     for idx in range(len(cubes)):
#         w, l, h = cubes[idx, 0], cubes[idx, 1], cubes[idx, 2]
#         first = 2*w*l + 2*w*h + 2*l*h
#         second = first + 4*(w + l + h)
#         b = second - first - 12
#         c = 2*first - second + 8
#         if 4 + b + c >= max_value:
#             continue
#         for x in range(1, layer_ubound + 1):
#             v = (4 * x + b) * x + c
#             if v > max_value:
#                 break
#             counts[v] += 1
#     return counts


@njit(parallel=True, cache=True)
def process_all(cubes, max_value, layer_ubound):
    n_threads = numba.get_num_threads()
    local = np.zeros((n_threads, max_value + 1), dtype=np.int64)
    for idx in prange(len(cubes)):
        tid = numba.get_thread_id()
        w, l, h = cubes[idx, 0], cubes[idx, 1], cubes[idx, 2]
        first = 2*w*l + 2*w*h + 2*l*h
        second = first + 4*(w + l + h)
        b = second - first - 12
        c = 2*first - second + 8
        if 4 + b + c >= max_value:
            continue
        for x in range(1, layer_ubound + 1):
            v = (4 * x + b) * x + c
            if v > max_value:
                break
            local[tid, v] += 1
    return local.sum(axis=0)


if __name__ == "__main__":
    start_time = time.time()
    chunk_end_time = start_time
    counts = np.zeros(MAX_VALUE + 1, dtype=np.int64)
    for i, chunk in enumerate(chunked_cuboids(CUBOID_UBOUND, CHUNK_SIZE)):  # BIG_CHUNK = 1M+
        counts += process_all(chunk, MAX_VALUE, LAYER_UBOUND)
        if i % 1000 == 0:
            print(f"{i} chunks processed in --- %s seconds ---" % (time.time() - chunk_end_time))
            chunk_end_time = time.time()

    counts = [(n, count) for n,count in enumerate(counts)]
    counts.sort(key=lambda x: x[1])
    print(counts[-25:])
    print([count for count in counts if count[1] == 1000])
    print("total time: %s seconds" % (time.time() - start_time))




    # i = 0
    # start_time = time.time()
    # chunks = (cuboids_for_i(i) for i in range(1, CUBOID_UBOUND+1))
    # counts = np.zeros(MAX_VALUE+1, dtype = np.int64)
    # with Pool() as pool:
    #     for partial in pool.imap_unordered(get_coverings, chunked_cuboids(CUBOID_UBOUND,CHUNK_SIZE)):
    #         counts += partial
    #         i+=1
    #         if i % 100 == 0:
    #             print(f"{i} chunks processed")

    # counts = [(n, count) for n,count in enumerate(counts)]
    # counts.sort(key=lambda x: x[1])
    # print(counts[-25:])
    # print([count for count in counts if count[1] == 1000])
    # print("--- %s seconds ---" % (time.time() - start_time))


# def compute_coeffs(cubes):
#     w, l, h = cubes[:, 0], cubes[:, 1], cubes[:, 2]
#     first = 2*w*l + 2*w*h + 2*l*h
#     second = first + 4*(w + l + h)
#     b = second - first - 12
#     c = 2*first - second + 8
#     return np.stack([b, c], axis=1)
    
# def get_coverings(cubes):

#     coeffs = compute_coeffs(cubes)
#     mask = coeffs[:, 0] + coeffs[:, 1] + 4 < MAX_VALUE
#     coeffs = coeffs[mask]

#     b,c = coeffs[:,0:1], coeffs[:,1:2]

#     all_values = FOUR_X_SQ + b*X + c
#     good_values = all_values <= MAX_VALUE

#     counts = np.bincount(all_values[good_values], minlength=MAX_VALUE+1)
    
#     return(counts)