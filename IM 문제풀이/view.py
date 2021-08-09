# view = [0, 0, 3, 5, 2, 5, 9, 0, 6, 4, 0, 6, 0, 0]
#
# count = 0
# for i in range(2, len(view) - 2):
#     if view[i] >= view[i-1] and view[i] >= view[i-2] and view[i] >= view[i+2] and view[i] >= view[i+1]:
#         count += 1
#         print(view[i])
#         for j in range(1, view[i]-1):
#             if view[i] - j > view[i-1] and view[i] - j > view[i-2] and view[i] - j > view[i+2] and view[i] - j > view[i+1]:
#                 count += 1
#                 print(view[i] - j)
T = 10

for test_case in range(1, T+1):
    len_width = int(input())
    view = list(map(int, input().split()))

    count = 0
    for i in range(2, len(view) - 2):
        if view[i] >= view[i-1] and view[i] >= view[i-2] and view[i] >= view[i+2] and view[i] >= view[i+1]:
            for j in range(0, view[i]):
                if view[i] - j > view[i-1] and view[i] - j > view[i-2] and view[i] - j > view[i+2] and view[i] - j > view[i+1]:
                    count += 1

    print(f"#{test_case} {count}")
