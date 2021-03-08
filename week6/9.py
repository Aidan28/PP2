a = int(input())
def isPrime(n):
    if a == 1: return False
    if a == 2: return True
    else:
        for i in range(2, n):
            if n % i == 0: return False
        return True
print(isPrime(a))