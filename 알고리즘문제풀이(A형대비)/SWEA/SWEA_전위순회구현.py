'''
꼼꼼하게 반복하고, 3번 풀고, 버리자!
문제 유형: 트리
문제 요약: 전위순회 트리 구현하기
풀이 전략: 전위순회 특징 파악
'''
import sys
sys.stdin = open("input.txt", "r")


def preorder(now):
    print(now, end="")
    if tree_list[now * 2] != 0:
        preorder(tree_list[now * 2])  # 왼쪽 자식이 누구인가?
    if tree_list[now * 2 + 1] != 0:
        preorder(tree_list[now * 2 + 1])  # 오른쪽 자식이 누구인가?
    # 재귀 작성 방식
    # 현재 : 매개변수
    # 재귀부분의 매개변수에 next를 넣어준다.
    # 전위 순회 : '나', 왼쪽자식, 오른쪽자식

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    tree_list = [0] * ((N + 1) * 2) # 몇 개짜리를 만들어야 할까? -> 주어진 간선 + 1(root)
    for i in range(N - 1):
        p, c = map(int, input().split()) # 어떻게 보면 p가 부모이지만 now의 개념과 비슷하고 c는 자식이지만 next와의 개념과 같음
        '''
        주어진 부모에서 2를 곱하거나 2를 곱하고 1을 더하면 자식은 트리 리스트에 저장!(인덱스)
        '''
        if tree_list[p * 2] == 0:
            tree_list[p * 2] = c
        else :
            tree_list[p * 2 + 1] = c
        preorder(1) # 1은 부모, now

