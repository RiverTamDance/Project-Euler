"""
Created by Taylor Richards
taylordrichards@gmail.com
August 03, 2024
"""
import time
import decimal

decimal.getcontext().prec = 102

def sqrt_ddigit_sum(n):
    d = decimal.Decimal(n)
    s = str(d.sqrt())
    s = s.replace('.','')
    ds = [int(i) for i in s[:100]]
    return(sum(ds))

def main():
    start_time = time.perf_counter()

    search_space = [n for n in range(1,101) if n not in [i**2 for i in range(11)]]
    digital_sums = [sqrt_ddigit_sum(n) for n in search_space]
    print(digital_sums)
    print(sum(digital_sums))


    end_time = time.perf_counter()
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()