def sobelX(a):
    b = np.zeros(shape = (a.shape[0] + a.shape[0] % 3, a.shape[1] + a.shape[1] % 3, a.shape[2]))
    for i in range(0, a.shape[0]):
        for j in range(0, a.shape[1]):
            b[i + a.shape[0] % 3, j + a.shape[1] % 3] = a[i, j]
    for l in range(3):
        j = 0
        while b.shape[1] - j > 3:
            i = 0
            while b.shape[0] - i > 3:
                matr = ([b[i, j, l], b[i + 1, j, l], b[i + 2, j, l]],
                [b[i, j + 1, l], b[i + 1, j + 1, l], b[i + 2, j + 1, l]],
                [b[i, j + 2, l], b[i + 1, j + 2, l], b[i + 2, j + 2, l]])
                matr = np.dot(matr, sobel_filter_X)
                b[i][j][l] = matr[0][0]
                b[i + 1, j, l] = matr[1][0]
                b[i + 2, j, l] = matr[2][0]
                b[i, j + 1, l] = matr[0][1]
                b[i + 1, j + 1, l] = matr[1][1]
                b[i + 2, j + 1, l] = matr[2][1]
                b[i, j + 2, l] = matr[0][2]
                b[i + 1, j + 2, l] = matr[1][2]
                b[i + 2, j + 2, l] = matr[2][2]
                i += 3
            j += 3
    return b




sobel_filter_X = ([-1, 2, -1], [0, 0, 0] ,[1, 2, 1])
sobel_filter_Y = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])