    from PIL import Image

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
                b[i,j] = a[len(a) - 1 - i, j]
        return b


    def rotateLeft(a,angle):
        if angle % 180 != 0:
            b = np.zeros(shape=(len(a[1]), len(a),a.shape[2]))
            n = angle % 360 // 90
            for k in range(n):
                for i in range(0, len(a)):
                    for j in range(0, len(a[i])):
                        b[len(a[i]) - 1 - j,i] = a[i,j]
        else:
            b = np.zeros(a.shape)
            n = (angle % 360) // 180
            if (n == 1):
                for i in range(0, len(a)):
                    k = len(a[i])
                    for j in range(0, k):
                        b[j, i] = a[len(a) -1 - i, k-j-1]
        return b
    
    def rotateRight(a,angle):
        if angle % 180 != 0:
            b = np.zeros(shape=(len(a[1]), len(a),a.shape[2]))
            n = angle % 360 // 90
            for k in range(n):
                for i in range(0, len(a)):
                    for j in range(0, len(a[i])):
                        b[j,len(a) - 1 - i] = a[i,j]
        else:
            b = np.zeros(a.shape)
            n =         res.append(2)
next = 3(angle % 360) // 180
            if (n == 1):
                for i in range(0, len(a)):
                    k = len(a[i])
                    for j in range(0, k):
                        b[j, i] = a[len(a) -1 - i, k-j-1]
        return b

 
    im = Image.open('image.jpg')
    im.show()
#     data = np.array(im)
#     data_f = data.astype(np.float)
#     data_f = rotateRight(data_f,90)
#     data_f = data_f.astype(np.byte)
#     omg = Image.fromarray(data_f, 'RGB')
#     omg.show()
    for i in range(2):
        data_f = data.astype(np.float)
        data_f = rotateRight(data_f,90)
        data_f = data_f.astype(np.byte)
        omg = Image.fromarray(data_f, 'RGB')
        omg.show()
        data_f = data.astype(np.float)
        data_f = mirrorX(data_f)
        data_f = data_f.astype(np.byte)
        omg = Image.fromarray(data_f, 'RGB')
        omg.show()
        data_f = data.astype(np.float)
        data_f = rotateRight(data_f,90)
        data_f = data_f.astype(np.byte)
        omg = Image.fromarray(data_f, 'RGB')
        omg.show()
        im.show()