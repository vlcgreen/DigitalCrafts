#Day 3 Homework Problem 2

m1 = [[1,3], [2,4]]
m2 = [[5,2], [1, 0]]
add = []


for a in range(0, 2):
    m3 = []
    for b in range(0, 2):
        m3.append(m1[a][b] + m2[a][b])

    add.append(m3)

print(add)



