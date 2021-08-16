T = 10

for test_case in range(1, 1+ T):
    test = int(input())
    search = input()
    str = input()

    count = 0
    for i in range(len(str) - len(search) + 1):
        for j in range(len(search)):
            if str[i+j] == search[j]:
                j += 1
                if j == len(search):
                    count += 1
            else :
                break

    print(f"{test_case} {count}")
