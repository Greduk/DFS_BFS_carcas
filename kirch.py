def set_to_kirch(f):  # из списка смежности в матрицу смежности
    a = [[0 for j in f] for i in f]
    n = []
    for i in f:
        n.append(list(i))
    for i in range(len(n)):
        a[i][i] = len(n[i])
        for j in range(len(n[i])):
            a[n[i][j]][i], a[i][n[i][j]] = 1, 1
    return a


def incident_to_kirch(n):  # из матрицы инцидентности в матрицу смежности
    a = [[0 for j in n] for i in n]
    for i in range(len(n)):
        a[i][i] = sum(n[i])
        for j in range(len(n[0])):
            if n[i][j]:
                for h in range(len(n)):
                    if n[h][j] and h != i:
                        a[h][i], a[i][h] = 1, 1
    return a


def adjacency_to_kirch(n):  # из матрицы Кирхгофа в матрицу смежности
    a = [[0 for j in n] for i in n]
    for i in range(len(n)):
        a[i][i] = sum(n[i])
        for j in range(len(n[i])):
            if n[i][j]:
                a[i][j] = -1
    return a
