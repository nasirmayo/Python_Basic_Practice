A=[[0, 2, 3, 5], [1, 3, 4, 6], [0, 2, 3, 5], [0, 1, 2, 3, 4, 5, 6]]
[[k for k in y if k!=x ] for x,y in enumerate(A)]

A = [[0, 2, 3, 5], [1, 3, 4, 6], [0, 2, 3, 5], [0, 1, 2, 3, 4, 5, 6]]

for i, e in enumerate(A):
    try:
        e.remove(i)
    except ValueError:
        pass

print(A)