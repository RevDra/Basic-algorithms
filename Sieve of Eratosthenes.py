def isPrime(n: int):
    if n >= 0:
        is_Prime = [True] * (n + 1)
        is_Prime[0] = is_Prime[1] = False
    
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_Prime[n]
    else: return False
