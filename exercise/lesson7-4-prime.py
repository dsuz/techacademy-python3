# pattern 1: 課題の仕様/実行結果に沿ったやり方
print('pattern 1')
prime_list = []
for n in range(1, 101):
    if n == 2:
        print(n)
        prime_list.append(n)
    if n > 2:
        for p in prime_list:
            if n % p == 0:
                break
        else:
            print(n)
            prime_list.append(n)

# pattern 2: 1 の判定を省略して短く書く
print('pattern 2')
for n in range(2, 101):
    for p in range(2, n):
        if n % p == 0:
            break
    else:
        print(n)

# pattern 3: 奇数のみに対して判定処理を行う
print('pattern 3')
for n in range(1, 101):
    if n == 2:  # 2は自明な素数として処理する
        print(n)
    elif n % 2 != 0 and n > 2:  # 3以上の奇数に対して素数かどうか判定する
        odd = 3  # odd は奇数
        while odd**2 <= n:
            if n % odd == 0:
                break
            odd += 2  # odd を次の奇数にする
        else:
            print(n)


