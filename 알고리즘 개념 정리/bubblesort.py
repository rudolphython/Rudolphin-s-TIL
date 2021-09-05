T = int(input())

for test_case in range(1, T+1):
    search, text = map(str, input().split())

    total = 0
    for i in range(len(text) - len(search) + 1):
        count = 0
        for j in range(len(search)):
            if search[j] == text[i+j]:
                count += 1
                if count == len(search):
                    total += 1

    print(total)