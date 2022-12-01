def liear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1


a = [140, 120, 150, 100, 170, 200, 90, 180]
b = [170, 150, 140, 90, 100, 120, 180, 200]
c = [120, 90, 200, 150, 180, 140, 100, 170]

# Extract common elements from a, b, c
common = [x for x in a if x in b and x in c]

for x in common:
    print(
        f'A[{liear_search(a, x) + 1}] with B[{liear_search(b, x) + 1}] with C[{liear_search(c, x) + 1}]')
