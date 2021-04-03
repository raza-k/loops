def do_xor(a, b):
    r = []
    for i in range(len(a)):
        if a[i] == 1 or b[i] == 1 and a[i] != b[i]:
            r.append(1)
        else:
            r.append(0)
    return r


r = do_xor(
    [1, 0],
    [0, 1]
)
print(r)
