def Land(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return Land(a - b, b)
    else:
        return Land(a, b - a)

print(Land(2, 6))