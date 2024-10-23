def rotate(A,B,C):
    R=(B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])
    return R

def grahamscan(A):
    n = len(A)             # количество элементов множества
    P = list(range(n))           # создание нового списка размером n

    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:   # если P[i]-ая точка лежит левее P[0]-ой точки
            P[i], P[0] = P[0], P[i]     # меняем местами номера этих точек

    for i in range(2, n):
        j = i
        while j > 1 and (rotate(A[P[0]], A[P[j - 1]], A[P[j]]) < 0):
            P[j], P[j - 1] = P[j - 1], P[j]
            j -= 1

    S = [P[0], P[1]]

    for i in range(2, n):
        while rotate(A[S[-2]], A[S[-1]], A[P[i]]) < 0:
            del S[-1]  # pop(S)
        S.append(P[i])  # push(S,P[i])

    return [A[i] for i in S]


def jarvismarch(A):
    n = len(A)
    P = list(range(n))

    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:
            P[i], P[0] = P[0], P[i]

    H = [P[0]]
    del P[0]
    P.append(H[0])

    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(A[H[-1]], A[P[right]], A[P[i]]) < 0:
                right = i
        if P[right] == H[0]:
            break
        else:
            H.append(P[right])
            del P[right]

    return [A[i] for i in H]

def minimal_corvex_hull(Set, convex_hull):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    # Рисуем точки
    x, y = zip(*Set)
    plt.scatter(x, y, color='blue', label='Точки')

    # Рисуем минимальную выпуклую оболочку
    hull_x, hull_y = zip(*convex_hull)
    plt.fill(hull_x + (hull_x[0],), hull_y + (hull_y[0],), color='lightgreen', alpha=0.5, label='Выпуклая оболочка')

    plt.title('Минимальная выпуклая оболочка')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.show()