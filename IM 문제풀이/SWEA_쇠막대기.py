T = int(input())

for test_case in range(1, T+1):
    arr = list(input())
    # print(arr)

    count = 0
    temp = []   # 쇠막대기 체크 리스트 초기화

    for i in range(len(arr)):
        if arr[i] == ")":   # 닫는 가로라면
            if arr[i-1] == "(":     # 바로 직전이 여는 가로였다면
                temp = temp[0:len(temp)-1]      # 레이저가 잘랐으니 레이저의 여는 가로는 제외하고
                count += len(temp)      # 기존의 열려있던 가로 더하기

            elif arr[i-1] == ")":   # 다시 닫는 가로가 2번 연속이라면, 이거는 쇠막대기의 닫는 가로이므로
                temp = temp[0:len(temp) - 1]    # 기존의 여는 가로를 차감해주고
                count += 1      # count는 1씩 증가

        elif arr[i] == "(":     # 여는 가로나오면 temp에 일단 넣고
            temp.append("c")


    print(f"#{test_case} {count}")


