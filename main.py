sum = 0
i = 0
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
while i<m:
  for j in range(0, k):
    sum += num_list[-1]
    i += 1
    j += 1
  sum += num_list[-2]
  i += 1
print(sum)