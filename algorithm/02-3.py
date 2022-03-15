n, m = map(int, input().split())
minlist = [] # 각 행의 작은 값들을 저장할 빈 리스트 생성
for i in range(n):
  list = list(map(int, input().split())) # n개의 각 행에 list를 만들어 원소를 대입
  minlist.append(min(list)) # 리스트에 대입된 원소들 중 작은 값을 minlist에 추가
max = max(minlist) # 각 행에 작은 값들만 모인 minlist에서 가장 큰 값을 max에 대입
print(max)