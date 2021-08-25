def enQueue(N, i):
    global rear # 함수 내에서 rear은 계속 바뀌니까 전역변수 선언
    rear = (rear + 1) % N # rear 계속 변화(원형)
    my_Q[rear] = i # 1번 인덱스에 i값 들어감, 0번은 비어두고 시작

def deQueue(N):
    global front    # front도 마찬가지로 전역번수 선언
    front = (front + 1) % N # 변화
    return my_Q[front] # pop 해주는 것은 앞에서 부터니깐

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N은 주어지는 자연수, M은 횟수
    arr = list(map(int, input().split()))
    my_Q = [0] * (N+1) # 길이의 더하기 1만큼 Q 생성(0은 비워두니까)
    rear = 0 # 초기화
    front = 0

    for i in arr: # 입력 리스트 돌면서 Q에 넣어주기
        enQueue(len(arr), i)

    for o in range(M):
        out = deQueue(len(arr)) # 넣어진 Q에서 제일 맨 앞값 빼오기
        enQueue(len(arr), out) # 빼온 값을 다시 넣어주기

    print(f"#{test_case} {deQueue(len(arr))}")



