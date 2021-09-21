def kirch_to_set(n):  # из матрицы Кирхгофа в список смежности
    a = [set() for i in n]
    for i in range(len(n[0])):
        for j in range(len(n)):
            if n[i][j] == -1:
                a[i].add(j)
    return a


def adjacency_to_set(n):  # из матрицы смежности в список смежности
    a = [set() for i in n]
    for i in range(len(n[0])):
        for j in range(len(n)):
            if n[i][j]:
                a[i].add(j)
    return a


def incident_to_set(n):  # из матрицы инцидентности в список смежности
    a = [set() for i in n]
    for i in range(len(n)):
        for j in range(len(n[0])):
            if n[i][j]:
                for h in range(len(n)):
                    if n[h][j] and h != i:
                        a[i].add(h)
                        a[h].add(i)
                        n[h][j], n[i][j] = 0, 0
                        break
    return a
