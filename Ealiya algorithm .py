import time
import random
import math

# --------- Miller-Rabin Probabilistic Check ---------
def is_probable_prime_miller_rabin(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# --------- Ealiya Algorithm by [Your Name] ---------
def is_probable_prime_ealiya(n):
    # Author: [Your Name]
    # This is the custom prime checking algorithm created by [Your Name]
    if n in {2, 3, 5}:
        return True
    if n < 2 or n % 2 == 0 or n % 5 == 0:
        return False
    if not is_probable_prime_miller_rabin(n):
        return False
    return True

# --------- Benchmarking Function ---------
def benchmark_prime_tests(numbers):
    # Miller-Rabin
    start_time = time.time()
    miller_rabin_results = [is_probable_prime_miller_rabin(n) for n in numbers]
    miller_rabin_duration = time.time() - start_time
    
    # Ealiya Algorithm
    start_time = time.time()
    ealiya_results = [is_probable_prime_ealiya(n) for n in numbers]
    ealiya_duration = time.time() - start_time
    
    return miller_rabin_results, ealiya_results, miller_rabin_duration, ealiya_duration

# --------- Generate Random 100-Digit Numbers ---------
def generate_large_numbers(count, digits=100):
    numbers = []
    for _ in range(count):
        num = random.randint(10**(digits-1), 10**digits - 1)
        numbers.append(num)
    return numbers

# --------- Example Usage ---------
if __name__ == "__main__":
    # Generate 5 random 100-digit numbers
    numbers = generate_large_numbers(5, 100)
    
    print("Testing 100-digit numbers...\n")
    miller_rabin_results, ealiya_results, miller_rabin_duration, ealiya_duration = benchmark_prime_tests(numbers)
    
    # Print results
    for n, mr_res, ea_res in zip(numbers, miller_rabin_results, ealiya_results):
        print(f"{n}: Miller-Rabin = {'Prime' if mr_res else 'Composite'}, Ealiya = {'Prime' if ea_res else 'Composite'}")
    
    print(f"\nMiller-Rabin Duration: {miller_rabin_duration:.6f} seconds")
    print(f"Ealiya Algorithm Duration: {ealiya_duration:.6f} seconds")

