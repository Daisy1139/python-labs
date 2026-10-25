def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def getPrimeList(n):
    list =[]
    for i in range(2,n):
        if isPrime(i):
            list.append(i)
    return list
print(getPrimeList(20))
