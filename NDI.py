# Newton's Divided Difference Interpolation

# Given data
x = [5, 7, 11, 13, 17]
y = [150, 392, 1452, 2366, 5202]

n = len(x)


table = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    table[i][0] = y[i]


for j in range(1, n):
    for i in range(n - j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])


print("Divided Difference Table:\n")
for i in range(n):
    for j in range(n - i):
        print(f"{table[i][j]:10.2f}", end=" ")
    print()


value = 9
result = table[0][0]

product = 1
for i in range(1, n):
    product *= (value - x[i-1])
    result += product * table[0][i]

print("\nInterpolated value at x =", value)
print("f(9) =", round(result, 2))