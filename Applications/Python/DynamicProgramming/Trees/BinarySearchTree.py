def BinarySearchTree(p, q):
    n = len(p)

    e = [[0 for x in range(n + 1)] for _ in range(0, n + 1)]
    w = [[0 for x in range(n + 1)] for _ in range(0, n + 1)]
    roots = [[0 for x in range(n)] for _ in range(n)]

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    for l in range(1, n + 1):
        for i in range(1, n - l +  2):
            j = i + l - 1
            e[i - 1][j] = 999999
            w[i - 1][j] = w[i][j] + p[i - 1] + q[i - 1]

            for r in range(i - 1, j):
                t = e[i - 1][r] + e[r + 1][j] + w[i - 1][j]

                if(t < e[i - 1][j]):
                    e[i - 1][j] = round(t, 3)
                    roots[i - 1][j - 1] = r + 1

    return e


p = [0.15, 0.1, 0.05, 0.1, 0.2]
q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]

result = BinarySearchTree(p, q)
print("Expected value: ", result[0][len(p)])