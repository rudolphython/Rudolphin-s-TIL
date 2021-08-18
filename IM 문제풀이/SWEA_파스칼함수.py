T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case}")

    my_list = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0 or j ==i:
                my_list[i][j] = 1
            else :
                my_list[i][j] = my_list[i-1][j-1] + my_list[i-1][j]



    for i in range(len(my_list)):
        result = my_list[i]
        result = map(str, my_list[i])
        result2 = " ".join(result)
        print(result2.rstrip(" 0"))
