import input_data

def rotate(A,B,C):
    R=(B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])
    return R

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def rotate(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

def grahamscan(A):
    n = len(A)
    P = list(range(n))

    merge_sort(A)
    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0]:
            P[i], P[0] = P[0], P[i]

    for i in range(2, n):
        j = i
        while j > 1 and (rotate(A[P[0]], A[P[j - 1]], A[P[j]]) < 0):
            P[j], P[j - 1] = P[j - 1], P[j]
            j -= 1

    S = [P[0], P[1]]
    for i in range(2, n):
        while rotate(A[S[-2]], A[S[-1]], A[P[i]]) < 0:
            del S[-1]
        S.append(P[i])

    return [A[i] for i in S]

print(grahamscan(input_data.Set_1_3))

Set = [[43.0416151,44.2198622], [43.1756719,44.2955701], [43.1937634,44.5338746]]
print("сорт", rotate(Set[0], Set[1], Set[2]))