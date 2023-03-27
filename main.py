import math

def get_num_divisors(n):
    if n == 1:
        return 1

    divisors = 2

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n // i:
                divisors += 2
            else:
                divisors += 1

    return divisors

highly_composite_nums = {}

if __name__ == '__main__':
    max_dividers = 0
    dividers = 0
    N = 1000_000
    for i in range(1, N + 1):
        dividers = get_num_divisors(i)
        if dividers > max_dividers:
            max_dividers = dividers
            highly_composite_nums[i] = dividers

    i = N
    while max_dividers >= dividers:
        i += 1
        dividers = get_num_divisors(i)

    highly_composite_nums[i] = dividers

    print(highly_composite_nums)
    print(dividers)
    print(i)

# { 1: 1, 2: 2, 4: 3, 6: 4, 12: 6, 24: 8, 36: 9, 48: 10, 60: 12, 120: 16, 180: 18,
# 240: 20, 360: 24, 720: 30, 840: 32, 1260: 36, 1680: 40, 2520: 48, 5040: 60, 7560: 64,
# 10080: 72, 15120: 80, 20160: 84, 25200: 90, 27720: 96, 45360: 100, 50400: 108, 55440: 120,
# 83160: 128, 110880: 144, 166320: 160, 221760: 168, 277200: 180, 332640: 192, 498960: 200,
# 554400: 216, 665280: 224, 720720: 240, 1081080: 256 }

# 100_000: 110880 (144 dzielniki)
# 1_000_000: 1081080 (256 dzielników)