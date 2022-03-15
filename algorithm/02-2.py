n, m = map(int, input().split())
Max = 0
list = [0 for _ in range(n)]
for i in range(n):
  list[n] = list(map(int, input().split()))
  Min = min(list[n])
  if Max<Min:
    Max = Min
print(Max)