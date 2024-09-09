def Seidel_func(A, b, eps):
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    index = 0
    while not converge:
        x_new = np.copy(x)
        index += 1
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        epsilon = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n)))
        converge = epsilon <= eps
        x = x_new
        print(f'{index} | {x} | {epsilon} ')
    return [round(item, 3) for item in x]