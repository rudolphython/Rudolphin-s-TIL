T = int(input())

for test_case in range(1, T+1):
    text, search = map(str, input().split())

    total = 0
    i = 0
    while i < len(text):
        count = 0
        for j in range(len(search)):
            if text[i+j] != search[j]:
                i += 1
                break
            elif text[i+j] == search[j]:
                count += 1
                if count == len(search):
                    total += 1
                    i += len(search)

    print(f"#{test_case} {len(text) - total*len(search) + total}")