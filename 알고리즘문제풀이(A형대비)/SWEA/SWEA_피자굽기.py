'''
꼼꼼하게 반복하고, 3번 풀고, 버리자!
문제 유형: Q
문제 요약: 치즈에 따른 피자 굽기 시간이 다르므로 제일 마지막 남은 피자를 구하는 문제
풀이 전략: 화덕의 크기 == 1바퀴, 오븐 안에 있는 피자와 굽기 전 피자를 슬라이싱해서 구분
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # 화덕크기: N, 피자개수: M
    pizza = list(map(int, input().split()))
    all_pizza = []
    for i in range(M):
        all_pizza.append([i+1, pizza[i]]) # 피자의 번호를 알아내야 하니 모든 피자에 번호를 붙이는 작업
    ovenin = all_pizza[:N] # 화덕 안에 피자가 모두 들어갈 수 없으니 슬라이싱
    ready = all_pizza[N:]

    while len(ovenin) > 1: # 오븐 피자가 1개일 때 중단
        check = ovenin.pop(0) # 먼저, 오븐에서 피자 하나를 꺼내고 안 익었으면 1/2
        check[1] //= 2
        if check[1] == 0: # 치즈가 없다면 새로운 피자를 넣는 작업
            if len(ready) > 0:
                ovenin.append(ready.pop(0))
        else :
            ovenin.append(check)

    print(f'#{test_case} {ovenin[0][0]}')




