T = int(input())

for test_case in range(1, T+1):
    price = int(input())
    money = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    while price != 0:
        money[50000] = price // 50000
        price = price % 50000
        money[10000] = price // 10000
        price = price % 10000
        money[5000] = price // 5000
        price = price % 5000
        money[1000] = price // 1000
        price = price % 1000
        money[500] = price // 500
        price = price % 500
        money[100] = price // 100
        price = price % 100
        money[50] = price // 50
        price = price % 50
        money[10] = price // 10
        price = price % 10


    print(f"#{test_case}", end = " ")
    for v in money.values():
        print(v, end = " ")