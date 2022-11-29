def MatrixMinMultiplications(matrixes):
    length = len(matrixes)

    if (length <= 2):
        return 0

    minimum = 9999999999
    for i in range(1, length - 1):
        multiplication = matrixes[0] * matrixes[-1] * matrixes[i]
        current = MatrixMinMultiplications(matrixes[0:i+1]) + MatrixMinMultiplications(matrixes[i:]) + multiplication
        minimum = min(minimum, current)

    return minimum

print(MatrixMinMultiplications([10, 100, 5, 50]))
