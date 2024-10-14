def tri_bulle(T):
    N = len(T)
    for i in range(1,N-1):
        for j in range(0,N-i-1):
            if T[j] > T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]


T = [27, 43, 15, 12, 2, 74, 93, 71]
print(T)
tri_bulle(T)
print("Le tableau trié est:",T)

