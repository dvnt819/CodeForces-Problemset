x = int(input())
for _ in range(x):
    a, b = map(int, input().split())
    count = max(0, (b - (a % b)) % b)
    print(count)
