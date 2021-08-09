test_case = int(input())
N = int(input())
Height = list(map(int, input().split()))

# cnt = 0
# for i in range(1, N):
#     if Height[0] > Height[i]: # 0번보다 작은 값이 발견 -> 빈칸 수 -. 격차
#         cnt += 1
# print(count + 1)

cnt = [0] * N
for i in range(0, N-1):
    for j in range(1, N): # i보단 커야하니까
        if i < j: # i보단 커야하니까
            if Height[i] > Height[j]:
                cnt[i] += 1

max_num = 0
for i in range(len(cnt)):
    if cnt[i] > max_num:
        max_num = cnt[i]



print("#{0} {1}".format(test_case, max_num))
