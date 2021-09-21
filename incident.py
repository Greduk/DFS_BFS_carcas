def set_to_incident(f):  # из списка смежности в матрицу инцидентности
    a = 0
    b = len(f)
    n = []
    for i in f:
        n.append(list(i))
        a += len(i)
    a //= 2
    x = [[0 for i in range(a)] for j in range(b)]
    curr_rib = 0
    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j] > i:
                x[n[i][j]][curr_rib], x[i][curr_rib] = 1, 1
                curr_rib += 1
    return x


def adjacency_to_incident(n):  # из матрицы смежности в матрицу инцидентности
    a = 0
    b = len(n)
    for i in n:
        a += i.count(1)
    a //= 2
    x = [[0 for i in range(a)] for j in range(b)]
    curr_rib = 0
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i][j]:
                x[j][curr_rib], x[i][curr_rib] = 1, 1
                n[i][j], n[j][i] = 0, 0
                curr_rib += 1
    return x


def kirch_to_incident(n):  # из матрицы Кирхгофа в матрицу инцидентности
    a = 0
    b = len(n)
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j and n[i][j]:
                a += 1
    a //= 2
    x = [[0 for i in range(a)] for j in range(b)]
    curr_rib = 0
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i][j] and i != j:
                x[j][curr_rib], x[i][curr_rib] = 1, 1
                n[i][j], n[j][i] = 0, 0
                curr_rib += 1
    return x
