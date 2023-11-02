n, m = list(map(int, input().split()))
count = n

for i in range(n // m):
    q = n // m
    r = n % m
    count += q
    n = q + r

print(count)