"""
Created by Taylor Richards
taylordrichards@gmail.com
November 16, 2025
"""
import time

def main():
    start_time = time.perf_counter()

    SEARCH_SIZE = 10**6
    search_space = set(range(1,SEARCH_SIZE+1))

    while search_space:
        n = search_space.pop()

    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()