'''
꼼꼼하게 반복하고, 3번 풀고, 버리자!
문제 유형: q
문제 요약: q 활용 접근, 리스트 추가 시 조건 적용
풀이 전략: q 구현
'''
import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T+1):
    test = int(input())
    nums = list(map(int, input().split()))
    count = 1
    while nums:
        minus = nums.pop(0)
        minus -= count
        count += 1
        if count == 6:
            count = 1
        if minus <= 0:
            minus = 0
            nums.append(minus)
            break
        nums.append(minus)


    print(nums)