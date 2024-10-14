def factorielle(n):
    if n == 1:
        return True
    else:
        return n * factorielle(n-1)

print(factorielle(4))