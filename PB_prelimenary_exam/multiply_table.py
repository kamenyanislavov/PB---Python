n = input()

n1 = int(n[2])
n2 = int(n[1])
n3 = int(n[0])

for i in range(1, (n1 + 1)):
    for j in range(1, (n2 + 1)):
        for k in range(1, (n3 + 1)):
            print(f'{i} * {j} * {k} = {i * j * k};')
