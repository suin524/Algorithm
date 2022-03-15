n, _ = map(int, input().split())
Max = 0
for _ in range(n):
    Min = min(list(map(int, input().split())))
    if (Max < Min):
        Max = Min
print(Max)
