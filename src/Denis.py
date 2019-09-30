    from PIL import Image
    import numpy as np


    def mirrorY(a):
    b = np.zeros(a.shape)
    for i in range(0, len(a)):
    n = len(a[i])
    for j in range(0, n):
    b[i, j] = a[i, n - j - 1]
    return b


    def mirrorX(a):
    b = np.zeros(a.shape)
    for i in range(0, len(a)):
    n = len(a[i])
    for j in range(0, n):
    b[i, j] = a[len(a) - 1 - i, j]
    return b


    def rotateCCW(a, angle):
    if angle % 180 != 0:
    b = np.zeros(shape=(len(a[1]), len(a), a.shape[2]))
    print(a.shape)
    print(b.shape)
    n = (angle % 360) // 90
    for k in range(n):
    for i in range(0, len(a)):
    for j in range(0, len(a[i])):
    b[i, j] = a[j, i]
    else:
    b = np.zeros(a.shape)
    n = (angle % 360) // 180
    if n == 1:
    for i in range(0, len(a)):
    k = len(a[i])
    for j in range(0, k):
    b[i, j] = a[len(a) - i - 1, k - j - 1]
    return b


    def rotateCW(a, angle):
    if angle % 180 != 0:
    b = np.zeros(shape=(len(a[1]), len(a), a.shape[2]))
    print(a.shape)
    print(b.shape)
    n = (angle % 360) // 90
    for k in range(n):
    for i in range(0, len(a)):
    for j in range(0, len(a[i])):
    b[i, j] = a[len(a) - j - 1, len(a[i]) - i - 1]
    else:
    b = np.zeros(a.shape)
    n = (angle % 360) // 180
    if n == 1:
    for i in range(0, len(a)):
    k = len(a[i])
    for j in range(0, k):
    b[i, j] = a[len(a) - i - 1, k - j - 1]
    return b

    im = Image.open('c:\\Popka.png')
    im.show()
    data = np.array(im)
    data_f = data.astype(np.float)
    data_f = mirrorX(data_f)
    data_f = data_f.astype(np.byte)
    omg = Image.fromarray(data_f, 'RGB')
    omg.show()

