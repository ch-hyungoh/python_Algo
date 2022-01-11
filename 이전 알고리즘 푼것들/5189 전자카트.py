def solve(num, count):
    global min_num 
    if num == 0: #0인 사무소로 되돌아왔을때
        if count == N: #모든 곳을 거쳐서 돌아왔으면
            if min_num > sum(number):
                min_num = sum(number)
            return
    if sum(number) > min_num: # runover가 뜨는데 계산 중간에 min보다 sum이 커지면 빠져 나오기
        return
    for i in range(N): #다 돌아봐서
        if not visited[i] and arr[i][num]: #방문하지 않았고 값이 0이 아니면
            number.append(arr[i][num]) #number에 추가
            visited[i] = 1 # 방문체크
            solve(i, count+1) # 방문한 곳에서 출발하고 count에 1더하기
            number.pop() # 더이상 없으면 방문한곳 빼고
            visited[i] = 0 # 방문체크 제거

for tc in range(1, 1+int(input())):
    N = int(input())
    min_num = 789456132 #min 값을 구하기 위해서 큰 값을 min 에 준다
    number = [] #방문해서 들어가는 값들이 들어가기 위한 빈 리스트
    visited = [0]*N # 방문했으면 체크하기
    arr = [list(map(int, input().split())) for _ in range(N)] 
    solve(0, 0)

    print("#{} {}".format(tc, min_num))