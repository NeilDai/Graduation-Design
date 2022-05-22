import numpy as np


def Seq2Array(seq):

    m = 0
    conv_shell = 0

    for i in range(len(seq)):
        n = len(seq[i])
        if n > m:
            m = n

    N = m + 2*conv_shell
    # N = 2935
    # m = 2925


    # 将所有序列长度补成m（2925）+5
    for i in range(len(seq)):
        while len(seq[i]) < m+conv_shell:
            seq[i] = seq[i] + '0'


    arrays = np.zeros((1, N, 4,))
    array = np.zeros((conv_shell, 4))

    for i in range(len(seq)):
        n = seq[i]

        array = np.empty((conv_shell, 4))
        for j in n:
            if j == "a":
                array = np.append(array, [[1, 0, 0, 0]], axis=0)
            if j == "t":
                array = np.append(array, [[0, 1, 0, 0]], axis=0)
            if j == "c":
                array = np.append(array, [[0, 0, 1, 0]], axis=0)
            if j == "g":
                array = np.append(array, [[0, 0, 0, 1]], axis=0)
            if j == "0":
                array = np.append(array, [[0, 0, 0, 0]], axis=0)
        # 让array升维，使跟X同维，可被添加至X
        array = array[np.newaxis, :]
        arrays = np.append(arrays, array, axis=0)

    # 删除X的第一个元素，可得shape(213,2935,4)
    arrays = np.delete(arrays, 0, axis=0)
    return arrays

if __name__ == '__main__':
    main()