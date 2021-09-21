def set_to_adjacency(f):  # из списка смежности в матрицу смежности
    a = [[0 for j in f] for i in f]
    n = []
    for i in f:
        n.append(list(i))
    for i in range(len(n)):
        for j in range(len(n[i])):
            a[n[i][j]][i], a[i][n[i][j]] = 1, 1
    return a


def incident_to_adjacency(n):  # из матрицы инцидентности в матрицу смежности
    a = [[0 for j in n] for i in n]
    for i in range(len(n)):
        for j in range(len(n[0])):
            if n[i][j]:
                for h in range(len(n)):
                    if n[h][j] and h != i:
                        a[h][i], a[i][h] = 1, 1
    return a


def kirch_to_adjacency(n):  # из матрицы Кирхгофа в матрицу смежности
    a = [[0 for j in n] for i in n]
    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] == -1:
                a[i][j] = 1
    return a
