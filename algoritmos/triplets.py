def compare_triplets(a, b):
    ap = 0
    bp = 0
    result = []
    for i in range(0, len(a)):
        if a[i] > b[i]:
            ap = ap + 1
        elif a[i] < b[i]:
            bp += 1
        else:
            continue
    result.append(ap)
    result.append(bp)
    return result


alice = [1, 2, 4]
bob = [0, 3, 4]

compare_triplets(alice, bob)
